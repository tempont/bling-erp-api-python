"""Example: Product Groups (Grupos de Produtos) Operations.

Demonstrates CRUD operations on product groups through the Bling API.

Endpoints:
    - GET /grupos-produtos
    - POST /grupos-produtos
    - GET /grupos-produtos/{idGrupoProduto}
    - PUT /grupos-produtos/{idGrupoProduto}
    - DELETE /grupos-produtos/{idGrupoProduto}
    - DELETE /grupos-produtos

Docs:
    - https://developer.bling.com.br/referencia#/Grupos%20de%20Produtos/get_grupos-produtos
    - https://developer.bling.com.br/referencia#/Grupos%20de%20Produtos/post_grupos-produtos
    - https://developer.bling.com.br/referencia#/Grupos%20de%20Produtos/get_grupos-produtos__idGrupoProduto_
    - https://developer.bling.com.br/referencia#/Grupos%20de%20Produtos/put_grupos-produtos__idGrupoProduto_
    - https://developer.bling.com.br/referencia#/Grupos%20de%20Produtos/delete_grupos-produtos__idGrupoProduto_
    - https://developer.bling.com.br/referencia#/Grupos%20de%20Produtos/delete_grupos-produtos

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.product_groups import (
        GruposProdutosDeleteResponse200,
        GruposProdutosGetResponse200,
        GruposProdutosIdGrupoProdutoGetResponse200,
        GruposProdutosIdGrupoProdutoPutRequest,
        GruposProdutosPostRequest,
        GruposProdutosPostResponse201,
    )

## ---------------------------------------------------------------------------
## LIST PRODUCT GROUPS
## ---------------------------------------------------------------------------


def listar_grupos(nome: str | None = None) -> GruposProdutosGetResponse200:
    """Lista grupos de produtos."""
    with BlingClient.from_env() as client:
        return client.grupos_produtos.listar(limite=10, nome=nome)


## ---------------------------------------------------------------------------
## GET GROUP BY ID
## ---------------------------------------------------------------------------


def obter_grupo(id_grupo_produto: int) -> GruposProdutosIdGrupoProdutoGetResponse200:
    """Obtém um grupo de produtos pelo ID."""
    with BlingClient.from_env() as client:
        return client.grupos_produtos.obter(id_grupo_produto=id_grupo_produto)


## ---------------------------------------------------------------------------
## CREATE GROUP
## ---------------------------------------------------------------------------


def criar_grupo(dados: GruposProdutosPostRequest) -> GruposProdutosPostResponse201:
    """Cria um novo grupo de produtos."""
    with BlingClient.from_env() as client:
        return client.grupos_produtos.criar(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE GROUP
## ---------------------------------------------------------------------------


def alterar_grupo(id_grupo_produto: int, dados: GruposProdutosIdGrupoProdutoPutRequest) -> None:
    """Atualiza um grupo de produtos."""
    with BlingClient.from_env() as client:
        client.grupos_produtos.alterar(id_grupo_produto=id_grupo_produto, dados=dados)


## ---------------------------------------------------------------------------
## DELETE GROUP
## ---------------------------------------------------------------------------


def remover_grupo(id_grupo_produto: int) -> None:
    """Remove um grupo de produtos."""
    with BlingClient.from_env() as client:
        client.grupos_produtos.remover(id_grupo_produto=id_grupo_produto)


## ---------------------------------------------------------------------------
## DELETE MULTIPLE GROUPS
## ---------------------------------------------------------------------------


def remover_grupos_varios(
    ids_grupos: list[int],
) -> GruposProdutosDeleteResponse200:
    """Remove múltiplos grupos de produtos."""
    with BlingClient.from_env() as client:
        return client.grupos_produtos.remover_varios(ids_grupos_produtos=ids_grupos)


def main() -> None:
    """Demonstrate product group operations."""
    id_grupo_produto = 100  # Exemplo — substitua pelo ID real.

    # Read operations
    print(listar_grupos().model_dump_json(indent=2, by_alias=True))
    time.sleep(1)
    print(obter_grupo(id_grupo_produto).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Write operations (commented out)
    # from bling_erp_api.models.generated.product_groups import (
    #     GruposProdutosIdGrupoProdutoPutRequest,
    #     GruposProdutosPostRequest,
    # )
    # group_data = GruposProdutosPostRequest(nome="Novo Grupo", id_grupo_produto_pai=None)
    # print(criar_grupo(group_data).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # update_data = GruposProdutosIdGrupoProdutoPutRequest(nome="Grupo Atualizado")
    # alterar_grupo(id_grupo_produto, update_data)
    # time.sleep(1)
    # remover_grupo(id_grupo_produto)
    # time.sleep(1)
    # print(remover_grupos_varios([id_grupo_produto]).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)


if __name__ == "__main__":
    main()
