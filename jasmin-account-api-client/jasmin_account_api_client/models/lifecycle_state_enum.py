from enum import Enum


class LifecycleStateEnum(str, Enum):
    AWAITING_CLEANUP = "AWAITING_CLEANUP"
    DORMANT = "DORMANT"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
