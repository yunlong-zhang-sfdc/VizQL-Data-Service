from enum import Enum


class QuantitativeFilterBaseQuantitativeFilterType(str, Enum):
    MAX = "MAX"
    MIN = "MIN"
    ONLY_NON_NULL = "ONLY_NON_NULL"
    ONLY_NULL = "ONLY_NULL"
    RANGE = "RANGE"

    def __str__(self) -> str:
        return str(self.value)
