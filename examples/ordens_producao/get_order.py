"""Example: Get a single production order by ID."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve production order details by ID."""
    with BlingClient.from_env() as client:
        response = client.ordens_producao.obter(12345678)
        print(response)


if __name__ == "__main__":
    main()
