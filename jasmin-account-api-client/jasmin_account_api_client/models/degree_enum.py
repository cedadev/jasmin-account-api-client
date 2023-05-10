from enum import Enum


class DegreeEnum(str, Enum):
    DOCTORATE = "Doctorate"
    FIRST_DEGREE = "First degree"
    OTHER = "Other"
    POSTGRADUATE_MASTERS = "Postgraduate Master's"

    def __str__(self) -> str:
        return str(self.value)
