from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio

# Bot tokeningiz
TOKEN = "8272777997:AAHuvA2doPRY2cp-I4qmb31JuUaNL2miKH0"

# Linklaringiz
VOTE_LINK = "https://openbudget.uz/sizning_link"        # ovoz berish link
SUPPORT_LINK = "https://t.me/mingboyev133"              # support (admin)
GROUP_LINK = "https://t.me/YaxshilikJamoasiGuruhi"      # telegram guruh

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    # Tugmalar
    buttons = [
        [types.InlineKeyboardButton(text="🗳 Ovoz berish", url=VOTE_LINK)],
        [types.InlineKeyboardButton(text="📞 Support (Admin)", url=SUPPORT_LINK)],
        [types.InlineKeyboardButton(text="👥 Telegram Guruh", url=GROUP_LINK)]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}! 👋\n\n"
        "Quyidagi tugmalardan foydalanishingiz mumkin:",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
