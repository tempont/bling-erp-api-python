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

import time
from typing import TYPE_CHECKING, Any

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.products import ProdutosDadosDTO

if TYPE_CHECKING:
    from bling_erp_api.models.generated.products import (
        ProdutosGetResponse200,
        ProdutosResponsePOSTPUT,
    )

SKU_LIST: list[str] = []

## ---------------------------------------------------------------------------
## GET ALL PRODUCTS WITH AUTO PAGINATION
## ---------------------------------------------------------------------------


def get_all_products() -> list[ProdutosGetResponse200]:
    """Return products with filters."""
    product_list: list[Any] = []
    with BlingClient.from_env() as client:
        for produto in client.produtos.iterar():
            product_dict = produto.model_dump()
            product_list.append(product_dict)

    return product_list


## ---------------------------------------------------------------------------
## GET PRODUCT PAGES
## ---------------------------------------------------------------------------


def get_product_pages() -> ProdutosGetResponse200:
    """Return products with filters."""
    with BlingClient.from_env() as client:
        return client.produtos.listar(
            limite=100,
            pagina=1,
            criterio=1,
        )


## ---------------------------------------------------------------------------
## GET PRODUCTS FILTERED BY ANY SUPPORTED BLING FIELD
## ---------------------------------------------------------------------------


def get_filtered_products(skus: list[str]) -> ProdutosGetResponse200:
    """Retornar produtos filtrados."""
    with BlingClient.from_env() as client:
        return client.produtos.listar(
            limite=10,
            codigos=skus,
        )


## ---------------------------------------------------------------------------
## POST PRODUCT
## ---------------------------------------------------------------------------


def post_product() -> ProdutosResponsePOSTPUT:
    """Creating a minimal test product."""
    client = BlingClient.from_env()

    payload = ProdutosDadosDTO(
        nome="Produto teste 1",
        descricao_curta="Um produto para testes.",
        tipo="P",
        formato="S",
        situacao="A",
        preco=10.0,
    )

    return client.products.create(data=payload)


## ---------------------------------------------------------------------------
## DELETE PRODUCTS
## ---------------------------------------------------------------------------


def delete_product(product_ids: list[int]) -> None:
    """Delete a product by ID."""
    client = BlingClient.from_env()
    client.products.delete_many(product_ids=product_ids)


def main() -> None:
    """Code executions."""
    print(get_all_products())
    time.sleep(1)

    print(post_product())
    time.sleep(1)

    print(get_product_pages().model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    print(get_filtered_products(SKU_LIST).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # delete_product([123456])
    # time.sleep(1)


if __name__ == "__main__":
    main()
