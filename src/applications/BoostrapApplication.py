from src.domain import environments
import requests


class BootstrapApplication:
    def __init__(self):
        self._set_telegram_webhook()

    @staticmethod
    def _set_telegram_webhook():
        webhook_url = f"{environments.BASE_URL}/webhook/telegram"
        webhook_register_url = f"https://api.telegram.org/bot{environments.TELEGRAM_TOKEN}/setWebHook?url={webhook_url}"

        r = requests.get(webhook_register_url)
        print(r.json())
