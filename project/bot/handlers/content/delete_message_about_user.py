from aiogram import types
from loguru import logger


async def delete_message_about_user(msg: types.Message):
    logger.info(f'Deleted user message {msg.from_user.id} from channel "{msg.chat.id}"')
    await msg.delete()
