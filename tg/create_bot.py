from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from token import token
import os

bot = Bot(token=os.getenv("BOTTOKEN"))
dispatcher = Dispatcher(bot)
