"""Example: List Accounts Payable.

Demonstrates listing contas a pagar with the typed Bling API SDK.

Endpoint:
    - GET /contas-pagar

Docs:
    - https://developer.bling.com.br/referencia#/Contas%20a%20Pagar/get_contas_pagar
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contas_pagar import (
        ContasPagarGetResponse200,
    )


def listar_contas_pagar(situacao: int = 1) -> ContasPagarGetResponse200:
    """Lista contas a pagar.

    Endpoint: GET /contas-pagar

    Lista contas a pagar filtradas por situação.

    Args:
        situacao: Situação da conta (Bling: ``situacao``, integer, opcional)

    Returns:
        Bling API response. Response schemas: 200: ContasDadosBaseDTO
    """
    with BlingClient.from_env() as client:
        return client.contas_pagar.listar(situacao=situacao)


def main() -> None:
    """Demonstrate listing accounts payable."""
    result = listar_contas_pagar(situacao=1)
    print(result.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
