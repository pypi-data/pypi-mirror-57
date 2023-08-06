from pathlib import Path
from typing import List, Optional, Pattern
from urllib.parse import urlparse

from pydantic import BaseSettings as _BaseSettings, validator

try:
    from arq.connections import RedisSettings

    redis_settings_default = 'redis://localhost:6379'
except ImportError:
    redis_settings_default = None

    class RedisSettings:
        """
        Mock arq.RedisSettings to satisfy pydantic if arq isn't installed
        """

        def __init__(self, *args, **kwargs):
            raise RuntimeError('arq not installed')


try:
    from buildpg import asyncpg  # noqa
except ImportError:
    pg_dsn_default = None
else:
    pg_dsn_default = 'postgres://postgres@localhost:5432/app'


try:
    from cryptography.fernet import Fernet
except ImportError:
    auth_key_default = None
else:
    # generate_key is used to avoid a public default value ever being used in production
    auth_key_default = Fernet.generate_key().decode()

# see https://developers.google.com/recaptcha/docs/faq#id-like-to-run-automated-tests-with-recaptcha-what-should-i-do
GREPAPTCHA_TEST_SECRET = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'


class BaseSettings(_BaseSettings):
    worker_func: str = None
    create_app: str = 'main.create_app'
    patch_paths: List[str] = []

    sql_path: Path = 'models.sql'
    pg_dsn: Optional[str] = pg_dsn_default
    # eg. the db already exists on heroku and never has to be created
    pg_db_exists = False

    redis_settings: Optional[RedisSettings] = redis_settings_default
    port: int = 8000

    auth_key: str = auth_key_default

    max_request_size = 10 * 1024 ** 2  # 10MB
    locale = 'en_US.utf8'

    http_client_timeout = 10
    create_http_client = True

    csrf_ignore_paths: List[Pattern] = []
    csrf_upload_paths: List[Pattern] = []
    csrf_cross_origin_paths: List[Pattern] = []
    cross_origin_origins: List[Pattern] = []

    cookie_name = 'aiohttp-app'

    grecaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
    grecaptcha_secret = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

    @property
    def sql(self):
        return self.sql_path.read_text()

    @property
    def _pg_dsn_parsed(self):
        return urlparse(self.pg_dsn)

    @property
    def pg_name(self):
        return self._pg_dsn_parsed.path.lstrip('/')

    @property
    def pg_host(self):
        return self._pg_dsn_parsed.hostname

    @property
    def pg_port(self):
        return self._pg_dsn_parsed.port

    @validator('redis_settings', always=True, pre=True)
    def parse_redis_settings(cls, v):
        if v is None:
            return

        if RedisSettings.__module__ != 'arq.connections':
            raise RuntimeError(f'arq must be installed to use redis, redis_settings set to {v!r}')
        conf = urlparse(v)
        return RedisSettings(
            host=conf.hostname, port=conf.port, password=conf.password, database=int((conf.path or '0').strip('/'))
        )

    class Config:
        fields = {'pg_dsn': {'env': 'DATABASE_URL'}, 'redis_settings': {'env': ['REDISCLOUD_URL', 'REDIS_URL']}}
