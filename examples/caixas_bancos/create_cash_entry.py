"""Example: Create a new cash/bank entry."""

from bling_erp_api import BlingClient
from bling_erp_api.types import JsonObject


def main() -> None:
    """Create a new cash/bank entry (credit)."""
    payload: JsonObject = {
        "data": "2025-02-01",
        "valor": 350.00,
        "debCred": "C",
        "competencia": "2025-02-01",
        "observacoes": "Venda balcão",
        "contaFinanceira": {"id": 1},
        "categoria": {"id": 10},
    }
    with BlingClient.from_env() as client:
        response = client.caixas_bancos.criar(payload)
        print(response)


if __name__ == "__main__":
    main()
