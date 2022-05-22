from aiogram import types

# Admin menu
admin_menu = types.InlineKeyboardMarkup()
admin_menu.add(types.InlineKeyboardButton('Добавить пост', callback_data='post_content'))


# Post keyboard
post_keyboard = types.InlineKeyboardMarkup()
post_keyboard.add(types.InlineKeyboardButton('Опубликовать пост', callback_data='post_message'))
post_keyboard.add(types.InlineKeyboardButton('Редактировать текст', callback_data='edit_message'))
post_keyboard.add(types.InlineKeyboardButton('Назад к меню', callback_data='back_to_menu'))