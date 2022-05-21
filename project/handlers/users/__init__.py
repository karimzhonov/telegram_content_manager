from aiogram import types, Dispatcher
from .user_answer import user_answer

chat_type = [types.ChatType.PRIVATE]


def setup(dp: Dispatcher):
    dp.register_message_handler(user_answer, chat_type=chat_type)
