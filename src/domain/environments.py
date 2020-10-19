import os

PORT = int(os.getenv("PORT", 5000))
DEV_MODE = bool(os.getenv("DEV_MODE") == "true")

# From here on the BASE_URL is assumed to have no trailing /
BASE_URL = os.environ["BASE_URL"].rstrip('//')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
