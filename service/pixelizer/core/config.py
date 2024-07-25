from .env_type import EnvTypeEnum
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    RedisDsn,
    PostgresDsn,
    KafkaDsn,
)


class _Config(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False,
                                      env_file='.env',
                                      env_file_encoding='utf-8',
                                      env_ignore_empty=True,
                                      env_nested_delimiter='_',
                                      extra='ignore')

    redis_url: RedisDsn
    postgres_url: PostgresDsn
    kafka_url: KafkaDsn
    minio_url: str
    minio_access_key: str
    minio_secret_key: str
    env_type: EnvTypeEnum


config = _Config()
