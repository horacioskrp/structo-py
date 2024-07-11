from enum import Enum
from pydantic import PostgresDsn, RedisDsn, validator, ValidationError
from pydantic_settings import BaseSettings
from typing import Any
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True
        env_file = ".env"


class Config(BaseConfig):
    DEBUG: int
    DEFAULT_LOCALE: str
    ENVIRONMENT: EnvironmentType
    POSTGRES_URL: str
    REDIS_URL: RedisDsn
    RELEASE_VERSION: str
    SHOW_SQL_ALCHEMY_QUERIES: int
    SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_EXPIRE_MINUTES: int

    @validator("ENVIRONMENT", pre=True)
    def validate_environment(cls, v: str) -> EnvironmentType:
        v = v.strip('"')  # Strip any surrounding quotes
        return EnvironmentType(v.lower())

    @validator("POSTGRES_URL", pre=True)
    def validate_postgres_url(cls, v: str) -> str:
        return v

    @validator("REDIS_URL", pre=True)
    def validate_redis_url(cls, v: str) -> str:
        return v


# Initialiser la configuration en chargeant les valeurs des variables d'environnement
config = Config()
