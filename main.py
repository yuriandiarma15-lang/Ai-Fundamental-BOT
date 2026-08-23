import asyncio
import logging

from aiogram import (
    Bot,
    Dispatcher
)

from config.settings import (
    BOT_TOKEN
)

from handlers.start import (
    router as start_router
)

from handlers.signal import (
    router as signal_router
)

from services.scheduler import (
    fundamental_scheduler
)


logging.basicConfig(
    level=logging.INFO
)


async def main():

    if not BOT_TOKEN:

        raise RuntimeError(
            "BOT_TOKEN belum diisi."
        )

    print(
        "=========================================="
    )

    print(
        "🤖 XAU AI FUNDAMENTAL BOT STARTING"
    )

    print(
        "=========================================="
    )

    bot = Bot(
        token=BOT_TOKEN
    )

    dp = Dispatcher()

    dp.include_router(
        start_router
    )

    dp.include_router(
        signal_router
    )

    # =========================================
    # FUNDAMENTAL SCHEDULER
    # =========================================

    asyncio.create_task(
        fundamental_scheduler(
            bot,
            None
        )
    )

    print(
        "📰 FUNDAMENTAL ENGINE ACTIVE"
    )

    print(
        "⏰ HIGH IMPACT PREPARE ACTIVE"
    )

    await dp.start_polling(
        bot
    )


if __name__ == "__main__":

    asyncio.run(
        main()
    )
