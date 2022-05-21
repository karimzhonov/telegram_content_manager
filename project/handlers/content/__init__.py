from aiogram import Dispatcher, types
from aiogram.types.message import ContentType
from .delete_message_about_user import delete_message_about_user

chat_type = [types.ChatType.GROUP, types.ChatType.CHANNEL, types.ChatType.SUPERGROUP]


def setup(dp: Dispatcher):
    dp.register_message_handler(delete_message_about_user, chat_type=chat_type,
                                content_types=[ContentType.NEW_CHAT_MEMBERS, ContentType.LEFT_CHAT_MEMBER])
