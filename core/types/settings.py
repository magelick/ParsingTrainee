from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Custom Settings class
    """

    # MongoDB environments
    MONGODB_HOST: str
    MONGODB_PORT: int

    # Twitch environments
    TWITCH_CLIENT_ID: str
    TWITCH_CLIENT_SECRET: str

    # Kafka environments
    KAFKA_BROKER_ID: int
    KAFKA_ZOOKEEPER_CONNECT: str
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: str
    KAFKA_ADVERTISED_LISTENERS: str
    KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: int
    KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: int
    KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: int

