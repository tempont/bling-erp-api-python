"""Example: List payment methods (Formas de Pagamentos).

Endpoints:
    - GET /formas-pagamentos

Docs:
    - https://developer.bling.com.br/referencia#/Formas%20de%20Pagamentos/get_formas_pagamentos

"""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.payment_methods import FormasPagamentosGetResponse200


def main() -> None:
    """Lista formas de pagamentos paginadas."""
    with BlingClient.from_env() as client:
        response = client.formas_pagamentos.listar(limite=10)
        parsed = FormasPagamentosGetResponse200.model_validate(response)
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
