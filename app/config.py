from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Kirov Security API Suite"
    app_version: str = "1.0.0"
    debug: bool = False
    api_key_required: bool = False
    hash_rounds: int = 12
    rate_limit_per_minute: int = 50

    model_config = {"env_file": ".env", "extra": "ignore"}

settings = Settings()
