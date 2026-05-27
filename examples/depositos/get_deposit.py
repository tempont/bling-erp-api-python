"""Exemplo que obtém um depósito pelo ID usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.depositos import DepositosIdDepositoGetResponse200


def main() -> None:
    """Obtém um depósito pelo ID."""
    with BlingClient.from_env() as client:
        response = client.depositos.obter(123)
        parsed = DepositosIdDepositoGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
