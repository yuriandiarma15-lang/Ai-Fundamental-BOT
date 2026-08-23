import asyncio

from aiogram import Router

from aiogram.filters import Command

from aiogram.types import Message

from services.news_cache import (
    refresh_news
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

    print(
        "🔥 /NEWS DITERIMA"
    )


    # =====================================================
    # LOADING
    # =====================================================

    loading = await message.answer(

        "📰 <b>XAU AI NEWS ENGINE</b>\n\n"

        "⏳ <b>Sedang memproses...</b>\n\n"

        "📡 Mengambil berita fundamental...\n"
        "🥇 XAUUSD / Gold\n"
        "💵 USD\n"
        "🏦 Federal Reserve\n"
        "📊 Data ekonomi AS",

        parse_mode="HTML"

    )


    try:

        await asyncio.sleep(
            0.5
        )


        await loading.edit_text(

            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"

            "🔎 <b>Menganalisis berita...</b>\n\n"

            "🥇 Gold / XAUUSD\n"
            "💵 USD\n"
            "🏦 Federal Reserve\n"
            "📊 CPI / NFP / PCE / GDP",

            parse_mode="HTML"

        )


        # =================================================
        # CACHE
        # =================================================

        _, high_impact = await asyncio.to_thread(

            refresh_news

        )


        # =================================================
        # NO NEWS
        # =================================================

        if not high_impact:

            await loading.edit_text(

                "📰 <b>XAU AI FUNDAMENTAL</b>\n\n"

                "✅ Analisis selesai.\n\n"

                "⚪ Belum ada High Impact News "
                "yang relevan terhadap XAUUSD.\n\n"

                "🤖 XAU AI",

                parse_mode="HTML"

            )

            return


        # =================================================
        # RESULT
        # =================================================

        text = (

            "📰 <b>XAU AI HIGH IMPACT NEWS</b>\n\n"

            "🇺🇸 <b>Berita yang berpotensi "
            "mempengaruhi USD / XAUUSD</b>\n\n"

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
                "GNews"
            )


            text += (

                "🔥 <b>"
                + title
                + "</b>\n"

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

            "Data diperbarui maksimal "
            "setiap 60 menit.\n\n"

            "⚠️ Gunakan bersama SMC, "
            "price action dan konfirmasi market."

        )


        await loading.edit_text(

            text,

            parse_mode="HTML",

            disable_web_page_preview=True

        )


        print(
            "✅ /NEWS SELESAI"
        )


    except Exception as e:

        print(
            "❌ NEWS ERROR:",
            repr(e)
        )


        try:

            await loading.edit_text(

                "❌ <b>NEWS ENGINE ERROR</b>\n\n"

                "Terjadi kesalahan saat mengambil "
                "berita.\n\n"

                "🔄 Silakan coba lagi.",

                parse_mode="HTML"

            )

        except Exception:

            pass
