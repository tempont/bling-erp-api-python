"""Example: List all logistics services."""

from bling_erp_api import BlingClient


def main() -> None:
    """List logistics services with default pagination."""
    with BlingClient.from_env() as client:
        response = client.logisticas_servicos.listar()
        print(response)


if __name__ == "__main__":
    main()
