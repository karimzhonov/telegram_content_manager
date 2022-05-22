import os
import random
from PIL import Image, ImageDraw, ImageFont
from project.manager import settings


def get_random_image() -> Image.Image:
    images = os.listdir(settings.MEDIA_DIR)
    image = random.choice(images)
    image_path = os.path.join(settings.MEDIA_DIR, image)
    return Image.open(image_path)


def paste_ico_to_image(image: Image.Image) -> Image.Image:
    ico_path = os.path.join(settings.BASE_DIR, 'ico.jpg')
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
    font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'project', 'font.ttf'), int(ico.size[0] * 0.5))
    draw = ImageDraw.Draw(image)
    draw.text((int(0.05 * image.size[1]), int(0.05 * image.size[1])),
              settings.CHANNEL_IMAGE_TEXT, (0, 0, 0), font)
    return image