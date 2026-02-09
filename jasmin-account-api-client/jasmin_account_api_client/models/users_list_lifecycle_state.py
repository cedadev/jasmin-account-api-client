from enum import Enum


class UsersListLifecycleState(str, Enum):
    ACCNT_DEL_HOME_MOVED = "ACCNT_DEL_HOME_MOVED"
    ACCNT_DEL_HOME_REMOVED = "ACCNT_DEL_HOME_REMOVED"
    ACCNT_DEL_NOTIFIED = "ACCNT_DEL_NOTIFIED"
    AWAITING_CLEANUP = "AWAITING_CLEANUP"
    DORMANT = "DORMANT"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
