"""Contas Financeiras resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.contas_contabeis import (
    ContasContabeisGetResponse200,
    ContasContabeisIdContaContabilGetResponse200,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params

if TYPE_CHECKING:
    from bling_erp_api.types import QueryParams


def _contas_contabeis_list_params(
    *,
    ocultar_invisiveis: bool | None = None,
    ocultar_tipo_conta_bancaria: bool | None = None,
    situacoes: list[int] | None = None,
    alias_integracao: str | None = None,
    ordenacao: str | None = None,
) -> QueryParams:
    """Build query params for GET /contas-contabeis."""
    return compact_params(
        {
            "ocultarInvisiveis": ocultar_invisiveis,
            "ocultarTipoContaBancaria": ocultar_tipo_conta_bancaria,
            "situacoes": situacoes,
            "aliasIntegracao": alias_integracao,
            "ordenacao": ordenacao,
        }
    )


class ContasContabeisResource(BaseResource):
    """Operações de contas financeiras do Bling.

    Este recurso mapeia os endpoints ``/contas-contabeis``. Os métodos
    canônicos usam português para acompanhar a documentação oficial; os
    métodos em inglês continuam disponíveis como aliases de compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        ocultar_invisiveis: bool | None = None,
        ocultar_tipo_conta_bancaria: bool | None = None,
        situacoes: list[int] | None = None,
        alias_integracao: str | None = None,
        ordenacao: str | None = None,
    ) -> ContasContabeisGetResponse200:
        """Lista contas financeiras.

        Endpoint: GET /contas-contabeis

        Obtém lista paginada de contas financeiras.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            ocultar_invisiveis: Oculta contas invisíveis (Bling: ``ocultarInvisiveis``, boolean, opcional)
            ocultar_tipo_conta_bancaria: Oculta contas bancárias (Bling: ``ocultarTipoContaBancaria``, boolean, opcional)
            situacoes: 1=Ativo, 2=Inativo, 3=Pendente, 4=Cancelada (Bling: ``situacoes``, array, opcional)
            alias_integracao: Alias da integração (Bling: ``aliasIntegracao``, string, opcional)
            ordenacao: Ordenação: descricao ou -descricao (Bling: ``ordenacao``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: ContasContabeisDadosDTO
        """
        params: QueryParams = {
            "pagina": pagina,
            "limite": limite,
            **_contas_contabeis_list_params(
                ocultar_invisiveis=ocultar_invisiveis,
                ocultar_tipo_conta_bancaria=ocultar_tipo_conta_bancaria,
                situacoes=situacoes,
                alias_integracao=alias_integracao,
                ordenacao=ordenacao,
            ),
        }
        raw = self._get("/contas-contabeis", params=params)
        return self._validate_response(ContasContabeisGetResponse200, raw)

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        hide_inactive: bool | None = None,
        hide_bank_accounts: bool | None = None,
        statuses: list[int] | None = None,
        integration_alias: str | None = None,
        ordering: str | None = None,
    ) -> ContasContabeisGetResponse200:
        """Compatibility alias for ``listar()``."""
        return self.listar(
            pagina=page,
            limite=limit,
            ocultar_invisiveis=hide_inactive,
            ocultar_tipo_conta_bancaria=hide_bank_accounts,
            situacoes=statuses,
            alias_integracao=integration_alias,
            ordenacao=ordering,
        )

    def obter(self, id_conta_contabil: int) -> ContasContabeisIdContaContabilGetResponse200:
        """Obtém uma conta financeira.

        Endpoint: GET /contas-contabeis/{idContaContabil}

        Obtém uma conta financeira pelo ID.

        Args:
            id_conta_contabil: ID da conta financeira (Bling: ``idContaContabil``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContasContabeisDadosDTO; 404: ErrorResponse
        """
        raw = self._get(f"/contas-contabeis/{id_conta_contabil}")
        return self._validate_response(ContasContabeisIdContaContabilGetResponse200, raw)

    def get(self, financial_account_id: int) -> ContasContabeisIdContaContabilGetResponse200:
        """Compatibility alias for ``obter()``."""
        return self.obter(id_conta_contabil=financial_account_id)
