from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from pymongo.client_session import ClientSession
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
    twitch_channel_vip,
)
from core.dependencies import (
    get_all_doc_form_collection,
    check_data_on_exits_into_db,
    get_data_from_topic,
    get_db_session,
)

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
async def get_auth_credentials_db(session: ClientSession = get_db_session):
    """
    Endpoint of get list auth credentials from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-auth-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_auth, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_auth)


@router.get(
    path="/user",
    status_code=status.HTTP_200_OK,
    summary="Get List Users From DB",
)
async def get_user_from_db(session: ClientSession = get_db_session):
    """
    Endpoint of get list users from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-user-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_user, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_user)


@router.get(
    path="/games",
    status_code=status.HTTP_200_OK,
    summary="Get Games From DB",
)
async def get_games_from_db(session: ClientSession = get_db_session):
    """
    Endpoint which get games from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-games-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_games, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_games)


@router.get(
    path="/games/top",
    status_code=status.HTTP_200_OK,
    summary="Get Top Games From DB",
)
async def get_top_games_from_db(session: ClientSession = get_db_session):
    """
    Endpoint which get top games from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-top-games-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_top_games, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_top_games)


@router.get(
    path="/games/analytic",
    status_code=status.HTTP_200_OK,
    summary="Get Game Analytics From DB",
)
async def get_games_analytic_from_db(session: ClientSession = get_db_session):
    """
    Endpoint which get games analytics from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-games-analytic-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_games_analytic, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_games_analytic)


@router.get(
    path="/channel",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Information From DB",
)
async def get_channel_information_db(session: ClientSession = get_db_session):
    """
    Endpoint which get channel information from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(
        topic_name="twitch-channel-information-topic"
    )
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_channel_information, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_channel_information)


@router.get(
    path="/channel/editor",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Editor From DB",
)
async def get_channel_editor_db(session: ClientSession = get_db_session):
    """
    Endpoint which get channel information from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-channel-editor-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_channel_editor, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_channel_editor)


@router.get(
    path="/channel/followed",
    status_code=status.HTTP_200_OK,
    summary="Get Followed Channels From DB",
)
async def get_followed_channels_db(session: ClientSession = get_db_session):
    """
    Endpoint which get followed channels from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(
        topic_name="twitch-channel-followed-topic"
    )
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_channel_followed, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_channel_followed)


@router.get(
    path="/channel/followers",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Followers From DB",
)
async def get_channel_followers_db(session: ClientSession = get_db_session):
    """
    Endpoint which get channel followers from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(
        topic_name="twitch-channel-followers-topic"
    )
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_channel_followers, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_channel_followers)


@router.get(
    path="/channel/emotes",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Emotes From DB",
)
async def get_channel_emotes_db(session: ClientSession = get_db_session):
    """
    Endpoint which get channel emotes from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-channel-emotes-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_channel_emotes, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_channel_emotes)


@router.get(
    path="/channel/chat/settings",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Chat Settings From DB",
)
async def get_channel_chat_settings_db(
    session: ClientSession = get_db_session,
):
    """
    Endpoint which get channel chat settings from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(
        topic_name="twitch-channel-chat-settings-topic"
    )
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data,
        collection=twitch_channel_chat_settings,
        session=session,
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_channel_chat_settings)


@router.get(
    path="/channel/vip",
    status_code=status.HTTP_200_OK,
    summary="Get VIP's Channel Persons From DB",
)
async def get_vip_channel_person_db(session: ClientSession = get_db_session):
    """
    Endpoint which get VIP's channel persons from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-channel-vip-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_channel_vip, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_channel_vip)


@router.get(
    path="/emotes/global",
    status_code=status.HTTP_200_OK,
    summary="Get Global Emotes From DB",
)
async def get_global_emotes_db(session: ClientSession = get_db_session):
    """
    Endpoint which get global emotes from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-global-emotes-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_global_emotes, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_global_emotes)


@router.get(
    path="/clips",
    status_code=status.HTTP_200_OK,
    summary="Get Clips From DB",
)
async def get_clips_db(session: ClientSession = get_db_session):
    """
    Endpoint which get clips from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-clips-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_clips, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_clips)


@router.get(
    path="/pools",
    status_code=status.HTTP_200_OK,
    summary="Get Pools From DB",
)
async def get_pools_db(session: ClientSession = get_db_session):
    """
    Endpoint which get pools from db
    :return:
    """
    # get valid data from topic
    topic_data = get_data_from_topic(topic_name="twitch-pools-topic")
    # check data on exits into db
    check_data_on_exits_into_db(
        data=topic_data, collection=twitch_pools, session=session
    )
    # return all data from collection
    return get_all_doc_form_collection(collection=twitch_pools)
