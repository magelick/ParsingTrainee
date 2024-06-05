from random import randint

import pytest

from core.utils.lamoda import (
    get_all_sneakers,
    get_sneaker_by_href,
    get_sneaker_by_article,
    get_sneakers_hrefs,
)

from core.utils.twitch import (
    authorize_by_twitch,
    get_twitch_tokens,
    get_pools,
    get_clips,
    get_chat_settings,
    get_channel_emotes,
    get_channel_editor,
    get_channel_information,
    get_vip_person_of_channel,
    get_followed_channels,
    get_channel_followers,
    get_global_emotes,
    get_user,
    get_games,
    get_top_games,
    get_game_analytics,
)


@pytest.mark.asyncio
async def test_lamoda_all_sneakers():
    sneakers = get_all_sneakers(page_int=randint(1, 10))

    for brand, info in sneakers.items():
        assert isinstance(brand, str)
        assert isinstance(info, dict)

        assert "model" in info
        assert "price" in info

        assert isinstance(info["model"], str)
        assert isinstance(info["price"], str)

        assert "Кроссовки" not in info["model"]


@pytest.mark.asyncio
async def test_lamoda_sneakers_hrefs():
    hrefs = get_sneakers_hrefs(page_int=randint(1, 10))

    for sneaker, href in hrefs.items():

        assert isinstance(sneaker, str)
        assert isinstance(href, str)

        assert "Кроссовки" not in sneaker
        assert "/p/" in href


@pytest.mark.asyncio
async def test_lamoda_sneaker_by_href():
    sneaker_info = get_sneaker_by_href(
        href="/p/rtladl534401/shoes-napapijri-krossovki/"
    )

    for title, value in sneaker_info.items():

        assert isinstance(title, str)
        assert isinstance(value, str)


@pytest.mark.asyncio
async def test_lamoda_sneaker_by_article():
    sneaker_info = get_sneaker_by_article(article="rtladl534401")

    for title, value in sneaker_info.items():

        assert isinstance(title, str)
        assert isinstance(value, str)


@pytest.mark.asyncio
async def test_authorize():
    authorize_code = authorize_by_twitch()
    assert isinstance(authorize_code, str)


@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_twitch_tokens():
    tokens = get_twitch_tokens(
        authorization_code="2zs9l6j8h626elx4z26h0dq6vp9iqc"
    )

    assert "access_token" in tokens
    assert "expires_in" in tokens
    assert "refresh_token" in tokens
    assert "scope" in tokens
    assert "token_type" in tokens

    assert isinstance(tokens["access_token"], str)
    assert isinstance(tokens["expires_in"], int)
    assert isinstance(tokens["refresh_token"], str)
    assert isinstance(tokens["scope"], list)
    assert isinstance(tokens["token_type"], str)

    assert tokens["scope"] == [
        "analytics:read:games",
        "channel:read:editors",
        "channel:read:goals",
        "channel:read:polls",
        "channel:read:vips",
        "moderator:read:followers",
        "user:read:follows",
    ]
    assert tokens["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_get_user(get_access_token):
    user = get_user(token=get_access_token)

    for data, value in user.items():
        assert isinstance(data, str)
        assert isinstance(value, list)

        for items in value:
            assert "id" in items
            assert "login" in items
            assert "display_name" in items
            assert "type" in items
            assert "broadcaster_type" in items
            assert "description" in items
            assert "profile_image_url" in items
            assert "offline_image_url" in items
            assert "view_count" in items
            assert "created_at" in items

            assert isinstance(items["id"], str)
            assert isinstance(items["login"], str)
            assert isinstance(items["display_name"], str)
            assert isinstance(items["type"], str)
            assert isinstance(items["broadcaster_type"], str)
            assert isinstance(items["description"], str)
            assert isinstance(items["profile_image_url"], str)
            assert isinstance(items["offline_image_url"], str)
            assert isinstance(items["view_count"], int)
            assert isinstance(items["created_at"], str)


@pytest.mark.asyncio
async def test_get_games(get_access_token):
    games = get_games(
        game_id="33214",
        token=get_access_token,
        igdb_id="1905",
        name="Fortnite",
    )

    for data, value in games.items():
        assert isinstance(data, str)
        assert isinstance(value, list)

        for items in value:
            assert "id" in items
            assert "name" in items
            assert "box_art_url" in items
            assert "igdb_id" in items

            assert isinstance(items["id"], str)
            assert isinstance(items["name"], str)
            assert isinstance(items["box_art_url"], str)
            assert isinstance(items["igdb_id"], str)


@pytest.mark.asyncio
async def test_get_top_games(get_access_token):
    top_games = get_top_games(token=get_access_token)

    for data, value in top_games.items():
        assert isinstance(data, str)
        assert isinstance(value, (list, dict))

        if isinstance(value, list):
            for items in value:
                assert "id" in items
                assert "name" in items
                assert "box_art_url" in items
                assert "igdb_id" in items

                assert isinstance(items["id"], str)
                assert isinstance(items["name"], str)
                assert isinstance(items["box_art_url"], str)
                assert isinstance(items["igdb_id"], str)

        elif isinstance(value, dict):
            assert "cursor" in value
            assert isinstance(value["cursor"], str)


@pytest.mark.asyncio
@pytest.mark.skip
async def test_get_game_analytic(get_access_token):
    analytic = get_game_analytics(token=get_access_token, game_id="")

    for data, value in analytic.items():
        assert isinstance(data, str)
        assert isinstance(value, (list, dict))

        if isinstance(value, list):
            for items in value:
                assert "game_id" in items
                assert "URL" in items
                assert "type" in items
                assert "date_range" in items
                assert "started_at" in items["date_range"]
                assert "ended_at" in items["date_range"]

                assert isinstance(items["game_id"], str)
                assert isinstance(items["URL"], str)
                assert isinstance(items["type"], str)
                assert isinstance(items["date_range"], dict)
                assert isinstance(items["date_range"]["started_at"], str)
                assert isinstance(items["date_range"]["ended_at"], str)

        elif isinstance(value, dict):
            assert "cursor" in value
            assert isinstance(value["cursor"], str)


@pytest.mark.asycnio
async def test_get_channel_information(get_access_token):
    info = get_channel_information(
        token=get_access_token, broadcaster_id="1088507447"
    )

    for data, value in info.items():
        assert isinstance(data, str)
        assert isinstance(value, list)

        for items in value:
            assert "broadcaster_id" in items
            assert "broadcaster_login" in items
            assert "broadcaster_name" in items
            assert "broadcaster_language" in items
            assert "game_name" in items
            assert "game_id" in items
            assert "title" in items
            assert "delay" in items
            assert "tags" in items
            assert "content_classification_labels" in items
            assert "is_branded_content" in items

            assert isinstance(items["broadcaster_id"], str)
            assert isinstance(items["broadcaster_login"], str)
            assert isinstance(items["broadcaster_name"], str)
            assert isinstance(items["broadcaster_language"], str)
            assert isinstance(items["game_name"], str)
            assert isinstance(items["game_id"], str)
            assert isinstance(items["title"], str)
            assert isinstance(items["delay"], int)
            assert isinstance(items["tags"], list)
            assert isinstance(items["content_classification_labels"], list)
            assert isinstance(items["is_branded_content"], bool)


@pytest.mark.asyncio
async def test_get_channel_editor(get_access_token):
    editor = get_channel_editor(
        token=get_access_token, broadcaster_id="1088507447"
    )

    for data, value in editor.items():
        assert isinstance(data, str)
        assert isinstance(value, list)


@pytest.mark.asyncio
async def test_get_followed_channel(get_access_token):
    followed_channel = get_followed_channels(
        token=get_access_token, user_id="1088507447"
    )

    for data, value in followed_channel.items():
        assert isinstance(data, (str, int))
        assert isinstance(value, (list, dict))


@pytest.mark.asyncio
async def test_get_channel_followers(get_access_token):
    followers = get_channel_followers(
        token=get_access_token, broadcaster_id="1088507447"
    )

    for data, value in followers.items():
        assert isinstance(data, str)
        assert isinstance(value, (list, dict, int))


@pytest.mark.asyncio
async def test_get_channel_emotes(get_access_token):
    emotes = get_channel_emotes(
        token=get_access_token, broadcaster_id="1088507447"
    )

    for data, value in emotes.items():
        assert isinstance(data, str)
        assert isinstance(value, (list, str))


@pytest.mark.asyncio
async def test_get_channel_chat_settings(get_access_token):
    settings = get_chat_settings(
        token=get_access_token, broadcaster_id="1088507447"
    )

    assert "data" in settings
    assert isinstance(settings["data"], list)


@pytest.mark.asyncio
async def test_get_channel_vip_person(get_access_token):
    persons = get_vip_person_of_channel(
        token=get_access_token, broadcaster_id="1088507447"
    )

    for data, value in persons.items():
        assert isinstance(data, str)
        assert isinstance(value, (list, dict))


@pytest.mark.asyncio
async def test_get_global_emotes(get_access_token):
    global_emotes = get_global_emotes(token=get_access_token)

    for data, value in global_emotes.items():
        assert isinstance(data, str)
        assert isinstance(value, (list, str))

        if isinstance(value, list):
            for items in value:
                assert "id" in items
                assert "name" in items
                assert "images" in items
                assert "format" in items
                assert "scale" in items
                assert "theme_mode" in items

                assert isinstance(items["id"], str)
                assert isinstance(items["name"], str)
                assert isinstance(items["images"], dict)
                assert isinstance(items["format"], list)
                assert isinstance(items["scale"], list)
                assert isinstance(items["theme_mode"], list)


@pytest.mark.asyncio
async def test_get_clips(get_access_token):
    clips = get_clips(token=get_access_token, broadcaster_id="1088507447")

    for data, value in clips.items():
        assert isinstance(data, str)
        assert isinstance(value, (list, dict))


@pytest.mark.asyncio
async def test_get_pools(get_access_token):
    pools = get_pools(token=get_access_token, broadcaster_id="1088507447")

    for data, value in pools.items():
        assert isinstance(data, str)
        assert isinstance(value, (list, dict))
