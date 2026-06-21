"""Example: Update Contact.

Demonstrates how to fully update an existing contact via PUT.

Endpoint:
    - PUT /contatos/{idContato}

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/put_contatos__idContato_

Note:
    The Bling API returns 204 No Content on success — no response body.

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contacts import (
        ContatosIdContatoPutRequest,
    )
    from bling_erp_api.types import JsonObject

CONTATO_ID = 12345678


def alterar_contato(id_contato: int, dados: ContatosIdContatoPutRequest) -> JsonObject:
    """Altera um contato pelo ID (PUT)."""
    with BlingClient.from_env() as client:
        return client.contatos.alterar(id_contato=id_contato, dados=dados)


def main() -> None:
    """Demonstrate updating a contact."""
    # payload = ContatosIdContatoPutRequest(
    #     id=0,
    #     nome="Nova Empresa LTDA - Matriz",
    #     situacao="A",
    #     tipo="J",
    # )
    # result = alterar_contato(CONTATO_ID, payload)
    # print(result)
    print("Update example — uncomment the lines above and run with real credentials.")
    time.sleep(1)


if __name__ == "__main__":
    main()
