from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


# =========================================================
# /START
# =========================================================

@router.message(
    CommandStart()
)
async def start(
    message: Message
):

    await message.answer(

        """
🤖 <b>XAU AI FUNDAMENTAL</b>

Selamat datang di
<b>XAU AI FUNDAMENTAL ENGINE</b>.

━━━━━━━━━━━━━━━━━━

📰 <b>FITUR BOT</b>

📰 Fundamental Gold
🚨 High Impact News
⏰ Prepare 30 menit sebelum news
📊 Actual / Forecast / Previous
🎯 Area harga XAUUSD
💵 Analisis USD
🏦 Analisis Federal Reserve
🔗 Sumber berita resmi

━━━━━━━━━━━━━━━━━━

📌 <b>COMMAND</b>

📰 /news
Melihat High Impact News yang
berpotensi memengaruhi XAUUSD.

📊 /signal
Melihat signal trading XAUUSD.

━━━━━━━━━━━━━━━━━━

⚠️ <b>CATATAN</b>

Analisis fundamental digunakan sebagai
konfirmasi tambahan dan bukan jaminan
pergerakan harga.

━━━━━━━━━━━━━━━━━━

🤖 <b>XAU AI FUNDAMENTAL</b>
""",

        parse_mode="HTML"

    )
