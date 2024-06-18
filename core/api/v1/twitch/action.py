from typing import Union

from fastapi import APIRouter, HTTPException
from fastapi.responses import ORJSONResponse
from fastapi_cache.decorator import cache
from starlette import status

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
    TwitchPoolsDetail,
    TwitchTokensDetail,
    TwitchVIPPersonChannelDetail,
)

from core.dependencies import check_data_on_exist, add_into_topic

# twitch router
router = APIRouter(prefix="/twitch", default_response_class=ORJSONResponse)


@router.get(
    path="/auth/",
    status_code=status.HTTP_200_OK,
    response_model=str,
    summary="Authorize on Twitch",
    tags=["Twitch Auth"],
)
async def authorize() -> Union[str, ORJSONResponse]:
    """
    Endpoint which redirect on page with important code in path params
    :return:
    """
    try:
        # return url with authorization code
        return authorize_by_twitch()
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/auth/{authorization_code}",
    status_code=status.HTTP_200_OK,
    summary="Get Twitch User Tokens And Other Variables",
    response_model=TwitchTokensDetail,
    tags=["Twitch Auth"],
)
async def get_tokens(
    authorization_code: str,
) -> Union[TwitchTokensDetail, ORJSONResponse]:
    """
    Endpoint which get
    :param authorization_code:
    :return:
    """
    try:
        # get auth credentials
        auth_data = get_twitch_tokens(authorization_code=authorization_code)
        # validate this data
        data = TwitchTokensDetail.model_validate(
            auth_data, from_attributes=True
        )
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-auth-topic", data=auth_data)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/auth/user/",
    status_code=status.HTTP_200_OK,
    summary="Get Twitch User Info",
    response_model=TwitchUserDetail,
    tags=["Twitch Auth"],
)
async def get_user_info(
    access_token: str,
) -> Union[TwitchUserDetail, ORJSONResponse]:
    """
    Endpoint which get user info with id by access token
    :param access_token:
    :return:
    """
    try:
        # get user
        user = get_user(token=access_token)
        # validate this data
        data = TwitchUserDetail.model_validate(user, from_attributes=True)
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-user-topic", data=user)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/games/{game_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Games",
    response_model=TwitchGameDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_twitch_games(
    game_id: str,
    token: str,
    name: str,
    igdb_id: str,
) -> Union[TwitchGameDetail, ORJSONResponse]:
    """
    Endpoint which get game by id
    :param game_id:
    :param token:
    :param name:
    :param igdb_id:
    :return:
    """
    try:
        # get game
        game = get_games(
            token=token, game_id=game_id, name=name, igdb_id=igdb_id
        )
        # validate this data
        data = TwitchGameDetail.model_validate(game, from_attributes=True)
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-games-topic", data=game)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/games/top/",
    status_code=status.HTTP_200_OK,
    summary="Get Top Games On Twitch",
    response_model=TwitchTopGameDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_top_games_on_twitch(
    token: str,
) -> Union[TwitchTopGameDetail, ORJSONResponse]:
    """
    Endpoint which get top games on twitch
    :return:
    """
    try:
        # get top games
        top_games = get_top_games(token=token)
        # validate this data
        data = TwitchTopGameDetail.model_validate(
            top_games, from_attributes=True
        )
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-top-games-topic", data=top_games)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/games/analytic/{game_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Game Analytic",
    response_model=TwitchGameAnalyticDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_game_analytic(
    game_id: str, token: str
) -> Union[TwitchGameAnalyticDetail, ORJSONResponse]:
    """
    Endpoint which get game analytic
    :param token:
    :param game_id:
    :return:
    """
    try:
        # get game analytic
        analytic = get_game_analytics(game_id=game_id, token=token)
        # validate this data
        data = TwitchGameAnalyticDetail.model_validate(
            analytic, from_attributes=True
        )
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-games-analytic-topic", data=analytic)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/channel/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Information",
    response_model=TwitchChannelInformationDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_channel_information_on_twitch(
    token: str, broadcaster_id: str
) -> Union[TwitchChannelInformationDetail, ORJSONResponse]:
    """
    Endpoint which get channel information
    :param token:
    :param broadcaster_id:
    :return:
    """
    try:
        # get channel information
        info = get_channel_information(
            token=token, broadcaster_id=broadcaster_id
        )
        # validate this data
        data = TwitchChannelInformationDetail.model_validate(
            info, from_attributes=True
        )
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(
            topic_name="twitch-channel-information-topic", data=info
        )
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/channel/editor/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Editor",
    response_model=TwitchChannelEditorDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_channel_editor_on_twitch(
    token: str, broadcaster_id: str
) -> Union[TwitchChannelEditorDetail, ORJSONResponse]:
    """
    Endpoint which get channel information
    :param token:
    :param broadcaster_id:
    :return:
    """
    try:
        # get channel information
        editor = get_channel_editor(token=token, broadcaster_id=broadcaster_id)
        # validate this data
        data = TwitchChannelEditorDetail.model_validate(
            editor, from_attributes=True
        )
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-channel-editor-topic", data=editor)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/channel/followed/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Followed Channels",
    response_model=TwitchFollowedChannelsDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_user_followed_channels(
    user_id: str, token: str
) -> Union[TwitchFollowedChannelsDetail, ORJSONResponse]:
    """
    Endpoint which get user followed channels
    :param token:
    :param user_id:
    :return:
    """
    try:
        # get followed channels
        channels = get_followed_channels(user_id=user_id, token=token)
        # validate this data
        data = TwitchFollowedChannelsDetail.model_validate(
            channels, from_attributes=True
        )
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(
            topic_name="twitch-channel-followed-topic", data=channels
        )
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/channel/followers/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Followers",
    response_model=TwitchChannelFollowersDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_channel_followers_on_twitch(
    broadcaster_id: str, token: str
) -> Union[TwitchChannelFollowersDetail, ORJSONResponse]:
    """
    Endpoint which get channel followers

    :param token:
    :param broadcaster_id:
    :return:
    """
    try:
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
        # add valid data into topic
        add_into_topic(
            topic_name="twitch-channel-followers-topic", data=followers
        )
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/channel/emotes/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Channel Emotes",
    response_model=TwitchChannelEmotesDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_channel_emotes_on_twitch(
    broadcaster_id: str, token: str
) -> Union[TwitchChannelEmotesDetail, ORJSONResponse]:
    """
    Endpoint which get channel emotes
    :param broadcaster_id:
    :param token:
    :return:
    """
    try:
        # get channel emotes
        emotes = get_channel_emotes(token=token, broadcaster_id=broadcaster_id)
        # validate this data
        data = TwitchChannelEmotesDetail.model_validate(
            emotes, from_attributes=True
        )
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-channel-emotes-topic", data=emotes)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/channel/chat/settings/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Chat Settings",
    response_model=TwitchChatSettingsDetail,
    tags=["Twitch Actions"],
)
async def get_chat_settings_on_twitch(
    broadcaster_id: str, token: str
) -> Union[TwitchChatSettingsDetail, ORJSONResponse]:
    """
    Endpoint which get chat settings
    :param token:
    :param broadcaster_id:
    :return:
    """
    try:
        # get chat settings
        settings = get_chat_settings(
            token=token, broadcaster_id=broadcaster_id
        )
        # validate this data
        data = TwitchChatSettingsDetail.model_validate(
            settings, from_attributes=True
        )
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(
            topic_name="twitch-channel-chat-settings-topic", data=settings
        )
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/channel/vip/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get VIP's Channel Person",
    response_model=TwitchVIPPersonChannelDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_vip_persons_on_twitch(
    broadcaster_id: str, token: str
) -> Union[TwitchVIPPersonChannelDetail, ORJSONResponse]:
    """
    Endpoint which get VIP's Channel Person
    :param broadcaster_id:
    :param token:
    :return:
    """
    try:
        # get vip persons
        vip_persons = get_vip_person_of_channel(
            token=token, broadcaster_id=broadcaster_id
        )
        # validate this data
        data = TwitchVIPPersonChannelDetail.model_validate(
            vip_persons, from_attributes=True
        )
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-channel-vip-topic", data=vip_persons)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/emotes/global/",
    status_code=status.HTTP_200_OK,
    summary="Get Global Emotes",
    response_model=TwitchGlobalEmotesDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_global_emotes_on_twitch(
    token: str,
) -> Union[TwitchGlobalEmotesDetail, ORJSONResponse]:
    """
    Endpoint which get global emotes
    :return:
    """
    try:
        # get global emotes
        emotes = get_global_emotes(token=token)
        # validate this data
        data = TwitchGlobalEmotesDetail.model_validate(
            emotes, from_attributes=True
        )
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-global-emotes-topic", data=emotes)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/clips/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Clips",
    response_model=TwitchClipsDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_clips_on_twitch(
    broadcaster_id: str, token: str
) -> Union[TwitchClipsDetail, ORJSONResponse]:
    """
    Endpoint which get clips
    :param broadcaster_id:
    :param token:
    :return:
    """
    try:
        # get clips
        clips = get_clips(token=token, broadcaster_id=broadcaster_id)
        # validate this data
        data = TwitchClipsDetail.model_validate(clips, from_attributes=True)
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-clips-topic", data=clips)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")


@router.get(
    path="/pools/{broadcaster_id}",
    status_code=status.HTTP_200_OK,
    summary="Get Pools",
    response_model=TwitchPoolsDetail,
    tags=["Twitch Actions"],
)
@cache()
async def get_pools_on_twitch(
    broadcaster_id: str, token: str
) -> Union[TwitchPoolsDetail, ORJSONResponse]:
    """
    Endpoint which get pools
    :param broadcaster_id:
    :param token:
    :return:
    """
    try:
        # get pools
        pools = get_pools(token=token, broadcaster_id=broadcaster_id)
        # validate this data
        data = TwitchPoolsDetail.model_validate(pools, from_attributes=True)
        # check validate data on exist
        check_data_on_exist(validate_data=data)  # type: ignore
        # add valid data into topic
        add_into_topic(topic_name="twitch-pools-topic", data=pools)
        # return valid data
        return data
    except HTTPException as e:
        return ORJSONResponse(
            status_code=e.status_code, content=f"Error: {str(e)}"
        )
    except Exception as e:
        return ORJSONResponse(status_code=500, content=f"Error: {str(e)}")
