import os
import dotenv


class Configuration:
    __instance: 'Configuration' = None

    @staticmethod
    def getInstance() -> 'Configuration':
        if Configuration.__instance is None:
            Configuration(".env.{}".format(os.getenv("FLASK_ENV", "development")))
        return Configuration.__instance

    def __init__(self, dotenvPath=".env.development") -> None:
        if Configuration.__instance is not None:
            raise Exception("Explicit call of the singleton constructor.")
        self.db = Configuration._DbConfiguration(dotenvPath)
        Configuration.__instance = self

    class _DbConfiguration:
        def __init__(self, dotenvPath=".env.development") -> None:
            dotenvcfg = dotenv.dotenv_values(dotenvPath)

            self.host = dotenvcfg.get("APP_DB_HOST")
            self.port = int(dotenvcfg.get("APP_DB_PORT"))
            self.user = dotenvcfg.get("APP_DB_USER")
            self.password = dotenvcfg.get("APP_DB_PASSWORD")
            self.file = dotenvcfg.get("APP_DB_FILE")
