"""Example: Products Workflow Examples.

Demonstrates listing and filtering products through the Bling products API.

Endpoints:
    - GET /produtos
    - POST /produtos
    - DELETE /produtos

Docs:
    - https://developer.bling.com.br/referencia#/Produtos/get_produtos
    - https://developer.bling.com.br/referencia#/Produtos/post_produtos
    - https://developer.bling.com.br/referencia#/Produtos/delete_produtos

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.products import ProdutosGetResponse200

SKU_LIST: list[str] = []


def get_all_products() -> ProdutosGetResponse200:
    """Return all products (max 100)."""
    with BlingClient.from_env() as client:
        return client.produtos.listar()


def get_filtered_products(skus: list[str]) -> ProdutosGetResponse200:
    """Retornar produtos filtrados."""
    with BlingClient.from_env() as client:
        return client.produtos.listar(
            limite=10,
            codigos=skus,
        )


def get_product_page() -> ProdutosGetResponse200:
    """Retornar páginas de produtos."""
    with BlingClient.from_env() as client:
        return client.produtos.listar(limite=10)


def main() -> None:
    """Endpoint: GET /produtos.

    Products examples.
    """
    if SKU_LIST:
        response = get_filtered_products(skus=SKU_LIST)
        print(response.model_dump_json(indent=2, by_alias=True))
    response = get_product_page()
    print(response.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
