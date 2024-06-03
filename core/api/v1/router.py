from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from core.api.v1.lamoda.action import router as lamoda_router
from core.api.v1.lamoda.db import router as lamoda_db_router
from core.api.v1.twitch.action import router as twitch_router
from core.api.v1.twitch.db import router as twitch_db_router

# v1 router
router = APIRouter(prefix="/v1", default_response_class=ORJSONResponse)
# include lamoda routers
router.include_router(router=lamoda_router)
router.include_router(router=lamoda_db_router)
# include twitch routers
router.include_router(router=twitch_router)
router.include_router(router=twitch_db_router)
