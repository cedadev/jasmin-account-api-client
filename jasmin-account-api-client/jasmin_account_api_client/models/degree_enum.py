from enum import Enum


class DegreeEnum(str, Enum):
    FIRST_DEGREE = "First degree"
    POSTGRADUATE_MASTERS = "Postgraduate Master's"
    DOCTORATE = "Doctorate"
    OTHER = "Other"

    def __str__(self) -> str:
        return str(self.value)
