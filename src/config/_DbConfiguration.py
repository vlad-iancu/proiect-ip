import dotenv


class _DbConfiguration:
    def __init__(self, dotenvPath=".env.development") -> None:
        dotenvcfg = dotenv.dotenv_values(dotenvPath)

        self.host = dotenvcfg.get("APP_DB_HOST")
        self.port = int(dotenvcfg.get("APP_DB_PORT"))
        self.user = dotenvcfg.get("APP_DB_USER")
        self.password = dotenvcfg.get("APP_DB_PASSWORD")
        self.file = dotenvcfg.get("APP_DB_FILE")
