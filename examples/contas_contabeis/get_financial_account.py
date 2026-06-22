"""Example: Get a financial account by ID."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contas_contabeis import (
        ContasContabeisIdContaContabilGetResponse200,
    )


def obter_conta(id_conta_contabil: int) -> ContasContabeisIdContaContabilGetResponse200:
    """Obtém uma conta contábil pelo ID."""
    with BlingClient.from_env() as client:
        return client.contas_contabeis.obter(id_conta_contabil=id_conta_contabil)


def main() -> None:
    """Run the example."""
    print(obter_conta(123456).model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
