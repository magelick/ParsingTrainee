from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from starlette import status

from pymongo.client_session import ClientSession

from core.utils.twitch import (
    authorize_by_twitch,
    get_twitch_tokens,
    get_user,
    get_games,
    get_top_games,
    get_game_analytics,
    get_channel_information,
    get_channel_editor,
    get_followed_channels,
    get_channel_followers,
    get_clips,
    get_channel_emotes,
    get_global_emotes,
    get_pools,
    get_vip_person_of_channel,
    get_chat_settings,
)

from core.types.twitch import (
    TwitchUserDetail,
    TwitchGameDetail,
    TwitchTopGameDetail,
    TwitchGameAnalyticDetail,
    TwitchChannelInformationDetail,
    TwitchChannelEditorDetail,
    TwitchChannelFollowersDetail,
    TwitchFollowedChannelsDetail,
    TwitchChannelEmotesDetail,
    TwitchGlobalEmotesDetail,
    TwitchChatSettingsDetail,
    TwitchClipsDetail,
    TwitchGetVIPPersonChannelDetail,
    TwitchPoolsDetail,
    TwitchTokensDetail,
)

from core.dependencies import (
    check_data_on_exist,
    get_db_session,
)


# twitch router
router = APIRouter(prefix="/twitch", default_response_class=ORJSONResponse)


@router.get(
    path="/auth/",
    status_code=status.HTTP_200_OK,
    summary="Authorize on Twitch",
    tags=["Twitch Auth"],
)
async def authorize():
    """
    Endpoint which redirect on page with important code in path params
    :return:
    """
    return authorize_by_twitch()


@router.get(
    path="/auth/{authorization_code}",
    status_code=status.HTTP_200_OK,
    summary="Get Twitch User Tokens And Other Variables",
    response_model=TwitchTokensDetail,
    tags=["Twitch Auth"],
)
async def get_tokens(
    authorization_code: str, session: ClientSession = get_db_session
) -> TwitchTokensDetail:
    """
    Endpoint which get
    :param session:
    :param authorization_code:
    :return:
    """
    # get auth credentials
    auth_data = get_twitch_tokens(authorization_code=authorization_code)
    # validate this data
    data = TwitchTokensDetail.model_validate(auth_data, from_attributes=True)
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(collection=twitch_auth, data=auth_data, session=session)
    # return valid data
    return data


@router.get(
    path="/auth/user/",
    status_code=status.HTTP_200_OK,
    summary="Get Twitch User Info",
    response_model=TwitchUserDetail,
    tags=["Twitch Auth"],
)
async def get_user_info(
    access_token: str, session: ClientSession = get_db_session
) -> TwitchUserDetail:
    """
    Endpoint which get user info with id by access token
    :param session:
    :param access_token:
    :return:
    """
    # get user
    user = get_user(token=access_token)
    # validate this data
    data = TwitchUserDetail.model_validate(user, from_attributes=True)
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(collection=twitch_user, data=user, session=session)
    # return valid data
    return data


@router.get(
    path="/games/{game_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Games",
    response_model=TwitchGameDetail,
    tags=["Twitch Actions"],
)
async def get_twitch_games(
    game_id: str,
    token: str,
    name: str,
    igdb_id: str,
    session: ClientSession = get_db_session,
) -> TwitchGameDetail:
    """
    Endpoint which get game by id
    :param session:
    :param game_id:
    :param token:
    :param name:
    :param igdb_id:
    :return:
    """
    # get game
    game = get_games(token=token, game_id=game_id, name=name, igdb_id=igdb_id)
    # validate this data
    data = TwitchGameDetail.model_validate(game, from_attributes=True)
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(collection=twitch_games, data=game, session=session)
    # return valid data
    return data


@router.get(
    path="/games/top/",
    status_code=status.HTTP_200_OK,
    summary="Get Top Games On Twitch",
    response_model=TwitchTopGameDetail,
    tags=["Twitch Actions"],
)
async def get_top_games_on_twitch(
    token: str, session: ClientSession = get_db_session
) -> TwitchTopGameDetail:
    """
    Endpoint which get top games on twitch
    :return:
    """
    # get top games
    top_games = get_top_games(token=token)
    # validate this data
    data = TwitchTopGameDetail.model_validate(top_games, from_attributes=True)
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(
    #     collection=twitch_top_games, data=top_games, session=session
    # )
    # return valid data
    return data


@router.get(
    path="/games/analytic/{game_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Game Analytic",
    response_model=TwitchGameAnalyticDetail,
    tags=["Twitch Actions"],
)
async def get_game_analytic(
    game_id: str, token: str, session: ClientSession = get_db_session
) -> TwitchGameAnalyticDetail:
    """
    Endpoint which get game analytic
    :param session:
    :param token:
    :param game_id:
    :return:
    """
    # get game analytic
    analytic = get_game_analytics(game_id=game_id, token=token)
    # validate this data
    data = TwitchGameAnalyticDetail.model_validate(
        analytic, from_attributes=True
    )
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(
    #     collection=twitch_games_analytic, data=analytic, session=session
    # )
    # return valid data
    return data


@router.get(
    path="/channel/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Information",
    response_model=TwitchChannelInformationDetail,
    tags=["Twitch Actions"],
)
async def get_channel_information_on_twitch(
    token: str, broadcaster_id: str, session: ClientSession = get_db_session
) -> TwitchChannelInformationDetail:
    """
    Endpoint which get channel information
    :param session:
    :param token:
    :param broadcaster_id:
    :return:
    """
    # get channel information
    info = get_channel_information(token=token, broadcaster_id=broadcaster_id)
    # validate this data
    data = TwitchChannelInformationDetail.model_validate(
        info, from_attributes=True
    )
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(
    #     collection=twitch_channel_information, data=info, session=session
    # )
    # return valid data
    return data


@router.get(
    path="/channel/editor/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Editor",
    response_model=TwitchChannelEditorDetail,
    tags=["Twitch Actions"],
)
async def get_channel_editor_on_twitch(
    token: str, broadcaster_id: str, session: ClientSession = get_db_session
) -> TwitchChannelEditorDetail:
    """
    Endpoint which get channel information
    :param session:
    :param token:
    :param broadcaster_id:
    :return:
    """
    # get channel information
    info = get_channel_editor(token=token, broadcaster_id=broadcaster_id)
    # validate this data
    data = TwitchChannelEditorDetail.model_validate(info, from_attributes=True)
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(
    #     collection=twitch_channel_editor, data=info, session=session
    # )
    # return valid data
    return data


@router.get(
    path="/channel/followed/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Followed Channels",
    response_model=TwitchFollowedChannelsDetail,
    tags=["Twitch Actions"],
)
async def get_user_followed_channels(
    user_id: str, token: str, session: ClientSession = get_db_session
) -> TwitchFollowedChannelsDetail:
    """
    Endpoint which get user followed channels
    :param session:
    :param token:
    :param user_id:
    :return:
    """
    # get followed channels
    channels = get_followed_channels(user_id=user_id, token=token)
    # validate this data
    data = TwitchFollowedChannelsDetail.model_validate(
        channels, from_attributes=True
    )
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(
    #     collection=twitch_channel_followed, data=channels, session=session
    # )
    # return valid data
    return data


@router.get(
    path="/channel/followers/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Followers",
    response_model=TwitchChannelFollowersDetail,
    tags=["Twitch Actions"],
)
async def get_channel_followers_on_twitch(
    broadcaster_id: str, token: str, session: ClientSession = get_db_session
) -> TwitchChannelFollowersDetail:
    """
    Endpoint which get channel followers
    :param session:
    :param token:
    :param broadcaster_id:
    :return:
    """
    # get channel followers
    followers = get_channel_followers(
        token=token, broadcaster_id=broadcaster_id
    )
    # validate this data
    data = TwitchChannelFollowersDetail.model_validate(
        followers, from_attributes=True
    )
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(
    #     collection=twitch_channel_followers, data=followers, session=session
    # )
    # return valid data
    return data


@router.get(
    path="/channel/emotes/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Emotes",
    response_model=TwitchChannelEmotesDetail,
    tags=["Twitch Actions"],
)
async def get_channel_emotes_on_twitch(
    broadcaster_id: str, token: str, session: ClientSession = get_db_session
) -> TwitchChannelEmotesDetail:
    """
    Endpoint which get channel emotes
    :param session:
    :param broadcaster_id:
    :param token:
    :return:
    """
    # get channel emotes
    emotes = get_channel_emotes(token=token, broadcaster_id=broadcaster_id)
    # validate this data
    data = TwitchChannelEmotesDetail.model_validate(
        emotes, from_attributes=True
    )
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(
    #     collection=twitch_channel_emotes, data=emotes, session=session
    # )
    # return valid data
    return data


@router.get(
    path="/channel/chat/settings/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Chat Settings",
    response_model=TwitchChatSettingsDetail,
    tags=["Twitch Actions"],
)
async def get_chat_settings_on_twitch(
    broadcaster_id: str, token: str, session: ClientSession = get_db_session
) -> TwitchChatSettingsDetail:
    """
    Endpoint which get chat settings
    :param session:
    :param token:
    :param broadcaster_id:
    :return:
    """
    # get chat settings
    settings = get_chat_settings(token=token, broadcaster_id=broadcaster_id)
    # validate this data
    data = TwitchChatSettingsDetail.model_validate(
        settings, from_attributes=True
    )
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(
    #     collection=twitch_channel_chat_settings, data=settings, session=session
    # )
    # return valid data
    return data


@router.get(
    path="/channel/vip/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get VIP's Channel Person",
    response_model=TwitchGetVIPPersonChannelDetail,
    tags=["Twitch Actions"],
)
async def get_vip_persons_on_twitch(
    broadcaster_id: str, token: str, session: ClientSession = get_db_session
) -> TwitchGetVIPPersonChannelDetail:
    """
    Endpoint which get VIP's Channel Person
    :param session:
    :param broadcaster_id:
    :param token:
    :return:
    """
    # get vip persons
    vip_persons = get_vip_person_of_channel(
        token=token, broadcaster_id=broadcaster_id
    )
    # validate this data
    data = TwitchGetVIPPersonChannelDetail.model_validate(
        vip_persons, from_attributes=True
    )
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(
    #     collection=twitch_channel_vip, data=vip_persons, session=session
    # )
    # return valid data
    return data


@router.get(
    path="/emotes/global/",
    status_code=status.HTTP_200_OK,
    summary="Get Global Emotes",
    response_model=TwitchGlobalEmotesDetail,
    tags=["Twitch Actions"],
)
async def get_global_emotes_on_twitch(
    token: str, session: ClientSession = get_db_session
) -> TwitchGlobalEmotesDetail:
    """
    Endpoint which get global emotes
    :return:
    """
    # get global emotes
    emotes = get_global_emotes(token=token)
    # validate this data
    data = TwitchGlobalEmotesDetail.model_validate(
        emotes, from_attributes=True
    )
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(
    #     collection=twitch_global_emotes, data=emotes, session=session
    # )
    # return valid data
    return data


@router.get(
    path="/clips/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Clips",
    response_model=TwitchClipsDetail,
    tags=["Twitch Actions"],
)
async def get_clips_on_twitch(
    broadcaster_id: str, token: str, session: ClientSession = get_db_session
) -> TwitchClipsDetail:
    """
    Endpoint which get clips
    :param session:
    :param broadcaster_id:
    :param token:
    :return:
    """
    # get clips
    clips = get_clips(token=token, broadcaster_id=broadcaster_id)
    # validate this data
    data = TwitchClipsDetail.model_validate(clips, from_attributes=True)
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(collection=twitch_clips, data=clips, session=session)
    # return valid data
    return data


@router.get(
    path="/pools/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Pools",
    response_model=TwitchPoolsDetail,
    tags=["Twitch Actions"],
)
async def get_pools_on_twitch(
    broadcaster_id: str, token: str, session: ClientSession = get_db_session
) -> TwitchPoolsDetail:
    """
    Endpoint which get pools
    :param session:
    :param broadcaster_id:
    :param token:
    :return:
    """
    # get pools
    pools = get_pools(token=token, broadcaster_id=broadcaster_id)
    # validate this data
    data = TwitchPoolsDetail.model_validate(pools, from_attributes=True)
    # check validate data on exist
    check_data_on_exist(validate_data=data)  # type: ignore
    # add valid data into db collection
    # add_doc_into_collection(collection=twitch_pools, data=pools, session=session)
    # return valid data
    return data
