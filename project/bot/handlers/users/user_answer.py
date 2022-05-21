from aiogram import types
from project.messages import USER_ANSWER_TEXT


async def user_answer(msg: types.Message):
    await msg.answer(USER_ANSWER_TEXT)
