import io
from project.bot import dp
from project.messages import CHANNEL_TEXT
from project.manager.settings import CHANNEL_ID
from project.manager.image import get_random_image, paste_ico_to_image


async def task_send_content(content=None):
    if content is None:
        content = get_random_image()

    content = paste_ico_to_image(content)

    with io.BytesIO() as buf:
        content.save(buf, 'PNG')
        content = buf.getvalue()
        await dp.bot.send_photo(CHANNEL_ID, content, CHANNEL_TEXT)
