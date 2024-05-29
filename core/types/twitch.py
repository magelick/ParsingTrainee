from pydantic import Field

from core.types.base import DTO


class TwitchBasic(DTO):
    """
    Basic schema of Twitch parser
    """

    ...


class TwitchTokens(TwitchBasic):
    """
    Schema of get twitch tokens
    """

    # access token
    access_token: str = Field(default=..., title="Access Token")
    # time expiring
    expires_in: int = Field(default=..., title="Time expiring")
    # token id
    id_token: int = Field(default=..., title="Token ID")
    # refresh token
    refresh_token: str = Field(default=..., title="Refresh token")
    # scope
    scope: list = Field(default=..., title="Scope")
    # token type
    token_type: str = "bearer"


class TwitchGameDetail(TwitchBasic):
    """
    Schema of get game detail
    """

    # game id
    id: str = Field(default=..., title="ID", description="ID some game")
    # game name
    name: str = Field(default=..., title="Name", description="Name some game")
    # game box art url
    box_art_url: str = Field(
        default=..., title="Box art url", description="Box art url some game"
    )
    # game igdb_id
    igdb_id: str = Field(
        default=..., title="Igdb_id", description="Igdb_id some game"
    )


class TwitchTopGameDetail(TwitchGameDetail):
    """
    Schema of get top game detail
    """

    ...


class TwitchChannelInformationDetail(TwitchBasic):
    """
    Schema of get Channel information
    """

    # broadcaster id
    broadcaster_id: str = Field(default=..., title="Broadcaster ID")
    # broadcaster login
    broadcaster_login: str = Field(default=..., title="Broadcaster Login")
    # broadcaster name
    broadcaster_name: str = Field(default=..., title="Broadcaster Name")
    # broadcaster language
    broadcaster_language: str = Field(
        default=..., title="Broadcaster language"
    )
    # game name
    game_name: str = Field(default=..., title="Game name")
    # game id
    game_id: str = Field(default=..., title="Game ID")
    # title
    title: str = Field(default=..., title="Title")
    # delay
    delay: int = Field(default=..., title="Delay")
    # tags
    tags: list = Field(default=..., title="Tags")
    # content classification labels
    content_classification_labels: list = Field(
        default=..., title="content classification labels"
    )
    # branded content
    is_branded_content: bool = Field(default=..., title="Branded content")


class TwitchChannelEditorDetail(TwitchBasic):
    """
    Schema of get channel editor
    """

    # user id
    user_id: str = Field(default=..., title="User ID")
    # user name
    user_name: str = Field(default=..., title="User Name")
    # time created
    created_at: str = Field(default=..., title="Time created")


class TwitchFollowedChannelsDetail(TwitchBasic):
    """
    Schema of get followed channels
    """

    # broadcaster id
    broadcaster_id: str = Field(default=..., title="Broadcaster ID")
    # broadcaster login
    broadcaster_login: str = Field(default=..., title="Broadcaster Login")
    # broadcaster name
    broadcaster_name: str = Field(default=..., title="Broadcaster name")
    # time followed
    followed_at: str = Field(default=..., title="Time followed")
    # total
    total: int = Field(default=..., title="Total followed channels")


class TwitchChannelFollowersDetail(TwitchBasic):
    """
    Schema of get channel followers
    """

    # time followed
    followed_at: str = Field(default=..., title="Time followed")
    # user id
    user_id: str = Field(default=..., title="User id")
    # user login
    user_login: str = Field(default=..., title="User Login")
    # user name
    user_name: str = Field(default=..., title="User Name")
    # total
    total: int = Field(default=..., title="Total followers")


class TwitchChannelEmotesDetail(TwitchBasic):
    """
    Schema of get channel emotes
    """

    # id
    id: str = Field(default=..., title="ID")
    # name
    name: str = Field(default=..., title="Name")
    # tier
    tier: str = Field(default=..., title="Tier")
    # emote type
    emote_type: str = Field(default=..., title="Emote Type")
    # emote id
    emote_set_id: str = Field(default=..., title="Emote ID")
    # emote format
    format: list = Field(default=..., title="Emote Format")
    # scale
    scale: list = Field(default=..., title="Scale")
    # theme mode
    theme_mode: list = Field(default=..., title="Theme Mode")
    # template
    template: str = Field(default=..., title="Template")


class TwitchGlobalEmotesDetail(TwitchChannelEmotesDetail):
    """
    Schema fo get global emotes
    """


class TwitchChatSettingsDetail(TwitchBasic):
    """
    Schema of get chat settings
    """

    # broadcaster id
    broadcaster_id: str = Field(default=..., title="Broadcaster ID")
    # emote mode
    emote_mode: bool = Field(default=..., title="Emote Mode")
    # follower mode
    follower_mode: bool = Field(default=..., title="Follower Mode")
    # follower mode duration
    follower_mode_duration: int = Field(
        default=..., title="Follower Mode Duration"
    )
    # moderator id
    moderator_id: str = Field(default=..., title="Moderator ID")
    # non moderator chat delay
    non_moderator_chat_delay: bool = Field(
        default=..., title="Non Moderator Chat Delay"
    )
    # non moderator chat delay duration
    non_moderator_chat_delay_duration: int = Field(
        default=..., title="Non Moderator Chat Delay Duration"
    )
    # slow mode
    slow_mode: bool = Field(default=..., title="Slow Mode")
    # slow mode wait time
    slow_mode_wait_time: int = Field(default=..., title="Slow Mode Wait Time")
    # subscriber mode
    subscriber_mode: bool = Field(default=..., title="Subscriber Mode")
    # unique chat mode
    unique_chat_mode: bool = Field(default=..., title="Unique Chat Mode")


class TwitchClipsDetail(TwitchBasic):
    """
    Schema of get clips
    """

    # id
    id: str = Field(default=..., title="ID")
    # url
    url: str = Field(default=..., title="Url")
    # embed url
    embed_url: str = Field(default=..., title="Embed Url")
    # broadcaster id
    broadcaster_id: str = Field(default=..., title="Broadcaster ID")
    # broadcaster name
    broadcaster_name: str = Field(default=..., title="Broadcaster Name")
    # creator id
    creator_id: str = Field(default=..., title="Creator ID")
    # creator name
    creator_name: str = Field(default=..., title="Creator Name")
    # video id
    video_id: str = Field(default=..., title="Video ID")
    # game id
    game_id: str = Field(default=..., title="Game ID")
    # language
    language: str = Field(default=..., title="Language")
    # title
    title: str = Field(default=..., title="Title")
    # view count
    view_count: int = Field(default=..., title="View Count")
    # time created
    created_at: str = Field(default=..., title="Time Created")
    # thumbnail url
    thumbnail_url: str = Field(default=..., title="Thumbnail Url")
    # duration
    duration: float = Field(default=..., title="Duration")
    # vod offset
    vod_offset: int = Field(default=..., title="Vod Offset")
    # is featured
    is_featured: bool = Field(default=..., title="Is Featured")


class TwitchGetVIPPersonChannelDetail(TwitchBasic):
    """
    Schema of get channel VIP person
    """

    # user id
    user_id: str = Field(default=..., title="User ID")
    # user name
    user_name: str = Field(default=..., title="User Name")
    # user login
    user_login: str = Field(default=..., title="User Login")


class TwitchPoolsDetail(TwitchBasic):
    """
    Schema of get pools
    """

    # id
    id: str = Field(default=..., title="ID")
    # broadcaster id
    broadcaster_id: str = Field(default=..., title="Broadcaster ID")
    # broadcaster name
    broadcaster_name: str = Field(default=..., title="Broadcaster Name")
    # broadcaster login
    broadcaster_login: str = Field(default=..., title="Broadcaster Login")
    # title
    title: str = Field(default=..., title="Title")
    # choices
    choices: list = Field(default=..., title="Choices")
    # bits voting enabled
    bits_voting_enabled: bool = Field(default=..., title="Bits Voting Enabled")
    # bits per vote
    bits_per_vote: int = Field(default=..., title="Bits Per Vote")
    # channel points voting enabled
    channel_points_voting_enabled: bool = Field(
        default=..., title="Channel Points Voting Enabled"
    )
    # channel points per vote
    channel_points_per_vote: int = Field(
        default=..., title="Channel Points Per Vote"
    )
    # status
    status: str = Field(default=..., title="Status")
    # duration
    duration: int = Field(default=..., title="Duration")
    # time started
    started_at: str = Field(default=..., title="Time Started")
    # time ended
    ended_at: str = Field(default=..., title="Time Ended")
