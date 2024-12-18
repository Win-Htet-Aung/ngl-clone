from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    port: int
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow"
    )
        

settings = Settings()
