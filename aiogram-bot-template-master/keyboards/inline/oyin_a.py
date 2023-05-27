from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

game = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('✊',callback_data='tas'),
            InlineKeyboardButton('✌️',callback_data='qayshi'),
            InlineKeyboardButton('🤚',callback_data='qagaz')
        ]
    ]
)