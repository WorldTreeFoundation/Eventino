from time import monotonic
from random import randint


class AuthKey:
    AUTH_EXPIRATION_SECS = 300

    def __init__(self) -> None:
        self._key: int
        self._gen_time: float

    @property
    def key(self) -> int:
        return self._key
    
    @key.setter
    def key(self) -> None:
        raise Exception("you can't rewrite auth key")

    def generate_auth_key(self) -> None:
        """Generate auth key and print it
        """
        self._key = str(randint(10 ** 4, 10 ** 5))
        self._gen_time = monotonic()
        print(f"send this key to the telegram bot: {self._key}")

    def check_auth_key(self, user_input: str) -> bool:
        """Check if user provided correct key in time

        Args:
            user_input (str): user provided key

        Returns:
            bool: auth passed flag
        """
        if self._gen_time - monotonic() > self.AUTH_EXPIRATION_SECS:
            self.generate_auth_key()
            return False
        if user_input != self._key:
            return False
        return True
