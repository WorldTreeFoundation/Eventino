from pydantic import BaseModel
from language.keyboards.keyboard import Keyboard


class Phrase(BaseModel):
    name: str
    text: str
    keyboard: str | Keyboard | None
