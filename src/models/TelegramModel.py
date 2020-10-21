import telegram

from src.domain import environments


class TelegramModel:
    def __init__(self):
        self.bot = telegram.Bot(environments.TELEGRAM_TOKEN)

    def respond_to_webhook(self, payload):
        update = telegram.update.Update.de_json(payload, self.bot)
        self.bot.sendMessage(chat_id=update.message.chat_id, text=payload['message']['text'])
