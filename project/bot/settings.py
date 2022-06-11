import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
ADMINS = [int(admin) for admin in os.environ.get('ADMINS').split(';')]