import os
import sys
from telegram import Update
from telegram.ext import (
    Application, ContextTypes,
    filters, MessageHandler,
)

from config import TG_TOKEN_ENV_NAME
from .db import AuthDB
from .auth_key import AuthKey


class AuthBot:
    def __init__(self) -> None:
        self.app: Application
        self.auth = AuthKey()

    @property
    def current_key(self) -> str:
        return self.auth.key

    def start(self) -> None:
        """Start bot
        """
        if AuthDB.server_has_admin():
            return
        self.auth.generate_auth_key()
        self._build()
        self._run()

    def _build(self) -> None:
        """Build bot
        """
        token = self._get_token()
        self.app = Application.builder().token(token).build()
        self.app.add_handler(MessageHandler(filters.TEXT, self._send_key))

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

    def _run(self) -> None:
        """Run bot
        """
        self.app.run_polling()

    async def _send_key(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Send an auth key
        """
        if AuthDB.server_has_admin():
            return
        if self.auth.check_auth_key(update.message.text):
            user_id = update.effective_user.id
            AuthDB.set_admin(user_id)
            await self._stop()
        else:
            await update.message.reply_text('try again')

    async def _stop(self) -> None:
        """Stop bot
        """
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
