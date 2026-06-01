"""Exemplo que lista produtos usando a API de recursos do SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.products import ProdutosGetResponse200

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
        parsed = ProdutosGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))
    response = get_product_page()
    parsed = ProdutosGetResponse200(**response)  # type: ignore[reportArgumentType]
    print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
