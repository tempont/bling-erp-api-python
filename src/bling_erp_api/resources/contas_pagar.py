"""Contas a Pagar resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contas_pagar import ContasBaixarContaDTO
    from bling_erp_api.types import JsonObject, QueryParams


def _contas_pagar_list_params(  # noqa: PLR0913
    *,
    data_emissao_inicial: str | None = None,
    data_emissao_final: str | None = None,
    data_vencimento_inicial: str | None = None,
    data_vencimento_final: str | None = None,
    data_pagamento_inicial: str | None = None,
    data_pagamento_final: str | None = None,
    situacao: int | None = None,
    id_contato: int | None = None,
) -> QueryParams:
    """Build query params for GET /contas/pagar."""
    return compact_params(
        {
            "dataEmissaoInicial": data_emissao_inicial,
            "dataEmissaoFinal": data_emissao_final,
            "dataVencimentoInicial": data_vencimento_inicial,
            "dataVencimentoFinal": data_vencimento_final,
            "dataPagamentoInicial": data_pagamento_inicial,
            "dataPagamentoFinal": data_pagamento_final,
            "situacao": situacao,
            "idContato": id_contato,
        }
    )


class ContasPagarResource(BaseResource):
    """Operações de contas a pagar do Bling.

    Este recurso mapeia os endpoints ``/contas/pagar``. Os métodos canônicos
    usam português para acompanhar a documentação oficial; os métodos em inglês
    continuam disponíveis como aliases de compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
        data_vencimento_inicial: str | None = None,
        data_vencimento_final: str | None = None,
        data_pagamento_inicial: str | None = None,
        data_pagamento_final: str | None = None,
        situacao: int | None = None,
        id_contato: int | None = None,
    ) -> JsonObject:
        """Lista contas a pagar.

        Endpoint: GET /contas/pagar

        Obtém lista paginada de contas a pagar.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            data_emissao_inicial: Data de emissão inicial (Bling: ``dataEmissaoInicial``, string, opcional)
            data_emissao_final: Data de emissão final (Bling: ``dataEmissaoFinal``, string, opcional)
            data_vencimento_inicial: Data de vencimento inicial (Bling: ``dataVencimentoInicial``, string, opcional)
            data_vencimento_final: Data de vencimento final (Bling: ``dataVencimentoFinal``, string, opcional)
            data_pagamento_inicial: Data de pagamento inicial (Bling: ``dataPagamentoInicial``, string, opcional)
            data_pagamento_final: Data de pagamento final (Bling: ``dataPagamentoFinal``, string, opcional)
            situacao: 1=Em aberto, 2=Pago, 3=Parcial, 4=Devolvido, 5=Cancelado (Bling: ``situacao``, integer, opcional)
            id_contato: ID do contato (Bling: ``idContato``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: ContasDadosBaseDTO
        """
        params = _contas_pagar_list_params(
            data_emissao_inicial=data_emissao_inicial,
            data_emissao_final=data_emissao_final,
            data_vencimento_inicial=data_vencimento_inicial,
            data_vencimento_final=data_vencimento_final,
            data_pagamento_inicial=data_pagamento_inicial,
            data_pagamento_final=data_pagamento_final,
            situacao=situacao,
            id_contato=id_contato,
        )
        return self._get(f"/contas/pagar?pagina={pagina}&limite={limite}", params=params)

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        issue_date_start: str | None = None,
        issue_date_end: str | None = None,
        due_date_start: str | None = None,
        due_date_end: str | None = None,
        payment_date_start: str | None = None,
        payment_date_end: str | None = None,
        status: int | None = None,
        contact_id: int | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lista contas a pagar.

        Endpoint: GET /contas/pagar

        Returns:
            Bling API response. Response schemas: 200: ContasDadosBaseDTO
        """
        return self.listar(
            pagina=page,
            limite=limit,
            data_emissao_inicial=issue_date_start,
            data_emissao_final=issue_date_end,
            data_vencimento_inicial=due_date_start,
            data_vencimento_final=due_date_end,
            data_pagamento_inicial=payment_date_start,
            data_pagamento_final=payment_date_end,
            situacao=status,
            id_contato=contact_id,
        )

    def obter(self, id_conta_pagar: int) -> JsonObject:
        """Obtém uma conta a pagar.

        Endpoint: GET /contas/pagar/{idContaPagar}

        Obtém uma conta a pagar pelo ID.

        Args:
            id_conta_pagar: ID da conta a pagar (Bling: ``idContaPagar``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContasPagarDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/contas/pagar/{id_conta_pagar}")

    def get(self, payable_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``."""
        return self.obter(id_conta_pagar=payable_id)

    def criar(self, dados: JsonObject) -> JsonObject:
        """Cria uma conta a pagar.

        Endpoint: POST /contas/pagar

        Cria uma nova conta a pagar.

        Args:
            dados: Dados da conta. Request body: ContasPagarSalvarDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self._post("/contas/pagar", json=to_json_object(dados))

    def create(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``."""
        return self.criar(dados=data)

    def alterar(self, id_conta_pagar: int, dados: JsonObject) -> JsonObject:
        """Altera uma conta a pagar.

        Endpoint: PUT /contas/pagar/{idContaPagar}

        Args:
            id_conta_pagar: ID da conta a pagar (Bling: ``idContaPagar``, integer, obrigatório)
            dados: Dados da conta para atualização

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/contas/pagar/{id_conta_pagar}", json=to_json_object(dados))

    def update(self, payable_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``."""
        return self.alterar(id_conta_pagar=payable_id, dados=data)

    def remover(self, id_conta_pagar: int) -> JsonObject:
        """Remove uma conta a pagar.

        Endpoint: DELETE /contas/pagar/{idContaPagar}

        Args:
            id_conta_pagar: ID da conta a pagar (Bling: ``idContaPagar``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/contas/pagar/{id_conta_pagar}")

    def delete(self, payable_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``."""
        return self.remover(id_conta_pagar=payable_id)

    def baixar(
        self,
        id_conta_pagar: int,
        dados: ContasBaixarContaDTO,
    ) -> JsonObject:
        """Baixa uma conta a pagar (registra o pagamento).

        Endpoint: POST /contas/pagar/{idContaPagar}/baixar

        Cria o pagamento de uma conta a pagar.

        Args:
            id_conta_pagar: ID da conta a pagar (Bling: ``idContaPagar``, integer, obrigatório)
            dados: Dados da baixa. Request body: ContasBaixarContaDTO

        Returns:
            Bling API response. Response schemas: 200: bordero; 400: ErrorResponse
        """
        return self._post(f"/contas/pagar/{id_conta_pagar}/baixar", json=to_json_object(dados))

    def settle(
        self,
        payable_id: int,
        data: ContasBaixarContaDTO,
    ) -> JsonObject:
        """Compatibility alias for ``baixar()``."""
        return self.baixar(id_conta_pagar=payable_id, dados=data)
