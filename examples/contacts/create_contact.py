"""Exemplo que cria um contato."""

from bling_erp_api import BlingClient
from bling_erp_api.types import JsonObject


def main() -> None:
    """Cria um contato simplificado."""
    payload: JsonObject = {
        "nome": "Nova Empresa LTDA",
        "tipo": "J",
        "situacao": "A",
    }
    with BlingClient.from_env() as client:
        response = client.contatos.criar(payload)
        print(response)


if __name__ == "__main__":
    main()
