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
