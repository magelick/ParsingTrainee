from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from core.api.v1.router import router as v1_router

# api router
router = APIRouter(prefix="/api", default_response_class=ORJSONResponse)
# include v1 router
router.include_router(router=v1_router)
