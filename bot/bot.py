from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
import logging

from bot.main import entrypoint, entrypoint_callback
from bot.settings import settings, choose_test, set_test
from bot.test import start_test, begin

bot = Bot(token="5516304149:AAGA_QenjbbN7cTu5oOjPgtDJecEhNMWdyc")
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

def register_db(dp: Dispatcher):
    dp.register_message_handler(entrypoint, commands="start")
    dp.register_callback_query_handler(entrypoint_callback, text="entrypoint")
    dp.register_callback_query_handler(settings, text="settings")
    dp.register_callback_query_handler(choose_test, text="choose_test_settings")
    dp.register_callback_query_handler(set_test, Text(startswith="test"))
    dp.register_callback_query_handler(start_test, text="start_test")
    dp.register_callback_query_handler(begin, Text(startswith="begin"))

if __name__ == "__main__":
    register_db(dp)
    executor.start_polling(dp, skip_updates=True)

