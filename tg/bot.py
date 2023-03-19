from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from create_bot import bot, dispatcher
from commands import register_handlers

async def on_startup(_):
    print("Бот онлайн!")


register_handlers(dispatcher)
executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)
