import asyncio

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.news_engine import (
    collect_official_news,
    find_high_impact_news
)


router = Router()


@router.message(Command("news"))
async def news_command(
    message: Message
):

    print(
        "🔥 /news MASUK"
    )

    # ==============================
    # LOADING
    # ==============================

    loading = await message.answer(
        "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
        "⏳ <b>Memproses...</b>\n\n"
        "📡 Mengambil berita pasar...\n"
        "🥇 Gold / XAUUSD\n"
        "💵 USD\n"
        "🏦 Federal Reserve\n\n"
        "Mohon tunggu...",
        parse_mode="HTML"
    )

    try:

        await asyncio.sleep(
            1
        )

        await loading.edit_text(
            "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
            "🔎 <b>Menganalisis relevansi...</b>\n\n"
            "🥇 XAUUSD\n"
            "💵 USD\n"
            "🏦 FOMC / Federal Reserve\n"
            "📊 CPI / PCE / NFP\n\n"
            "Menyaring berita yang berpotensi "
            "mempengaruhi Gold...",
            parse_mode="HTML"
        )

        # ==============================
        # AMBIL NEWS
        # ==============================

        news = await asyncio.to_thread(
            collect_official_news
        )

        print(
            "📰 Total news:",
            len(news)
        )

        # ==============================
        # FILTER
        # ==============================

        high_impact = await asyncio.to_thread(
            find_high_impact_news,
            news
        )

        print(
            "🔥 Relevant news:",
            len(high_impact)
        )

        # ==============================
        # TIDAK ADA
        # ==============================

        if not high_impact:

            await loading.edit_text(
                "📰 <b>XAU AI NEWS</b>\n\n"
                "⚪ Tidak ditemukan berita penting "
                "yang relevan terhadap USD / XAUUSD "
                "saat ini.",
                parse_mode="HTML"
            )

            return

        # ==============================
        # HASIL
        # ==============================

        text = (
            "📰 <b>XAU AI HIGH IMPACT NEWS</b>\n\n"
            "🇺🇸 Berita yang berpotensi "
            "mempengaruhi USD / XAUUSD\n\n"
        )

        for item in high_impact[:7]:

            title = item.get(
                "title",
                "-"
            )

            link = item.get(
                "link",
                ""
            )

            source = item.get(
                "source",
                "Google News"
            )

            text += (
                f"🔥 <b>{title}</b>\n"
                f"📰 {source}\n"
            )

            if link:

                text += (
                    f'<a href="{link}">'
                    "🔗 Baca berita"
                    "</a>\n"
                )

            text += "\n"

        text += (
            "━━━━━━━━━━━━━━━━━━\n"
            "🤖 <b>XAU AI FUNDAMENTAL</b>\n\n"
            "Berita difilter khusus berdasarkan "
            "potensi dampaknya terhadap USD dan Gold."
        )

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

        await loading.edit_text(
            "❌ <b>NEWS ERROR</b>\n\n"
            "Gagal mengambil berita.\n\n"
            f"<code>{str(e)[:400]}</code>",
            parse_mode="HTML"
        )
