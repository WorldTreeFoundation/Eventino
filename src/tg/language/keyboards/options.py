from pydantic import BaseModel


class Options(BaseModel):
    __root__: list[list[str]]
