import pytest
from tests.conftest import client


@pytest.mark.asyncio
async def test_authorize():
    base_url = "http://0.0.0.0:8002/api/v1/twitch/auth/"

    response = client.get(base_url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_twitch_tokens():
    base_url = "http://0.0.0.0:8002/api/v1/twitch/auth/"
    authorize_code = "mm44wdfpbnj284l7qq7lfj1xhfhnge"
    url = f"{base_url}{authorize_code}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_user(get_access_token):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/auth/user/"
    url = f"{base_url}?access_token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_games(get_access_token):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/games/"
    game_id = "33214"
    name = "Fortnite"
    igdb_id = "1905"
    url = f"{base_url}{game_id}?name={name}&igdb_id={igdb_id}&token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_top_games(get_access_token):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/games/top/"
    url = f"{base_url}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.xfail
async def test_get_games_analytic(get_access_token):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/games/analytic/"
    game_id = "1234"
    url = f"{base_url}{game_id}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_channel_information(get_access_token, get_user_id):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/channel/"
    url = f"{base_url}{get_user_id}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_channel_editor(get_access_token, get_user_id):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/channel/editor/"
    url = f"{base_url}{get_user_id}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_followed_channel(get_access_token, get_user_id):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/channel/followed/"
    url = f"{base_url}{get_user_id}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_channel_followers(get_access_token, get_user_id):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/channel/followers/"
    url = f"{base_url}{get_user_id}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_channel_emotes(get_access_token, get_user_id):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/channel/emotes/"
    url = f"{base_url}{get_user_id}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_channel_chat_settings(get_access_token, get_user_id):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/channel/chat/settings/"
    url = f"{base_url}{get_user_id}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_vip_channel_persons(get_access_token, get_user_id):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/channel/vip/"
    url = f"{base_url}{get_user_id}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_global_emotes(get_access_token, get_user_id):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/emotes/global"
    url = f"{base_url}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_clips(get_access_token, get_user_id):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/clips/"
    url = f"{base_url}{get_user_id}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_pools(get_access_token, get_user_id):
    base_url = "http://0.0.0.0:8002/api/v1/twitch/pools/"
    url = f"{base_url}{get_user_id}?token={get_access_token}"

    response = client.get(url)

    assert response.status_code == 200
