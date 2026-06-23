"""Example: Delete a Bordero.

Demonstrates removing a single bordero through the Bling borderos API.

Endpoint:
    - DELETE /borderos/{idBordero}

Docs:
    - https://developer.bling.com.br/referencia#/Border%C3%B4s/delete_borderos__idBordero_

"""

from __future__ import annotations

import time

from bling_erp_api import BlingClient

## ---------------------------------------------------------------------------
## DELETE A BORDERO BY ID
## ---------------------------------------------------------------------------


def remover_bordero(id_bordero: int) -> None:
    """Remove um bordero pelo ID.

    Endpoint: DELETE /borderos/{idBordero}

    Remove um bordero pelo ID. Retorna 204 No Content em caso de sucesso.

    Args:
        id_bordero: ID do bordero (Bling: ``idBordero``, integer, obrigatório)

    Returns:
        None (204 No Content).
    """
    with BlingClient.from_env() as client:
        client.borderos.remover(id_bordero=id_bordero)


def main() -> None:
    """Demonstrate delete bordero operation."""
    bordero_id = 123456  # Example — replace with real ID.

    remover_bordero(bordero_id)
    print("Bordero removido com sucesso (204 No Content).")
    time.sleep(1)


if __name__ == "__main__":
    main()
