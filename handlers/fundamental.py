import asyncio

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.news_engine import (
    collect_official_news,
    find_high_impact_news
)

from services.news_result import (
    process_news_result
)

from services.economic_calendar import (
    EconomicEvent
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

    loading = await message.answer(
        "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
        "⏳ Sedang mengambil berita terbaru...\n\n"
        "📡 Memeriksa sumber resmi\n"
        "🏦 Memeriksa Federal Reserve\n"
        "🏛️ Memeriksa Treasury\n"
        "📊 Memeriksa BLS\n"
        "🔥 Memfilter High Impact News\n\n"
        "Mohon tunggu sebentar...",
        parse_mode="HTML"
    )

    try:

        news_list = await asyncio.to_thread(
            collect_official_news
        )

        high_impact = await asyncio.to_thread(
            find_high_impact_news,
            news_list
        )

        if not high_impact:

            await loading.edit_text(
                "📰 <b>XAU AI NEWS ENGINE</b>\n\n"
                "✅ Tidak ditemukan High Impact News "
                "dari sumber resmi saat ini.",
                parse_mode="HTML"
            )

            return

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

            lines.append(
                f"🔥 <b>{title}</b>"
            )

            if source_url:

                lines.append(
                    f'<a href="{source_url}">'
                    "Official Source</a>"
                )

            lines.append("")

        await loading.edit_text(
            "\n".join(lines),
            parse_mode="HTML"
        )

    except Exception as e:

        print(
            "NEWS ERROR:",
            e
        )

        await loading.edit_text(
            "❌ <b>Gagal mengambil berita.</b>\n\n"
            "Silakan coba kembali beberapa saat lagi.",
            parse_mode="HTML"
        )


# =========================================================
# /FUNDAMENTAL
# =========================================================

@router.message(
    Command("fundamental")
)
async def fundamental_command(
    message: Message
):

    loading = await message.answer(
        "🧠 <b>XAU AI FUNDAMENTAL ENGINE</b>\n\n"
        "⏳ Sedang melakukan analisis...\n\n"
        "📡 Mengambil berita resmi\n"
        "🏦 Federal Reserve\n"
        "🏛️ Treasury\n"
        "📊 BLS\n"
        "🧠 Menganalisis fundamental\n"
        "🥇 Menganalisis dampak terhadap XAUUSD\n"
        "📍 Menghitung area harga\n\n"
        "Mohon tunggu sebentar...",
        parse_mode="HTML"
    )

    try:

        # =================================================
        # AMBIL NEWS
        # =================================================

        news_list = await asyncio.to_thread(
            collect_official_news
        )

        high_impact = await asyncio.to_thread(
            find_high_impact_news,
            news_list
        )

        if not high_impact:

            await loading.edit_text(
                "🧠 <b>XAU AI FUNDAMENTAL</b>\n\n"
                "⚪ Belum ada High Impact News "
                "yang dapat dianalisis.",
                parse_mode="HTML"
            )

            return

        lines = [
            "🧠 <b>XAU AI FUNDAMENTAL</b>",
            "",
            "🥇 <b>XAUUSD FUNDAMENTAL ANALYSIS</b>",
            "━━━━━━━━━━━━━━",
            ""
        ]

        # =================================================
        # ANALISIS SETIAP NEWS
        # =================================================

        for news in high_impact:

            title = news.get(
                "title",
                "-"
            )

            actual = news.get(
                "actual",
                "-"
            )

            forecast = news.get(
                "forecast",
                "-"
            )

            previous = news.get(
                "previous",
                "-"
            )

            event_time = news.get(
                "event_time"
            )

            source_name = news.get(
                "source_name",
                "Official Source"
            )

            source_url = news.get(
                "source_url",
                ""
            )

            # =============================================
            # BUAT ECONOMIC EVENT
            # =============================================

            if not event_time:

                from datetime import datetime

                event_time = datetime.now()

            event = EconomicEvent(

                title=title,

                event_time=event_time,

                impact="HIGH",

                country=news.get(
                    "country",
                    "US"
                ),

                forecast=forecast,

                previous=previous,

                actual=actual,

                source_name=source_name,

                source_url=source_url

            )

            # =============================================
            # PROCESS FUNDAMENTAL
            # =============================================

            result = await asyncio.to_thread(
                process_news_result,
                event
            )

            # =============================================
            # HASIL
            # =============================================

            lines.append(
                f"🔥 <b>{title}</b>"
            )

            lines.append("")

            lines.append(
                f"📊 Actual: {actual}"
            )

            lines.append(
                f"📈 Forecast: {forecast}"
            )

            lines.append(
                f"📉 Previous: {previous}"
            )

            lines.append("")

            if result:

                lines.append(
                    str(result)
                )

            if source_url:

                lines.append("")

                lines.append(
                    f'<a href="{source_url}">'
                    f"🔗 {source_name}</a>"
                )

            lines.append(
                "\n━━━━━━━━━━━━━━\n"
            )

        # =================================================
        # KIRIM HASIL
        # =================================================

        final_text = "\n".join(
            lines
        )

        await loading.edit_text(
            final_text,
            parse_mode="HTML"
        )

    except Exception as e:

        print(
            "FUNDAMENTAL ERROR:",
            e
        )

        await loading.edit_text(
            "❌ <b>Fundamental analysis gagal.</b>\n\n"
            "Silakan coba kembali beberapa saat lagi.",
            parse_mode="HTML"
        )
