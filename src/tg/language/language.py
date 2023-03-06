from __future__ import annotations

import os
from pydantic import BaseModel

from tg.language.phrase import Phrase
from config import BOT_LANGUAGE_PACK, LANGUAGE_PACK_FOLDER


class Language(BaseModel):
    phrases: list[Phrase]

    @staticmethod
    def parse() -> Language:
        """Parse language pack file specified in config.py"""
        path = Language._get_pack_path()
        return Language.parse_file(path)

    @staticmethod
    def _get_pack_path() -> str:
        """Construct pack path"""
        return os.path.join(
            os.getcwd(),
            LANGUAGE_PACK_FOLDER,
            BOT_LANGUAGE_PACK,
        )
