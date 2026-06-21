"""Example: List contact types.

Demonstrates retrieving all available contact types through the Bling contacts API.

Endpoint:
    - GET /contatos/tipos

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/get_contatos_tipos

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contacts import (
        ContatosTiposGetResponse200,
    )


def listar_tipos() -> ContatosTiposGetResponse200:
    """Lista tipos de contato disponíveis."""
    with BlingClient.from_env() as client:
        return client.contatos.listar_tipos()


def main() -> None:
    """Demonstrate listing contact types."""
    print(listar_tipos().model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
