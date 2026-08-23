import asyncio
import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.news_engine import (
    collect_official_news_async,
    find_high_impact_news
)


router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("news"))
async def news_command(message: Message):

    logger.info(
        "🔥 /news diterima"
    )

    # =====================================================
    # LOADING LANGSUNG
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
        "✅ Loading berhasil dikirim"
    )

    try:

        # =================================================
        # AMBIL NEWS PARALEL
        # =================================================

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "🔄 <b>MENGAMBIL DATA RESMI...</b>\n\n"
            "🏦 Federal Reserve\n"
            "🏛️ U.S. Treasury\n"
            "📊 Bureau of Labor Statistics",
            parse_mode="HTML"
        )

        news = await collect_official_news_async()

        logger.info(
            "📰 Total news: %s",
            len(news)
        )

        # =================================================
        # FILTER
        # =================================================

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "✅ Data berhasil diterima.\n\n"
            "🔎 <b>MENGANALISIS...</b>\n\n"
            "💵 USD\n"
            "🥇 XAUUSD / GOLD\n"
            "🏦 Federal Reserve\n"
            "📊 Economic Data",
            parse_mode="HTML"
        )

        high_impact = await asyncio.to_thread(
            find_high_impact_news,
            news
        )

        logger.info(
            "🔥 High Impact: %s",
            len(high_impact)
        )

        # =================================================
        # NO NEWS
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
        # RESULT
        # =================================================

        text = (
            "📰 <b>XAU AI HIGH IMPACT NEWS</b>\n\n"
            "🇺🇸 <b>NEWS RELEVAN TERHADAP "
            "XAUUSD / USD</b>\n\n"
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
            "Berita difilter berdasarkan "
            "potensi pengaruh terhadap USD "
            "dan XAUUSD.\n\n"
            "⚠️ Gunakan bersama SMC, price action "
            "dan konfirmasi market."
        )

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
            "❌ NEWS ERROR"
        )

        try:

            await loading.edit_text(
                "❌ <b>XAU AI NEWS ENGINE</b>\n\n"
                "Gagal mengambil data news.\n\n"
                f"<code>{str(e)[:500]}</code>",
                parse_mode="HTML"
            )

        except Exception:

            pass
