from enum import Enum


class UsersListUserType(str, Enum):
    SERVICE = "SERVICE"
    SHARED = "SHARED"
    STANDARD = "STANDARD"
    TRAINING = "TRAINING"

    def __str__(self) -> str:
        return str(self.value)
