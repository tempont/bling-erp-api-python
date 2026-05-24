"""Example that lists products using the SDK resource API."""

from bling_erp_api import BlingClient


def main() -> None:
    """Fetch the first page of products."""
    with BlingClient.from_env() as client:
        response = client.products.list(limit=10)
        print(response)


if __name__ == "__main__":
    main()
