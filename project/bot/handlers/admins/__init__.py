from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.builtin import CommandStart

from project.bot.filters import IsAdminFilter
from project.bot.storage import Session
from .menu import admin_menu
from .post_content import click_post_content_button, sended_photo_for_post, edit_message_post
from .post_content import post_message_to_channel, edited_message_post

chat_type = [types.ChatType.PRIVATE]


def setup(dp: Dispatcher):
    dp.register_message_handler(admin_menu, IsAdminFilter(), CommandStart(), chat_type=chat_type, state='*')
    dp.register_callback_query_handler(click_post_content_button, IsAdminFilter(), lambda c: c.data == 'post_content',
                                       chat_type=chat_type, state='*')
    dp.register_message_handler(sended_photo_for_post, IsAdminFilter(), state=Session.photo,
                                content_types=[types.ContentType.PHOTO])
    dp.register_callback_query_handler(post_message_to_channel, IsAdminFilter(), lambda c: c.data == 'post_message',
                                       chat_type=chat_type, state='*')
    dp.register_callback_query_handler(edit_message_post, IsAdminFilter(), lambda c: c.data == 'edit_message',
                                       chat_type=chat_type, state='*')
    dp.register_message_handler(edited_message_post, IsAdminFilter(), chat_type=chat_type, state=Session.edit_text)
    dp.register_callback_query_handler(admin_menu, IsAdminFilter(), lambda c: c.data == 'back_to_menu',
                                       chat_type=chat_type, state='*')
