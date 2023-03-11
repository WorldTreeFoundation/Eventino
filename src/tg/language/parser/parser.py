import os
from pydantic import BaseModel
from typing import Generic, TypeVar
from abc import ABC, abstractstaticmethod

from config import LANGUAGE_PACK_FOLDER
from language.phrases.phrase import Phrase
from language.keyboards.keyboard import Keyboard

PackType = TypeVar('PackType', Phrase, Keyboard)


class Parser(ABC, Generic[PackType], BaseModel):
    """Abstract parser class for `PhrasesParser` and `KeyboardsParser`
    """

    pack: list[PackType]
    """Parsed pack data
    """

    @abstractstaticmethod
    def parse(*args, **kwargs) -> list[PackType]:
        """Parse language pack file specified in config.py
        """
        return []

    @staticmethod
    def _get_pack_path(pack: str) -> str:
        """Construct pack path
        """
        return os.path.join(
            os.getcwd(),
            LANGUAGE_PACK_FOLDER,
            pack,
        )
