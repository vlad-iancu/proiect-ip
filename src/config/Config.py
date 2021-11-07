import json
import os
from .DbConfig import DbConfig
from .AppEnvironmentEnum import AppEnvironment


class Config:
    def __init__(self, configFilePath: str = "conf.json") -> None:
        self.initialiseDefaults()
        self.initialiseFromConfigFile(configFilePath)
        self.initialiseFromEnvVars()

    def initialiseDefaults(self):
        self.env: AppEnvironment = AppEnvironment.DEV
        self.host: str = "127.0.0.1"
        self.port: int = 8000
        self.db: DbConfig = DbConfig()

    def initialiseFromConfigFile(self, configFilePath: str):
        with open(configFilePath, "r") as f:
            parsed = json.loads(f.read())

            env = str(parsed["env"])
            self.env = AppEnvironment.parse(env)

            envConfigObj = parsed[env]

            self.host = str(envConfigObj['host'])
            self.port = int(envConfigObj['port'])
            self.db = DbConfig(envConfigObj['db'])

    def initialiseFromEnvVars(self):
        appEnv = os.getenv("APP_ENV")
        if appEnv is not None:
            self.env = AppEnvironment.parse(appEnv)

        appHost = os.getenv("APP_HOST")
        if appHost is not None:
            self.host = str(appHost)

        appPort = os.getenv("APP_PORT")
        if appPort is not None:
            self.port = int(appPort)

        appDbHost = os.getenv("APP_DB_HOST")
        if appDbHost is not None:
            self.db.host = str(appDbHost)

        appDbPort = os.getenv("APP_DB_PORT")
        if appDbPort is not None:
            self.db.port = int(appDbPort)

        appDbUser = os.getenv("APP_DB_USER")
        if appDbUser is not None:
            self.db.user = str(appDbUser)

        appDbPassword = os.getenv("APP_DB_PASSWORD")
        if appDbPassword is not None:
            self.db.password = str(appDbPassword)


ConfigObject = Config()
