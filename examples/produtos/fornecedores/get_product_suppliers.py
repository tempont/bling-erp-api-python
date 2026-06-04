"""Example: Product Suppliers (Fornecedores) Operations.

Demonstrates CRUD operations on product-supplier relationships through the Bling API.

Endpoints:
    - GET /produtos/fornecedores
    - POST /produtos/fornecedores
    - GET /produtos/fornecedores/{idProdutoFornecedor}
    - PUT /produtos/fornecedores/{idProdutoFornecedor}
    - DELETE /produtos/fornecedores/{idProdutoFornecedor}

Docs:
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Fornecedores/get_produtos_fornecedores
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Fornecedores/post_produtos_fornecedores
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Fornecedores/get_produtos_fornecedores__idProdutoFornecedor_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Fornecedores/put_produtos_fornecedores__idProdutoFornecedor_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Fornecedores/delete_produtos_fornecedores__idProdutoFornecedor_

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.product_suppliers import (
        ProdutosFornecedoresGetResponse200,
        ProdutosFornecedoresIdProdutoFornecedorGetResponse200,
        ProdutosFornecedoresIdProdutoFornecedorPutRequest,
        ProdutosFornecedoresIdProdutoFornecedorPutResponse200,
        ProdutosFornecedoresPostRequest,
        ProdutosFornecedoresPostResponse201,
    )

## ---------------------------------------------------------------------------
## LIST SUPPLIERS
## ---------------------------------------------------------------------------


def listar_fornecedores(
    id_produto: int | None = None,
) -> ProdutosFornecedoresGetResponse200:
    """Lista fornecedores vinculados a produtos."""
    with BlingClient.from_env() as client:
        return client.produtos_fornecedores.listar(
            limite=10,
            id_produto=id_produto,
        )


## ---------------------------------------------------------------------------
## ITERATE OVER SUPPLIERS
## ---------------------------------------------------------------------------


def iterar_fornecedores() -> list[dict[str, Any]]:
    """Itera automaticamente sobre todos os fornecedores."""
    with BlingClient.from_env() as client:
        return [f.model_dump() for f in client.produtos_fornecedores.iterar(limite=10)]


## ---------------------------------------------------------------------------
## GET SUPPLIER BY ID
## ---------------------------------------------------------------------------


def obter_fornecedor(
    id_produto_fornecedor: int,
) -> ProdutosFornecedoresIdProdutoFornecedorGetResponse200:
    """Obtém um vínculo produto-fornecedor pelo ID."""
    with BlingClient.from_env() as client:
        return client.produtos_fornecedores.obter(
            id_produto_fornecedor=id_produto_fornecedor,
        )


## ---------------------------------------------------------------------------
## CREATE SUPPLIER LINK
## ---------------------------------------------------------------------------


def criar_fornecedor(
    dados: ProdutosFornecedoresPostRequest,
) -> ProdutosFornecedoresPostResponse201:
    """Cria um novo vínculo entre produto e fornecedor."""
    with BlingClient.from_env() as client:
        return client.produtos_fornecedores.criar(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE SUPPLIER LINK
## ---------------------------------------------------------------------------


def alterar_fornecedor(
    id_produto_fornecedor: int,
    dados: ProdutosFornecedoresIdProdutoFornecedorPutRequest,
) -> ProdutosFornecedoresIdProdutoFornecedorPutResponse200:
    """Atualiza um vínculo produto-fornecedor."""
    with BlingClient.from_env() as client:
        return client.produtos_fornecedores.alterar(
            id_produto_fornecedor=id_produto_fornecedor,
            dados=dados,
        )


## ---------------------------------------------------------------------------
## DELETE SUPPLIER LINK
## ---------------------------------------------------------------------------


def remover_fornecedor(id_produto_fornecedor: int) -> None:
    """Remove um vínculo produto-fornecedor."""
    with BlingClient.from_env() as client:
        client.produtos_fornecedores.remover(
            id_produto_fornecedor=id_produto_fornecedor,
        )


def main() -> None:
    """Demonstrate product supplier operations."""
    id_produto = 123456789  # Exemplo — substitua pelo ID real.
    id_produto_fornecedor = 987654321  # Exemplo — substitua pelo ID real.

    # Read operations
    print(listar_fornecedores(id_produto=id_produto).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)
    print(obter_fornecedor(id_produto_fornecedor).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)
    print(iterar_fornecedores())
    time.sleep(1)

    # Write operations (commented out)
    # from bling_erp_api.models.generated.product_suppliers import (
    #     ProdutosFornecedoresIdProdutoFornecedorPutRequest,
    #     ProdutosFornecedoresPostRequest,
    # )
    # supplier_data = ProdutosFornecedoresPostRequest(
    #     id_produto=id_produto,
    #     id_fornecedor=123,
    # )
    # print(criar_fornecedor(supplier_data).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # update_data = ProdutosFornecedoresIdProdutoFornecedorPutRequest(
    #     id_produto=id_produto,
    #     id_fornecedor=456,
    # )
    # print(alterar_fornecedor(id_produto_fornecedor, update_data).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # remover_fornecedor(id_produto_fornecedor)
    # time.sleep(1)


if __name__ == "__main__":
    main()
