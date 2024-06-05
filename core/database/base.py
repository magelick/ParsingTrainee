from pymongo import MongoClient
from core.settings import SETTINGS

# Initial MongoDB cluster
client: MongoClient = MongoClient(
    f"mongodb://{SETTINGS.MONGO_INITDB_ROOT_USERNAME}:{SETTINGS.MONGO_INITDB_ROOT_PASSWORD}@{SETTINGS.MONGODB_HOST}:{SETTINGS.MONGODB_PORT}/"
)
# Initial Parsing database
lamoda_db = client["lamoda-database"]
twitch_db = client["twitch-database"]
# Initial Lamoda collections
lamoda_list_sneakers = lamoda_db["lamoda-list-sneakers-collection"]
lamoda_list_sneaker_hrefs = lamoda_db["lamoda-list-sneaker-hrefs-collection"]
lamoda_sneaker_detail = lamoda_db["lamoda-sneaker-detail"]

# Initial Twitch Collections
twitch_auth = twitch_db["twitch-auth-collections"]
twitch_user = twitch_db["twitch-user-collections"]
twitch_games = twitch_db["twitch-games-collections"]
twitch_top_games = twitch_db["twitch-top-games-collections"]
twitch_games_analytic = twitch_db["twitch-games-analytic-collections"]
twitch_channel_information = twitch_db[
    "twitch-channel-information-collections"
]
twitch_channel_editor = twitch_db["twitch-channel-editor-collections"]
twitch_channel_followed = twitch_db["twitch-channel-followed-collections"]
twitch_channel_followers = twitch_db["twitch-channel-followers-collections"]
twitch_channel_emotes = twitch_db["twitch-channel-emotes-collections"]
twitch_channel_chat_settings = twitch_db[
    "twitch-channel-chat-settings-collections"
]
twitch_channel_vip = twitch_db["twitch-channel-vip-collections"]
twitch_global_emotes = twitch_db["twitch-global-emotes-collections"]
twitch_clips = twitch_db["twitch-clips-collections"]
twitch_pools = twitch_db["twitch-pools-collections"]
