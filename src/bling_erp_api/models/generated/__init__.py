"""OpenAPI-generated Pydantic models."""

# pyright: reportUnsupportedDunderAll=false

from __future__ import annotations

from importlib import import_module

_schemas = import_module("bling_erp_api.models.generated.schemas")

__all__ = list(_schemas.__all__)


def __getattr__(name: str) -> object:
    if name in __all__:
        return getattr(_schemas, name)
    raise AttributeError(name)
