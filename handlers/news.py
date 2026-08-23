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
# LOADING ANIMATION
# =========================================================

async def loading_animation(
    message: Message,
    stop_event: asyncio.Event
):

    loading_messages = [

        (
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "⏳ Menghubungkan ke sumber berita resmi..."
        ),

        (
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "📡 Mengambil berita terbaru..."
        ),

        (
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "🏦 Memeriksa Federal Reserve..."
        ),

        (
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "📊 Memeriksa data ekonomi AS..."
        ),

        (
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "🥇 Menganalisis relevansi terhadap XAUUSD..."
        ),

        (
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "🔥 Memfilter High Impact News..."
        ),

    ]


    index = 0


    while not stop_event.is_set():

        try:

            await message.edit_text(
                loading_messages[index],
                parse_mode="HTML"
            )

        except Exception:

            pass


        index = (
            index + 1
        ) % len(
            loading_messages
        )


        try:

            await asyncio.wait_for(
                stop_event.wait(),
                timeout=1.5
            )

        except asyncio.TimeoutError:

            pass


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
    # LANGSUNG BALAS
    # =====================================================

    loading = await message.answer(

        "📰 <b>XAU AI NEWS ENGINE</b>\n\n"

        "⏳ <b>Memulai analisis...</b>\n\n"

        "📡 Menghubungkan ke sumber resmi...\n"
        "🏦 Federal Reserve\n"
        "🏛️ U.S. Treasury\n"
        "📊 Bureau of Labor Statistics\n\n"

        "Mohon tunggu..."

        ,

        parse_mode="HTML"
    )


    # =====================================================
    # START ANIMATION
    # =====================================================

    stop_loading = asyncio.Event()


    loading_task = asyncio.create_task(
        loading_animation(
            loading,
            stop_loading
        )
    )


    try:

        # =================================================
        # AMBIL NEWS
        # =================================================

        news_list = await asyncio.to_thread(
            collect_official_news
        )


        # =================================================
        # FILTER HIGH IMPACT
        # =================================================

        high_impact = await asyncio.to_thread(
            find_high_impact_news,
            news_list
        )


        # =================================================
        # HENTIKAN LOADING
        # =================================================

        stop_loading.set()

        await loading_task


        # =================================================
        # TIDAK ADA NEWS
        # =================================================

        if not high_impact:

            await loading.edit_text(

                "📰 <b>XAU AI NEWS ENGINE</b>\n\n"

                "✅ Analisis selesai.\n\n"

                "Tidak ditemukan High Impact News "
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
            "🇺🇸 <b>US / USD RELATED NEWS</b>",
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


        # =================================================
        # TELEGRAM LIMIT
        # =================================================

        # Telegram maksimal sekitar 4096 karakter.
        # Kita batasi supaya tidak error.

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


    except Exception as e:

        print(
            "NEWS ERROR:",
            repr(e)
        )


        stop_loading.set()


        try:

            await loading_task

        except Exception:

            pass


        await loading.edit_text(

            "❌ <b>XAU AI NEWS ENGINE ERROR</b>\n\n"

            "Terjadi masalah saat mengambil berita.\n\n"

            "🔄 Silakan coba kembali.",

            parse_mode="HTML"

        )
