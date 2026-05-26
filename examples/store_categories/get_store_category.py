"""Example: Get a single store category binding."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve a store category binding by ID."""
    with BlingClient.from_env() as client:
        response = client.store_categories.obter(123456)
        print(response)


if __name__ == "__main__":
    main()
