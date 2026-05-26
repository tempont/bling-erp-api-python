"""Exemplo que lista formas de pagamento usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista formas de pagamento ativas."""
    with BlingClient.from_env() as client:
        response = client.formas_pagamentos.listar(situacao=1)
        print(response)


if __name__ == "__main__":
    main()
