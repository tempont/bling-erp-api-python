"""Exemplo que obtém um grupo de produtos pelo ID usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém um grupo de produtos pelo ID."""
    with BlingClient.from_env() as client:
        response = client.grupos_produtos.obter(100)
        print(response)


if __name__ == "__main__":
    main()
