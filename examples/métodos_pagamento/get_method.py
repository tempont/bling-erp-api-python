"""Example: Get a Payment Method by ID.

Endpoints:
    - GET /formas-pagamentos/{idFormaPagamento}

Docs:
    - https://developer.bling.com.br/referencia#/Formas%20de%20Pagamento/get_formas_pagamentos__idFormaPagamento_

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.payment_methods import (
        FormasPagamentosIdFormaPagamentoGetResponse200,
    )


def obter_forma_pagamento(payment_method_id: int) -> FormasPagamentosIdFormaPagamentoGetResponse200:
    """Obtém uma forma de pagamento pelo ID.

    Endpoint: GET /formas-pagamentos/{idFormaPagamento}

    Obtém uma forma de pagamento pelo ID.

    Args:
        payment_method_id: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: FormasPagamentosDadosBaseDTO, FormasPagamentosDadosDTO; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.formas_pagamentos.obter(id_forma_pagamento=payment_method_id)


def main() -> None:
    """Demonstrate getting a payment method by ID."""
    payment_method_id = 10  # Exemplo — substitua pelo ID real.
    print(obter_forma_pagamento(payment_method_id).model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
