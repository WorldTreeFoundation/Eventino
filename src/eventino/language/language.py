from pprint import pformat
from typing import Iterator
from telegram.ext import ConversationHandler

from eventino.language.phrase import Phrase
from eventino.language.phrases_parser import PhrasesParser


class Language:
    def __init__(self) -> None:
        self._phrases: dict[str, Phrase] = {}
        self._parse_phrases()

    def _parse_phrases(self) -> None:
        parsed_phrases = PhrasesParser.parse()

        for phrase in parsed_phrases:
            if phrase.name in self._phrases:
                raise Exception(f"phrase '{phrase.name}' has duplicate")
            self._phrases[phrase.name] = phrase

        for phrase in self._phrases.values():
            if phrase.continuation is None:
                phrase.continuation = ConversationHandler.END
            elif phrase.continuation not in self._phrases:
                raise Exception(
                    f"phrase '{phrase.name}' requires "
                    f"phrase '{phrase.continuation}' as continuation"
                )

    def __repr__(self) -> str:
        return pformat(self._phrases)

    def __getattr__(self, __name: str) -> Phrase:
        return self[__name]

    def __getitem__(self, phrase_name: str) -> Phrase:
        return self._phrases[phrase_name]

    def __iter__(self) -> Iterator[Phrase]:
        return iter(self._phrases.values())
