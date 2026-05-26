"""Exemplo que atualiza um contato existente."""

from bling_erp_api import BlingClient
from bling_erp_api.types import JsonObject

CONTATO_ID = 12345678


def main() -> None:
    """Altera dados de um contato por ``PUT``."""
    payload: JsonObject = {"nome": "Nova Empresa LTDA - Matriz"}
    with BlingClient.from_env() as client:
        response = client.contatos.alterar(CONTATO_ID, payload)
        print(response)


if __name__ == "__main__":
    main()
