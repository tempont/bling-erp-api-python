"""Example: Get a single logistics entry by ID."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve logistics details by ID."""
    with BlingClient.from_env() as client:
        response = client.logisticas.obter(101)
        print(response)


if __name__ == "__main__":
    main()
