"""Exemplo que lista produtos usando a API de recursos do SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Busca a primeira página de produtos."""
    with BlingClient.from_env() as client:
        response = client.produtos.listar(limite=10, nome="Camiseta")
        print(response)


if __name__ == "__main__":
    main()
