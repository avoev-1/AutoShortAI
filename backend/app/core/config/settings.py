from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AutoShortAI"
    app_env: str = "development"
    app_version: str = "0.1.0"

    database_url: str = "postgresql+asyncpg://autoshort:autoshort@postgres:5432/autoshort"
    redis_url: str = "redis://redis:6379/0"
    cors_origins: str = "http://localhost:5173"

    enable_real_publishing: bool = False
    enable_paid_apis: bool = False
    daily_api_budget_usd: float = 0
    max_daily_publications: int = 0

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
