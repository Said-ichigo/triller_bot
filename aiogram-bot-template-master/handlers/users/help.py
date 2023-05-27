from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyrıqlar: ",
            "/start - Bottı iske túsiriw",
            "/help - Járdem",
            "/game - bul oyindasiz sizge 777 sani tuse utasiz!")
    
    await message.answer("\n".join(text))
