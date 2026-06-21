"""Example: Get Contact by ID.

Demonstrates how to retrieve a single contact by its Bling ID.

Endpoint:
    - GET /contatos/{idContato}

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/get_contatos__idContato_

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contacts import (
        ContatosIdContatoGetResponse200,
    )

CONTATO_ID = 12345678


def obter_contato(id_contato: int) -> ContatosIdContatoGetResponse200:
    """Obtém um contato pelo ID."""
    with BlingClient.from_env() as client:
        return client.contatos.obter(id_contato=id_contato)


def main() -> None:
    """Demonstrate getting a contact by ID."""
    result = obter_contato(CONTATO_ID)
    print(result.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
