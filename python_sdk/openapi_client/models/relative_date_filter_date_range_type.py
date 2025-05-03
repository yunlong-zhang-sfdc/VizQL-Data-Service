from enum import Enum

class RelativeDateFilterDateRangeType(str, Enum):
    CURRENT = "CURRENT"
    LAST = "LAST"
    LASTN = "LASTN"
    NEXT = "NEXT"
    NEXTN = "NEXTN"
    TODATE = "TODATE"

    def __str__(self) -> str:
        return str(self.value)
