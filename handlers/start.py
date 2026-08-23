from aiogram import Router

from aiogram.filters import CommandStart

from aiogram.types import Message


router = Router()


@router.message(
    CommandStart()
)
async def start(
    message: Message
):

    await message.answer(
        """
🤖 <b>XAU AI FUNDAMENTAL</b>

Selamat datang.

Bot ini memberikan:

📰 Fundamental Gold
🚨 High Impact News
⏰ Prepare 30 menit sebelum news
📊 Actual / Forecast / Previous
🎯 Area harga XAUUSD
🔗 Sumber berita resmi

Gunakan:

/news

untuk melihat fundamental terbaru.
""",
        parse_mode="HTML"
    )
