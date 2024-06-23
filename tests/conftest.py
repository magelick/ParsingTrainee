import pytest
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis.client import Redis  # type: ignore
from starlette.testclient import TestClient

from app import app as FastAPP
from core.settings import SETTINGS

# Initial APIClient
client = TestClient(FastAPP)


@pytest.fixture(scope="session")
def get_access_token():
    """
    Fixture which get access token from twitch user credentials
    :return:
    """
    authorize_code = "q6elrrgn40h7iowj6w6fryw5v5vaiu"
    url = f"http://0.0.0.0:8002/api/v1/twitch/auth/{authorize_code}"

    response = client.get(url).json()

    access_token = response.get("access_token")

    return access_token


@pytest.fixture(scope="session")
def get_user_id(get_access_token):
    """
    Fixture which get user (broadcaster) ID
    :return:
    """
    url = f"http://0.0.0.0:8002/api/v1/twitch/auth/user/?access_token={get_access_token}"

    user = client.get(url).json()
    user_data = user.get("data")

    return user_data[0].get("id")


@pytest.fixture(scope="session")
def get_init_cache():
    redis = Redis.from_url(SETTINGS.REDIS_URL.unicode_string())
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache", expire=60)
