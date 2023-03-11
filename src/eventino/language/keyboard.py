from pydantic import BaseModel


class Keyboard(BaseModel):
    __root__: list[list[str]]
