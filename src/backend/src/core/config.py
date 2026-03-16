# ./src/core/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/music_manager"
    SECRET_KEY: str = "change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24h
    DOWNLOADS_DIR: str = "/tmp/music_manager/downloads"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
