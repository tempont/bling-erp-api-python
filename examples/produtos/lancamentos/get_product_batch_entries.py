"""Example: Batch Entries (Lançamentos de Lotes) Operations.

Demonstrates read and write operations on batch entries and stock balances
through the Bling API.

Endpoints:
    - GET /produtos/lotes/{idLote}/lancamentos
    - POST /produtos/lotes/{idLote}/lancamentos
    - GET /produtos/lotes/lancamentos/{idLancamento}
    - PATCH /produtos/lotes/lancamentos/{idLancamento}
    - GET /produtos/{idProduto}/lotes/saldo/soma
    - GET /produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo/soma
    - GET /produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo
    - GET /produtos/{idProduto}/lotes/{idLote}/depositos/{idDeposito}/saldo

Docs:
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes%20Lan%C3%A7amentos/get_produtos_lotes__idLote__lancamentos
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes%20Lan%C3%A7amentos/post_produtos_lotes__idLote__lancamentos
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes%20Lan%C3%A7amentos/get_produtos_lotes_lancamentos__idLancamento_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes%20Lan%C3%A7amentos/patch_produtos_lotes_lancamentos__idLancamento_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes%20Lan%C3%A7amentos/get_produtos__idProduto__lotes_saldo_soma
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes%20Lan%C3%A7amentos/get_produtos__idProduto__lotes_depositos__idDeposito__saldo_soma
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes%20Lan%C3%A7amentos/get_produtos__idProduto__lotes_depositos__idDeposito__saldo
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Lotes%20Lan%C3%A7amentos/get_produtos__idProduto__lotes__idLote__depositos__idDeposito__saldo

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from collections.abc import Sequence

    from bling_erp_api.models.generated.product_batch_entries import (
        LoteLancamentoDTO,
        LoteLancamentoObservacaoDTO,
        ProdutosIdProdutoLotesDepositosIdDepositoSaldoGetResponse200,
        ProdutosIdProdutoLotesDepositosIdDepositoSaldoSomaGetResponse200,
        ProdutosIdProdutoLotesIdLoteDepositosIdDepositoSaldoGetResponse200,
        ProdutosIdProdutoLotesSaldoSomaGetResponse200,
        ProdutosLotesIdLoteLancamentosGetResponse200,
        ProdutosLotesIdLoteLancamentosPostResponse200,
        ProdutosLotesLancamentosIdLancamentoGetResponse200,
    )

## ---------------------------------------------------------------------------
## LIST ENTRIES FOR A BATCH
## ---------------------------------------------------------------------------


def listar_lancamentos(
    id_lote: int,
) -> ProdutosLotesIdLoteLancamentosGetResponse200:
    """Lista lançamentos de um lote."""
    with BlingClient.from_env() as client:
        return client.lotes_lancamentos.listar(id_lote=id_lote)


## ---------------------------------------------------------------------------
## GET ENTRY BY ID
## ---------------------------------------------------------------------------


def obter_lancamento(
    id_lancamento: int,
) -> ProdutosLotesLancamentosIdLancamentoGetResponse200:
    """Obtém um lançamento de lote pelo ID."""
    with BlingClient.from_env() as client:
        return client.lotes_lancamentos.obter(id_lancamento=id_lancamento)


## ---------------------------------------------------------------------------
## CREATE BATCH ENTRY
## ---------------------------------------------------------------------------


def criar_lancamento(
    id_lote: int,
    dados: LoteLancamentoDTO,
) -> ProdutosLotesIdLoteLancamentosPostResponse200:
    """Cria um lançamento em um lote."""
    with BlingClient.from_env() as client:
        return client.lotes_lancamentos.criar(id_lote=id_lote, dados=dados)


## ---------------------------------------------------------------------------
## UPDATE ENTRY ATTRIBUTE
## ---------------------------------------------------------------------------


def alterar_atributo_lancamento(
    id_lancamento: int,
    dados: LoteLancamentoObservacaoDTO,
) -> None:
    """Altera um atributo (observação) de um lançamento."""
    with BlingClient.from_env() as client:
        client.lotes_lancamentos.alterar_atributo(
            id_lancamento=id_lancamento,
            dados=dados,
        )


## ---------------------------------------------------------------------------
## GET TOTAL STOCK BALANCE
## ---------------------------------------------------------------------------


def obter_saldos_soma(
    id_produto: int,
) -> ProdutosIdProdutoLotesSaldoSomaGetResponse200:
    """Obtém o saldo total de lotes de um produto (todos os depósitos)."""
    with BlingClient.from_env() as client:
        return client.lotes_lancamentos.obter_saldos_soma(id_produto=id_produto)


## ---------------------------------------------------------------------------
## GET STOCK BALANCE BY DEPOSIT (SUM)
## ---------------------------------------------------------------------------


def obter_saldos_soma_deposito(
    id_produto: int,
    id_deposito: int,
) -> ProdutosIdProdutoLotesDepositosIdDepositoSaldoSomaGetResponse200:
    """Obtém o saldo total de lotes em um depósito específico."""
    with BlingClient.from_env() as client:
        return client.lotes_lancamentos.obter_saldos_soma_deposito(
            id_produto=id_produto,
            id_deposito=id_deposito,
        )


## ---------------------------------------------------------------------------
## GET STOCK BALANCE BY DEPOSIT (DETAIL)
## ---------------------------------------------------------------------------


def obter_saldos(
    id_produto: int,
    id_deposito: int,
    ids_lotes: Sequence[int],
) -> ProdutosIdProdutoLotesDepositosIdDepositoSaldoGetResponse200:
    """Obtém o saldo detalhado por lote em um depósito."""
    with BlingClient.from_env() as client:
        return client.lotes_lancamentos.obter_saldos(
            id_produto=id_produto,
            id_deposito=id_deposito,
            ids_lotes=ids_lotes,
        )


## ---------------------------------------------------------------------------
## GET SPECIFIC BATCH BALANCE
## ---------------------------------------------------------------------------


def obter_saldos_saldo(
    id_produto: int,
    id_lote: int,
    id_deposito: int,
) -> ProdutosIdProdutoLotesIdLoteDepositosIdDepositoSaldoGetResponse200:
    """Obtém o saldo de um lote específico em um depósito."""
    with BlingClient.from_env() as client:
        return client.lotes_lancamentos.obter_saldos_saldo(
            id_produto=id_produto,
            id_lote=id_lote,
            id_deposito=id_deposito,
        )


def main() -> None:
    """Demonstrate batch entry and stock balance operations."""
    id_lote = 123456789  # Exemplo — substitua pelo ID real.
    id_lancamento = 987654321  # Exemplo — substitua pelo ID real.
    id_produto = 111222333  # Exemplo — substitua pelo ID real.
    id_deposito = 444555666  # Exemplo — substitua pelo ID real.

    # Read operations
    print(listar_lancamentos(id_lote).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)
    print(obter_lancamento(id_lancamento).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)
    print(obter_saldos_soma(id_produto).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)
    print(
        obter_saldos_soma_deposito(id_produto, id_deposito).model_dump_json(indent=2, by_alias=True)
    )
    time.sleep(1)
    print(obter_saldos(id_produto, id_deposito, [id_lote]).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)
    print(
        obter_saldos_saldo(id_produto, id_lote, id_deposito).model_dump_json(
            indent=2, by_alias=True
        )
    )
    time.sleep(1)

    # Write operations (commented out)
    # from bling_erp_api.models.generated.product_batch_entries import (
    #     LoteLancamentoDTO,
    #     LoteLancamentoObservacaoDTO,
    # )
    # entry = LoteLancamentoDTO(quantidade=10.0, tipo="E")
    # print(criar_lancamento(id_lote, entry).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # obs = LoteLancamentoObservacaoDTO(observacao="Nota atualizada")
    # alterar_atributo_lancamento(id_lancamento, obs)
    # time.sleep(1)


if __name__ == "__main__":
    main()
