from pymongo import MongoClient
from core.settings import SETTINGS

# Initial MongoDB cluster
client: MongoClient = MongoClient(
    host=SETTINGS.MONGODB_HOST, port=SETTINGS.MONGODB_PORT
)
# Initial Parsing database
parsing_db = client["parsing-database"]
# Initial Lamoda and Twitch collections
lamoda_collections = parsing_db["lamoda-collection"]
twitch_collections = parsing_db["twitch-collection"]
