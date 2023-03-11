from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()


@router.get(
    "/event",
    status_code=201,
)
def all_events() -> JSONResponse:
    return JSONResponse(jsonable_encoder({"events": ['event1', 'event2']}), 200)


@router.get(
    "/event/{user_id}",
    status_code=201,
)
def all_events(user_id: int) -> JSONResponse:
    return JSONResponse(jsonable_encoder({
        "user_id": user_id,
        "events": ['event1', 'event2']
    }), 200)
