"""Example: Update multiple contacts' status.

Demonstrates bulk status update of contacts through the Bling contacts API.

Endpoint:
    - POST /contatos/situacoes

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/post_contatos_situacoes

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contacts import (
        ContatosSituacoesPostResponse200,
    )


def alterar_situacao_varios(
    ids_contatos: list[int], situacao: Literal["A", "I", "E", "S"]
) -> ContatosSituacoesPostResponse200:
    """Altera a situação de múltiplos contatos (ex.: I=Inativo)."""
    with BlingClient.from_env() as client:
        return client.contatos.alterar_situacao_varios(ids_contatos=ids_contatos, situacao=situacao)


def main() -> None:
    """Demonstrate bulk contact status update."""
    # Write operations (commented out)
    # ids_contatos = [11111111, 22222222]
    # print(alterar_situacao_varios(ids_contatos, situacao="I").model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
