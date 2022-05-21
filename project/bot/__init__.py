from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from project.bot.settings import BOT_TOKEN


dp = Dispatcher(
    Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML, validate_token=True),
    storage=MemoryStorage()
)