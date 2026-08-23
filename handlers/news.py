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

    print(
        f"📰 /news RECEIVED | "
        f"user_id={message.from_user.id if message.from_user else '-'}"
    )

    # =====================================================
    # LOADING LANGSUNG
    # =====================================================

    loading = await message.answer(
        "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
        "⏳ <b>BOT SEDANG MEMPROSES...</b>\n\n"
        "📡 Mengambil berita terbaru...\n"
        "🏦 Memeriksa Federal Reserve...\n"
        "🏛️ Memeriksa U.S. Treasury...\n"
        "📊 Memeriksa BLS...\n\n"
        "Mohon tunggu...",
        parse_mode="HTML"
    )

    print(
        "📰 Loading message berhasil dikirim."
    )

    try:

        # =================================================
        # STATUS 1
        # =================================================

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "⏳ <b>MENGAMBIL BERITA...</b>\n\n"
            "📡 Menghubungkan ke sumber resmi...",
            parse_mode="HTML"
        )

        # =================================================
        # AMBIL BERITA
        # =================================================

        news_list = await asyncio.to_thread(
            collect_official_news
        )

        print(
            f"📰 Total news: {len(news_list)}"
        )


        # =================================================
        # STATUS 2
        # =================================================

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "✅ Berita berhasil diambil.\n\n"
            "🔎 Sedang memfilter berita "
            "yang berpengaruh terhadap XAUUSD...",
            parse_mode="HTML"
        )


        # =================================================
        # FILTER
        # =================================================

        high_impact = await asyncio.to_thread(
            find_high_impact_news,
            news_list
        )

        print(
            f"🔥 High impact news: {len(high_impact)}"
        )


        # =================================================
        # TIDAK ADA HASIL
        # =================================================

        if not high_impact:

            await loading.edit_text(
                "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
                "✅ Analisis selesai.\n\n"
                "⚪ Tidak ditemukan berita High Impact "
                "yang relevan terhadap XAUUSD saat ini.",
                parse_mode="HTML"
            )

            return


        # =================================================
        # HASIL
        # =================================================

        lines = [

            "📰 <b>XAU AI HIGH IMPACT NEWS</b>",
            "",
            "🇺🇸 <b>NEWS YANG BERDAMPAK KE XAUUSD</b>",
            ""
        ]


        for news in high_impact:

            title = news.get(
                "title",
                "-"
            )


            source_url = news.get(
                "source_url",
                news.get(
                    "link",
                    ""
                )
            )


            source_name = news.get(
                "source_name",
                news.get(
                    "source",
                    "Official Source"
                )
            )


            lines.append(
                f"🔥 <b>{title}</b>"
            )


            if source_url:

                lines.append(
                    f'<a href="{source_url}">'
                    f"🔗 {source_name}"
                    "</a>"
                )


            lines.append("")


        result = "\n".join(
            lines
        )


        if len(result) > 4000:

            result = (
                result[:3900]
                + "\n\n..."
            )


        await loading.edit_text(
            result,
            parse_mode="HTML",
            disable_web_page_preview=True
        )


        print(
            "✅ /news selesai."
        )


    except Exception as e:

        print(
            "❌ NEWS ERROR:",
            repr(e)
        )


        try:

            await loading.edit_text(
                "❌ <b>NEWS ENGINE ERROR</b>\n\n"
                "Terjadi kesalahan saat mengambil berita.\n\n"
                "🔄 Silakan coba lagi.",
                parse_mode="HTML"
            )

        except Exception as edit_error:

            print(
                "❌ ERROR EDIT LOADING:",
                repr(edit_error)
            )
