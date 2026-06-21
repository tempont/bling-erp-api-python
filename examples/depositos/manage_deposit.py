"""Example: Deposit Write Operations.

Demonstrates create and update operations on deposits through the Bling deposits API.

Endpoints:
    - POST /depositos
    - PUT /depositos/{idDeposito}

Docs:
    - https://developer.bling.com.br/referencia#/Dep%C3%B3sitos

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.depositos import (
        DepositosDadosDTO,
        DepositosIdDepositoGetResponse200,
        DepositosIdDepositoPutResponse200,
        DepositosPostResponse201,
    )


## ---------------------------------------------------------------------------
## GET A DEPOSIT BY ID
## ---------------------------------------------------------------------------


def obter_deposito(id_deposito: int) -> DepositosIdDepositoGetResponse200:
    """Obtém um depósito pelo ID."""
    with BlingClient.from_env() as client:
        return client.depositos.obter(id_deposito=id_deposito)


## ---------------------------------------------------------------------------
## CREATE A DEPOSIT
## ---------------------------------------------------------------------------


def criar_deposito(dados: DepositosDadosDTO) -> DepositosPostResponse201:
    """Cria um novo depósito."""
    with BlingClient.from_env() as client:
        return client.depositos.criar(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE A DEPOSIT (PUT)
## ---------------------------------------------------------------------------


def alterar_deposito(
    id_deposito: int,
    dados: DepositosDadosDTO,
) -> DepositosIdDepositoPutResponse200:
    """Atualiza um depósito por completo (PUT)."""
    with BlingClient.from_env() as client:
        return client.depositos.alterar(id_deposito=id_deposito, dados=dados)


def main() -> None:
    """Demonstrate deposit write operations."""
    deposit_id = 123456789  # Exemplo — substitua pelo ID real.

    # Read operations
    print(obter_deposito(deposit_id).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Write operations (commented out to avoid side effects)
    # dados_criar = DepositosDadosDTO(
    #     descricao="Depósito Teste",
    #     situacao=1,
    #     padrao=False,
    #     desconsiderar_saldo=False,
    # )
    # resultado = criar_deposito(dados_criar)
    # print(resultado.model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)

    # dados_alterar = DepositosDadosDTO(
    #     descricao="Depósito Alterado",
    #     situacao=1,
    #     padrao=False,
    #     desconsiderar_saldo=False,
    # )
    # resultado = alterar_deposito(deposit_id, dados_alterar)
    # print(resultado.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
