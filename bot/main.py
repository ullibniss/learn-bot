#!venv/bin/python
from aiogram import types

from utils import get_keyboard

async def entrypoint(message: types.Message):
    keyboard = get_keyboard()
    keyboard.add(types.InlineKeyboardButton(text="Настройки", callback_data="settings"))
    keyboard.add(types.InlineKeyboardButton(text="Начать тест", callback_data="start_test"))
    await message.answer(text="Привет, это учебный бот лехи", reply_markup=keyboard)

async def entrypoint_callback(call: types.CallbackQuery):
    keyboard = get_keyboard()
    keyboard.add(types.InlineKeyboardButton(text="Настройки", callback_data="settings"))
    keyboard.add(types.InlineKeyboardButton(text="Начать тест", callback_data="start_test"))
    await call.message.edit_text("Привет, это учебный бот лехи")
    await call.message.edit_reply_markup(keyboard)


