"""Example: Get contact types for a contact.

Demonstrates retrieving the contact types associated with a specific contact
through the Bling contacts API.

Endpoint:
    - GET /contatos/{idContato}/tipos

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/get_contatos__idContato__tipos

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contacts import (
        ContatosIdContatoTiposGetResponse200,
    )


def obter_tipos_contato(id_contato: int) -> ContatosIdContatoTiposGetResponse200:
    """Obtém os tipos de contato associados a um contato."""
    with BlingClient.from_env() as client:
        return client.contatos.obter_tipo_contato(id_contato=id_contato)


def main() -> None:
    """Demonstrate getting contact types for a contact."""
    contato_id = 12345678  # Exemplo — substitua pelo ID real.

    # Read operations
    print(obter_tipos_contato(contato_id).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
