import httpx
import sqlite3
import core.config as config

from di.di_container import DiContainer
from data.repositories.auth_repo import AuthRepo

network_client = httpx.Client(
    base_url=config.base_url
)

local_db = sqlite3.connect(config.database_path)


container = DiContainer()

container.register(sqlite3.Connection, local_db)
container.register(AuthRepo, AuthRepo(network_client, local_db))

