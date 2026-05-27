"""Example: Get a single cash/bank entry by ID."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.caixas_bancos import CaixasBancosLancamentoDTO


def main() -> None:
    """Retrieve cash/bank entry details by ID."""
    with BlingClient.from_env() as client:
        response = client.caixas_bancos.obter(12345678)
        parsed = CaixasBancosLancamentoDTO(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
