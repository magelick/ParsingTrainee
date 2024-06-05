import pytest
from starlette.testclient import TestClient

from core.utils.twitch import get_twitch_tokens, get_user
from app import app as FastAPP

# Initial APIClient
client = TestClient(FastAPP)


@pytest.fixture(scope="session")
def get_access_token():
    """
    Fixture which get access token from twitch user credentials
    :return:
    """
    auth_data = get_twitch_tokens(
        authorization_code="cnwozppbxrszmv1b68b57s79fjdytp"
    )
    print(auth_data)
    return auth_data.get("access_token")


@pytest.fixture(scope="session")
def get_user_id(get_access_token):
    """
    Fixture which get user (broadcaster) ID
    :return:
    """
    user = get_user(token=get_access_token)
    return user[0]["id"]
