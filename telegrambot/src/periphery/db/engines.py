from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine

from src.periphery.envs import Env


db_url = URL.create(
    drivername="postgresql+asyncpg",
    database=Env.postgres_database.value,
    username=Env.postgres_username.value,
    password=Env.postgres_password.value,
    host=Env.postgres_host.value,
    port=Env.postgres_port.value,
)

postgres_engine = create_async_engine(db_url, echo=Env.postgres_echo.value)
