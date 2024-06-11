from pathlib import Path

from core.types.settings import Settings
from pykafka import KafkaClient

# Main full path to the project
BASE_DIR = Path(__file__).resolve().parent.parent
# Initial instance of Settings
SETTINGS = Settings()  # type: ignore
# Initial Kafka instances
client = KafkaClient(hosts="kafka:9092")
