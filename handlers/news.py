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

    print(
        "📰 /news diterima"
    )


    # =====================================================
    # LOADING LANGSUNG
    # =====================================================

    loading = await message.answer(

        "📰 <b>XAU AI NEWS ENGINE</b>\n\n"

        "⏳ <b>Sedang memproses...</b>\n\n"

        "📡 Mengambil berita terbaru...\n"
        "🏦 Memeriksa Federal Reserve...\n"
        "🏛️ Memeriksa U.S. Treasury...\n"
        "📊 Memeriksa BLS...\n\n"

        "Mohon tunggu sebentar...",

        parse_mode="HTML"

    )


    print(
        "📰 Loading /news berhasil dikirim"
    )


    try:

        # =================================================
        # LOADING ANIMATION
        # =================================================

        await asyncio.sleep(
            1
        )


        await loading.edit_text(

            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"

            "⏳ <b>MENGAMBIL BERITA...</b>\n\n"

            "📡 Menghubungkan ke sumber resmi...\n"
            "🏦 Federal Reserve\n"
            "🏛️ U.S. Treasury\n"
            "📊 Bureau of Labor Statistics",

            parse_mode="HTML"

        )


        # =================================================
        # AMBIL NEWS
        #
        # PENTING:
        # dijalankan di thread supaya Telegram
        # tidak ikut macet.
        # =================================================

        news = await asyncio.to_thread(

            collect_official_news

        )


        print(
            f"📰 Total berita ditemukan: {len(news)}"
        )


        # =================================================
        # UPDATE LOADING
        # =================================================

        await loading.edit_text(

            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"

            "✅ Data berita berhasil diperoleh.\n\n"

            "🔎 <b>Menganalisis relevansi XAUUSD...</b>\n\n"

            "💵 USD\n"
            "🥇 Gold / XAUUSD\n"
            "🏦 Federal Reserve\n"
            "📊 Data ekonomi AS",

            parse_mode="HTML"

        )


        await asyncio.sleep(
            0.8
        )


        # =================================================
        # FILTER HIGH IMPACT
        # =================================================

        high_impact = await asyncio.to_thread(

            find_high_impact_news,

            news

        )


        print(
            f"🔥 High Impact ditemukan: {len(high_impact)}"
        )


        # =================================================
        # TIDAK ADA NEWS
        # =================================================

        if not high_impact:

            await loading.edit_text(

                "📰 <b>FUNDAMENTAL XAUUSD</b>\n\n"

                "✅ Analisis selesai.\n\n"

                "⚪ Saat ini belum ditemukan "
                "High Impact News yang relevan "
                "terhadap XAUUSD dari sumber resmi.\n\n"

                "🤖 <b>XAU AI FUNDAMENTAL</b>",

                parse_mode="HTML"

            )

            return


        # =================================================
        # HASIL
        # =================================================

        text = (

            "📰 <b>XAU AI HIGH IMPACT NEWS</b>\n\n"

            "🇺🇸 <b>NEWS YANG BERPENGARUH "
            "TERHADAP XAUUSD / USD</b>\n\n"

        )


        # Maksimal 5 berita

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
        # BATAS TELEGRAM
        # =================================================

        if len(text) > 4000:

            text = (
                text[:3900]
                + "\n\n..."
            )


        # =================================================
        # GANTI LOADING MENJADI HASIL
        # =================================================

        await loading.edit_text(

            text,

            parse_mode="HTML",

            disable_web_page_preview=True

        )


        print(
            "✅ /news selesai"
        )


    except Exception as e:

        print(
            "❌ NEWS ERROR:",
            repr(e)
        )


        # =================================================
        # ERROR MESSAGE
        # =================================================

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
                "❌ Gagal mengubah loading:",
                repr(edit_error)
            )
