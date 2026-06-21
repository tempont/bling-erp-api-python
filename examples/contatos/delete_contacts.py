"""Example: Remove multiple contacts.

Demonstrates bulk deletion of contacts through the Bling contacts API.

Endpoint:
    - DELETE /contatos

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/delete_contatos

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contacts import (
        ContatosDeleteResponse200,
    )


def remover_varios_contatos(ids_contatos: list[int]) -> ContatosDeleteResponse200:
    """Remove múltiplos contatos pelos IDs."""
    with BlingClient.from_env() as client:
        return client.contatos.remover_varios(ids_contatos=ids_contatos)


def main() -> None:
    """Demonstrate bulk contact deletion."""
    # Write operations (commented out)
    # ids_contatos = [11111111, 22222222]
    # print(remover_varios_contatos(ids_contatos).model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
