"""Borderôs resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.borderos import BorderosIdBorderoGetResponse200
from bling_erp_api.resources.base import BaseResource

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class BorderosResource(BaseResource):
    """Operações de borderôs do Bling.

    Este recurso mapeia os endpoints ``/borderos``. Os métodos canônicos usam
    português para acompanhar a documentação oficial.
    """

    def obter(self, id_bordero: int) -> BorderosIdBorderoGetResponse200:
        """Obtém um borderô.

        Endpoint: GET /borderos/{idBordero}

        Obtém os detalhes de um borderô pelo ID.

        Args:
            id_bordero: ID do borderô (Bling: ``idBordero``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: BorderosDadosDTO; 404: ErrorResponse
        """
        raw = self._get(f"/borderos/{id_bordero}")
        return self._validate_response(BorderosIdBorderoGetResponse200, raw)

    def get(self, bordero_id: int) -> BorderosIdBorderoGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém um borderô.

        Endpoint: GET /borderos/{idBordero}

        Obtém os detalhes de um borderô pelo ID.

        Args:
            bordero_id: ID do borderô (Bling: ``idBordero``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: BorderosDadosDTO; 404: ErrorResponse
        """
        return self.obter(id_bordero=bordero_id)

    def remover(self, id_bordero: int) -> JsonObject:
        """Remove um borderô.

        Endpoint: DELETE /borderos/{idBordero}

        Remove um borderô pelo ID.

        Args:
            id_bordero: ID do borderô (Bling: ``idBordero``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/borderos/{id_bordero}")

    def delete(self, bordero_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove um borderô.

        Endpoint: DELETE /borderos/{idBordero}

        Remove um borderô pelo ID.

        Args:
            bordero_id: ID do borderô (Bling: ``idBordero``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(id_bordero=bordero_id)
