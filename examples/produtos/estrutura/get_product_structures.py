"""Example: Product Structures (Estruturas) Operations.

Demonstrates CRUD operations on product structures (composição de produtos)
through the Bling API.

Endpoints:
    - GET /produtos/estruturas/{idProdutoEstrutura}
    - PUT /produtos/estruturas/{idProdutoEstrutura}
    - POST /produtos/estruturas/{idProdutoEstrutura}/componentes
    - PATCH /produtos/estruturas/{idProdutoEstrutura}/componentes/{idComponente}
    - DELETE /produtos/estruturas/{idProdutoEstrutura}/componentes
    - DELETE /produtos/estruturas

Docs:
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Estruturas/get_produtos_estruturas__idProdutoEstrutura_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Estruturas/put_produtos_estruturas__idProdutoEstrutura_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Estruturas/post_produtos_estruturas__idProdutoEstrutura__componentes
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Estruturas/patch_produtos_estruturas__idProdutoEstrutura__componentes__idComponente_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Estruturas/delete_produtos_estruturas__idProdutoEstrutura__componentes
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Estruturas/delete_produtos_estruturas

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from collections.abc import Sequence

    from bling_erp_api.models.generated.product_structures import (
        ProdutosComponenteDTO,
        ProdutosEstruturaDTO,
        ProdutosEstruturasDeleteResponse200,
        ProdutosEstruturasIdProdutoEstruturaGetResponse200,
    )

## ---------------------------------------------------------------------------
## GET STRUCTURE BY ID
## ---------------------------------------------------------------------------


def obter_estrutura(
    id_produto_estrutura: int,
) -> ProdutosEstruturasIdProdutoEstruturaGetResponse200:
    """Obtém a estrutura (composição) de um produto."""
    with BlingClient.from_env() as client:
        return client.produtos_estruturas.obter(
            id_produto_estrutura=id_produto_estrutura,
        )


## ---------------------------------------------------------------------------
## UPDATE STRUCTURE
## ---------------------------------------------------------------------------


def alterar_estrutura(
    id_produto_estrutura: int,
    dados: ProdutosEstruturaDTO,
) -> None:
    """Atualiza a estrutura de um produto (PUT)."""
    with BlingClient.from_env() as client:
        client.produtos_estruturas.alterar(
            id_produto_estrutura=id_produto_estrutura,
            dados=dados,
        )


## ---------------------------------------------------------------------------
## LINK COMPONENTS TO STRUCTURE
## ---------------------------------------------------------------------------


def vincular_componentes(
    id_produto_estrutura: int,
    componentes: Sequence[ProdutosComponenteDTO],
) -> None:
    """Vincula componentes a uma estrutura de produto."""
    with BlingClient.from_env() as client:
        client.produtos_estruturas.vincular_componentes(
            id_produto_estrutura=id_produto_estrutura,
            componentes=componentes,
        )


## ---------------------------------------------------------------------------
## UPDATE A COMPONENT
## ---------------------------------------------------------------------------


def alterar_componente(
    id_produto_estrutura: int,
    id_componente: int,
    dados: ProdutosComponenteDTO,
) -> None:
    """Altera um componente específico da estrutura."""
    with BlingClient.from_env() as client:
        client.produtos_estruturas.alterar_componente(
            id_produto_estrutura=id_produto_estrutura,
            id_componente=id_componente,
            dados=dados,
        )


## ---------------------------------------------------------------------------
## REMOVE COMPONENTS FROM STRUCTURE
## ---------------------------------------------------------------------------


def remover_componentes(
    id_produto_estrutura: int,
    ids_componentes: Sequence[int],
) -> None:
    """Remove componentes de uma estrutura de produto."""
    with BlingClient.from_env() as client:
        client.produtos_estruturas.remover_componentes(
            id_produto_estrutura=id_produto_estrutura,
            ids_componentes=ids_componentes,
        )


## ---------------------------------------------------------------------------
## DELETE MULTIPLE STRUCTURES
## ---------------------------------------------------------------------------


def remover_estruturas_varias(
    ids_produtos: Sequence[int],
) -> ProdutosEstruturasDeleteResponse200:
    """Remove a estrutura de múltiplos produtos."""
    with BlingClient.from_env() as client:
        return client.produtos_estruturas.remover_varios(
            ids_produtos=ids_produtos,
        )


def main() -> None:
    """Demonstrate product structure operations."""
    id_produto_estrutura = 123456789  # Exemplo — substitua pelo ID real.

    # Read operations
    print(obter_estrutura(id_produto_estrutura).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Write operations (commented out)
    # from bling_erp_api.models.generated.product_structures import (
    #     ProdutosComponenteDTO,
    #     ProdutosEstruturaDTO,
    # )
    # estrutura_dto = ProdutosEstruturaDTO(descricao="Nova estrutura")
    # alterar_estrutura(id_produto_estrutura, estrutura_dto)
    # time.sleep(1)
    # componente = ProdutosComponenteDTO(id_produto=123, quantidade=1.0)
    # vincular_componentes(id_produto_estrutura, [componente])
    # time.sleep(1)
    # alterar_componente(id_produto_estrutura, 456, componente)
    # time.sleep(1)
    # remover_componentes(id_produto_estrutura, [456])
    # time.sleep(1)
    # print(remover_estruturas_varias([id_produto_estrutura]).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)


if __name__ == "__main__":
    main()
