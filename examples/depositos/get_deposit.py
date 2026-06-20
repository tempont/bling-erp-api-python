"""Example: Get a deposit by ID.

Demonstrates how to retrieve a single deposit from the Bling deposits API.

Endpoint:
    - GET /depositos/{idDeposito}

Docs:
    - https://developer.bling.com.br/referencia#/Depositos/get_depositos__idDeposito_

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.depositos import (
        DepositosIdDepositoGetResponse200,
    )


def obter_deposito(id_deposito: int) -> DepositosIdDepositoGetResponse200:
    """Obtém um depósito pelo ID."""
    with BlingClient.from_env() as client:
        return client.depositos.obter(id_deposito=id_deposito)


def main() -> None:
    """Obtém e exibe um depósito."""
    print(obter_deposito(123).model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
