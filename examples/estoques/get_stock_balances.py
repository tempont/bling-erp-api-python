"""Example: Get Stock Balances."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.estoques import EstoquesSaldosGetResponse200


def obter_saldos(
    ids_produtos: list[int],
) -> EstoquesSaldosGetResponse200:
    """Obtém saldos de estoque."""
    with BlingClient.from_env() as client:
        return client.estoques.obter_saldos(ids_produtos=ids_produtos)


def main() -> None:
    """Demonstrate obtaining stock balances."""
    result = obter_saldos([1, 2])
    print(result.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
