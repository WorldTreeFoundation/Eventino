from pprint import pformat
from telegram.ext import ConversationHandler

from tg.language.phrase import Phrase
from tg.language.language_parser import LanguageParser


class Language:
    def __init__(self) -> None:
        self._phrases: dict[str, Phrase] = {}
        self._parse_phrases()

    def _parse_phrases(self) -> None:
        parsed_phrases = LanguageParser.parse()

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
