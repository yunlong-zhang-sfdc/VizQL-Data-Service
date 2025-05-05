from enum import Enum


class Function(str, Enum):
    AVG = "AVG"
    COLLECT = "COLLECT"
    COUNT = "COUNT"
    COUNTD = "COUNTD"
    DAY = "DAY"
    MAX = "MAX"
    MEDIAN = "MEDIAN"
    MIN = "MIN"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    STDEV = "STDEV"
    SUM = "SUM"
    TRUNC_DAY = "TRUNC_DAY"
    TRUNC_MONTH = "TRUNC_MONTH"
    TRUNC_QUARTER = "TRUNC_QUARTER"
    TRUNC_WEEK = "TRUNC_WEEK"
    TRUNC_YEAR = "TRUNC_YEAR"
    VAR = "VAR"
    WEEK = "WEEK"
    YEAR = "YEAR"

    def __str__(self) -> str:
        return str(self.value)
