from pydantic_settings import BaseSettings

class OpenaiSettings(BaseSettings):
    OPENAI_API_KEY: str