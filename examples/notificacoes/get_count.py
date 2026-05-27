"""Example: Get notification count for a period."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve the number of notifications for the current year."""
    with BlingClient.from_env() as client:
        response = client.notificacoes.obter_quantidade()
        print(response)


if __name__ == "__main__":
    main()
