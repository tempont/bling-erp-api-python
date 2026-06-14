"""Logísticas - Serviços resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.logisticas import (
    LogisticasServicosGetResponse200,
    LogisticasServicosIdLogisticaServicoGetResponse200,
    LogisticasServicosIdLogisticaServicoPutResponse200,
    LogisticasServicosPostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class LogisticasServicosResource(BaseResource):
    """Operações de serviços de logísticas do Bling. Mapeia /logisticas/servicos.

    Métodos canônicos em pt-BR. Aliases em inglês disponíveis para compatibilidade.
    """

    def listar(
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        tipo_integracao: str | None = None,
    ) -> LogisticasServicosGetResponse200:
        """Lista serviços de logísticas.

        Endpoint: GET /logisticas/servicos

        Lista serviços de logísticas cadastrados com paginação.

        Args:
            pagina: Número da página (Bling: ``pagina``, integer, opcional)
            limite: Quantidade por página (Bling: ``limite``, integer, opcional)
            tipo_integracao: Tipo de integração (Bling: ``tipoIntegracao``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: LogisticasServicosDadosDTO; 400: ErrorResponse
        """
        params = compact_params({"tipoIntegracao": tipo_integracao})
        raw = self._get(f"/logisticas/servicos?pagina={pagina}&limite={limite}", params=params)
        return self._validate_response(LogisticasServicosGetResponse200, raw)

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        integration_type: str | None = None,
    ) -> LogisticasServicosGetResponse200:
        """Compatibility alias for ``listar()``.

        Lista serviços de logísticas.

        Endpoint: GET /logisticas/servicos

        Args:
            page: Page number (Bling: ``pagina``, integer, opcional)
            limit: Items per page (Bling: ``limite``, integer, opcional)
            integration_type: Integration type (Bling: ``tipoIntegracao``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: LogisticasServicosDadosDTO; 400: ErrorResponse
        """
        return self.listar(pagina=page, limite=limit, tipo_integracao=integration_type)

    def obter(
        self, id_logistica_servico: int
    ) -> LogisticasServicosIdLogisticaServicoGetResponse200:
        """Obtém um serviço de logística.

        Endpoint: GET /logisticas/servicos/{idLogisticaServico}

        Obtém um serviço de logística pelo ID.

        Args:
            id_logistica_servico: ID do serviço (Bling: ``idLogisticaServico``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasServicosDadosDTO; 404: ErrorResponse
        """
        raw = self._get(f"/logisticas/servicos/{id_logistica_servico}")
        return self._validate_response(LogisticasServicosIdLogisticaServicoGetResponse200, raw)

    def get(self, service_id: int) -> LogisticasServicosIdLogisticaServicoGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém um serviço de logística.

        Endpoint: GET /logisticas/servicos/{idLogisticaServico}

        Args:
            service_id: ID do serviço (Bling: ``idLogisticaServico``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasServicosDadosDTO; 404: ErrorResponse
        """
        return self.obter(id_logistica_servico=service_id)

    def criar(self, dados: JsonObject) -> LogisticasServicosPostResponse201:
        """Cria um serviço de logística.

        Endpoint: POST /logisticas/servicos

        Cria um novo serviço de logística personalizada.

        Args:
            dados: Dados do serviço (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: LogisticasServicosDadosSaveDTO; 400: ErrorResponse
        """
        raw = self._post("/logisticas/servicos", json=to_json_object(dados))
        return self._validate_response(LogisticasServicosPostResponse201, raw)

    def create(self, data: JsonObject) -> LogisticasServicosPostResponse201:
        """Compatibility alias for ``criar()``.

        Cria um serviço de logística.

        Endpoint: POST /logisticas/servicos

        Args:
            data: Dados do serviço (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: LogisticasServicosDadosSaveDTO; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(
        self, id_logistica_servico: int, dados: JsonObject
    ) -> LogisticasServicosIdLogisticaServicoPutResponse200:
        """Altera um serviço de logística.

        Endpoint: PUT /logisticas/servicos/{idLogisticaServico}

        Altera dados de um serviço de logística personalizada pelo ID.

        Args:
            id_logistica_servico: ID do serviço (Bling: ``idLogisticaServico``, integer, obrigatório)
            dados: Dados do serviço (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasServicosDadosSaveDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        raw = self._put(f"/logisticas/servicos/{id_logistica_servico}", json=to_json_object(dados))
        return self._validate_response(LogisticasServicosIdLogisticaServicoPutResponse200, raw)

    def update(
        self, service_id: int, data: JsonObject
    ) -> LogisticasServicosIdLogisticaServicoPutResponse200:
        """Compatibility alias for ``alterar()``.

        Altera um serviço de logística.

        Endpoint: PUT /logisticas/servicos/{idLogisticaServico}

        Args:
            service_id: ID do serviço (Bling: ``idLogisticaServico``, integer, obrigatório)
            data: Dados do serviço (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasServicosDadosSaveDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_logistica_servico=service_id, dados=data)

    def alterar_situacao(self, id_logistica_servico: int, ativo: bool) -> JsonObject:  # noqa: FBT001
        """Ativa ou desativa um serviço de logística.

        Endpoint: PATCH /logisticas/{idLogisticaServico}/situacoes

        Desativa ou ativa um serviço de uma logística personalizada pelo ID.

        Args:
            id_logistica_servico: ID do serviço (Bling: ``idLogisticaServico``, integer, obrigatório)
            ativo: Ativar ou desativar (Bling: request body, boolean, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(
            f"/logisticas/{id_logistica_servico}/situacoes",
            json=to_json_object({"ativo": ativo}),
        )

    def set_status(self, service_id: int, active: bool) -> JsonObject:  # noqa: FBT001
        """Compatibility alias for ``alterar_situacao()``.

        Ativa ou desativa um serviço de logística.

        Endpoint: PATCH /logisticas/{idLogisticaServico}/situacoes

        Args:
            service_id: ID do serviço (Bling: ``idLogisticaServico``, integer, obrigatório)
            active: Ativar ou desativar (Bling: request body, boolean, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar_situacao(id_logistica_servico=service_id, ativo=active)
