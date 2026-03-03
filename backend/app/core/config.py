from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Rutas Ocultas Backend"
    environment: str = "development"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/rutas_ocultas"
    clerk_issuer: str = "https://your-clerk-domain.clerk.accounts.dev"
    clerk_jwks_url: str = "https://your-clerk-domain.clerk.accounts.dev/.well-known/jwks.json"
    clerk_audience: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
