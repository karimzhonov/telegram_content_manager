import os

SCHEDUALE_ENABLE = bool(os.environ.get('SCHEDUALE_ENABLE'))
CHANNEL_ID = int(os.environ.get('CHANNEL_ID'))
BASE_DIR = os.getcwd()
MEDIA_DIR = os.path.join(BASE_DIR, 'images')
CHANNEL_NAME = 'More Mebel'

CHANNEL_IMAGE_TEXT = 'Тел: +998998798832'
