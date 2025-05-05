from enum import Enum


class ReturnFormat(str, Enum):
    ARRAYS = "ARRAYS"
    OBJECTS = "OBJECTS"

    def __str__(self) -> str:
        return str(self.value)
