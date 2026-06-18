"""Example: Get Stock Balances by Deposit.

Endpoint:
    - GET /estoques/saldos/{idDeposito}

Docs:
    - https://developer.bling.com.br/referencia#/Estoques/get_estoques_saldos__idDeposito_

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.estoques import (
        EstoquesSaldosIdDepositoGetResponse200,
    )


def obter_saldos_por_deposito(
    id_deposito: int,
    ids_produtos: list[int],
) -> EstoquesSaldosIdDepositoGetResponse200:
    """Obtém saldos de estoque por depósito."""
    with BlingClient.from_env() as client:
        return client.estoques.obter_saldos_por_deposito(id_deposito, ids_produtos=ids_produtos)


def main() -> None:
    """Run the example."""
    result = obter_saldos_por_deposito(1, [1])
    print(result.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
