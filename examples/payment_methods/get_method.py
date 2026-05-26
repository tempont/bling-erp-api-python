"""Exemplo que obtém uma forma de pagamento pelo ID usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém uma forma de pagamento pelo ID."""
    with BlingClient.from_env() as client:
        response = client.formas_pagamentos.obter(10)
        print(response)


if __name__ == "__main__":
    main()
