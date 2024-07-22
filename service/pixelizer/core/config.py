from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    RedisDsn,
    PostgresDsn,
    KafkaDsn,
)


class _RedisConfig(BaseSettings):
    model_fields = SettingsConfigDict(env_prefix='redis_')

    url: RedisDsn


class _DbConfig(BaseSettings):
    model_fields = SettingsConfigDict(env_prefix='postgres_')

    url: PostgresDsn


class _KafkaConfig(BaseSettings):
    model_fields = SettingsConfigDict(env_prefix='kafka_')

    url: KafkaDsn


class _MinioConfig(BaseSettings):
    model_fields = SettingsConfigDict(env_prefix='minio_')

    url: str
    access_key: str
    secret_key: str


class _KeycloackConfig(BaseSettings):
    model_fields = SettingsConfigDict(env_prefix='keycloack')

    url: str
    client_id: str
    realm_name: str
    client_secret_key: str


class _Config(BaseSettings):
    model_fields = SettingsConfigDict(secrets_dir='/var/run',
                                      env_file='.env',
                                      env_ignore_empty=True,
                                      env_file_encoding='utf-8')

    redis = _RedisConfig()
    db = _DbConfig()
    kafka = _KafkaConfig()
    minio = _MinioConfig()
    keycloack = _KeycloackConfig()


config = _Config()
