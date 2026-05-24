"""Example script that fetches products from the Bling API."""

from bling_erp_api.auth.bling_client import get_client

ENDPOINT = "/Api/v3/produtos"


def get_example() -> None:
    """Perform a GET request against the products endpoint."""
    client = get_client()
    response = client.get(ENDPOINT)
    print(response.json())  # noqa: T201


if __name__ == "__main__":
    get_example()
