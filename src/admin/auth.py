from time import monotonic
from random import randint

from .db import AuthDB
from .telegram import AuthBot


class AdminAuth:
    AUTH_EXPIRATION_SECS = 300

    def __init__(self) -> None:
        self._key: int
        self._gen_time: float
        self._bot = AuthBot()

    @property
    def key(self) -> int:
        return self._key

    def ensure_server_has_admin(self) -> bool:
        """If server's admin doesn't exist, block server main loop
        until admin log in

        Returns:
            bool: server has admin status
        """
        self._bot.start()

        while not AuthDB.server_has_admin():
            self.generate_auth_key()
            user_input = input("please, provide auth key from frontend: ")

            if self.check_auth_key(user_input):
                AuthDB.set_admin()
                break

        return True

    def generate_auth_key(self) -> tuple[str, float]:
        """Generate auth key and return it with its generation time
        """
        self._key = str(randint(10 ** 4, 10 ** 5))
        self._gen_time = monotonic()

    def check_auth_key(self, user_input: str) -> bool:
        """Check if user provided correct key in time

        Args:
            user_input (str): user provided key

        Returns:
            bool: auth passed flag
        """
        if self._gen_time - monotonic() > self.AUTH_EXPIRATION_SECS:
            return False
        if user_input != self._key:
            return False
        return True
