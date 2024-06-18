import warnings

from . import services_list, services_retrieve, services_roles_list, services_roles_retrieve


def __getattr__(name):
    if name == "services_roles_retrieve":
        warnings.warn("services_roles_retrieve is deprecated, please use services_roles_list instead", FutureWarning)
        return globals()["services_roles_list"]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "services_list",
    "services_retrieve",
    "services_roles_list",
    "services_roles_retrieve",
]
