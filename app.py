from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis.asyncio import Redis  # type: ignore

from core.api.router import router as api_router
from core.settings import SETTINGS

# Most high router
app = FastAPI(
    title="Parsing-Test-Project",
    description="Simple parsing Lamoda and Twitch",
    default_response_class=ORJSONResponse,
)
# include api router
app.include_router(router=api_router)


@app.on_event("startup")
async def startup():
    """
    Func which initial redis like cache db
    :return:
    """
    redis = Redis.from_url(SETTINGS.REDIS_URL.unicode_string())
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache", expire=60)
