"""Example: Logistics Shipments (Remessas) Operations.

Demonstrates read operations on logistics shipments through the Bling API.

Endpoints:
    - GET /logisticas/{idLogistica}/remessas
    - GET /logisticas/remessas/{idRemessa}
    - POST /logisticas/remessas
    - PUT /logisticas/remessas/{idRemessa}
    - DELETE /logisticas/remessas/{idRemessa}
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.logisticas import (
        LogisticasIdLogisticaRemessasGetResponse200,
        LogisticasRemessasIdRemessaGetResponse200,
        LogisticasRemessasIdRemessaPutResponse200,  # pyright: ignore[reportUnusedImport]  # noqa: F401
        LogisticasRemessasPostResponse201,  # pyright: ignore[reportUnusedImport]  # noqa: F401
    )


def listar_por_logistica(id_logistica: int) -> LogisticasIdLogisticaRemessasGetResponse200:
    """Lista remessas de uma logística."""
    with BlingClient.from_env() as client:
        return client.logisticas_remessas.listar_por_logistica(id_logistica=id_logistica)


def obter_remessa(id_remessa: int) -> LogisticasRemessasIdRemessaGetResponse200:
    """Obtém uma remessa pelo ID."""
    with BlingClient.from_env() as client:
        return client.logisticas_remessas.obter(id_remessa=id_remessa)


# def criar_remessa(dados: JsonObject) -> LogisticasRemessasPostResponse201:
#     """Cria uma remessa de postagem."""
#     with BlingClient.from_env() as client:
#         return client.logisticas_remessas.criar(dados=dados)


# def alterar_remessa(id_remessa: int, dados: JsonObject) -> LogisticasRemessasIdRemessaPutResponse200:
#     """Altera uma remessa de postagem pelo ID."""
#     with BlingClient.from_env() as client:
#         return client.logisticas_remessas.alterar(id_remessa=id_remessa, dados=dados)


def main() -> None:
    """Demonstrate logistics shipments operations."""
    logistics_id = 1  # Exemplo — substitua pelo ID real.
    shipment_id = 501  # Exemplo — substitua pelo ID real.

    # Read operations
    remessas = listar_por_logistica(logistics_id)
    print(remessas.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    remessa = obter_remessa(shipment_id)
    print(remessa.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Write operations (commented out)
    # payload = JsonObject({...})
    # print(criar_remessa(payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # print(alterar_remessa(shipment_id, payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)


if __name__ == "__main__":
    main()
