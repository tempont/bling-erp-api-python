"""Produtos — Lotes lançamentos e saldos resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Sequence

    from bling_erp_api.models.generated.product_batch_entries import (
        LoteLancamentoDTO,
        LoteLancamentoObservacaoDTO,
    )
    from bling_erp_api.types import JsonObject


class ProductBatchEntriesResource(BaseResource):
    """Operações em ``/produtos/lotes/lancamentos`` e saldos de lote."""

    def obter(self, id_lancamento: int) -> JsonObject:
        """Obtém um lançamento de um lote de produto.

        Endpoint: GET /produtos/lotes/lancamentos/{idLancamento}

        Obtém um lançamento de um lote de produto pelo ID do lançamento.

        Args:
            id_lancamento: ID do lançamento (Bling: ``idLancamento``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LoteLancamentoDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._get(f"/produtos/lotes/lancamentos/{id_lancamento}")

    def alterar_atributo(
        self,
        id_lancamento: int,
        dados: LoteLancamentoObservacaoDTO,
    ) -> JsonObject:
        """Altera a observação de um lançamento de um lote de um produto.

        Endpoint: PATCH /produtos/lotes/lancamentos/{idLancamento}

        Altera a observação de um lançamento de um lote de um produto pelo ID do lançamento.

        Request body schema: LoteLancamentoObservacaoDTO

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(
            f"/produtos/lotes/lancamentos/{id_lancamento}",
            json=to_json_object(dados),
        )

    def listar(self, id_lote: int) -> JsonObject:
        """Obtém os lançamentos de um lote de produto.

        Endpoint: GET /produtos/lotes/{idLote}/lancamentos

        Obtém os lançamentos de um lote de produto pelo ID.

        Args:
            id_lote: ID do lote (Bling: ``idLote``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LoteLancamentoDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._get(f"/produtos/lotes/{id_lote}/lancamentos")

    def criar(self, id_lote: int, dados: LoteLancamentoDTO) -> JsonObject:
        """Cria um lançamento de um lote.

        Endpoint: POST /produtos/lotes/{idLote}/lancamentos

        Inclui lançamento de um lote.

        Args:
            id_lote: ID do lote (Bling: ``idLote``, integer, obrigatório)
            dados: Dados do lançamento do lote.

        Request body schema: LoteLancamentoDTO

        Returns:
            Bling API response. Response schemas: 200: LoteLancamentoDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/produtos/lotes/{id_lote}/lancamentos", json=to_json_object(dados))

    def obter_saldos(
        self,
        id_produto: int,
        id_deposito: int,
        *,
        ids_lotes: Sequence[int],
    ) -> JsonObject:
        """Obtém os saldos dos lotes de um produto por depósito.

        Endpoint: GET /produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo

        Obtém os saldos dos lotes de um produto por depósito.

        Args:
            ids_lotes: IDs dos lotes (Bling: ``idsLotes[]``, array, obrigatório)
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            id_deposito: ID do depósito (Bling: ``idDeposito``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SaldoLoteDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._get(
            f"/produtos/{id_produto}/lotes/depositos/{id_deposito}/saldo",
            params=compact_params({"idsLotes[]": list(ids_lotes)}),
        )

    def obter_saldos_soma(self, id_produto: int) -> JsonObject:
        """Obtém o saldo total dos lotes de um produto.

        Endpoint: GET /produtos/{idProduto}/lotes/saldo/soma

        Obtém o saldo total dos lotes de um produto pelo ID do produto.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SaldoSomaLotesTodosDepositosDTO; 404: ErrorResponse
        """
        return self._get(f"/produtos/{id_produto}/lotes/saldo/soma")

    def obter_saldos_soma_deposito(self, id_produto: int, id_deposito: int) -> JsonObject:
        """Obtém a soma dos saldos dos lotes de um produto em um depósito.

        Endpoint: GET /produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo/soma

        Obtém a soma dos saldos dos lotes de um produto em um depósito.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            id_deposito: ID do depósito (Bling: ``idDeposito``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SaldoSomaLotesDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._get(f"/produtos/{id_produto}/lotes/depositos/{id_deposito}/saldo/soma")

    def obter_saldos_saldo(self, id_produto: int, id_lote: int, id_deposito: int) -> JsonObject:
        """Obtém o saldo de um lote de produto.

        Endpoint: GET /produtos/{idProduto}/lotes/{idLote}/depositos/{idDeposito}/saldo

        Obtém o saldo de um lote de produto.

        Args:
            id_lote: ID do lote (Bling: ``idLote``, integer, obrigatório)
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            id_deposito: ID do depósito (Bling: ``idDeposito``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SaldoLoteDTO; 404: ErrorResponse
        """
        return self._get(
            f"/produtos/{id_produto}/lotes/{id_lote}/depositos/{id_deposito}/saldo",
        )
