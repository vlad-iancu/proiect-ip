from typing import Any, Dict
import json


class LoggingEntry:
    def __init__(self, type: str = None, properties: Dict[str, Any] = None, at: str = None) -> None:
        self._id: int = 0
        self._type: str = type
        self._properties_json: str = json.dumps(properties) if properties else None
        self._at: str = at
