import os
import dotenv


class __Configuration:
    def __init__(self) -> None:
        self.db_host: str = None
        self.db_port: int = None
        self.db_user: str = None
        self.db_password: str = None
        self.db_file: str = None
        self.auth_secret: str = None


__configuration: __Configuration = None


def get_configuration() -> __Configuration:
    global __configuration

    if __configuration is None:
        envfile = ".env.{}".format(os.getenv("FLASK_ENV", "development"))
        dotenvcfg = dotenv.dotenv_values(envfile)

        cfg = __Configuration()

        cfg.db_host = os.getenv("APP_DB_HOST") or dotenvcfg.get("APP_DB_HOST")

        db_port = os.getenv("APP_DB_PORT") or dotenvcfg.get("APP_DB_PORT")
        cfg.db_port = None if db_port is None else int(db_port)

        cfg.db_user = os.getenv("APP_DB_USER") or dotenvcfg.get("APP_DB_USER")

        cfg.db_password = os.getenv("APP_DB_PASSWORD") or dotenvcfg.get("APP_DB_PASSWORD")

        cfg.db_file = os.getenv("APP_DB_FILE") or dotenvcfg.get("APP_DB_FILE")

        cfg.auth_secret = os.getenv("APP_AUTH_SECRET") or dotenvcfg.get("APP_AUTH_SECRET")

        __configuration = cfg

    return __configuration
