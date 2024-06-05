from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from starlette import status

from core.database.base import (
    twitch_clips,
    twitch_pools,
    twitch_global_emotes,
    twitch_channel_chat_settings,
    twitch_channel_emotes,
    twitch_channel_followers,
    twitch_channel_followed,
    twitch_channel_editor,
    twitch_channel_information,
    twitch_games_analytic,
    twitch_top_games,
    twitch_games,
    twitch_user,
    twitch_auth,
)
from core.dependencies import get_all_doc_form_collection

# twitch db router
router = APIRouter(
    prefix="/twitch/db",
    default_response_class=ORJSONResponse,
    tags=["Twitch DB"],
)


@router.get(
    path="/auth",
    status_code=status.HTTP_200_OK,
    summary="Get List Auth Credentials From DB",
)
async def get_auth_credentials_db():
    """
    Endpoint of get list auth credentials from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_auth)


@router.get(
    path="/user",
    status_code=status.HTTP_200_OK,
    summary="Get List Users From DB",
)
async def get_user_from_db():
    """
    Endpoint of get list users from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_user)


@router.get(
    path="/games",
    status_code=status.HTTP_200_OK,
    summary="Get Games From DB",
)
async def get_games_from_db():
    """
    Endpoint which get games from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_games)


@router.get(
    path="/games/top",
    status_code=status.HTTP_200_OK,
    summary="Get Top Games From DB",
)
async def get_top_games_from_db():
    """
    Endpoint which get top games from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_top_games)


@router.get(
    path="/games/analytic",
    status_code=status.HTTP_200_OK,
    summary="Get Game Analytics From DB",
)
async def get_games_analytic_from_db():
    """
    Endpoint which get games analytics from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_games_analytic)


@router.get(
    path="/channel",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Information From DB",
)
async def get_channel_information_db():
    """
    Endpoint which get channel information from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_channel_information)


@router.get(
    path="/channel/editor",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Editor From DB",
)
async def get_channel_editor_db():
    """
    Endpoint which get channel information from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_channel_editor)


@router.get(
    path="/channel/followed",
    status_code=status.HTTP_200_OK,
    summary="Get Followed Channels From DB",
)
async def get_followed_channels_db():
    """
    Endpoint which get followed channels from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_channel_followed)


@router.get(
    path="/channel/followers",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Followers From DB",
)
async def get_channel_followers_db():
    """
    Endpoint which get channel followers from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_channel_followers)


@router.get(
    path="/channel/emotes",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Emotes From DB",
)
async def get_channel_emotes_db():
    """
    Endpoint which get channel emotes from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_channel_emotes)


@router.get(
    path="/channel/chat/settings",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Chat Settings From DB",
)
async def get_channel_chat_settings_db():
    """
    Endpoint which get channel chat settings from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_channel_chat_settings)


@router.get(
    path="/channel/vip",
    status_code=status.HTTP_200_OK,
    summary="Get VIP's Channel Persons From DB",
)
async def get_vip_channel_person_db():
    """
    Endpoint which get VIP's channel persons from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_channel_chat_settings)


@router.get(
    path="/emotes/global",
    status_code=status.HTTP_200_OK,
    summary="Get Global Emotes From DB",
)
async def get_global_emotes_db():
    """
    Endpoint which get global emotes from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_global_emotes)


@router.get(
    path="/clips",
    status_code=status.HTTP_200_OK,
    summary="Get Clips From DB",
)
async def get_clips_db():
    """
    Endpoint which get clips from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_clips)


@router.get(
    path="/pools",
    status_code=status.HTTP_200_OK,
    summary="Get Pools From DB",
)
async def get_pools_db():
    """
    Endpoint which get pools from db
    :return:
    """
    return get_all_doc_form_collection(collection=twitch_pools)
