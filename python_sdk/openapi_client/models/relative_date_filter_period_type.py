from enum import Enum

class RelativeDateFilterPeriodType(str, Enum):
    DAYS = "DAYS"
    HOURS = "HOURS"
    MINUTES = "MINUTES"
    MONTHS = "MONTHS"
    QUARTERS = "QUARTERS"
    WEEKS = "WEEKS"
    YEARS = "YEARS"

    def __str__(self) -> str:
        return str(self.value)
