"""Example: Delete Contact.

Demonstrates how to remove a contact by its Bling ID.

Endpoint:
    - DELETE /contatos/{idContato}

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/delete_contatos__idContato_

Note:
    The Bling API returns 204 No Content on success — no response body.

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject

CONTATO_ID = 12345678


def remover_contato(id_contato: int) -> JsonObject:
    """Remove um contato pelo ID."""
    with BlingClient.from_env() as client:
        return client.contatos.remover(id_contato=id_contato)


def main() -> None:
    """Demonstrate deleting a contact."""
    result = remover_contato(CONTATO_ID)
    print(f"Contact {CONTATO_ID} removed. Response: {result}")
    time.sleep(1)


if __name__ == "__main__":
    main()
