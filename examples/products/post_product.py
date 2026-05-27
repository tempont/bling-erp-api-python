"""Exemplo de código para criar um produto.."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


def create_product(data: JsonObject) -> JsonObject:
    """Cria um produto no Bling."""
    with BlingClient.from_env() as client:
        return client.products.create(data)
