from pprint import pformat
from typing import Iterator

from eventino.language.phrases.phrase import Phrase
from eventino.language.phrases.phrases_parser import PhrasesParser
from eventino.language.keyboards.keyboards_parser import KeyboardsParser


class Language:
    def __init__(self) -> None:
        self._phrases: dict[str, Phrase] = {}
        self._parse_phrases()

    def _parse_phrases(self) -> None:
        parsed_keyboards = KeyboardsParser.parse()
        self._phrases = PhrasesParser.parse(keyboards=parsed_keyboards)

    def __repr__(self) -> str:
        return pformat(self._phrases)

    def __getattr__(self, __name: str) -> Phrase:
        return self[__name]

    def __getitem__(self, phrase_name: str) -> Phrase:
        return self._phrases[phrase_name]

    def __iter__(self) -> Iterator[Phrase]:
        return iter(self._phrases.values())
