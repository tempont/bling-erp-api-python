"""Exemplo que lista depósitos usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista depósitos com situação 'Ativo'."""
    with BlingClient.from_env() as client:
        response = client.depositos.listar(situacao=1)
        print(response)


if __name__ == "__main__":
    main()
