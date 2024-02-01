from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    FUTURE_FORGE_API_KEY: SecretStr
    VISION_CRAFT_API_KEY: SecretStr

    technical_support: str
    ads: str

    admin_chat: int
    admin_id: int

    channel_link: str

    driver_name: str
    postgres_user: str
    postgres_password: SecretStr
    postgres_host: str
    postgres_port: str
    postgres_database: str
    sqlite_database: str

    is_sqlite: bool
    is_debug: bool

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    @property
    def postgres_dsn(self) -> str:
        return f"{self.driver_name}://{self.postgres_user}:{self.postgres_password.get_secret_value()}@{self.postgres_host}:{self.postgres_port}/{self.postgres_database}"

    @property
    def sqlite_dsn(self) -> str:
        return self.sqlite_database

config: Settings = Settings()
