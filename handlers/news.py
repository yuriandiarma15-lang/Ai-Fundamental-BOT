import asyncio
import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.news_engine import (
    collect_official_news,
    find_high_impact_news
)


router = Router()

logger = logging.getLogger(__name__)


# =========================================================
# /NEWS
# =========================================================

@router.message(Command("news"))
async def news_command(message: Message):

    logger.info(
        "🔥 /news diterima dari user_id=%s",
        message.from_user.id if message.from_user else "unknown"
    )

    # =====================================================
    # 1. KIRIM LOADING TERLEBIH DAHULU
    # =====================================================

    loading = await message.answer(
        "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
        "⏳ <b>MEMPROSES...</b>\n\n"
        "📡 Mengambil berita resmi...\n"
        "🏦 Federal Reserve\n"
        "🏛️ U.S. Treasury\n"
        "📊 BLS\n\n"
        "Mohon tunggu...",
        parse_mode="HTML"
    )

    logger.info(
        "✅ Loading /news berhasil dikirim | message_id=%s",
        loading.message_id
    )

    try:

        # =================================================
        # 2. AMBIL DATA
        # =================================================

        await asyncio.sleep(0.5)

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "⏳ <b>MENGAMBIL DATA...</b>\n\n"
            "🔄 Menghubungi sumber resmi...\n"
            "🏦 Federal Reserve\n"
            "🏛️ U.S. Treasury\n"
            "📊 Bureau of Labor Statistics",
            parse_mode="HTML"
        )

        news = await asyncio.to_thread(
            collect_official_news
        )

        logger.info(
            "📰 Total news: %s",
            len(news)
        )

        # =================================================
        # 3. FILTER
        # =================================================

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "✅ Data berhasil diterima.\n\n"
            "🔎 <b>MEMFILTER NEWS...</b>\n\n"
            "💵 USD\n"
            "🥇 GOLD / XAUUSD\n"
            "🏦 FED\n"
            "📊 ECONOMIC DATA\n\n"
            "Mencari hanya berita yang "
            "berpotensi memengaruhi Gold...",
            parse_mode="HTML"
        )

        await asyncio.sleep(0.5)

        high_impact = await asyncio.to_thread(
            find_high_impact_news,
            news
        )

        logger.info(
            "🔥 High Impact: %s",
            len(high_impact)
        )

        # =================================================
        # 4. TIDAK ADA HASIL
        # =================================================

        if not high_impact:

            await loading.edit_text(
                "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
                "✅ Analisis selesai.\n\n"
                "⚪ Tidak ditemukan High Impact News "
                "yang relevan terhadap XAUUSD / USD.\n\n"
                "🤖 <b>XAU AI FUNDAMENTAL</b>",
                parse_mode="HTML"
            )

            return

        # =================================================
        # 5. HASIL
        # =================================================

        text = (
            "📰 <b>XAU AI HIGH IMPACT NEWS</b>\n\n"
            "🇺🇸 <b>NEWS RELEVAN XAUUSD / USD</b>\n\n"
        )

        for item in high_impact[:5]:

            title = item.get(
                "title",
                "-"
            )

            link = item.get(
                "source_url",
                item.get(
                    "link",
                    ""
                )
            )

            source = item.get(
                "source_name",
                item.get(
                    "source",
                    "Official Source"
                )
            )

            text += (
                f"🔥 <b>{title}</b>\n"
            )

            if link:

                text += (
                    f'<a href="{link}">'
                    f"🔗 {source}"
                    f"</a>\n"
                )

            text += "\n"

        text += (
            "━━━━━━━━━━━━━━━━━━\n\n"
            "🧠 <b>XAU AI FUNDAMENTAL</b>\n\n"
            "News difilter berdasarkan potensi "
            "dampaknya terhadap USD dan XAUUSD.\n\n"
            "⚠️ Gunakan bersama price action, "
            "SMC dan konfirmasi market."
        )

        # =================================================
        # 6. GANTI LOADING MENJADI HASIL
        # =================================================

        await loading.edit_text(
            text,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

        logger.info(
            "✅ /news selesai"
        )

    except Exception as e:

        logger.exception(
            "❌ /news ERROR"
        )

        try:

            await loading.edit_text(
                "❌ <b>XAU AI NEWS ENGINE</b>\n\n"
                "Terjadi kesalahan ketika mengambil "
                "data news.\n\n"
                f"<code>{str(e)[:500]}</code>\n\n"
                "🔄 Silakan coba lagi.",
                parse_mode="HTML"
            )

        except Exception as edit_error:

            logger.exception(
                "❌ Tidak bisa edit pesan loading: %s",
                edit_error
            )
