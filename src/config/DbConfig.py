from typing import Any


class DbConfig:
    def __init__(self, dbConfigObj: Any = None) -> None:
        self.host: str = "127.0.0.1"
        self.port: int = 8000
        self.user: str = ""
        self.password: str = ""

        if dbConfigObj is not None:
            self.host = str(dbConfigObj["host"])
            self.port = int(dbConfigObj["port"])
            self.user = str(dbConfigObj["user"])
            self.password = str(dbConfigObj["password"])
