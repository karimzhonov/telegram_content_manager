import asyncio
from aiogram import executor, types
from project.bot import dp, filters
from project.bot.handlers import users, admins, content
from project.manager import tasks


async def on_startup(_):
    asyncio.create_task(tasks.start())

    dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Вывести справку"),
    ])


def main():
    # Setup
    admins.setup(dp)
    users.setup(dp)
    content.setup(dp)
    filters.setup(dp)
    # Setup handlers
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)


if __name__ == '__main__':
    main()
