"""Common hand-written models shared across generated resources."""

from __future__ import annotations

from bling_erp_api.models.base import BlingModel


class Identifier(BlingModel):
    """Minimal identifier object reused by several endpoints."""

    id: int
