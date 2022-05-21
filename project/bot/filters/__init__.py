from aiogram import Dispatcher

from .is_channel_or_group import IsChannelOrGroupFilter
from .is_admin import IsAdminFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdminFilter)
    dp.filters_factory.bind(IsChannelOrGroupFilter)
