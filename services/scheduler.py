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
        "⏰ High Impact Prepare: -30 menit"
    )

    print(
        "=========================================="
    )

    while True:

        try:

            news = (
                collect_official_news()
            )

            high_impact = (
                find_high_impact_news(
                    news
                )
            )

            now = datetime.now(
                WIB
            )

            for event in high_impact:

                # =========================================
                # Untuk tahap awal RSS belum selalu memberi
                # waktu rilis ekonomi.
                #
                # Event calendar akan kita sambungkan pada
                # tahap berikutnya.
                # =========================================

                print(
                    "HIGH IMPACT:",
                    event.get(
                        "title"
                    )
                )

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
