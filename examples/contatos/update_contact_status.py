"""Example: Update a single contact's status.

Demonstrates changing the status of an individual contact through the Bling
contacts API.

Endpoint:
    - PATCH /contatos/{idContato}/situacoes

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/patch_contatos__idContato__situacoes

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


def alterar_situacao_contato(id_contato: int, situacao: Literal["A", "I", "E", "S"]) -> JsonObject:
    """Altera a situação de um contato (ex.: A=Ativo, I=Inativo)."""
    with BlingClient.from_env() as client:
        return client.contatos.alterar_situacao(id_contato=id_contato, situacao=situacao)


def main() -> None:
    """Demonstrate updating a single contact's status."""
    # Write operations (commented out)
    # contato_id = 12345678  # Exemplo — substitua pelo ID real.
    # response = alterar_situacao_contato(contato_id, situacao="A")
    # print(f"Status atualizado: {response}")


if __name__ == "__main__":
    main()
