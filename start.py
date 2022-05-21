import asyncio
from aiogram import executor
from project.bot import dp
from project import schedules, handlers, filters


def main():
    # Setup
    handlers.setup(dp)
    filters.setup(dp)
    # Create task for schedule
    loop = asyncio.get_event_loop()
    loop.create_task(schedules.start())
    # Setup handlers
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
