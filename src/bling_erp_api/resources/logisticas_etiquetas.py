"""Logísticas - Etiquetas resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class LogisticasEtiquetasResource(BaseResource):
    """Operações de etiquetas de logísticas do Bling. Mapeia /logisticas/etiquetas.

    Métodos canônicos em pt-BR. Aliases em inglês disponíveis para compatibilidade.
    """

    def obter(self, *, formato: str, ids_vendas: list[int]) -> JsonObject:
        """Obtém etiquetas das vendas.

        Endpoint: GET /logisticas/etiquetas

        Obtém as etiquetas dos pedidos de venda a partir dos IDs dos pedidos.

        Args:
            formato: Formato do arquivo (Bling: ``formato``, string, obrigatório)
            ids_vendas: IDs dos pedidos de venda (Bling: ``idsVendas[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasEtiquetasDadosResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._get(
            "/logisticas/etiquetas", params={"formato": formato, "idsVendas[]": ids_vendas}
        )

    def get(self, *, format: str, sale_ids: list[int]) -> JsonObject:  # noqa: A002
        """Compatibility alias for ``obter()``.

        Obtém etiquetas das vendas.

        Endpoint: GET /logisticas/etiquetas

        Args:
            format: Formato do arquivo (Bling: ``formato``, string, obrigatório)
            sale_ids: IDs dos pedidos de venda (Bling: ``idsVendas[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LogisticasEtiquetasDadosResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.obter(formato=format, ids_vendas=sale_ids)
