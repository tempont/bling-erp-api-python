"""Example: List all notifications for a period."""

from bling_erp_api import BlingClient


def main() -> None:
    """List notifications for January 2025."""
    with BlingClient.from_env() as client:
        response = client.notificacoes.listar(periodo="2025-01")
        print(response)


if __name__ == "__main__":
    main()
