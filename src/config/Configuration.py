import os
from typing import Dict
import dotenv


class __Configuration:
    def __init__(self) -> None:
        self.db_host: str = None
        self.db_port: int = None
        self.db_user: str = None
        self.db_password: str = None
        self.db_file: str = None


__configurations: Dict[str, __Configuration] = {}


def get_configuration(envfile: str = None) -> __Configuration:
    global __configurations
    if envfile is None:
        envfile = ".env.{}".format(os.getenv("FLASK_ENV", "development"))

    if envfile not in __configurations:
        dotenvcfg = dotenv.dotenv_values(envfile)

        cfg = __Configuration()
        cfg.db_host = dotenvcfg.get("APP_DB_HOST")
        cfg.db_port = int(dotenvcfg.get("APP_DB_PORT"))
        cfg.db_user = dotenvcfg.get("APP_DB_USER")
        cfg.db_password = dotenvcfg.get("APP_DB_PASSWORD")
        cfg.db_file = dotenvcfg.get("APP_DB_FILE")

        __configurations[envfile] = cfg

    return __configurations[envfile]
