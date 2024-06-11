import pytest
from starlette.testclient import TestClient

from app import app as FastAPP

# Initial APIClient
client = TestClient(FastAPP)


@pytest.fixture(scope="session")
def get_access_token():
    """
    Fixture which get access token from twitch user credentials
    :return:
    """
    authorize_code = "x2lxvytraf2b8p3lwvwm5pq7m5jght"
    url = f"http://0.0.0.0:8002/api/v1/twitch/auth/{authorize_code}"

    response = client.get(url)

    return response.json().get("access_token")


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
