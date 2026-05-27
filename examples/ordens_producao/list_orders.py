"""Example: List production orders filtered by status."""

from bling_erp_api import BlingClient


def main() -> None:
    """List open production orders."""
    with BlingClient.from_env() as client:
        response = client.ordens_producao.listar(ids_situacoes=[1])
        print(response)


if __name__ == "__main__":
    main()
