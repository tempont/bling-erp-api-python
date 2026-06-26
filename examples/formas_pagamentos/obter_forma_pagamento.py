"""Example: Get a single payment method (Formas de Pagamentos).

Endpoint:
    - GET /formas-pagamentos/{idFormaPagamento}

Docs:
    - https://developer.bling.com.br/referencia#/Formas%20de%20Pagamentos/get_formas_pagamentos__idFormaPagamento_

"""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.payment_methods import (
    FormasPagamentosIdFormaPagamentoGetResponse200,
)


def main() -> None:
    """Obtém uma forma de pagamento pelo ID."""
    with BlingClient.from_env() as client:
        response = client.formas_pagamentos.obter(id_forma_pagamento=12345)
        parsed = FormasPagamentosIdFormaPagamentoGetResponse200.model_validate(response)
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
