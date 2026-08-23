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

    print("🔥 /news MASUK HANDLER")

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

    print(
        "✅ Loading /news terkirim:",
        loading.message_id
    )

    try:

        # =================================================
        # LOADING ANIMATION
        # =================================================

        await asyncio.sleep(1)

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "🔎 <b>MENGANALISIS BERITA...</b>\n\n"
            "💵 USD\n"
            "🥇 XAUUSD\n"
            "🏦 Federal Reserve\n"
            "📊 Data ekonomi AS\n\n"
            "Sedang menyaring berita yang relevan...",
            parse_mode="HTML"
        )

        # =================================================
        # AMBIL BERITA
        # =================================================

        news = await asyncio.to_thread(
            collect_official_news
        )

        print(
            "📰 Total berita:",
            len(news)
        )

        # =================================================
        # UPDATE LOADING
        # =================================================

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "✅ Data resmi berhasil diperoleh.\n\n"
            "🧠 <b>FILTERING XAUUSD / USD...</b>\n\n"
            "❌ Berita perbankan umum\n"
            "❌ Enforcement action\n"
            "❌ Application / merger\n"
            "❌ Berita administratif\n\n"
            "✅ FOMC\n"
            "✅ Interest Rate\n"
            "✅ CPI / PCE\n"
            "✅ NFP / Employment\n"
            "✅ Powell / Fed Policy",
            parse_mode="HTML"
        )

        await asyncio.sleep(1)

        # =================================================
        # FILTER HIGH IMPACT
        # =================================================

        high_impact = await asyncio.to_thread(
            find_high_impact_news,
            news
        )

        print(
            "🔥 High Impact:",
            len(high_impact)
        )

        # =================================================
        # TIDAK ADA NEWS
        # =================================================

        if not high_impact:

            await loading.edit_text(
                "📰 <b>XAU AI NEWS</b>\n\n"
                "✅ Analisis selesai.\n\n"
                "⚪ Saat ini tidak ditemukan "
                "High Impact News yang relevan "
                "terhadap USD / XAUUSD.\n\n"
                "🤖 <b>XAU AI FUNDAMENTAL</b>",
                parse_mode="HTML"
            )

            return

        # =================================================
        # HASIL
        # =================================================

        text = (
            "📰 <b>XAU AI HIGH IMPACT NEWS</b>\n\n"
            "🇺🇸 <b>NEWS RELEVAN USD / XAUUSD</b>\n\n"
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
            "News telah difilter berdasarkan "
            "potensi pengaruh terhadap USD "
            "dan XAUUSD.\n\n"
            "⚠️ Gunakan bersama price action, "
            "SMC dan konfirmasi market."
        )

        # =================================================
        # BATAS TELEGRAM
        # =================================================

        if len(text) > 4000:

            text = (
                text[:3900]
                + "\n\n..."
            )

        # =================================================
        # GANTI LOADING → HASIL
        # =================================================

        await loading.edit_text(
            text,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

        print(
            "✅ /news SELESAI"
        )

    except Exception as e:

        print(
            "❌ /news ERROR:",
            repr(e)
        )

        try:

            await loading.edit_text(
                "❌ <b>XAU AI NEWS ERROR</b>\n\n"
                "Terjadi kesalahan saat mengambil "
                "atau menganalisis berita.\n\n"
                f"<code>{str(e)[:500]}</code>",
                parse_mode="HTML"
            )

        except Exception as edit_error:

            print(
                "❌ Gagal edit loading:",
                repr(edit_error)
            )
