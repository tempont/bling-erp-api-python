"""Logísticas - Remessas resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.logisticas import (
    LogisticasIdLogisticaRemessasGetResponse200,
    LogisticasRemessasIdRemessaGetResponse200,
    LogisticasRemessasIdRemessaPutResponse200,
    LogisticasRemessasPostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class LogisticasRemessasResource(BaseResource):
    """Operações de remessas de logísticas do Bling. Mapeia /logisticas/remessas.

    Métodos canônicos em pt-BR. Aliases em inglês disponíveis para compatibilidade.
    """

    def listar_por_logistica(
        self, id_logistica: int
    ) -> LogisticasIdLogisticaRemessasGetResponse200:
        """Lista remessas de uma logística.

        Endpoint: GET /logisticas/{idLogistica}/remessas

        Obtém as remessas de postagem de uma logística pelo ID.

        Args:
            id_logistica: ID da logística (Bling: ``idLogistica``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessasDadosDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        raw = self._get(f"/logisticas/{id_logistica}/remessas")
        return self._validate_response(LogisticasIdLogisticaRemessasGetResponse200, raw)

    def list_by_logistics(self, logistics_id: int) -> LogisticasIdLogisticaRemessasGetResponse200:
        """Compatibility alias for ``listar_por_logistica()``.

        Lista remessas de uma logística.

        Endpoint: GET /logisticas/{idLogistica}/remessas

        Args:
            logistics_id: ID da logística (Bling: ``idLogistica``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessasDadosDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.listar_por_logistica(id_logistica=logistics_id)

    def obter(self, id_remessa: int) -> LogisticasRemessasIdRemessaGetResponse200:
        """Obtém uma remessa de postagem.

        Endpoint: GET /logisticas/remessas/{idRemessa}

        Obtém uma remessa de postagem pelo ID.

        Args:
            id_remessa: ID da remessa de postagem (Bling: ``idRemessa``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessasDadosBaseDTO; 404: ErrorResponse
        """
        raw = self._get(f"/logisticas/remessas/{id_remessa}")
        return self._validate_response(LogisticasRemessasIdRemessaGetResponse200, raw)

    def get(self, shipment_id: int) -> LogisticasRemessasIdRemessaGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém uma remessa de postagem.

        Endpoint: GET /logisticas/remessas/{idRemessa}

        Args:
            shipment_id: ID da remessa de postagem (Bling: ``idRemessa``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessasDadosBaseDTO; 404: ErrorResponse
        """
        return self.obter(id_remessa=shipment_id)

    def criar(self, dados: JsonObject) -> LogisticasRemessasPostResponse201:
        """Cria uma remessa de postagem.

        Endpoint: POST /logisticas/remessas

        Cria uma remessa de postagem de uma logística.

        Args:
            dados: Dados da remessa (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: LogisticasRemessaRemessaDTO; 400: ErrorResponse
        """
        raw = self._post("/logisticas/remessas", json=to_json_object(dados))
        return self._validate_response(LogisticasRemessasPostResponse201, raw)

    def create(self, data: JsonObject) -> LogisticasRemessasPostResponse201:
        """Compatibility alias for ``criar()``.

        Cria uma remessa de postagem.

        Endpoint: POST /logisticas/remessas

        Args:
            data: Dados da remessa (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: LogisticasRemessaRemessaDTO; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(
        self, id_remessa: int, dados: JsonObject
    ) -> LogisticasRemessasIdRemessaPutResponse200:
        """Altera uma remessa de postagem.

        Endpoint: PUT /logisticas/remessas/{idRemessa}

        Altera uma remessa de postagem pelo ID.

        Args:
            id_remessa: ID da remessa de postagem (Bling: ``idRemessa``, integer, obrigatório)
            dados: Dados da remessa (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessaRemessaDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        raw = self._put(f"/logisticas/remessas/{id_remessa}", json=to_json_object(dados))
        return self._validate_response(LogisticasRemessasIdRemessaPutResponse200, raw)

    def update(
        self, shipment_id: int, data: JsonObject
    ) -> LogisticasRemessasIdRemessaPutResponse200:
        """Compatibility alias for ``alterar()``.

        Altera uma remessa de postagem.

        Endpoint: PUT /logisticas/remessas/{idRemessa}

        Args:
            shipment_id: ID da remessa de postagem (Bling: ``idRemessa``, integer, obrigatório)
            data: Dados da remessa (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessaRemessaDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_remessa=shipment_id, dados=data)

    def remover(self, id_remessa: int) -> JsonObject:
        """Remove uma remessa de postagem.

        Endpoint: DELETE /logisticas/remessas/{idRemessa}

        Remove uma remessa de postagem pelo ID.

        Args:
            id_remessa: ID da remessa de postagem (Bling: ``idRemessa``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/logisticas/remessas/{id_remessa}")

    def delete(self, shipment_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove uma remessa de postagem.

        Endpoint: DELETE /logisticas/remessas/{idRemessa}

        Args:
            shipment_id: ID da remessa de postagem (Bling: ``idRemessa``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(id_remessa=shipment_id)
