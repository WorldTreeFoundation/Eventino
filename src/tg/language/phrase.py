from __future__ import annotations

from pydantic import BaseModel

from tg.language.keyboard import Keyboard


class Phrase(BaseModel):
    name: str
    text: str
    keyboard: Keyboard | None
    continuation: int | str | None

    @property
    def reply_keyboard(self) -> list[list[str]]:
        return self.keyboard.__root__
