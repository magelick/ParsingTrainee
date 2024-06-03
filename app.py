from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.api.router import router as api_router

# Most high router
app = FastAPI(
    title="Parsing-Test-Project",
    description="Simple parsing Lamoda and Twitch",
    default_response_class=ORJSONResponse,
)
# include api router
app.include_router(router=api_router)
