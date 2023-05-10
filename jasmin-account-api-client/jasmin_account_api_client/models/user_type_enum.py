from enum import Enum


class UserTypeEnum(str, Enum):
    SERVICE = "SERVICE"
    SHARED = "SHARED"
    STANDARD = "STANDARD"
    TRAINING = "TRAINING"

    def __str__(self) -> str:
        return str(self.value)
