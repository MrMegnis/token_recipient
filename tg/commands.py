from tg.create_bot import dispatcher
from aiogram import types, Dispatcher

async def start(message : types.Message):
    await message.answer("Gigashitposter bot!")

async def help(message: types.Message):
    await message.answer("Gigashitposter bot!")

async def echo(message : types.Message):
    await message.answer(message.text)


def register_handlers(dp : Dispatcher):
    # dp.register_message_handler(echo)
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help, commands=["help"])