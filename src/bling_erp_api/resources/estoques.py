"""Estoques resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.estoques import (
    EstoquesPostResponse201,
    EstoquesSaldosGetResponse200,
    EstoquesSaldosIdDepositoGetResponse200,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, QueryParams


def _estoques_saldos_params(
    *,
    ids_produtos: list[int],
    codigos: list[str] | None = None,
    filtro_saldo_estoque: int | None = None,
) -> QueryParams:
    """Build query params for GET /estoques/saldos."""
    return compact_params(
        {
            "idsProdutos[]": ids_produtos,
            "codigos[]": codigos,
            "filtroSaldoEstoque": filtro_saldo_estoque,
        }
    )


class EstoquesResource(BaseResource):
    """Operações de estoques do Bling.

    Este recurso mapeia os endpoints ``/estoques``.
    Os métodos canônicos usam português para acompanhar a documentação oficial;
    os métodos em inglês continuam disponíveis como aliases de compatibilidade.
    """

    def obter_saldos(
        self,
        *,
        ids_produtos: list[int],
        codigos: list[str] | None = None,
        filtro_saldo_estoque: int | None = None,
    ) -> EstoquesSaldosGetResponse200:
        """Obtém saldo em estoque de produtos.

        Endpoint: GET /estoques/saldos

        Obtém o saldo em estoque de produtos, em todos os depósitos.

        Args:
            ids_produtos: IDs dos produtos (Bling: ``idsProdutos[]``, array, obrigatório)
            codigos: Códigos dos produtos (Bling: ``codigos[]``, array, opcional)
            filtro_saldo_estoque: 0=Zerado, 1=Positivo, 2=Negativo (Bling: ``filtroSaldoEstoque``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: EstoquesSaldosBaseDTO; 400: ErrorResponse
        """
        params = _estoques_saldos_params(
            ids_produtos=ids_produtos,
            codigos=codigos,
            filtro_saldo_estoque=filtro_saldo_estoque,
        )
        raw = self._get("/estoques/saldos", params=params)
        return self._validate_response(EstoquesSaldosGetResponse200, raw)

    def get_balances(
        self,
        *,
        product_ids: list[int],
        codes: list[str] | None = None,
        stock_balance_filter: int | None = None,
    ) -> EstoquesSaldosGetResponse200:
        """Compatibility alias for ``obter_saldos()``.

        Gets stock balances for products.

        Endpoint: GET /estoques/saldos

        Args:
            product_ids: Product IDs (Bling: ``idsProdutos[]``, array, obrigatório)
            codes: Product codes (Bling: ``codigos[]``, array, opcional)
            stock_balance_filter: 0=Zero, 1=Positive, 2=Negative (Bling: ``filtroSaldoEstoque``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: EstoquesSaldosBaseDTO; 400: ErrorResponse
        """
        return self.obter_saldos(
            ids_produtos=product_ids,
            codigos=codes,
            filtro_saldo_estoque=stock_balance_filter,
        )

    def obter_saldos_por_deposito(
        self,
        id_deposito: int,
        *,
        ids_produtos: list[int],
        codigos: list[str] | None = None,
        filtro_saldo_estoque: int | None = None,
    ) -> EstoquesSaldosIdDepositoGetResponse200:
        """Obtém saldo em estoque por depósito.

        Endpoint: GET /estoques/saldos/{idDeposito}

        Obtém o saldo em estoque de produtos pelo ID do depósito.

        Args:
            id_deposito: ID do depósito (Bling: ``idDeposito``, integer, obrigatório)
            ids_produtos: IDs dos produtos (Bling: ``idsProdutos[]``, array, obrigatório)
            codigos: Códigos dos produtos (Bling: ``codigos[]``, array, opcional)
            filtro_saldo_estoque: 0=Zerado, 1=Positivo, 2=Negativo (Bling: ``filtroSaldoEstoque``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: EstoquesSaldosBaseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        params = _estoques_saldos_params(
            ids_produtos=ids_produtos,
            codigos=codigos,
            filtro_saldo_estoque=filtro_saldo_estoque,
        )
        raw = self._get(f"/estoques/saldos/{id_deposito}", params=params)
        return self._validate_response(EstoquesSaldosIdDepositoGetResponse200, raw)

    def get_balances_by_deposit(
        self,
        deposit_id: int,
        *,
        product_ids: list[int],
        codes: list[str] | None = None,
        stock_balance_filter: int | None = None,
    ) -> EstoquesSaldosIdDepositoGetResponse200:
        """Compatibility alias for ``obter_saldos_por_deposito()``.

        Gets stock balances by deposit.

        Endpoint: GET /estoques/saldos/{idDeposito}

        Args:
            deposit_id: Deposit ID (Bling: ``idDeposito``, integer, obrigatório)
            product_ids: Product IDs (Bling: ``idsProdutos[]``, array, obrigatório)
            codes: Product codes (Bling: ``codigos[]``, array, opcional)
            stock_balance_filter: 0=Zero, 1=Positive, 2=Negative (Bling: ``filtroSaldoEstoque``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: EstoquesSaldosBaseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.obter_saldos_por_deposito(
            id_deposito=deposit_id,
            ids_produtos=product_ids,
            codigos=codes,
            filtro_saldo_estoque=stock_balance_filter,
        )

    def criar(self, dados: JsonObject) -> EstoquesPostResponse201:
        """Cria um registro de estoque.

        Endpoint: POST /estoques

        Cria um registro de lançamento no estoque.

        Args:
            dados: Dados do registro (Bling: request body)

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        raw = self._post("/estoques", json=to_json_object(dados))
        return self._validate_response(EstoquesPostResponse201, raw)

    def create(self, data: JsonObject) -> EstoquesPostResponse201:
        """Compatibility alias for ``criar()``.

        Creates a stock entry.

        Endpoint: POST /estoques

        Args:
            data: Stock entry data (Bling: request body)

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self.criar(dados=data)
