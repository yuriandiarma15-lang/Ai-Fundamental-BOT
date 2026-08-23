import asyncio

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.news_engine import (
    collect_official_news,
    find_high_impact_news
)


router = Router()


# =========================================================
# /NEWS
# =========================================================

@router.message(Command("news"))
async def news_command(message: Message):

    print("📰 /news DITERIMA")

    # =====================================================
    # LOADING LANGSUNG
    # =====================================================

    loading = await message.answer(
        "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
        "⏳ <b>SEDANG MEMPROSES...</b>\n\n"
        "📡 Mengambil berita terbaru...\n"
        "🏦 Memeriksa Federal Reserve...\n"
        "🏛️ Memeriksa U.S. Treasury...\n"
        "📊 Memeriksa BLS...\n\n"
        "Mohon tunggu sebentar...",
        parse_mode="HTML"
    )

    print("✅ Loading /news terkirim")

    try:

        # =================================================
        # ANIMASI LOADING
        # =================================================

        await asyncio.sleep(0.5)

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "⏳ <b>MENGAMBIL DATA RESMI...</b>\n\n"
            "📡 Federal Reserve\n"
            "🏛️ U.S. Treasury\n"
            "📊 Bureau of Labor Statistics\n\n"
            "Mohon tunggu...",
            parse_mode="HTML"
        )

        # =================================================
        # AMBIL NEWS
        # =================================================

        news = await asyncio.to_thread(
            collect_official_news
        )

        print(
            f"📰 TOTAL NEWS: {len(news)}"
        )

        # =================================================
        # UPDATE LOADING
        # =================================================

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "✅ Data resmi berhasil diterima.\n\n"
            "🔎 <b>MEMFILTER NEWS...</b>\n\n"
            "💵 USD\n"
            "🥇 XAUUSD / GOLD\n"
            "🏦 Monetary Policy\n"
            "📊 Economic Data\n\n"
            "Mencari hanya berita yang berpotensi "
            "berpengaruh terhadap Gold / USD...",
            parse_mode="HTML"
        )

        await asyncio.sleep(0.5)

        # =================================================
        # FILTER HIGH IMPACT
        # =================================================

        high_impact = await asyncio.to_thread(
            find_high_impact_news,
            news
        )

        print(
            f"🔥 HIGH IMPACT: {len(high_impact)}"
        )

        # =================================================
        # TIDAK ADA NEWS
        # =================================================

        if not high_impact:

            await loading.edit_text(
                "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
                "✅ Analisis selesai.\n\n"
                "⚪ Tidak ditemukan High Impact News "
                "yang relevan terhadap XAUUSD / USD "
                "dari sumber resmi.\n\n"
                "🤖 <b>XAU AI FUNDAMENTAL</b>",
                parse_mode="HTML"
            )

            return

        # =================================================
        # HASIL
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
            "━━━━━━━━━━━━━━━━━━\n"
            "🧠 <b>XAU AI FUNDAMENTAL</b>\n\n"
            "News difilter berdasarkan potensi "
            "dampaknya terhadap USD dan XAUUSD.\n\n"
            "⚠️ Gunakan bersama price action, "
            "SMC dan konfirmasi market."
        )

        # =================================================
        # TELEGRAM LIMIT
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
            "❌ NEWS ERROR:",
            repr(e)
        )

        try:

            await loading.edit_text(
                "❌ <b>XAU AI NEWS ENGINE</b>\n\n"
                "Terjadi kesalahan saat mengambil "
                "atau menganalisis berita.\n\n"
                "🔄 Silakan coba kembali.",
                parse_mode="HTML"
            )

        except Exception as edit_error:

            print(
                "❌ GAGAL EDIT LOADING:",
                repr(edit_error)
            )
