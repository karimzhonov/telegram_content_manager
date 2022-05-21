from aiogram import types
from project.bot import dp
from project.bot.keyboards import admin_menu as keyboard


async def admin_menu(msg):
    text = f'Hello, {msg.from_user.full_name}\nThis is admin panel'
    if isinstance(msg, types.Message):
        await msg.answer(text, reply_markup=keyboard)
    elif isinstance(msg, types.CallbackQuery):
        await msg.message.delete()
        await dp.bot.send_message(msg.message.chat.id, text, reply_markup=keyboard)
