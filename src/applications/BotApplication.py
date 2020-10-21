from src.models import ChatProvidersFactoryModel


class BotApplication:
    def __init__(self, provider: str):
        self.chat_provider = ChatProvidersFactoryModel.ChatProvidersFactoryModel().create(chat_provider_type=provider)

    def respond_to_webhook(self, payload):
        self.chat_provider.respond_to_webhook(payload=payload)
