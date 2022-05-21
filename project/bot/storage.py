from aiogram.dispatcher.filters.state import State, StatesGroup


class Session(StatesGroup):
    bot_message_id = State()
    photo = State()
    edit_text = State()
