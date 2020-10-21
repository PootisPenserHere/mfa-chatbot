from src.models import ChatProvidersFactoryModel


class BotApplication:
    def __init__(self, provider: str):
        self.chat_provider = ChatProvidersFactoryModel.ChatProvidersFactoryModel().create(chat_provider_type=provider)

    def respond_to_webhook(self, payload: object):
        print(f"response {payload['message']['text']}")
        self.chat_provider.respond_to_webhook(payload=payload, message=payload['message']['text'])
