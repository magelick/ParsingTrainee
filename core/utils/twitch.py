import requests
from pydantic import Json

from core.settings import SETTINGS


def authorize_by_twitch() -> str:
    """
    Func which authorize user with needs scopes
    :return:
    """
    # declaring url and params
    url = "https://id.twitch.tv/oauth2/authorize"
    parameters = {
        "response_type": "code",
        "client_id": "mujzbtoibyr6vk91k3xjpyfyhqp7le",
        "redirect_uri": "http://localhost:8001",
        "scope": " ".join(
            [
                "analytics:read:games",
                "channel:read:editors",
                "channel:read:goals",
                "channel:read:vips",
                "channel:read:polls",
                "moderator:read:followers",
                "user:read:follows",
            ]
        ),
    }
    # return redirect uri with query params
    redirect_uri = (
        requests.Request("GET", url, params=parameters).prepare().url
    )
    print(redirect_uri)
    return redirect_uri


def get_twitch_tokens(authorization_code: str) -> Json:
    """
    Func which get access and refresh tokens and other information
    :param authorization_code:
    :return:
    """
    # declaring url and data
    url = "https://id.twitch.tv/oauth2/token"
    data = {
        "client_id": SETTINGS.TWITCH_CLIENT_ID,
        "client_secret": SETTINGS.TWITCH_CLIENT_SECRET,
        "code": authorization_code,
        "grant_type": "authorization_code",
        "redirect_uri": "http://localhost:8001",
    }
    # return response with needing data
    response = requests.post(url, data=data)
    return response.json()


def get_user(token) -> Json:
    """
    Func which get user info
    :return:
    """
    # declaring url and
    url = "https://api.twitch.tv/helix/users"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with user information
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_games(token: str, game_id: str, name: str, igdb_id: str) -> Json:
    """
    Func which get game information by id, name and igdb_id
    :param game_id:
    :param token:
    :param name:
    :param igdb_id:
    :return:
    """
    # declaring url and headers
    url = f"https://api.twitch.tv/helix/games?id={game_id}&name={name}&igdb_id={igdb_id}"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with game
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_top_games(token: str) -> Json:
    """
    Func which get top games
    :param token:
    :return:
    """
    # declaring url and headers
    url = "https://api.twitch.tv/helix/games/top"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with top games
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_game_analytics(token: str, game_id: str) -> Json:
    """
    Func which get game analytic
    :param game_id:
    :param token:
    :return:
    """
    # declaring url and headers
    url = f"https://api.twitch.tv/helix/analytics/games?game_id={game_id}"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with game analytic
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_channel_information(token: str, broadcaster_id: str) -> Json:
    """
    Func which get information about channel
    :param token:
    :param broadcaster_id:
    :return:
    """
    # declaring url and headers
    url = (
        f"https://api.twitch.tv/helix/channels?broadcaster_id={broadcaster_id}"
    )
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with information
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_channel_editor(token: str, broadcaster_id: str) -> Json:
    """
    Func which get channel editor
    :param token: 'x8d5893vntkgiufs1of9a8smbsqhov'
    :param broadcaster_id:
    :return:
    """
    # declaring url and headers
    url = f"https://api.twitch.tv/helix/channels/editors?broadcaster_id={broadcaster_id}"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with channel editor
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_followed_channels(token: str, user_id: str) -> Json:
    """
    Func which get followed channels
    :param token:
    :param user_id:
    :return:
    """
    # declaring url and headers
    url = f"https://api.twitch.tv/helix/channels/editors?broadcaster_id={user_id}"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with followed channels
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_channel_followers(token: str, broadcaster_id: str) -> Json:
    """
    Func which get channel followers
    :param token:
    :param broadcaster_id:
    :return:
    """
    # declaring url and headers
    url = f"https://api.twitch.tv/helix/channels/followers?broadcaster_id={broadcaster_id}"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with channel followers
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_channel_emotes(token: str, broadcaster_id: str) -> Json:
    """
    Func which get channel emotes
    :param broadcaster_id:
    :param token:
    :return:
    """
    # declaring url and headers
    url = f"https://api.twitch.tv/helix/chat/emotes?broadcaster_id={broadcaster_id}"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with channel emotes
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_global_emotes(token: str) -> Json:
    """
    Func which get global emotes
    :param token: 'x8d5893vntkgiufs1of9a8smbsqhov'
    :return:
    """
    # declaring url and headers
    url = "https://api.twitch.tv/helix/chat/emotes/global"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with global emotes
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_chat_settings(token: str, broadcaster_id: str) -> Json:
    """
    Func which get chat settings
    :param broadcaster_id:
    :param token: 'x8d5893vntkgiufs1of9a8smbsqhov'
    :return:
    """
    # declaring url and headers
    url = f"https://api.twitch.tv/helix/chat/emotes?broadcaster_id={broadcaster_id}"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with chat settings
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_clips(token: str, broadcaster_id: str) -> Json:
    """
    Func which get clips
    :param token: 'x8d5893vntkgiufs1of9a8smbsqhov'
    :param game_id:
    :param id:
    :param broadcaster_id:
    :return:
    """
    # declaring url, params and headers
    url = "https://api.twitch.tv/helix/clips"
    params = {"broadcaster_id": broadcaster_id}
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with clips
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


def get_vip_person_of_channel(token: str, broadcaster_id: str) -> Json:
    """
    Func which get channel vip persons
    :param broadcaster_id:
    :param token:
    :return:
    """
    # declaring url and headers
    url = f"https://api.twitch.tv/helix/channels/vips?broadcaster_id={broadcaster_id}"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with channel vip persons
    response = requests.get(url=url, headers=headers)
    return response.json()


def get_pools(token: str, broadcaster_id: str) -> Json:
    """
    Func which get pools
    :param broadcaster_id:
    :param token:
    :return:
    """
    # declaring url and headers
    url = f"https://api.twitch.tv/helix/polls?broadcaster_id={broadcaster_id}"
    headers = {
        "Client-Id": SETTINGS.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}",
    }
    # return json response with pools
    response = requests.get(url=url, headers=headers)
    return response.json()
