from functools import reduce
from pydantic import BaseModel

from .options import Options


class Keyboard(BaseModel):
    name: str
    options: Options

    def flat(self) -> list[str]:
        """Get all options in 1D list

        Returns:
            list[str]
        """
        return reduce(lambda x, y: x + y, self.options.__root__)
