from src.models import TelegramModel


class BotApplication:
    def __init__(self):
        self.telegram_model = TelegramModel.TelegramModel()

    def respond_to_webhook(self, payload):
        self.telegram_model.respond_to_webhook(payload=payload)
