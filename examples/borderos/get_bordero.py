"""Example: Get a Bordero by ID.

Demonstrates retrieving a single bordero through the Bling borderos API.

Endpoint:
    - GET /borderos/{idBordero}

Docs:
    - https://developer.bling.com.br/referencia#/Border%C3%B4s/get_borderos__idBordero_

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.borderos import BorderosIdBorderoGetResponse200


## ---------------------------------------------------------------------------
## GET A BORDERO BY ID
## ---------------------------------------------------------------------------


def obter_bordero(id_bordero: int) -> BorderosIdBorderoGetResponse200:
    """Obtém um bordero pelo ID.

    Endpoint: GET /borderos/{idBordero}

    Obtém um bordero pelo ID.

    Args:
        id_bordero: ID do bordero (Bling: ``idBordero``, integer, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: BorderosDadosDTO; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.borderos.obter(id_bordero=id_bordero)


def main() -> None:
    """Demonstrate get bordero operation."""
    bordero_id = 123456  # Example — replace with real ID.

    bordero = obter_bordero(bordero_id)
    print(bordero.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
