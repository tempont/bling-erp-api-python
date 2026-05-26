"""Depósitos resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, QueryParams


def _depositos_list_params(
    *,
    descricao: str | None = None,
    situacao: int | None = None,
) -> QueryParams:
    """Build query params for GET /depositos."""
    return compact_params({"descricao": descricao, "situacao": situacao})


class DepositosResource(BaseResource):
    """Operações de depósitos do Bling.

    Este recurso mapeia os endpoints ``/depositos``.
    Os métodos canônicos usam português para acompanhar a documentação oficial;
    os métodos em inglês continuam disponíveis como aliases de compatibilidade.
    """

    def listar(
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        descricao: str | None = None,
        situacao: int | None = None,
    ) -> JsonObject:
        """Lista depósitos.

        Endpoint: GET /depositos

        Lista os depósitos cadastrados.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            descricao: Descrição do depósito (Bling: ``descricao``, string, opcional)
            situacao: 0=Inativo, 1=Ativo (Bling: ``situacao``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: DepositosDadosDTO
        """
        params = _depositos_list_params(descricao=descricao, situacao=situacao)
        return self._get(f"/depositos?pagina={pagina}&limite={limite}", params=params)

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        description: str | None = None,
        status: int | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lists deposits.

        Endpoint: GET /depositos

        Args:
            page: Page number (Bling: ``pagina``, integer, opcional)
            limit: Results per page (Bling: ``limite``, integer, opcional)
            description: Deposit description (Bling: ``descricao``, string, opcional)
            status: 0=Inactive, 1=Active (Bling: ``situacao``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: DepositosDadosDTO
        """
        return self.listar(pagina=page, limite=limit, descricao=description, situacao=status)

    def obter(self, id_deposito: int) -> JsonObject:
        """Obtém um depósito.

        Endpoint: GET /depositos/{idDeposito}

        Obtém um depósito pelo ID.

        Args:
            id_deposito: ID do depósito (Bling: ``idDeposito``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: DepositosDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/depositos/{id_deposito}")

    def get(self, deposit_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Gets a deposit.

        Endpoint: GET /depositos/{idDeposito}

        Args:
            deposit_id: Deposit ID (Bling: ``idDeposito``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: DepositosDadosDTO; 404: ErrorResponse
        """
        return self.obter(id_deposito=deposit_id)

    def criar(self, dados: JsonObject) -> JsonObject:
        """Cria um depósito.

        Endpoint: POST /depositos

        Cria um novo depósito.

        Args:
            dados: Dados do depósito (Bling: request body)

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self._post("/depositos", json=to_json_object(dados))

    def create(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Creates a deposit.

        Endpoint: POST /depositos

        Args:
            data: Deposit data (Bling: request body)

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(self, id_deposito: int, dados: JsonObject) -> JsonObject:
        """Altera um depósito.

        Endpoint: PUT /depositos/{idDeposito}

        Altera um depósito existente.

        Args:
            id_deposito: ID do depósito (Bling: ``idDeposito``, integer, obrigatório)
            dados: Dados do depósito para atualização (Bling: request body)

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/depositos/{id_deposito}", json=to_json_object(dados))

    def update(self, deposit_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Updates a deposit.

        Endpoint: PUT /depositos/{idDeposito}

        Args:
            deposit_id: Deposit ID (Bling: ``idDeposito``, integer, obrigatório)
            data: Deposit update data (Bling: request body)

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_deposito=deposit_id, dados=data)
