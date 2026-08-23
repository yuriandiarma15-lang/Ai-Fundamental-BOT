import asyncio

from datetime import datetime

import pytz

from config.settings import (
    TIMEZONE,
    NEWS_REFRESH_SECONDS,
    SCHEDULER_INTERVAL_SECONDS
)

from services.news_cache import (
    refresh_news
)


WIB = pytz.timezone(
    TIMEZONE
)


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
        "⏰ GNews refresh: setiap 60 menit"
    )

    print(
        "=========================================="
    )


    first_run = True


    while True:

        try:

            # =============================================
            # REFRESH GNEWS
            # =============================================

            if first_run:

                await asyncio.to_thread(
                    refresh_news,
                    True
                )

                first_run = False


            else:

                await asyncio.to_thread(
                    refresh_news,
                    False
                )


            # =============================================
            # LOG
            # =============================================

            now = datetime.now(
                WIB
            )


            print(
                "🕐 FUNDAMENTAL CHECK:",
                now.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )


            # =============================================
            # TIDAK ADA KIRIM TELEGRAM OTOMATIS DULU
            #
            # Karena GNews bukan economic calendar.
            # =============================================

            await asyncio.sleep(
                SCHEDULER_INTERVAL_SECONDS
            )


        except asyncio.CancelledError:

            raise


        except Exception as e:

            print(
                "❌ FUNDAMENTAL SCHEDULER ERROR:",
                repr(e)
            )


            await asyncio.sleep(
                30
            )
