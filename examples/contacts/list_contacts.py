"""Exemplo que lista contatos usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista a primeira página de contatos."""
    with BlingClient.from_env() as client:
        response = client.contatos.listar(pesquisa="Ana", limite=10)
        print(response)


if __name__ == "__main__":
    main()
