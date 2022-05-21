from aiogram import types

# Admin menu
admin_menu = types.InlineKeyboardMarkup()
admin_menu.add(types.InlineKeyboardButton('Post', callback_data='post_content'))


# Post keyboard
post_keyboard = types.InlineKeyboardMarkup()
post_keyboard.add(types.InlineKeyboardButton('Post', callback_data='post_message'))
post_keyboard.add(types.InlineKeyboardButton('Edit text', callback_data='edit_message'))
post_keyboard.add(types.InlineKeyboardButton('Back', callback_data='back_to_menu'))