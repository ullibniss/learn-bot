import copy

from aiogram import types
from copy import deepcopy

from utils import get_keyboard, parse_test_json
from time import sleep
from random import shuffle

class Test:
    test_name = "nmap_scan_flags"
    data = None
    stats = []

async def start_test(call: types.CallbackQuery):

    buttons = [
        types.InlineKeyboardButton(text="Начать", callback_data="begin"),
    ]

    await call.message.edit_text(f"""
Привет

Сейчас будет тест на тему: { Test.test_name } 

Каждое задание будет состоять из вопроса и четырех ответов,

Удачи
""")
    await call.message.edit_reply_markup(get_keyboard(buttons))

async def begin(call: types.CallbackQuery):
    previous_answer = None
    if not Test.data:
        Test.data = parse_test_json(Test.test_name + ".json")
        shuffle(Test.data["tasks"])

    data = call.data.split(":")

    if len(data) == 1:
        task_num = 0
    else:
        task_num = int(data[1])
        previous_answer = int(data[2])


    if previous_answer:
        Test.stats.append({
            f"actual_answer": previous_answer,
            "correct_answer": Test.data["tasks"][task_num-1]["correct_answer"],
            "is_correct": previous_answer == Test.data["tasks"][task_num-1]["correct_answer"]
        })

    if "answers" in Test.data["tasks"][task_num]:
        shuffle(Test.data["tasks"][task_num]["answers"])
        buttons = [types.InlineKeyboardButton(text=Test.data["tasks"][task_num]["answers"][i]["answer"], callback_data=f"begin:{task_num+1}:{i+1}") for i in range(len(Test.data["tasks"][task_num]["answers"]))]
        await call.message.edit_text(Test.data["tasks"][task_num]["question"])
        await call.message.edit_reply_markup(get_keyboard(buttons, 1))
    else:
        await end(call)

async def end(call: types.CallbackQuery):
    text=""
    total=0
    for i in range(len(Test.stats)):
        if Test.stats[i]["is_correct"]:
            total += 1

        text = f"""{text}
---
Вопрос {i+1}:
Ваш ответ: {Test.stats[i]['actual_answer']}        
Правильный ответ: {Test.stats[i]['correct_answer']}
Решено?: {'Да' if Test.stats[i]["is_correct"] else 'Нет'}
"""
    text = f"""{text}
---
Результат: { total } / {len(Test.stats)}
"""
    buttons = [
        types.InlineKeyboardButton(text="В начало", callback_data="entrypoint"),
        types.InlineKeyboardButton(text="Еще раз", callback_data="begin")
    ]
    Test.stats = []
    Test.data = []
    await call.message.edit_text(text)
    await call.message.edit_reply_markup(get_keyboard(buttons, 1))