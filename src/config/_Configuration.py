import os
from ._DbConfiguration import _DbConfiguration


class _Configuration:
    __instance: '_Configuration' = None

    @staticmethod
    def getInstance() -> '_Configuration':
        if _Configuration.__instance is None:
            _Configuration(".env.{}".format(os.getenv("FLASK_ENV", "development")))
        return _Configuration.__instance

    def __init__(self, dotenvPath=".env.development") -> None:
        if _Configuration.__instance is not None:
            raise Exception("Explicit call of the singleton constructor.")
        self.db = _DbConfiguration(dotenvPath)
        _Configuration.__instance = self
