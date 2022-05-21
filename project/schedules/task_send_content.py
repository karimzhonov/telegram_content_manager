import os, io
import random
from PIL import Image, ImageDraw, ImageFont

import project.settings as settings
from project.bot import dp


async def task_send_content():
    photo = await get_content()
    await dp.bot.send_photo(settings.CHANNEL_ID, photo, settings.CHANNEL_TEXT)


async def get_content():
    images = os.listdir(settings.MEDIA_DIR)
    image = random.choice(images)
    image_path = os.path.join(settings.MEDIA_DIR, image)
    ico_path = os.path.join(settings.BASE_DIR, '..', 'ico.jpg')
    # Open image and resize
    image = Image.open(image_path)
    (height, width) = image.size
    # Open Ico and resize
    ico = Image.open(ico_path)
    (h, w) = ico.size
    if width > height:
        height = int((width * h * 0.1) / w)
        ico = ico.resize((int(width * 0.1), height))
    else:
        width = int((height * w * 0.1) / h)
        ico = ico.resize((width, int(height * 0.1)))
    image.paste(ico, (int(image.size[0] - 0.05 * image.size[1] - ico.size[0]), int(0.95 * image.size[1] - ico.size[1])))
    # Put text
    font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'font.ttf'), int(ico.size[0] * 0.5))
    draw = ImageDraw.Draw(image)
    draw.text((int(0.05 * image.size[1]), int(0.05 * image.size[1])),
              settings.CHANNEL_IMAGE_TEXT, (0, 0, 0), font)
    with io.BytesIO() as buf:
        image.save(buf, 'PNG')
        return buf.getvalue()
