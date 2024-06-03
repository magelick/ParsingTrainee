import pytest
from tests.conftest import client


@pytest.mark.asyncio
async def test_authorize():
    response = client.get("http://0.0.0.0:8002/api/v1/twitch/auth/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, str)


@pytest.mark.asyncio
async def test_get_twitch_tokens():
    response = client.get(
        "http://0.0.0.0:8002/api/v1/twitch/auth/cnwozppbxrszmv1b68b57s79fjdytp"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_user(get_access_token):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/auth/user/?access_token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_games(get_access_token):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/games/33214?name=Fortnite&igdb_id=1905&token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_top_games(get_access_token):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/games/top/?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_games_analytic(get_access_token):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/games/analytic/1234?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_channel_information(get_access_token, get_user_id):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/channel/{get_user_id}?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_channel_editor(get_access_token, get_user_id):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/channel/editor/{get_user_id}?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_followed_channel(get_access_token, get_user_id):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/channel/followed/{get_user_id}?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_channel_followers(get_access_token, get_user_id):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/channel/followers/{get_user_id}?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_channel_emotes(get_access_token, get_user_id):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/channel/emotes/{get_user_id}?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_channel_chat_settings(get_access_token, get_user_id):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/channel/chat/settings/{get_user_id}?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_vip_channel_persons(get_access_token, get_user_id):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/channel/vip/{get_user_id}?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_global_emotes(get_access_token, get_user_id):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/emotes/global?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_clips(get_access_token, get_user_id):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/clips/{get_user_id}?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_pools(get_access_token, get_user_id):
    response = client.get(
        f"http://0.0.0.0:8002/api/v1/twitch/pools/{get_user_id}?token={get_access_token}"
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
