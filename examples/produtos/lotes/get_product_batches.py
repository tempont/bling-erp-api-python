"""Example: Product Batches (Lotes) Operations.

Demonstrates CRUD operations on product batches (lotes) through the Bling API.

Endpoints:
    - GET /produtos/lotes
    - PUT /produtos/lotes
    - DELETE /produtos/lotes
    - GET /produtos/lotes/controla-lote
    - GET /produtos/lotes/{idLote}
    - PUT /produtos/lotes/{idLote}
    - PATCH /produtos/lotes/{idLote}/status
    - POST /produtos/{idProduto}/lotes/controla-lote/desativar

Docs:
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes/get_produtos_lotes
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes/put_produtos_lotes
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes/delete_produtos_lotes
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes/get_produtos_lotes_controla-lote
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes/get_produtos_lotes__idLote_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes/put_produtos_lotes__idLote_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes/patch_produtos_lotes__idLote__status
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes/post_produtos__idProduto__lotes_controla-lote_desativar

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from collections.abc import Sequence

    from bling_erp_api.models.generated.product_batches import (
        LotePutRequestDTO,
        LotesDTO,
        LoteStatusDTO,
        ProdutosLotesControlaLoteGetResponse200,
        ProdutosLotesGetResponse200,
        ProdutosLotesIdLoteGetResponse200,
        ProdutosLotesPutResponse200,
    )

## ---------------------------------------------------------------------------
## LIST BATCHES
## ---------------------------------------------------------------------------


def listar_lotes(ids_produtos: Sequence[int]) -> ProdutosLotesGetResponse200:
    """Lista lotes de produtos."""
    with BlingClient.from_env() as client:
        return client.lotes.listar(ids_produtos=ids_produtos, limite=10)


## ---------------------------------------------------------------------------
## ITERATE OVER BATCHES
## ---------------------------------------------------------------------------


def iterar_lotes(ids_produtos: Sequence[int]) -> list[dict[str, Any]]:
    """Itera automaticamente sobre todos os lotes."""
    batch_list: list[dict[str, Any]] = []
    with BlingClient.from_env() as client:
        batch_list.extend(
            lote.model_dump() for lote in client.lotes.iterar(ids_produtos=ids_produtos, limite=10)
        )

    return batch_list


## ---------------------------------------------------------------------------
## GET BATCH BY ID
## ---------------------------------------------------------------------------


def obter_lote(id_lote: int) -> ProdutosLotesIdLoteGetResponse200:
    """Obtém um lote pelo ID."""
    with BlingClient.from_env() as client:
        return client.lotes.obter(id_lote=id_lote)


## ---------------------------------------------------------------------------
## CHECK BATCH CONTROL
## ---------------------------------------------------------------------------


def listar_produtos_controlam_lote(
    ids_produtos: Sequence[int],
) -> ProdutosLotesControlaLoteGetResponse200:
    """Lista produtos que controlam lote."""
    with BlingClient.from_env() as client:
        return client.lotes.listar_produtos_controlam_lote(
            ids_produtos=ids_produtos,
        )


## ---------------------------------------------------------------------------
## CREATE MULTIPLE BATCHES
## ---------------------------------------------------------------------------


def criar_lotes_varios(lotes: Sequence[LotesDTO]) -> ProdutosLotesPutResponse200:
    """Cria múltiplos lotes."""
    with BlingClient.from_env() as client:
        return client.lotes.criar_varios(lotes=lotes)


## ---------------------------------------------------------------------------
## UPDATE BATCH
## ---------------------------------------------------------------------------


def alterar_lote(id_lote: int, dados: LotePutRequestDTO) -> None:
    """Altera um lote (PUT)."""
    with BlingClient.from_env() as client:
        client.lotes.alterar(id_lote=id_lote, dados=dados)


## ---------------------------------------------------------------------------
## UPDATE BATCH STATUS
## ---------------------------------------------------------------------------


def alterar_situacao_lote(id_lote: int, dados: LoteStatusDTO) -> None:
    """Altera a situação de um lote."""
    with BlingClient.from_env() as client:
        client.lotes.alterar_situacao(id_lote=id_lote, dados=dados)


## ---------------------------------------------------------------------------
## DEACTIVATE BATCH CONTROL
## ---------------------------------------------------------------------------


def desativar_controle_lote(id_produto: int) -> None:
    """Desativa o controle de lote para um produto."""
    with BlingClient.from_env() as client:
        client.lotes.alterar_situacao_desativar(id_produto=id_produto)


## ---------------------------------------------------------------------------
## DELETE MULTIPLE BATCHES
## ---------------------------------------------------------------------------


def remover_lotes_varios(ids_lotes: Sequence[int]) -> None:
    """Remove múltiplos lotes."""
    with BlingClient.from_env() as client:
        client.lotes.remover_varios(ids_lotes=ids_lotes)


def main() -> None:
    """Demonstrate product batch operations."""
    ids_produtos = [123456789]  # Exemplo — substitua pelos IDs reais.
    id_lote = 987654321  # Exemplo — substitua pelo ID real.

    # Read operations
    print(listar_lotes(ids_produtos).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    print(obter_lote(id_lote).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    print(listar_produtos_controlam_lote(ids_produtos).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    print(iterar_lotes(ids_produtos))
    time.sleep(1)

    # Write operations (commented out)
    # from bling_erp_api.models.generated.product_batches import (
    #     LotePutRequestDTO,
    #     LoteStatusDTO,
    #     LotesDTO,
    # )
    # lote = LotesDTO(id_produto=ids_produtos[0], descricao="Lote teste")
    # print(criar_lotes_varios([lote]).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # update = LotePutRequestDTO(descricao="Lote atualizado")
    # alterar_lote(id_lote, update)
    # time.sleep(1)
    # status = LoteStatusDTO(situacao="I")
    # alterar_situacao_lote(id_lote, status)
    # time.sleep(1)
    # desativar_controle_lote(ids_produtos[0])
    # time.sleep(1)
    # remover_lotes_varios([id_lote])
    # time.sleep(1)


if __name__ == "__main__":
    main()
