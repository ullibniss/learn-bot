from aiogram import types
import json

def get_keyboard(buttons: list = [], row_width: int = 2):
    keyboard = types.InlineKeyboardMarkup(row_width=row_width)
    keyboard.add(*buttons)
    return keyboard

def parse_test_json(filename: str) -> dict:
    with open("tests/" + filename, "r") as f:
        data = json.load(f)
        f.close()
        return data
