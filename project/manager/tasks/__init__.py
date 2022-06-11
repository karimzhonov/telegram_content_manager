import asyncio
import aioschedule
from .task_send_content import task_send_content

aioschedule.every().day.at('7:00').do(task_send_content)

# aioschedule.every(10).seconds.do(task_send_content)

async def start():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(0.1)
