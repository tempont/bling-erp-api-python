"""Example: Product Stores (Lojas) Operations.

Demonstrates CRUD operations on product-store relationships through the
Bling API.

Endpoints:
    - GET /produtos/lojas
    - POST /produtos/lojas
    - GET /produtos/lojas/{idProdutoLoja}
    - PUT /produtos/lojas/{idProdutoLoja}
    - DELETE /produtos/lojas/{idProdutoLoja}

Docs:
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lojas/get_produtos_lojas
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lojas/post_produtos_lojas
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lojas/get_produtos_lojas__idProdutoLoja_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lojas/put_produtos_lojas__idProdutoLoja_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lojas/delete_produtos_lojas__idProdutoLoja_

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.product_stores import (
        ProdutosLojasGetResponse200,
        ProdutosLojasIdProdutoLojaGetResponse200,
        ProdutosLojasIdProdutoLojaPutRequest,
        ProdutosLojasIdProdutoLojaPutResponse200,
        ProdutosLojasPostRequest,
        ProdutosLojasPostResponse201,
    )


## ---------------------------------------------------------------------------
## LIST STORES
## ---------------------------------------------------------------------------


def listar_lojas(
    id_produto: int | None = None,
) -> ProdutosLojasGetResponse200:
    """Lista lojas vinculadas a produtos."""
    with BlingClient.from_env() as client:
        return client.produtos_lojas.listar(limite=10, id_produto=id_produto)


## ---------------------------------------------------------------------------
## ITERATE OVER STORES
## ---------------------------------------------------------------------------


def iterar_lojas() -> list[dict[str, object]]:
    """Itera automaticamente sobre todas as lojas."""
    with BlingClient.from_env() as client:
        return [store.model_dump() for store in client.produtos_lojas.iterar(limite=10)]


## ---------------------------------------------------------------------------
## GET STORE BY ID
## ---------------------------------------------------------------------------


def obter_loja(
    id_produto_loja: int,
) -> ProdutosLojasIdProdutoLojaGetResponse200:
    """Obtém um vínculo produto-loja pelo ID."""
    with BlingClient.from_env() as client:
        return client.produtos_lojas.obter(
            id_produto_loja=id_produto_loja,
        )


## ---------------------------------------------------------------------------
## CREATE STORE LINK
## ---------------------------------------------------------------------------


def criar_loja(
    dados: ProdutosLojasPostRequest,
) -> ProdutosLojasPostResponse201:
    """Cria um novo vínculo entre produto e loja."""
    with BlingClient.from_env() as client:
        return client.produtos_lojas.criar(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE STORE LINK
## ---------------------------------------------------------------------------


def alterar_loja(
    id_produto_loja: int,
    dados: ProdutosLojasIdProdutoLojaPutRequest,
) -> ProdutosLojasIdProdutoLojaPutResponse200:
    """Atualiza um vínculo produto-loja."""
    with BlingClient.from_env() as client:
        return client.produtos_lojas.alterar(
            id_produto_loja=id_produto_loja,
            dados=dados,
        )


## ---------------------------------------------------------------------------
## DELETE STORE LINK
## ---------------------------------------------------------------------------


def remover_loja(id_produto_loja: int) -> None:
    """Remove um vínculo produto-loja."""
    with BlingClient.from_env() as client:
        client.produtos_lojas.remover(
            id_produto_loja=id_produto_loja,
        )


def main() -> None:
    """Demonstrate product store operations."""
    id_produto = 123456789  # Exemplo — substitua pelo ID real.
    id_produto_loja = 987654321  # Exemplo — substitua pelo ID real.

    # Read operations
    print(listar_lojas(id_produto=id_produto).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)
    print(obter_loja(id_produto_loja).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)
    print(iterar_lojas())
    time.sleep(1)

    # Write operations (commented out)
    # from bling_erp_api.models.generated.product_stores import (
    #     ProdutosLojasIdProdutoLojaPutRequest,
    #     ProdutosLojasPostRequest,
    # )
    # store_data = ProdutosLojasPostRequest(id_produto=id_produto, id_loja=123)
    # print(criar_loja(store_data).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # update_data = ProdutosLojasIdProdutoLojaPutRequest(
    #     id_produto=id_produto, id_loja=456
    # )
    # print(alterar_loja(id_produto_loja, update_data).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # remover_loja(id_produto_loja)
    # time.sleep(1)


if __name__ == "__main__":
    main()
