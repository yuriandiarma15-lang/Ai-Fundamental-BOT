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

logger = logging.getLogger("main")


# =========================================================
# MAIN
# =========================================================

async def main():

    # =====================================================
    # CHECK TOKEN
    # =====================================================

    if not BOT_TOKEN:

        raise RuntimeError(
            "❌ BOT_TOKEN belum diisi di environment."
        )


    # =====================================================
    # START
    # =====================================================

    print()
    print("==========================================")
    print("🤖 XAU AI FUNDAMENTAL BOT STARTING")
    print("==========================================")


    # =====================================================
    # CREATE BOT
    # =====================================================

    bot = Bot(
        token=BOT_TOKEN
    )


    # =====================================================
    # CREATE DISPATCHER
    # =====================================================

    dp = Dispatcher()


    # =====================================================
    # REGISTER START HANDLER
    # =====================================================

    dp.include_router(
        start_router
    )

    print(
        "✅ START HANDLER ACTIVE"
    )


    # =====================================================
    # REGISTER SIGNAL HANDLER
    # =====================================================

    dp.include_router(
        signal_router
    )

    print(
        "✅ SIGNAL HANDLER ACTIVE"
    )


    # =====================================================
    # REGISTER NEWS HANDLER
    # =====================================================

    dp.include_router(
        news_router
    )

    print(
        "✅ NEWS HANDLER ACTIVE"
    )


    # =====================================================
    # START FUNDAMENTAL SCHEDULER
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

    print()
    print("==========================================")
    print("📡 TELEGRAM POLLING ACTIVE")
    print("==========================================")
    print()


    try:

        await dp.start_polling(
            bot
        )


    except asyncio.CancelledError:

        logger.info(
            "🛑 BOT POLLING CANCELLED"
        )

        raise


    except Exception as e:

        logger.exception(
            "❌ POLLING ERROR: %s",
            e
        )

        raise


    finally:

        # =================================================
        # STOP FUNDAMENTAL SCHEDULER
        # =================================================

        if not scheduler_task.done():

            logger.info(
                "🛑 Menghentikan fundamental scheduler..."
            )

            scheduler_task.cancel()

            try:

                await scheduler_task

            except asyncio.CancelledError:

                pass


        # =================================================
        # CLOSE BOT SESSION
        # =================================================

        try:

            await bot.session.close()

        except Exception as e:

            logger.warning(
                "⚠️ Gagal menutup bot session: %s",
                e
            )


        print()
        print("🛑 BOT STOPPED")


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
            "🛑 Bot dihentikan oleh user."
        )
