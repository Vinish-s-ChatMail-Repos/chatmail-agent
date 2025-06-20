"""Module providing bassic settings from pydantic"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Class that has all the env variables"""

    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GOOGLE_REDIRECT_URI: str = ""
    DATABASE_URL: str = ""
    LLM_BASE_URL: str = ""
    LLM_MODEL: str = ""
    LLM_API_KEY: str = ""
    class Config:
        """Class that loads the env file file"""
        
        env_file = ".env"

settings = Settings()
