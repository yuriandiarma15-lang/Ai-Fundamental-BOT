import asyncio

from datetime import datetime

import pytz

from config.settings import (
    TIMEZONE,
    NEWS_PREPARE_MINUTES
)

from services.news_engine import (
    collect_official_news,
    find_high_impact_news
)

from services.news_prepare import (
    prepare_news
)


WIB = pytz.timezone(
    TIMEZONE
)


_processed_prepare = set()


async def fundamental_scheduler(
    bot,
    chat_id
):

    print(
        "=========================================="
    )

    print(
        "📰 XAU AI FUNDAMENTAL SCHEDULER ACTIVE"
    )

    print(
        f"⏰ High Impact Prepare: -{NEWS_PREPARE_MINUTES} menit"
    )

    print(
        "=========================================="
    )


    while True:

        try:

            # =============================================
            # AMBIL NEWS RESMI
            # =============================================

            news = await asyncio.to_thread(
                collect_official_news
            )


            # =============================================
            # FILTER HIGH IMPACT
            # =============================================

            high_impact = await asyncio.to_thread(
                find_high_impact_news,
                news
            )


            now = datetime.now(
                WIB
            )


            # =============================================
            # CEK SETIAP EVENT
            # =============================================

            for event in high_impact:

                title = event.get(
                    "title",
                    ""
                )

                event_time = event.get(
                    "event_time"
                )


                # =========================================
                # RSS BELUM PUNYA WAKTU EVENT
                # =========================================

                if not event_time:

                    print(
                        "HIGH IMPACT TANPA WAKTU:",
                        title
                    )

                    continue


                # =========================================
                # KONVERSI WAKTU
                # =========================================

                if isinstance(
                    event_time,
                    str
                ):

                    try:

                        event_time = datetime.fromisoformat(
                            event_time
                        )

                    except Exception:

                        print(
                            "FORMAT WAKTU ERROR:",
                            title
                        )

                        continue


                # =========================================
                # PASTIKAN TIMEZONE
                # =========================================

                if event_time.tzinfo is None:

                    event_time = WIB.localize(
                        event_time
                    )


                # =========================================
                # HITUNG SELISIH KE NEWS
                # =========================================

                seconds_until_news = (
                    event_time - now
                ).total_seconds()


                minutes_until_news = (
                    seconds_until_news / 60
                )


                # =========================================
                # PREPARE -30 MENIT
                # =========================================

                if (
                    NEWS_PREPARE_MINUTES - 1
                    <= minutes_until_news
                    <=
                    NEWS_PREPARE_MINUTES + 1
                ):

                    event_id = (
                        f"{title}|"
                        f"{event_time.isoformat()}"
                    )


                    # =====================================
                    # JANGAN KIRIM DUPLIKAT
                    # =====================================

                    if event_id in _processed_prepare:

                        continue


                    print(
                        "🚨 PREPARE NEWS:",
                        title
                    )


                    # =====================================
                    # BUAT ANALISIS
                    # =====================================

                    try:

                        # sementara object sederhana
                        class Event:
                            pass


                        prepared_event = Event()


                        prepared_event.title = (
                            event.get(
                                "title",
                                "-"
                            )
                        )

                        prepared_event.event_time = (
                            event_time
                        )

                        prepared_event.impact = (
                            event.get(
                                "impact",
                                "HIGH"
                            )
                        )

                        prepared_event.country = (
                            event.get(
                                "country",
                                "US"
                            )
                        )

                        prepared_event.forecast = (
                            event.get(
                                "forecast",
                                "-"
                            )
                        )

                        prepared_event.previous = (
                            event.get(
                                "previous",
                                "-"
                            )
                        )

                        prepared_event.actual = (
                            event.get(
                                "actual",
                                "-"
                            )
                        )

                        prepared_event.source_name = (
                            event.get(
                                "source_name",
                                event.get(
                                    "source",
                                    ""
                                )
                            )
                        )

                        prepared_event.source_url = (
                            event.get(
                                "source_url",
                                event.get(
                                    "link",
                                    ""
                                )
                            )
                        )


                        result = await asyncio.to_thread(
                            prepare_news,
                            prepared_event
                        )


                        # =================================
                        # KIRIM KE ADMIN
                        # =================================

                        await bot.send_message(

                            chat_id=chat_id,

                            text=result,

                            parse_mode="HTML",

                            disable_web_page_preview=True

                        )


                        _processed_prepare.add(
                            event_id
                        )


                    except Exception as e:

                        print(
                            "PREPARE ERROR:",
                            e
                        )


            # =============================================
            # CEK SETIAP 30 DETIK
            # =============================================

            await asyncio.sleep(
                30
            )


        except asyncio.CancelledError:

            raise


        except Exception as e:

            print(
                "FUNDAMENTAL SCHEDULER ERROR:",
                e
            )

            await asyncio.sleep(
                30
            )
