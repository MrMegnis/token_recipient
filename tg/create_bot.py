from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from token import token

bot = Bot(token=token)
dispatcher = Dispatcher(bot)
