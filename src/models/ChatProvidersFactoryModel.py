from src.models import TelegramModel
from src.domain.constants import ChatProviders


class ChatProvidersFactoryModel:
    @staticmethod
    # TODO adjust the return type when the models are standardized
    def create(chat_provider_type: str) -> object:
        if chat_provider_type == ChatProviders.TELEGRAM:
            return TelegramModel.TelegramModel()
