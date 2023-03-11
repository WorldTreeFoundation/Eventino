from .phrase import Phrase
from config import PHRASES_PACK_PATH
from eventino.language.parser.parser import Parser
from eventino.language.keyboards.keyboard import Keyboard


class PhrasesParser(Parser[Phrase]):
    @staticmethod
    def parse(keyboards: dict[str, Keyboard]) -> list[Phrase]:
        """Parse language pack file specified in config.py"""
        phrases: dict[str, Phrase] = {}

        path = PhrasesParser._get_pack_path(PHRASES_PACK_PATH)
        parsed_phrases = PhrasesParser.parse_file(path).pack

        for phrase in parsed_phrases:
            if phrase.name in phrases:
                raise Exception(f"phrase '{phrase.name}' has duplicate")
            phrases[phrase.name] = phrase

        for phrase in phrases.values():
            if phrase.keyboard is None:
                continue

            if phrase.keyboard not in keyboards:
                raise Exception(f"no known keyboard '{phrase.keyboard}'")

            for option in keyboards[phrase.keyboard].flat():
                if option not in phrases:
                    raise Exception(
                        f"keyboard '{phrase.keyboard}' requires "
                        f"phrase '{option}' as possible continuation"
                    )

            phrase.keyboard = keyboards[phrase.keyboard]

        return phrases
