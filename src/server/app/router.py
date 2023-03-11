from fastapi import APIRouter

from .db.models import Event
from .db.tables import events
from .db.connection import database

router = APIRouter()


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@router.get(
    "/events/",
    response_model=list[Event],
)
async def all_events():
    query = events.select()
    return await database.fetch_all(query)
