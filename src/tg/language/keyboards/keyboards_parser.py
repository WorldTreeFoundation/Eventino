from .keyboard import Keyboard
from config import KEYBOARDS_PACK_PATH
from language.parser.parser import Parser


class KeyboardsParser(Parser[Keyboard]):
    @staticmethod
    def parse() -> list[Keyboard]:
        """Parse language pack file specified in config.py"""
        path = KeyboardsParser._get_pack_path(KEYBOARDS_PACK_PATH)
        keyboards = KeyboardsParser.parse_file(path).pack
        return {
            keyboard.name: keyboard
            for keyboard in keyboards
        }
