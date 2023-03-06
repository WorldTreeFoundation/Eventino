from telegram.ext import ConversationHandler
from pydantic import BaseModel

from tg.language.keyboard import Keyboard


class Phrase(BaseModel):
    name: str
    text: str
    reply_keyboard: Keyboard | None
    continuation: str | None
