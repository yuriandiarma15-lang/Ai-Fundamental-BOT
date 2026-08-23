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

@router.message(
    Command("news")
)
async def news_command(
    message: Message
):

    # =====================================================
    # LOADING AWAL
    # =====================================================

    loading = await message.answer(
        "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
        "⏳ <b>Memulai proses...</b>\n\n"
        "🔄 Mohon tunggu...",
        parse_mode="HTML"
    )

    try:

        # =================================================
        # STEP 1
        # =================================================

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "⏳ <b>Mengambil berita terbaru...</b>\n\n"
            "📡 Menghubungi sumber resmi\n"
            "🏦 Memeriksa Federal Reserve\n"
            "📊 Memeriksa BLS\n\n"
            "🔄 Sedang memproses...",
            parse_mode="HTML"
        )

        news_list = await asyncio.to_thread(
            collect_official_news
        )


        # =================================================
        # STEP 2
        # =================================================

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "✅ Berita berhasil diterima\n\n"
            "🔍 <b>Memfilter berita...</b>\n\n"
            "🇺🇸 Memeriksa berita USD\n"
            "🥇 Memeriksa relevansi XAUUSD\n"
            "🔥 Memeriksa High Impact...",
            parse_mode="HTML"
        )

        high_impact = await asyncio.to_thread(
            find_high_impact_news,
            news_list
        )


        # =================================================
        # NO NEWS
        # =================================================

        if not high_impact:

            await loading.edit_text(
                "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
                "✅ <b>Proses selesai</b>\n\n"
                "⚪ Tidak ditemukan High Impact News "
                "yang relevan dengan XAUUSD.",
                parse_mode="HTML"
            )

            return


        # =================================================
        # STEP 3
        # =================================================

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "✅ Berita ditemukan\n"
            f"🔥 High Impact: <b>{len(high_impact)}</b>\n\n"
            "🧠 Menyiapkan hasil...\n"
            "📊 Menyusun data...\n"
            "⏳ Hampir selesai...",
            parse_mode="HTML"
        )


        # =================================================
        # BUILD RESULT
        # =================================================

        lines = [
            "📰 <b>HIGH IMPACT NEWS</b>",
            ""
        ]


        for news in high_impact:

            title = news.get(
                "title",
                "-"
            )

            source_url = news.get(
                "source_url",
                ""
            )

            if not source_url:

                source_url = news.get(
                    "link",
                    ""
                )


            lines.append(
                f"🔥 <b>{title}</b>"
            )


            if source_url:

                lines.append(
                    f'<a href="{source_url}">'
                    "🔗 Official Source</a>"
                )


            lines.append("")


        result = "\n".join(
            lines
        )


        # =================================================
        # FINAL RESULT
        # =================================================

        await loading.edit_text(
            result,
            parse_mode="HTML"
        )


    except Exception as e:

        print(
            "NEWS ERROR:",
            e
        )


        await loading.edit_text(
            "❌ <b>NEWS ENGINE ERROR</b>\n\n"
            "Bot mengalami masalah saat mengambil berita.\n\n"
            "🔄 Silakan coba lagi.",
            parse_mode="HTML"
        )
