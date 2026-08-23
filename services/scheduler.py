import asyncio

from datetime import datetime

import pytz

from config.settings import (
    TIMEZONE,
    NEWS_PREPARE_MINUTES,
    ADMIN_CHAT_ID
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
    chat_id=None
):

    # =====================================================
    # ADMIN CHAT
    # =====================================================

    if not chat_id:

        chat_id = ADMIN_CHAT_ID


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
            # CEK EVENT
            # =============================================

            for event in high_impact:

                title = event.get(
                    "title",
                    ""
                )


                # =========================================
                # EVENT TIME
                # =========================================

                event_time = event.get(
                    "event_time"
                )


                # =========================================
                # RSS TANPA EVENT TIME
                #
                # JANGAN SPAM LOG
                # =========================================

                if not event_time:

                    continue


                # =========================================
                # PARSE TIME
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
                # TIMEZONE
                # =========================================

                if event_time.tzinfo is None:

                    event_time = WIB.localize(
                        event_time
                    )

                else:

                    event_time = event_time.astimezone(
                        WIB
                    )


                # =========================================
                # HITUNG WAKTU
                # =========================================

                seconds_until_news = (
                    event_time - now
                ).total_seconds()


                minutes_until_news = (
                    seconds_until_news / 60
                )


                # =========================================
                # EVENT SUDAH LEWAT
                # =========================================

                if seconds_until_news < 0:

                    continue


                # =========================================
                # PREPARE WINDOW
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
                    # DUPLIKAT
                    # =====================================

                    if event_id in _processed_prepare:

                        continue


                    print(
                        "=========================================="
                    )

                    print(
                        "🚨 PREPARE NEWS:",
                        title
                    )

                    print(
                        "⏰ EVENT:",
                        event_time.strftime(
                            "%Y-%m-%d %H:%M:%S %Z"
                        )
                    )

                    print(
                        "=========================================="
                    )


                    # =====================================
                    # BUAT OBJECT EVENT
                    # =====================================

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


                    # =====================================
                    # ANALISIS PREPARE
                    # =====================================

                    try:

                        result = await asyncio.to_thread(
                            prepare_news,
                            prepared_event
                        )


                        # =================================
                        # KIRIM TELEGRAM
                        # =================================

                        if not chat_id:

                            print(
                                "⚠️ ADMIN_CHAT_ID belum tersedia."
                            )

                            continue


                        await bot.send_message(

                            chat_id=chat_id,

                            text=result,

                            parse_mode="HTML",

                            disable_web_page_preview=True

                        )


                        # =================================
                        # TANDAI SUDAH DIKIRIM
                        # =================================

                        _processed_prepare.add(
                            event_id
                        )


                        print(
                            "✅ PREPARE BERHASIL DIKIRIM:",
                            title
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
