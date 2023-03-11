from pydantic import BaseModel


# Data models
class Event(BaseModel):
    """Event data
    """
    id: int
    title: str
    guest_limit: int
    info: str
    active: bool
