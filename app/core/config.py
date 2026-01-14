from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Telegram Bot Admin"
    API_V1_STR: str = "/api/v1"
    
    # Бд
    DATABASE_URL: str = "sqlite+aiosqlite:///./bot.db"
    
    #Bot
    BOT_TOKEN: str = ""  
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()