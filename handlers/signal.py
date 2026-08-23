from aiogram import Router

from aiogram.filters import Command

from aiogram.types import Message

from services.news_engine import (
    collect_official_news,
    find_high_impact_news
)


router = Router()


@router.message(
    Command("news")
)
async def news_command(
    message: Message
):

    news = collect_official_news()

    high_impact = (
        find_high_impact_news(
            news
        )
    )

    if not high_impact:

        await message.answer(
            """
📰 <b>FUNDAMENTAL XAUUSD</b>

Saat ini belum ditemukan
High Impact News dari sumber
resmi yang terdeteksi.

🤖 XAU AI FUNDAMENTAL
""",
            parse_mode="HTML"
        )

        return

    text = (
        "📰 <b>HIGH IMPACT NEWS</b>\n\n"
    )

    for item in high_impact[:5]:

        title = item.get(
            "title",
            "-"
        )

        link = item.get(
            "link",
            ""
        )

        text += (
            f"🔥 <b>{title}</b>\n"
            f'<a href="{link}">'
            f"Official Source"
            f"</a>\n\n"
        )

    await message.answer(
        text,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
