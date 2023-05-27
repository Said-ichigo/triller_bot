from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.kino_a import moves_menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Sálem, {message.from_user.full_name}! bul bot xush kelip siz."
                        f"Bot sizge hazirgikundegi eng kop korilip atirgan kino ham animelerdi korsetedi",
                        reply_markup=moves_menu)
