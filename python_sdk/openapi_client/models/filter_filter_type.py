from enum import Enum

class FilterFilterType(str, Enum):
    DATE = "DATE"
    MATCH = "MATCH"
    QUANTITATIVE_DATE = "QUANTITATIVE_DATE"
    QUANTITATIVE_NUMERICAL = "QUANTITATIVE_NUMERICAL"
    SET = "SET"
    TOP = "TOP"

    def __str__(self) -> str:
        return str(self.value)
