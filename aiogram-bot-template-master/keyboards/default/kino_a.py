from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

moves_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎥kinolar"),
            KeyboardButton(text="🇯🇵Animelar"),
            KeyboardButton(text="🎞Seryalar")
        ],
        [
            KeyboardButton(text="🕹Oyin"),
            KeyboardButton(text="locaatsiya",request_contact=True)
        ]
    ],
resize_keyboard=True
)
