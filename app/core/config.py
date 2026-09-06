import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    postgre_db_url: str
    contact_points: str
    cassandra_port: int
    CQLENG_ALLOW_SCHEMA_MANAGEMENT: int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


setting = Setting()  # type: ignore

os.environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"] = str(
    setting.CQLENG_ALLOW_SCHEMA_MANAGEMENT
)
