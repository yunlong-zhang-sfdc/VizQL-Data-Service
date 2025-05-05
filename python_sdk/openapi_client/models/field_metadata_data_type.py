from enum import Enum


class FieldMetadataDataType(str, Enum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DATETIME = "DATETIME"
    INTEGER = "INTEGER"
    REAL = "REAL"
    SPATIAL = "SPATIAL"
    STRING = "STRING"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
