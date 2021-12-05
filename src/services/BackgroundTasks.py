import asyncio
from functools import wraps
from typing import Any, Callable
from src.models.LoggingEntry import LoggingEntry
from src.repositories.LogRepository import LogRepository
from src.services.LoggingService import LoggingService
from flask import g

bgTasksEventLoop = asyncio.new_event_loop()
bgTasksLoggingService = LoggingService(LogRepository(g.db))


def backgroundTask(f: Callable[[Any], None]):
    @wraps(f)
    def wrapped(*args):
        if callable(f):
            bgTasksEventLoop.run_in_executor(None, f, *args)
        else:
            raise TypeError('Task must be a callable')

    return wrapped


@backgroundTask
def loggingBackgroundTask(loggingEntry: LoggingEntry) -> None:
    bgTasksLoggingService.log(loggingEntry)
