"""Exemplo que lista contas a pagar usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista contas a pagar com situação 'Em aberto'."""
    with BlingClient.from_env() as client:
        response = client.contas_pagar.listar(situacao=1)
        print(response)


if __name__ == "__main__":
    main()
