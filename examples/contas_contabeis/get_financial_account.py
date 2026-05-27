"""Exemplo que obtém uma conta financeira pelo ID usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contas_contabeis import (
    ContasContabeisIdContaContabilGetResponse200,
)


def main() -> None:
    """Obtém uma conta financeira pelo ID."""
    with BlingClient.from_env() as client:
        response = client.contas_contabeis.obter(123456)
        parsed = ContasContabeisIdContaContabilGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
