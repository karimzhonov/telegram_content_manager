import asyncio
from aiogram import executor
from project.bot import dp, filters, handlers
from project.manager import tasks


def main():
    # Setup
    handlers.setup(dp)
    filters.setup(dp)
    # Create task for schedule
    loop = asyncio.get_event_loop()
    loop.create_task(tasks.start())
    # Setup handlers
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
