"""Example: Create Contact.

Demonstrates how to create a new contact.

Endpoint:
    - POST /contatos

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/post_contatos

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contacts import (
        ContatosPostRequest,
        ContatosPostResponse201,
    )


def criar_contato(dados: ContatosPostRequest) -> ContatosPostResponse201:
    """Cria um novo contato."""
    with BlingClient.from_env() as client:
        return client.contatos.criar(dados=dados)


def main() -> None:
    """Demonstrate creating a contact."""
    # payload = ContatosPostRequest(
    #     id=0,
    #     nome="Nova Empresa LTDA",
    #     tipo="J",
    #     situacao="A",
    # )
    # result = criar_contato(payload)
    # print(result.model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    print("Create example — uncomment the lines above and run with real credentials.")
    time.sleep(1)


if __name__ == "__main__":
    main()
