import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "a3f9c1e0d4b9fddf3a7c8e2e6e1f2a4b5d6c7e8f9a0b1c2d3e4f5g6h7i8j9k0l"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DB_NAME: str = "tasks.db"

    class Config:
        env_file = ".env"

settings = Settings()