"""Exemplo que obtém uma forma de pagamento pelo ID usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.payment_methods import (
    FormasPagamentosIdFormaPagamentoGetResponse200,
)


def main() -> None:
    """Obtém uma forma de pagamento pelo ID."""
    with BlingClient.from_env() as client:
        response = client.formas_pagamentos.obter(10)
        parsed = FormasPagamentosIdFormaPagamentoGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
