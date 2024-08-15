import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import random

from gtts import gTTS
import os

from config import TOKEN
import keyboards as kb


bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, я - бот. Нажми на кнопку - получишь результат', reply_markup=kb.main)

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer(f'Этот бот умеет выполнять команды: \n /start \n /links \n /dynamic')

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f'Выбери категорию, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_links)

@dp.callback_query(F.data == 'video')
async def video(callback: CallbackQuery):
    await callback.answer("Видео подгружается", show_alert=True)
    await callback.message.answer('Вот свежие видео!')

@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
    await callback.answer("Новости подгружаются", show_alert=True)
    await callback.message.answer('Вот свежие новости!')

@dp.callback_query(F.data == 'music')
async def music(callback: CallbackQuery):
    await callback.answer("Музыка подгружается", show_alert=True)
    await callback.message.answer('Вот хитовая музыка!')

@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer(f'Показать больше', reply_markup=kb.inline_keyboard_dynamic)

@dp.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
    await callback.answer("Опции подгружаются")
    await callback.message.edit_text('Выбери опцию', reply_markup=await kb.options_keaboard())

@dp.callback_query(F.data == 'Опция 1')
async def option_1(callback: CallbackQuery):
    # Отправляем сообщение с названием клавиши
    await callback.message.answer(f"Опция 1")
    # Не забываем ответить на callback, чтобы убрать "часики"
    await callback.answer()

@dp.callback_query(F.data == 'Опция 2')
async def option_2(callback: CallbackQuery):
    # Отправляем сообщение с названием клавиши
    await callback.message.answer(f"Опция 2")
    # Не забываем ответить на callback, чтобы убрать "часики"
    await callback.answer()


@dp.message(F.text == "Привет")
async def hello(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.main)

@dp.message(F.text == "Пока")
async def bye(message: Message):
    await message.answer(f'Пока, {message.from_user.first_name}', reply_markup=kb.main)



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())