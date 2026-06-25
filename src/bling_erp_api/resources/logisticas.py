"""Logísticas resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.logisticas import (
    LogisticasGetResponse200,
    LogisticasIdLogisticaGetResponse200,
    LogisticasPostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, QueryParams


def _logisticas_list_params(
    *,
    tipo_integracao: str | None = None,
    tipos_integracoes: list[str] | None = None,
    situacao: str | None = None,
    logisticas_reversas: bool | None = None,
) -> QueryParams:
    return compact_params(
        {
            "tipoIntegracao": tipo_integracao,
            "tiposIntegracoes[]": tipos_integracoes,
            "situacao": situacao,
            "logisticasReversas": logisticas_reversas,
        }
    )


class LogisticasResource(BaseResource):
    """Operações de logísticas do Bling. Mapeia /logisticas.

    Métodos canônicos em pt-BR. Aliases em inglês disponíveis para compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        tipo_integracao: str | None = None,
        tipos_integracoes: list[str] | None = None,
        situacao: str | None = None,
        logisticas_reversas: bool | None = None,
    ) -> LogisticasGetResponse200:
        """Lista logísticas.

        Endpoint: GET /logisticas

        Lista logísticas cadastradas com paginação.

        Args:
            pagina: Número da página (Bling: ``pagina``, integer, opcional)
            limite: Quantidade por página (Bling: ``limite``, integer, opcional)
            tipo_integracao: Tipo de integração (Bling: ``tipoIntegracao``, string, opcional)
            tipos_integracoes: Lista de tipos de integração (Bling: ``tiposIntegracoes[]``, array, opcional)
            situacao: Situação (Bling: ``situacao``, string, opcional)
            logisticas_reversas: Apenas logísticas reversas (Bling: ``logisticasReversas``, boolean, opcional)

        Returns:
            Bling API response. Response schemas: 200: LogisticasDadosBaseDTO; 404: ErrorResponse
        """
        params: QueryParams = {
            "pagina": pagina,
            "limite": limite,
            **_logisticas_list_params(
                tipo_integracao=tipo_integracao,
                tipos_integracoes=tipos_integracoes,
                situacao=situacao,
                logisticas_reversas=logisticas_reversas,
            ),
        }
        raw = self._get("/logisticas", params=params)
        return self._validate_response(LogisticasGetResponse200, raw)

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        integration_type: str | None = None,
        integration_types: list[str] | None = None,
        status: str | None = None,
        reverse_logistics: bool | None = None,
    ) -> LogisticasGetResponse200:
        """Compatibility alias for ``listar()``.

        Lista logísticas.

        Endpoint: GET /logisticas

        Args:
            page: Page number (Bling: ``pagina``, integer, opcional)
            limit: Items per page (Bling: ``limite``, integer, opcional)
            integration_type: Integration type (Bling: ``tipoIntegracao``, string, opcional)
            integration_types: List of integration types (Bling: ``tiposIntegracoes[]``, array, opcional)
            status: Status (Bling: ``situacao``, string, opcional)
            reverse_logistics: Only reverse logistics (Bling: ``logisticasReversas``, boolean, opcional)

        Returns:
            Bling API response. Response schemas: 200: LogisticasDadosBaseDTO; 404: ErrorResponse
        """
        return self.listar(
            pagina=page,
            limite=limit,
            tipo_integracao=integration_type,
            tipos_integracoes=integration_types,
            situacao=status,
            logisticas_reversas=reverse_logistics,
        )

    def obter(
        self, id_logistica: int, *, listar_servicos_inativos: bool | None = None
    ) -> LogisticasIdLogisticaGetResponse200:
        """Obtém uma logística.

        Endpoint: GET /logisticas/{idLogistica}

        Obtém uma logística pelo ID.

        Args:
            id_logistica: ID da logística (Bling: ``idLogistica``, integer, obrigatório)
            listar_servicos_inativos: Incluir serviços inativos (Bling: ``listarServicosInativos``, boolean, opcional)

        Returns:
            Bling API response. Response schemas: 200: LogisticasDadosDTO; 404: ErrorResponse
        """
        params = compact_params({"listarServicosInativos": listar_servicos_inativos})
        raw = self._get(f"/logisticas/{id_logistica}", params=params)
        return self._validate_response(LogisticasIdLogisticaGetResponse200, raw)

    def get(
        self, logistics_id: int, *, list_inactive_services: bool | None = None
    ) -> LogisticasIdLogisticaGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém uma logística.

        Endpoint: GET /logisticas/{idLogistica}

        Args:
            logistics_id: ID da logística (Bling: ``idLogistica``, integer, obrigatório)
            list_inactive_services: Incluir serviços inativos (Bling: ``listarServicosInativos``, boolean, opcional)

        Returns:
            Bling API response. Response schemas: 200: LogisticasDadosDTO; 404: ErrorResponse
        """
        return self.obter(
            id_logistica=logistics_id, listar_servicos_inativos=list_inactive_services
        )

    def criar(self, dados: JsonObject) -> LogisticasPostResponse201:
        """Cria uma logística.

        Endpoint: POST /logisticas

        Cria uma nova logística.

        Args:
            dados: Dados da logística (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: LogisticasLogisticaDTO; 400: ErrorResponse
        """
        raw = self._post("/logisticas", json=to_json_object(dados))
        return self._validate_response(LogisticasPostResponse201, raw)

    def create(self, data: JsonObject) -> LogisticasPostResponse201:
        """Compatibility alias for ``criar()``.

        Cria uma logística.

        Endpoint: POST /logisticas

        Args:
            data: Dados da logística (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: LogisticasLogisticaDTO; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(self, id_logistica: int, dados: JsonObject) -> JsonObject:
        """Altera uma logística.

        Endpoint: PUT /logisticas/{idLogistica}

        Altera uma logística pelo ID.

        Args:
            id_logistica: ID da logística (Bling: ``idLogistica``, integer, obrigatório)
            dados: Dados da logística (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse
        """
        return self._put(f"/logisticas/{id_logistica}", json=to_json_object(dados))

    def update(self, logistics_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera uma logística.

        Endpoint: PUT /logisticas/{idLogistica}

        Args:
            logistics_id: ID da logística (Bling: ``idLogistica``, integer, obrigatório)
            data: Dados da logística (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse
        """
        return self.alterar(id_logistica=logistics_id, dados=data)

    def remover(self, id_logistica: int) -> JsonObject:
        """Remove uma logística.

        Endpoint: DELETE /logisticas/{idLogistica}

        Remove uma logística pelo ID.

        Args:
            id_logistica: ID da logística (Bling: ``idLogistica``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/logisticas/{id_logistica}")

    def delete(self, logistics_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove uma logística.

        Endpoint: DELETE /logisticas/{idLogistica}

        Args:
            logistics_id: ID da logística (Bling: ``idLogistica``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(id_logistica=logistics_id)
