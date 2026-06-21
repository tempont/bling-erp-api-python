"""Example: Get a single receivable.

Endpoint: GET /contas-receber/{idContaReceber}
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contas_receber import (
        ContasReceberIdContaReceberGetResponse200,
    )


def obter_conta(
    id_conta_receber: int,
) -> ContasReceberIdContaReceberGetResponse200:
    """Obtém uma conta a receber pelo ID."""
    with BlingClient.from_env() as client:
        return client.contas_receber.obter(
            id_conta_receber=id_conta_receber,
        )


def main() -> None:
    """Demonstrate single receivable operations."""
    conta_id = 123456
    print(obter_conta(conta_id).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
