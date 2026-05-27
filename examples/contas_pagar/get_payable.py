"""Exemplo que obtém uma conta a pagar pelo ID usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contas_pagar import ContasPagarIdContaPagarGetResponse200


def main() -> None:
    """Obtém uma conta a pagar pelo ID."""
    with BlingClient.from_env() as client:
        response = client.contas_pagar.obter(123456)
        parsed = ContasPagarIdContaPagarGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
