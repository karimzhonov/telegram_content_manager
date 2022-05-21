from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from project.settings import ADMINS


class IsAdminFilter(BoundFilter):
    async def check(self, msg: types.Message) -> bool:
        return msg.from_user.id in ADMINS
