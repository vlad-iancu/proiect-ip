from typing import List
from sqlite3 import Connection
from src.models.LoggingEntry import LoggingEntry


class LogRepository:
    def __init__(self, connection: Connection) -> None:
        self.conn = connection

    def write(self, entry: LoggingEntry) -> None:
        try:
            self.conn.execute(
                "INSERT INTO Log (type, properties_json, at) VALUES (?, ?, ?)",
                (entry._type, entry._properties_json, entry._at)
            )
            self.conn.commit()
        except:
            print("Failed to write log.")

    def writeBulk(self, loggingEntries: List[LoggingEntry]) -> None:
        try:
            self.conn.executemany(
                "INSERT INTO Log (type, properties_json, at) VALUES (?, ?, ?)",
                [(entry._type, entry._properties_json, entry._at) for entry in loggingEntries]
            )
            self.conn.commit()
        except:
            print("Failed to write logs.")
