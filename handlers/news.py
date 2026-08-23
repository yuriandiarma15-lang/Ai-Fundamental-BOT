from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("news"))
async def news_command(message: Message):

    print("🔥🔥🔥 /NEWS MASUK HANDLER 🔥🔥🔥")

    await message.answer(
        "🟢 <b>NEWS HANDLER BERFUNGSI</b>\n\n"
        "Bot menerima command /news.",
        parse_mode="HTML"
    )
