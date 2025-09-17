import warnings

from . import users_grants_list, users_list, users_partial_update, users_retrieve, users_services_list


def __getattr__(name):
    if name == "users_services_retrieve":
        warnings.warn("users_services_retrieve is deprecated, please use users_services_list instead", FutureWarning)
        return globals()["users_services_list"]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "users_list",
    "users_grants_list",
    "users_services_list",
    "users_retrieve",
    "users_partial_update",
]
