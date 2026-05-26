"""Exemplo que obtém uma conta a receber pelo ID usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém uma conta a receber pelo ID."""
    with BlingClient.from_env() as client:
        response = client.contas_receber.obter(123456)
        print(response)


if __name__ == "__main__":
    main()
