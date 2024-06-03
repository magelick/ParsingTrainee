from typing import List, Dict

from pydantic import Field

from core.types.base import DTO


class TwitchBasic(DTO):
    """
    Basic schema of Twitch parser
    """

    ...


class TwitchTokensDetail(TwitchBasic):
    """
    Schema of get twitch tokens
    """

    access_token: str = Field(default=..., title="Access Token")

    expires_in: int = Field(default=..., title="Time expiring")

    id_token: str = Field(default=None, title="Token ID")

    refresh_token: str = Field(default=..., title="Refresh token")

    scope: list = Field(default=..., title="Scope")

    token_type: str = Field(default="bearer", title="Token Type")


class TwitchUserInfo(TwitchBasic):
    """
    Schema of get user info
    """

    id: str = Field(default=..., title="ID")
    login: str = Field(default=..., title="Login")
    display_name: str = Field(default=..., title="Display Name")
    type: str = Field(default=None, title="Display Name")
    broadcaster_type: str = Field(default=..., title="Broadcaster Type")
    description: str = Field(default=..., title="Description")
    profile_image_url: str = Field(default=..., title="Profile Image Url")
    offline_image_url: str = Field(default=..., title="Profile Image Url")
    view_count: int = Field(default=..., title="View Count")
    email: str = Field(default=None, title="Email")
    created_at: str = Field(default=..., title="Created At")


class TwitchUserDetail(TwitchBasic):
    """
    Schema of get user detail
    """

    data: List[TwitchUserInfo] = Field(default=..., title="Data User Detail")


class TwitchGameDetailInfo(TwitchBasic):
    """
    Schema of get game detail info
    """

    id: str = Field(
        default=...,
        title="ID",
    )

    name: str = Field(default=..., title="Name")

    box_art_url: str = Field(default=..., title="Box art url")

    igdb_id: str = Field(default=..., title="Igdb_id")


class TwitchGameDetail(TwitchBasic):
    """
    Schema of get game detail
    """

    data: List[TwitchGameDetailInfo] = Field(
        default=..., title="Data Game Detail"
    )


class TwitchTopGameDetail(TwitchGameDetail):
    """
    Schema of get top game detail
    """

    pagination: Dict = Field(default=..., title="Pagination")


class TwitchGameAnalyticInfo(TwitchBasic):
    """
    Schema fo get game analytic info
    """

    game_id: str = Field(default=..., title="Game ID")
    url: str = Field(default=..., title="URL")
    type: str = Field(default="overview_v2", title="Type")
    date_range: dict = Field(default=..., title="Date Range")


class TwitchGameAnalyticDetail(TwitchBasic):
    """
    Schema of get game analytic
    """

    data: List[TwitchGameAnalyticInfo] = Field(
        default=..., title="Data Game Analytic Detail"
    )
    pagination: Dict = Field(default=..., title="Pagination")


class TwitchChannelInformationInfo(TwitchBasic):
    """
    Schema of get Channel information
    """

    broadcaster_id: str = Field(default=..., title="Broadcaster ID")

    broadcaster_login: str = Field(default=..., title="Broadcaster Login")

    broadcaster_name: str = Field(default=..., title="Broadcaster Name")

    broadcaster_language: str = Field(
        default=..., title="Broadcaster Language"
    )

    game_name: str = Field(default=..., title="Game Name")

    game_id: str = Field(default=..., title="Game ID")

    title: str = Field(default=..., title="Title")

    delay: int = Field(default=..., title="Delay")

    tags: list = Field(default=..., title="Tags")

    content_classification_labels: list = Field(
        default=..., title="Content Classification Labels"
    )

    is_branded_content: bool = Field(default=..., title="Branded content")


class TwitchChannelInformationDetail(TwitchBasic):
    """
    Schema of Channel Information Detail
    """

    data: List[TwitchChannelInformationInfo] = Field(
        default=..., title="Data Channel Information Detail"
    )


class TwitchChannelEditorInfo(TwitchBasic):
    """
    Schema of get channel editor info
    """

    user_id: str = Field(default=..., title="User ID")

    user_name: str = Field(default=..., title="User Name")

    created_at: str = Field(default=..., title="Time created")


class TwitchChannelEditorDetail(TwitchBasic):
    """
    Schema of get channel editor detail
    """

    data: List[TwitchChannelEditorInfo] = Field(
        default=..., title="Data Channel Editor Detail"
    )


class TwitchFollowedChannelsInfo(TwitchBasic):
    """
    Schema of get followed channels info
    """

    broadcaster_id: str = Field(default=..., title="Broadcaster ID")

    broadcaster_login: str = Field(default=..., title="Broadcaster Login")

    broadcaster_name: str = Field(default=..., title="Broadcaster name")

    followed_at: str = Field(default=..., title="Time followed")


class TwitchFollowedChannelsDetail(TwitchBasic):
    """
    Schema of get followed channels detail
    """

    total: int = Field(default=None, title="Total followed channels")

    data: List[TwitchFollowedChannelsInfo] = Field(
        default=..., title="Data Followed Channels Detail"
    )

    pagination: Dict = Field(default=None, title="Pagination")


class TwitchChannelFollowersInfo(TwitchBasic):
    """
    Schema of get channel followers info
    """

    followed_at: str = Field(default=..., title="Time followed")

    user_id: str = Field(default=..., title="User id")

    user_login: str = Field(default=..., title="User Login")

    user_name: str = Field(default=..., title="User Name")


class TwitchChannelFollowersDetail(TwitchBasic):
    """
    Schema of get channel followers detail
    """

    total: int = Field(default=..., title="Total followers")

    data: List[TwitchChannelFollowersInfo] = Field(
        default=..., title="Data Channel Followers Detail"
    )

    pagination: Dict = Field(default=None, title="Pagination")


class TwitchChannelEmotesInfo(TwitchBasic):
    """
    Schema of get channel emotes info
    """

    id: str = Field(default=..., title="ID")

    name: str = Field(default=..., title="Name")

    images: dict = Field(default=..., title="Images")

    tier: str = Field(default=..., title="Tier")

    emote_type: str = Field(default=..., title="Emote Type")

    emote_set_id: str = Field(default=..., title="Emote Set ID")

    format: list = Field(default=..., title="Format")

    scale: list = Field(default=..., title="Scale")

    theme_mode: list = Field(default=..., title="Theme Mode")


class TwitchChannelEmotesDetail(TwitchBasic):
    """
    Schema of get channel emotes detail
    """

    data: List[TwitchChannelFollowersInfo] = Field(
        default=..., title="Data Channels Emotes Detail"
    )
    template: str = Field(default=..., title="Template")


class TwitchGlobalEmotesInfo(TwitchBasic):
    """
    Schema fo get global emotes info
    """

    id: str = Field(default=..., title="ID")

    name: str = Field(default=..., title="Name")

    images: dict = Field(default=..., title="Images")

    format: list = Field(default=..., title="Format")

    scale: list = Field(default=..., title="Scale")

    theme_mode: list = Field(default=..., title="Theme Mode")


class TwitchGlobalEmotesDetail(TwitchBasic):
    """
    Schema fo get global emotes detail
    """

    data: List[TwitchGlobalEmotesInfo] = Field(
        default=..., title="Data Global Emotes Detail"
    )
    template: str = Field(default=..., title="Template")


class TwitchChatSettingsInfo(TwitchBasic):
    """
    Schema of get chat settings info
    """

    broadcaster_id: str = Field(default=..., title="Broadcaster ID")

    emote_mode: bool = Field(default=..., title="Emote Mode")

    follower_mode: bool = Field(default=..., title="Follower Mode")

    follower_mode_duration: int = Field(
        default=..., title="Follower Mode Duration"
    )

    moderator_id: str = Field(default=..., title="Moderator ID")

    non_moderator_chat_delay: bool = Field(
        default=..., title="Non Moderator Chat Delay"
    )

    non_moderator_chat_delay_duration: int = Field(
        default=..., title="Non Moderator Chat Delay Duration"
    )

    slow_mode: bool = Field(default=..., title="Slow Mode")

    slow_mode_wait_time: int = Field(default=..., title="Slow Mode Wait Time")

    subscriber_mode: bool = Field(default=..., title="Subscriber Mode")

    unique_chat_mode: bool = Field(default=..., title="Unique Chat Mode")


class TwitchChatSettingsDetail(TwitchBasic):
    """
    Schema of get chat settings detail
    """

    data: List[TwitchChatSettingsInfo] = Field(
        default=..., title="Data Chat Settings Detail"
    )


class TwitchClipsInfo(TwitchBasic):
    """
    Schema of get clips info
    """

    id: str = Field(default=..., title="ID")

    url: str = Field(default=..., title="Url")

    embed_url: str = Field(default=..., title="Embed Url")

    broadcaster_id: str = Field(default=..., title="Broadcaster ID")

    broadcaster_name: str = Field(default=..., title="Broadcaster Name")

    creator_id: str = Field(default=..., title="Creator ID")

    creator_name: str = Field(default=..., title="Creator Name")

    video_id: str = Field(default=..., title="Video ID")

    game_id: str = Field(default=..., title="Game ID")

    language: str = Field(default=..., title="Language")

    title: str = Field(default=..., title="Title")

    view_count: int = Field(default=..., title="View Count")

    created_at: str = Field(default=..., title="Time Created")

    thumbnail_url: str = Field(default=..., title="Thumbnail Url")

    duration: float = Field(default=..., title="Duration")

    vod_offset: int = Field(default=..., title="Vod Offset")

    is_featured: bool = Field(default=..., title="Is Featured")


class TwitchClipsDetail(TwitchBasic):
    """
    Schema of get clips detail
    """

    data: List[TwitchClipsInfo] = Field(
        default=..., title="Data Global Emotes Detail"
    )

    pagination: Dict = Field(default=None, title="Pagination")


class TwitchGetVIPPersonChannelInfo(TwitchBasic):
    """
    Schema of get channel VIP person info
    """

    user_id: str = Field(default=..., title="User ID")

    user_name: str = Field(default=..., title="User Name")

    user_login: str = Field(default=..., title="User Login")


class TwitchGetVIPPersonChannelDetail(TwitchBasic):
    """
    Schema of get channel VIP person detail
    """

    data: List[TwitchGetVIPPersonChannelInfo] = Field(
        default=..., title="Data VIP Channel Person Detail"
    )

    pagination: Dict = Field(default=None, title="Pagination")


class TwitchPoolsChoices(TwitchBasic):
    """
    Schema of get pool choices
    """

    id: str = Field(default=..., title="ID")

    title: str = Field(default=..., title="Title")

    votes: int = Field(default=..., title="Votes")

    channel_points_votes: int = Field(
        default=..., title="Channel Points Votes"
    )

    bits_votes: int = Field(default=..., title="Bits Votes")


class TwitchPoolsInfo(TwitchBasic):
    """
    Schema of get pools info
    """

    id: str = Field(default=..., title="ID")

    broadcaster_id: str = Field(default=..., title="Broadcaster ID")

    broadcaster_name: str = Field(default=..., title="Broadcaster Name")

    broadcaster_login: str = Field(default=..., title="Broadcaster Login")

    title: str = Field(default=..., title="Title")

    choices: List[TwitchPoolsChoices] = Field(default=..., title="Choices")

    bits_voting_enabled: bool = Field(default=..., title="Bits Voting Enabled")

    bits_per_vote: int = Field(default=..., title="Bits Per Vote")

    channel_points_voting_enabled: bool = Field(
        default=..., title="Channel Points Voting Enabled"
    )

    channel_points_per_vote: int = Field(
        default=..., title="Channel Points Per Vote"
    )

    status: str = Field(default=..., title="Status")

    duration: int = Field(default=..., title="Duration")

    started_at: str = Field(default=..., title="Time Started")


class TwitchPoolsDetail(TwitchBasic):
    """
    Schema of get pools detail
    """

    data: List[TwitchPoolsInfo] = Field(
        default=..., title="Data VIP Channel Person Detail"
    )

    pagination: Dict = Field(default=None, title="Pagination")
