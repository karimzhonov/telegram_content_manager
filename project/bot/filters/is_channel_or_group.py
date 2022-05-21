from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsChannelOrGroupFilter(BoundFilter):
    async def check(self, msg: types.Message) -> bool:
        return msg.chat.type == 'channel' or msg.chat.type == 'group'