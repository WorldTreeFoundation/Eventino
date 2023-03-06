import os
from pydantic import BaseModel

from tg.language.phrase import Phrase
from config import BOT_LANGUAGE_PACK, LANGUAGE_PACK_FOLDER


class LanguageParser(BaseModel):
    phrases: list[Phrase]

    @staticmethod
    def parse() -> list[Phrase]:
        """Parse language pack file specified in config.py"""
        path = LanguageParser._get_pack_path()
        return LanguageParser.parse_file(path).phrases

    @staticmethod
    def _get_pack_path() -> str:
        """Construct pack path"""
        return os.path.join(
            os.getcwd(),
            LANGUAGE_PACK_FOLDER,
            BOT_LANGUAGE_PACK,
        )
