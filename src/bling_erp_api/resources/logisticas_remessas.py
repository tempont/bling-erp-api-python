"""Logísticas - Remessas resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class LogisticasRemessasResource(BaseResource):
    """Operações de remessas de logísticas do Bling. Mapeia /logisticas/remessas.

    Métodos canônicos em pt-BR. Aliases em inglês disponíveis para compatibilidade.
    """

    def listar_por_logistica(self, id_logistica: int) -> JsonObject:
        """Lista remessas de uma logística.

        Endpoint: GET /logisticas/{idLogistica}/remessas

        Obtém as remessas de postagem de uma logística pelo ID.

        Args:
            id_logistica: ID da logística (Bling: ``idLogistica``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessasDadosDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._get(f"/logisticas/{id_logistica}/remessas")

    def list_by_logistics(self, logistics_id: int) -> JsonObject:
        """Compatibility alias for ``listar_por_logistica()``.

        Lista remessas de uma logística.

        Endpoint: GET /logisticas/{idLogistica}/remessas

        Args:
            logistics_id: ID da logística (Bling: ``idLogistica``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessasDadosDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.listar_por_logistica(id_logistica=logistics_id)

    def obter(self, id_remessa: int) -> JsonObject:
        """Obtém uma remessa de postagem.

        Endpoint: GET /logisticas/remessas/{idRemessa}

        Obtém uma remessa de postagem pelo ID.

        Args:
            id_remessa: ID da remessa de postagem (Bling: ``idRemessa``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessasDadosBaseDTO; 404: ErrorResponse
        """
        return self._get(f"/logisticas/remessas/{id_remessa}")

    def get(self, shipment_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém uma remessa de postagem.

        Endpoint: GET /logisticas/remessas/{idRemessa}

        Args:
            shipment_id: ID da remessa de postagem (Bling: ``idRemessa``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessasDadosBaseDTO; 404: ErrorResponse
        """
        return self.obter(id_remessa=shipment_id)

    def criar(self, dados: JsonObject) -> JsonObject:
        """Cria uma remessa de postagem.

        Endpoint: POST /logisticas/remessas

        Cria uma remessa de postagem de uma logística.

        Args:
            dados: Dados da remessa (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: LogisticasRemessaRemessaDTO; 400: ErrorResponse
        """
        return self._post("/logisticas/remessas", json=to_json_object(dados))

    def create(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria uma remessa de postagem.

        Endpoint: POST /logisticas/remessas

        Args:
            data: Dados da remessa (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: LogisticasRemessaRemessaDTO; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(self, id_remessa: int, dados: JsonObject) -> JsonObject:
        """Altera uma remessa de postagem.

        Endpoint: PUT /logisticas/remessas/{idRemessa}

        Altera uma remessa de postagem pelo ID.

        Args:
            id_remessa: ID da remessa de postagem (Bling: ``idRemessa``, integer, obrigatório)
            dados: Dados da remessa (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasRemessaRemessaDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/logisticas/remessas/{id_remessa}", json=to_json_object(dados))

    def update(self, shipment_id: int, data: JsonObject) -> JsonObject:
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
