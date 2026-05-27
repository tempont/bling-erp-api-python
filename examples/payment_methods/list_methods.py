"""Exemplo que lista formas de pagamento usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.payment_methods import FormasPagamentosGetResponse200


def main() -> None:
    """Lista formas de pagamento ativas."""
    with BlingClient.from_env() as client:
        response = client.formas_pagamentos.listar(situacao=1)
        parsed = FormasPagamentosGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
