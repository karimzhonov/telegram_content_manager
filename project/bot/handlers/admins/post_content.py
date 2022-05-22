import io
import os.path
from datetime import datetime
from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from project.bot import dp
from project.bot.storage import Session
from project.messages import CHANNEL_TEXT
from project.manager.settings import MEDIA_DIR
from project.bot.keyboards import admin_menu, post_keyboard
from project.manager.tasks.task_send_content import task_send_content


async def click_post_content_button(call: types.CallbackQuery, state: FSMContext):
    text = 'Отправте фото для публикации'
    await state.update_data(bot_message_id=call.message.message_id)
    await Session.photo.set()
    await call.message.delete_reply_markup()
    await call.message.edit_text(text)


async def sended_photo_for_post(msg: types.Message, state: FSMContext):
    # Download photo
    photo = msg.photo.pop()
    await msg.delete()
    data = await state.get_data()
    await dp.bot.delete_message(msg.chat.id, data['bot_message_id'])
    with io.BytesIO() as buf:
        await photo.download(destination_file=buf)
        content = buf.getvalue()
    # Send message
    text = CHANNEL_TEXT
    if msg.caption is not None:
        text = msg.caption

    bot_message = await dp.bot.send_photo(msg.chat.id, content, text, reply_markup=post_keyboard)
    await state.update_data(photo=content, bot_message_id=bot_message.message_id, text=CHANNEL_TEXT)


async def post_message_to_channel(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    # Create filename
    now = str(datetime.now()).split('.')[0]
    now = '_'.join(now.split())
    now = '-'.join(now.split(':'))
    file_path = os.path.join(MEDIA_DIR, f'photo_{now}.jpg')
    # save photo
    with open(file_path, 'wb') as file:
        file.write(data['photo'])
    # send to chanel
    await task_send_content(data['photo'], data['text'])
    # Response to admin
    text = 'Сообщение опубликовано'
    await call.message.delete()
    await dp.bot.send_message(call.message.chat.id, text, reply_markup=admin_menu)


async def edit_message_post(call: types.CallbackQuery, state: FSMContext):
    text = 'Введите текст'
    await Session.edit_text.set()
    await call.message.delete()
    msg = await dp.bot.send_message(call.message.chat.id, text)
    await state.update_data(bot_message_id=msg.message_id)


async def edited_message_post(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    await dp.bot.delete_message(msg.chat.id, data['bot_message_id'])
    await msg.delete()
    await state.update_data(text=msg.text)
    await dp.bot.send_photo(msg.chat.id, data['photo'], msg.text, reply_markup=post_keyboard)
