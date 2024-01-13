from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Initializing all the sensitive variables from the .env file"""

    secret_key: str = Field(alias="SECRET_KEY")
    access_token_expire_minutes: int = Field(
        alias="ACCESS_TOKEN_EXPIRE_MINUTES", default=False
    )
    database_url: str = Field(alias="DATABASE_URL")
    app_host: str = Field(alias="APP_HOST", default="0.0.0.0")
    app_port: int = Field(alias="APP_PORT", default=8000)
    app_debug: bool = Field(alias="APP_DEBUG", default=False)

    model_config = SettingsConfigDict(env_file="../.env")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
