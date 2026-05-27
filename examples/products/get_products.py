"""Exemplo que lista produtos usando a API de recursos do SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject

SKU_LIST: list[str] = []


def get_all_products() -> JsonObject:
    """Retornar todos os produtos."""
    with BlingClient.from_env() as client:
        return client.produtos.listar()


def get_filtered_products(skus: list[str]) -> JsonObject:
    """Retornar produtos filtrados."""
    with BlingClient.from_env() as client:
        return client.produtos.listar(
            limite=10,
            codigos=skus,
        )


def get_product_page() -> JsonObject:
    """Retornar páginas de produtos."""
    with BlingClient.from_env() as client:
        return client.produtos.listar(limite=10)


def main() -> None:
    """Endpoint: GET /produtos.

    Products examples.
    """
    if SKU_LIST:
        response = get_filtered_products(skus=SKU_LIST)
        print(response)
    response: JsonObject = get_product_page()

    print(response)


if __name__ == "__main__":
    main()
