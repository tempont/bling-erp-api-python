"""Logísticas - Objetos resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class LogisticasObjetosResource(BaseResource):
    """Operações de objetos de logísticas do Bling. Mapeia /logisticas/objetos.

    Métodos canônicos em pt-BR. Aliases em inglês disponíveis para compatibilidade.
    """

    def criar(self, dados: JsonObject) -> JsonObject:
        """Cria um objeto de logística.

        Endpoint: POST /logisticas/objetos

        Cria um objeto de logística personalizada.

        Args:
            dados: Dados do objeto (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: LogisticasObjetosObjetoDTO; 400: ErrorResponse
        """
        return self._post("/logisticas/objetos", json=to_json_object(dados))

    def create(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria um objeto de logística.

        Endpoint: POST /logisticas/objetos

        Args:
            data: Dados do objeto (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: LogisticasObjetosObjetoDTO; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def obter(self, id_objeto: int) -> JsonObject:
        """Obtém um objeto de logística.

        Endpoint: GET /logisticas/objetos/{idObjeto}

        Obtém um objeto de logística pelo ID.

        Args:
            id_objeto: ID do objeto logístico (Bling: ``idObjeto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasObjetosDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/logisticas/objetos/{id_objeto}")

    def get(self, object_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém um objeto de logística.

        Endpoint: GET /logisticas/objetos/{idObjeto}

        Args:
            object_id: ID do objeto logístico (Bling: ``idObjeto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasObjetosDadosDTO; 404: ErrorResponse
        """
        return self.obter(id_objeto=object_id)

    def alterar(self, id_objeto: int, dados: JsonObject) -> JsonObject:
        """Altera um objeto de logística.

        Endpoint: PUT /logisticas/objetos/{idObjeto}

        Altera dados de um objeto de logística personalizada pelo ID.

        Args:
            id_objeto: ID do objeto logístico (Bling: ``idObjeto``, integer, obrigatório)
            dados: Dados do objeto (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasObjetosObjetoDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/logisticas/objetos/{id_objeto}", json=to_json_object(dados))

    def update(self, object_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera um objeto de logística.

        Endpoint: PUT /logisticas/objetos/{idObjeto}

        Args:
            object_id: ID do objeto logístico (Bling: ``idObjeto``, integer, obrigatório)
            data: Dados do objeto (Bling: request body, object, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasObjetosObjetoDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_objeto=object_id, dados=data)

    def remover(self, id_objeto: int) -> JsonObject:
        """Remove um objeto de logística.

        Endpoint: DELETE /logisticas/objetos/{idObjeto}

        Remove um objeto de logística personalizada que não esteja em uma PLP.

        Args:
            id_objeto: ID do objeto logístico (Bling: ``idObjeto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/logisticas/objetos/{id_objeto}")

    def delete(self, object_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove um objeto de logística.

        Endpoint: DELETE /logisticas/objetos/{idObjeto}

        Args:
            object_id: ID do objeto logístico (Bling: ``idObjeto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(id_objeto=object_id)
