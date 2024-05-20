from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Custom Settings class
    """

    # MongoDB environments
    MONGODB_HOST: str
    MONGODB_PORT: int
