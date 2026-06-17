"""Example: Get a Logistics by ID.

Endpoints:
    - GET /logisticas/{idLogistica}

Docs:
    - https://developer.bling.com.br/referencia#/Logisticas/get_logisticas__idLogistica_

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.logisticas import (
        LogisticasIdLogisticaGetResponse200,
    )


def obter_logistica(logistics_id: int) -> LogisticasIdLogisticaGetResponse200:
    """Obtém uma logística pelo ID."""
    with BlingClient.from_env() as client:
        return client.logisticas.obter(id_logistica=logistics_id)


def main() -> None:
    """Demonstrate a logistics retrieval."""
    print(obter_logistica(101).model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
