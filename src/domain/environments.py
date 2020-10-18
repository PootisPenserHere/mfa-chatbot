import os

PORT = int(os.getenv("PORT", 5000))
DEV_MODE = bool(os.getenv("DEV_MODE") == "true")

BASE_URL = os.environ["BASE_URL"]
