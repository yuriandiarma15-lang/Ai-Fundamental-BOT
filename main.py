import asyncio
import logging

from aiogram import Bot, Dispatcher

from config.settings import BOT_TOKEN

from handlers.start import router as start_router
from handlers.signal import router as signal_router
from handlers.news import router as news_router

from services.scheduler import fundamental_scheduler


# =========================================================
# LOGGING
# =========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)


# =========================================================
# MAIN
# =========================================================

async def main():

    # =====================================================
    # CHECK BOT TOKEN
    # =====================================================

    if not BOT_TOKEN:

        raise RuntimeError(
            "❌ BOT_TOKEN belum diisi di environment."
        )


    # =====================================================
    # START MESSAGE
    # =====================================================

    print()
    print("==========================================")
    print("🤖 XAU AI FUNDAMENTAL BOT STARTING")
    print("==========================================")


    # =====================================================
    # BOT
    # =====================================================

    bot = Bot(
        token=BOT_TOKEN
    )


    # =====================================================
    # DISPATCHER
    # =====================================================

    dp = Dispatcher()


    # =====================================================
    # HANDLER START
    # =====================================================

    dp.include_router(
        start_router
    )

    print(
        "✅ START HANDLER ACTIVE"
    )


    # =====================================================
    # HANDLER SIGNAL
    # =====================================================

    dp.include_router(
        signal_router
    )

    print(
        "✅ SIGNAL HANDLER ACTIVE"
    )


    # =====================================================
    # HANDLER NEWS
    # =====================================================

    dp.include_router(
        news_router
    )

    print(
        "✅ NEWS HANDLER ACTIVE"
    )


    # =====================================================
    # FUNDAMENTAL SCHEDULER
    # =====================================================

    scheduler_task = asyncio.create_task(

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


    # =====================================================
    # POLLING
    # =====================================================

    try:

        print(
            "=========================================="
        )

        print(
            "📡 TELEGRAM POLLING ACTIVE"
        )

        print(
            "=========================================="
        )

        await dp.start_polling(
            bot
        )


    except asyncio.CancelledError:

        print(
            "🛑 BOT POLLING CANCELLED"
        )

        raise


    except Exception as e:

        print(
            "❌ POLLING ERROR:",
            repr(e)
        )

        raise


    finally:

        # ================================================
        # STOP SCHEDULER
        # ================================================

        if not scheduler_task.done():

            scheduler_task.cancel()

            try:

                await scheduler_task

            except asyncio.CancelledError:

                pass


        # ================================================
        # CLOSE BOT SESSION
        # ================================================

        await bot.session.close()

        print(
            "🛑 BOT STOPPED"
        )


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    try:

        asyncio.run(
            main()
        )

    except KeyboardInterrupt:

        print(
            "🛑 Bot dihentikan."
        )
