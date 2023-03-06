from __future__ import annotations

from pydantic import BaseModel

from tg.language.keyboard import Keyboard


class Phrase(BaseModel):
    name: str
    text: str
    reply_keyboard: Keyboard | None
    continuation: int | str | None
