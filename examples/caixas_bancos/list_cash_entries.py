"""Example: List cash/bank entries with date filters."""

from bling_erp_api import BlingClient


def main() -> None:
    """List cash/bank entries filtered by date range and reconciliation status."""
    with BlingClient.from_env() as client:
        response = client.caixas_bancos.listar(
            data_inicial="2024-01-01",
            data_final="2024-12-31",
            situacao_conciliacao=1,
            situacao="R",
        )
        print(response)


if __name__ == "__main__":
    main()
