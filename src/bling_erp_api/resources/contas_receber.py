"""Contas a Receber resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contas_receber import ContasBaixarContaDTO
    from bling_erp_api.types import JsonObject, QueryParams


def _contas_receber_list_params(  # noqa: PLR0913
    *,
    situacoes: list[int] | None = None,
    tipo_filtro_data: str | None = None,
    data_inicial: str | None = None,
    data_final: str | None = None,
    ids_categorias: list[int] | None = None,
    id_portador: int | None = None,
    id_contato: int | None = None,
    id_vendedor: int | None = None,
    id_forma_pagamento: int | None = None,
    boleto_gerado: int | None = None,
) -> QueryParams:
    """Build query params for GET /contas/receber."""
    return compact_params(
        {
            "situacoes[]": situacoes,
            "tipoFiltroData": tipo_filtro_data,
            "dataInicial": data_inicial,
            "dataFinal": data_final,
            "idsCategorias[]": ids_categorias,
            "idPortador": id_portador,
            "idContato": id_contato,
            "idVendedor": id_vendedor,
            "idFormaPagamento": id_forma_pagamento,
            "boletoGerado": boleto_gerado,
        }
    )


class ContasReceberResource(BaseResource):
    """Operações de contas a receber do Bling.

    Este recurso mapeia os endpoints ``/contas/receber``. Os métodos canônicos
    usam português para acompanhar a documentação oficial; os métodos em inglês
    continuam disponíveis como aliases de compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        situacoes: list[int] | None = None,
        tipo_filtro_data: str | None = None,
        data_inicial: str | None = None,
        data_final: str | None = None,
        ids_categorias: list[int] | None = None,
        id_portador: int | None = None,
        id_contato: int | None = None,
        id_vendedor: int | None = None,
        id_forma_pagamento: int | None = None,
        boleto_gerado: int | None = None,
    ) -> JsonObject:
        """Lista contas a receber.

        Endpoint: GET /contas/receber

        Obtém lista paginada de contas a receber.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            situacoes: Situações: 1=Em aberto, 2=Recebido, 3=Parcial, 4=Devolvido, 5=Cancelado (Bling: ``situacoes[]``, array, opcional)
            tipo_filtro_data: E=Emissão, V=Vencimento, R=Recebimento (Bling: ``tipoFiltroData``, string, opcional)
            data_inicial: Data inicial do filtro (Bling: ``dataInicial``, string, opcional)
            data_final: Data final do filtro (Bling: ``dataFinal``, string, opcional)
            ids_categorias: IDs das categorias (Bling: ``idsCategorias[]``, array, opcional)
            id_portador: ID da conta financeira/portador (Bling: ``idPortador``, integer, opcional)
            id_contato: ID do contato (Bling: ``idContato``, integer, opcional)
            id_vendedor: ID do vendedor (Bling: ``idVendedor``, integer, opcional)
            id_forma_pagamento: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, opcional)
            boleto_gerado: 0=Não emitido, 1=Emitido (Bling: ``boletoGerado``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: ContasReceberDadosListDTO
        """
        params = _contas_receber_list_params(
            situacoes=situacoes,
            tipo_filtro_data=tipo_filtro_data,
            data_inicial=data_inicial,
            data_final=data_final,
            ids_categorias=ids_categorias,
            id_portador=id_portador,
            id_contato=id_contato,
            id_vendedor=id_vendedor,
            id_forma_pagamento=id_forma_pagamento,
            boleto_gerado=boleto_gerado,
        )
        return self._get(f"/contas/receber?pagina={pagina}&limite={limite}", params=params)

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        statuses: list[int] | None = None,
        date_filter_type: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        category_ids: list[int] | None = None,
        financial_account_id: int | None = None,
        contact_id: int | None = None,
        salesperson_id: int | None = None,
        payment_method_id: int | None = None,
        boleto_generated: int | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``."""
        return self.listar(
            pagina=page,
            limite=limit,
            situacoes=statuses,
            tipo_filtro_data=date_filter_type,
            data_inicial=start_date,
            data_final=end_date,
            ids_categorias=category_ids,
            id_portador=financial_account_id,
            id_contato=contact_id,
            id_vendedor=salesperson_id,
            id_forma_pagamento=payment_method_id,
            boleto_gerado=boleto_generated,
        )

    def obter(self, id_conta_receber: int) -> JsonObject:
        """Obtém uma conta a receber.

        Endpoint: GET /contas/receber/{idContaReceber}

        Args:
            id_conta_receber: ID da conta a receber (Bling: ``idContaReceber``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContasReceberDadosListDTO; 404: ErrorResponse
        """
        return self._get(f"/contas/receber/{id_conta_receber}")

    def get(self, receivable_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``."""
        return self.obter(id_conta_receber=receivable_id)

    def criar(self, dados: JsonObject) -> JsonObject:
        """Cria uma conta a receber.

        Endpoint: POST /contas/receber

        Args:
            dados: Dados da conta. Request body: ContasReceberSalvarDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self._post("/contas/receber", json=to_json_object(dados))

    def create(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``."""
        return self.criar(dados=data)

    def alterar(self, id_conta_receber: int, dados: JsonObject) -> JsonObject:
        """Altera uma conta a receber.

        Endpoint: PUT /contas/receber/{idContaReceber}

        Args:
            id_conta_receber: ID da conta a receber (Bling: ``idContaReceber``, integer, obrigatório)
            dados: Dados da conta para atualização

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/contas/receber/{id_conta_receber}", json=to_json_object(dados))

    def update(self, receivable_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``."""
        return self.alterar(id_conta_receber=receivable_id, dados=data)

    def remover(self, id_conta_receber: int) -> JsonObject:
        """Remove uma conta a receber.

        Endpoint: DELETE /contas/receber/{idContaReceber}

        Args:
            id_conta_receber: ID da conta a receber (Bling: ``idContaReceber``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/contas/receber/{id_conta_receber}")

    def delete(self, receivable_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``."""
        return self.remover(id_conta_receber=receivable_id)

    def baixar(
        self,
        id_conta_receber: int,
        dados: ContasBaixarContaDTO | JsonObject,
    ) -> JsonObject:
        """Baixa uma conta a receber (registra o recebimento).

        Endpoint: POST /contas/receber/{idContaReceber}/baixar

        Args:
            id_conta_receber: ID da conta a receber (Bling: ``idContaReceber``, integer, obrigatório)
            dados: Dados da baixa. Request body: ContasBaixarContaDTO

        Returns:
            Bling API response. Response schemas: 200: bordero; 400: ErrorResponse
        """
        return self._post(f"/contas/receber/{id_conta_receber}/baixar", json=to_json_object(dados))

    def settle(
        self,
        receivable_id: int,
        data: ContasBaixarContaDTO | JsonObject,
    ) -> JsonObject:
        """Compatibility alias for ``baixar()``."""
        return self.baixar(id_conta_receber=receivable_id, dados=data)

    def obter_boletos(self, *, id_origem: int, situacoes: list[int] | None = None) -> JsonObject:
        """Obtém boletos vinculados a uma venda ou NF.

        Endpoint: GET /contas/receber/boletos

        Obtém os boletos vinculados a um idOrigem (venda ou nota fiscal).

        Args:
            id_origem: ID da venda ou nota fiscal (Bling: ``idOrigem``, integer, obrigatório)
            situacoes: Situações: 1=Aberto, 2=Recebido, 3=Parcial, 4=Devolvido, 5=Parcial devolvido, 6=Cancelado (Bling: ``situacoes[]``, array, opcional)

        Returns:
            Bling API response. Response schemas: 200: ContasReceberBoletosDadosBaseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        params = compact_params({"situacoes[]": situacoes})
        return self._get(f"/contas/receber/boletos?idOrigem={id_origem}", params=params)

    def get_boletos(self, *, source_id: int, statuses: list[int] | None = None) -> JsonObject:
        """Compatibility alias for ``obter_boletos()``."""
        return self.obter_boletos(id_origem=source_id, situacoes=statuses)

    def cancelar_boletos(self, dados: JsonObject) -> JsonObject:
        """Cancela boletos em aberto.

        Endpoint: POST /contas/receber/boletos/cancelar

        Cancela um ou todos os boletos em aberto vinculados a uma venda ou NF.

        Args:
            dados: Dados de cancelamento. Request body: ContasReceberBoletosCancelarDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse
        """
        return self._post("/contas/receber/boletos/cancelar", json=to_json_object(dados))

    def cancel_boletos(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``cancelar_boletos()``."""
        return self.cancelar_boletos(dados=data)
