from aiogram import Bot, Dispatcher, executor, types
from utils import get_keyboard
from os import listdir
from test import Test

async def settings(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Общие", callback_data="general_settings"),
        types.InlineKeyboardButton(text="Выбрать тест", callback_data="choose_test_settings")
    ]
    buttons.append(types.InlineKeyboardButton(text="Назад", callback_data="entrypoint"))
    keyboard = get_keyboard(buttons, 1)
    await call.message.edit_text("Настроки:")
    await call.message.edit_reply_markup(keyboard)

async def choose_test(call: types.CallbackQuery):
    tests = listdir("../tests")
    buttons = []
    for test in tests:
        buttons.append(types.InlineKeyboardButton(text=f"{test[:-5] + (' <--' if test[:-5] == Test.test_name else '')}️", callback_data=f"test:{test[:-5]}"))
    buttons.append(types.InlineKeyboardButton(text="Назад", callback_data="settings"))
    await call.message.edit_text("Выберите тест:")
    await call.message.edit_reply_markup(get_keyboard(buttons, 1))

async def set_test(call: types.CallbackQuery):
    test_name = call.data.split(":")[1]
    Test.test_name = test_name
    await choose_test(call)