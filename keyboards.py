from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]
], resize_keyboard=True)

inline_keyboard_links = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Видео", callback_data='video', url='https://www.youtube.com/watch?v=9bZkp7q19f0')],
   [InlineKeyboardButton(text="Новости", callback_data='news', url='https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtRnlHZ0pCUlNnQVAB?hl=ru&gl=RU&ceid=RU:ru')],
   [InlineKeyboardButton(text="Музыка", callback_data='music', url='https://music.yandex.by/home')]
])

inline_keyboard_dynamic = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='more')]
])

more = ["Опция 1", "Опция 2"]

async def options_keaboard():
    keyboard = InlineKeyboardBuilder()
    for key in more:
        keyboard.add(InlineKeyboardButton(text=key, callback_data=f'option {key}'))

    return keyboard.adjust(2).as_markup()

