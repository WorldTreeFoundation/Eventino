import os
from telegram import Update
from telegram.ext import (
    Application, filters,
    ContextTypes, MessageHandler,
)

from config import TG_TOKEN_ENV_NAME
from eventino.language import Language


class Eventino:
    def __init__(self) -> None:
        self.app: Application
        self.language = Language()

    def start(self) -> None:
        """Start bot
        """
        self._build()
        self._run()

    def _build(self) -> None:
        """Build bot
        """
        token = self._get_token()
        self.app = Application.builder().token(token).build()
        # TODO: add handlers
        self.app.add_handler(MessageHandler(filters.TEXT, self._echo))

    def _run(self) -> None:
        """Run bot
        """
        self.app.run_polling()

    @staticmethod
    def _get_token() -> str:
        """Get telegram bot's token

        Raises:
            Exception: you must provide bot's telegram token via env variable

        Returns:
            str: bot's token
        """
        token = os.getenv(TG_TOKEN_ENV_NAME)

        if token is None:
            raise Exception(
                f"you must provide env var '{TG_TOKEN_ENV_NAME}'"
                " with your bot's telegram token"
            )

        return token

    async def _echo(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Send an auth key
        """
        await update.message.reply_text(update.message.text)
