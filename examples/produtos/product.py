"""Example: Single Product Operations.

Demonstrates CRUD operations on individual products through the Bling products API.

Endpoints:
    - GET /produtos/{idProduto}
    - POST /produtos
    - PUT /produtos/{idProduto}
    - PATCH /produtos/{idProduto}
    - DELETE /produtos/{idProduto}

Docs:
    - https://developer.bling.com.br/referencia#/Produtos/get_produtos__idProduto_
    - https://developer.bling.com.br/referencia#/Produtos/post_produtos
    - https://developer.bling.com.br/referencia#/Produtos/put_produtos__idProduto_
    - https://developer.bling.com.br/referencia#/Produtos/patch_produtos__idProduto_
    - https://developer.bling.com.br/referencia#/Produtos/delete_produtos__idProduto_

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.products import (
        ProdutosDadosDTO,
        ProdutosDadosPatchDTO,
        ProdutosIdProdutoGetResponse200,
        ProdutosResponsePOSTPUT,
    )

## ---------------------------------------------------------------------------
## GET A PRODUCT BY ID
## ---------------------------------------------------------------------------


def obter_produto(product_id: int) -> ProdutosIdProdutoGetResponse200:
    """Obtém um produto pelo ID."""
    with BlingClient.from_env() as client:
        return client.produtos.obter(id_produto=product_id)


## ---------------------------------------------------------------------------
## CREATE A PRODUCT
## ---------------------------------------------------------------------------


def criar_produto(dados: ProdutosDadosDTO) -> ProdutosResponsePOSTPUT:
    """Cria um novo produto."""
    client = BlingClient.from_env()
    return client.products.create(data=dados)


## ---------------------------------------------------------------------------
## UPDATE A PRODUCT (PUT)
## ---------------------------------------------------------------------------


def alterar_produto(product_id: int, dados: ProdutosDadosDTO) -> ProdutosResponsePOSTPUT:
    """Atualiza um produto por completo (PUT)."""
    with BlingClient.from_env() as client:
        return client.produtos.alterar(id_produto=product_id, dados=dados)


## ---------------------------------------------------------------------------
## PARTIAL UPDATE A PRODUCT (PATCH)
## ---------------------------------------------------------------------------


def alterar_produto_parcialmente(
    product_id: int, dados: ProdutosDadosPatchDTO
) -> ProdutosResponsePOSTPUT:
    """Atualiza um produto parcialmente (PATCH)."""
    with BlingClient.from_env() as client:
        return client.produtos.alterar_parcialmente(id_produto=product_id, dados=dados)


## ---------------------------------------------------------------------------
## DELETE A PRODUCT
## ---------------------------------------------------------------------------


def remover_produto(product_id: int) -> None:
    """Remove um produto pelo ID."""
    with BlingClient.from_env() as client:
        client.produtos.remover(id_produto=product_id)


def main() -> None:
    """Demonstrate single product operations."""
    product_id = 16656139131  # Exemplo — substitua pelo ID real.

    # Read operations
    print(obter_produto(product_id).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Write operations (commented out)
    # payload = ProdutosDadosDTO(
    #     nome="Produto teste 1",
    #     descricao_curta="Produto para testes de CRUD.",
    #     tipo="P",
    #     formato="S",
    #     situacao="A",
    #     preco=10.0,
    # )
    # print(criar_produto(payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # print(alterar_produto(product_id, payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # patch_payload = ProdutosDadosPatchDTO(nome="Produto alterado parcialmente")
    # print(alterar_produto_parcialmente(product_id, patch_payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # remover_produto(product_id)
    # time.sleep(1)


if __name__ == "__main__":
    main()
