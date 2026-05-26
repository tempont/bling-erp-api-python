"""Example: Get a single product category."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve a product category by ID."""
    with BlingClient.from_env() as client:
        response = client.product_categories.obter(123456)
        print(response)


if __name__ == "__main__":
    main()
