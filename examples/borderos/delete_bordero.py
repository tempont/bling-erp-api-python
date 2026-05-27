"""Example: Delete a bordero by ID."""

from bling_erp_api import BlingClient


def main() -> None:
    """Remove a bordero by ID (soft delete)."""
    # NOTE: DELETE returns 204 No Content (empty response). No response model needed.
    with BlingClient.from_env() as client:
        response = client.borderos.remover(123456)
        print(response)


if __name__ == "__main__":
    main()
