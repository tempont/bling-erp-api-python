"""Example: Get a Single Account Payable.

Demonstrates fetching a single conta a pagar by ID with the typed Bling API SDK.

Endpoint:
    - GET /contas-pagar/{idContaPagar}

Docs:
    - https://developer.bling.com.br/referencia#/Contas%20a%20Pagar/get_contas_pagar__idContaPagar_
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contas_pagar import (
        ContasPagarIdContaPagarGetResponse200,
    )


def obter_conta_pagar(id_conta_pagar: int) -> ContasPagarIdContaPagarGetResponse200:
    """ObtÃ©m uma conta a pagar pelo ID.

    Endpoint: GET /contas-pagar/{idContaPagar}

    ObtÃ©m uma conta a pagar pelo ID.

    Args:
        id_conta_pagar: ID da conta a pagar (Bling: ``idContaPagar``, integer, obrigatÃ³rio)

    Returns:
        Bling API response. Response schemas: 200: ContasPagarDadosDTO; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.contas_pagar.obter(id_conta_pagar=id_conta_pagar)


def main() -> None:
    """Demonstrate fetching a single account payable."""
    conta_id = 123456  # Substitua pelo ID real.
    result = obter_conta_pagar(conta_id)
    print(result.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
