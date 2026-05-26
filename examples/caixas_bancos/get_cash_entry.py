"""Example: Get a single cash/bank entry by ID."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve cash/bank entry details by ID."""
    with BlingClient.from_env() as client:
        response = client.caixas_bancos.obter(12345678)
        print(response)


if __name__ == "__main__":
    main()
