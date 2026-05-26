"""Exemplo que obtém um depósito pelo ID usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém um depósito pelo ID."""
    with BlingClient.from_env() as client:
        response = client.depositos.obter(123)
        print(response)


if __name__ == "__main__":
    main()
