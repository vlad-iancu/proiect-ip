from typing import List
from src.models.LoggingEntry import LoggingEntry
from src.repositories.LogRepository import LogRepository


class LoggingService:
    DEFAULT_MAX_ENTRIES = 20

    def __init__(self, logRepository: LogRepository) -> None:
        self.repo = logRepository
        self.currentEntries: List[LoggingEntry] = []

    def log(self, loggingEntry: LoggingEntry):
        self.currentEntries.append(loggingEntry)
        if len(self.currentEntries) >= self.DEFAULT_MAX_ENTRIES:
            self.repo.writeBulk(self.currentEntries)
            self.currentEntries.clear()
