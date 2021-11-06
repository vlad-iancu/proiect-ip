from enum import Enum


class AppEnvironment(Enum):
    DEV = 0
    TEST = 1

    @classmethod
    def parse(cls, value: str) -> 'AppEnvironment':
        if value.lower() == "dev":
            return AppEnvironment.DEV
        if value.lower() == "test":
            return AppEnvironment.TEST
        raise ValueError(
            f"The argument '{value}' cannot be parsed into an AppEnvironment value.")
