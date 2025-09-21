"""config.py"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Pydantic Settings"""
    # This defines the environment variable we are looking for.
    # The name must match the variable name.
    METEO_API_URL: str

    # This tells Pydantic to look for a .env file
    model_config = SettingsConfigDict(env_file=(".env.ci", ".env"))

# Create a single, importable instance of the settings
settings = Settings()
