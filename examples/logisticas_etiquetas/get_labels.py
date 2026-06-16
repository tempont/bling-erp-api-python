"""Example: Get shipping labels for sales orders."""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.logisticas import LogisticasEtiquetasGetResponse200


def obter_etiquetas(
    *,
    formato: str,
    ids_vendas: list[int],
) -> LogisticasEtiquetasGetResponse200:
    """Obtém etiquetas de logística para pedidos de venda.

    Endpoint: GET /logisticas/etiquetas

    Obtém etiquetas de envio para pedidos de venda, no formato especificado.

    Args:
        formato: Formato das etiquetas (Bling: ``formato``, string, obrigatório).
            Ex: "PDF", "ZPL"
        ids_vendas: IDs dos pedidos de venda (Bling: ``idsVendas``, array de
            inteiros, obrigatório).

    Returns:
        Bling API response. Response schemas: 200: LogisticasEtiquetasGetResponse200
    """
    with BlingClient.from_env() as client:
        return client.logisticas_etiquetas.obter(
            formato=formato,
            ids_vendas=ids_vendas,
        )


def main() -> None:
    """Demonstrate getting shipping labels for sales orders."""
    result = obter_etiquetas(
        formato="PDF",
        ids_vendas=[1],
    )
    print(result.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
