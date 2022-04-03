from utility.config import config


class FillLevelException(Exception):
    """Exception was raised because given fill level was not supported."""

    def __init__(self, given_fill_level: float, message=f"Fill level is not in [0, {config.default_fill_level()}) liters range. "):
        message += f"Given fill level was {given_fill_level}."
        super().__init__(message)
