"""Example: List Contacts.

Demonstrates how to list paginated contacts with optional search filter.

Endpoint:
    - GET /contatos

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/get_contatos

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contacts import ContatosGetResponse200


def listar_contatos(
    *, pagina: int = 1, limite: int = 100, pesquisa: str | None = None
) -> ContatosGetResponse200:
    """Lista contatos com paginação e filtro opcional."""
    with BlingClient.from_env() as client:
        return client.contatos.listar(pagina=pagina, limite=limite, pesquisa=pesquisa)


def main() -> None:
    """Demonstrate listing contacts."""
    result = listar_contatos(pesquisa="Ana", limite=10)
    print(result.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
