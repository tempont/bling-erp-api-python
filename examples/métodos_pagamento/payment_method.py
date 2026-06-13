"""Example: Payment Method Operations.

Demonstrates CRUD operations on payment methods through the Bling payment methods API.

Endpoints:
    - GET /formas-pagamentos
    - GET /formas-pagamentos/{idFormaPagamento}
    - POST /formas-pagamentos
    - PUT /formas-pagamentos/{idFormaPagamento}
    - DELETE /formas-pagamentos/{idFormaPagamento}
    - PATCH /formas-pagamentos/{idFormaPagamento}/situacao
    - PATCH /formas-pagamentos/{idFormaPagamento}/padrao

Docs:
    - https://developer.bling.com.br/referencia#/Formas%20de%20Pagamento

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.payment_methods import (
        FormasPagamentosGetResponse200,
        FormasPagamentosIdFormaPagamentoGetResponse200,
        FormasPagamentosIdFormaPagamentoPutRequest,
        FormasPagamentosIdFormaPagamentoPutResponse200,
        FormasPagamentosPostRequest,
        FormasPagamentosPostResponse201,
    )

## ---------------------------------------------------------------------------
## LIST PAYMENT METHODS
## ---------------------------------------------------------------------------


def listar_formas_pagamento(
    *,
    pagina: int = 1,
    limite: int = 100,
    situacao: int | None = None,
    tipos_pagamentos: list[int] | None = None,
) -> FormasPagamentosGetResponse200:
    """Lista formas de pagamento com filtros opcionais."""
    with BlingClient.from_env() as client:
        return client.formas_pagamentos.listar(
            pagina=pagina,
            limite=limite,
            situacao=situacao,
            tipos_pagamentos=tipos_pagamentos,
        )


## ---------------------------------------------------------------------------
## GET A PAYMENT METHOD BY ID
## ---------------------------------------------------------------------------


def obter_forma_pagamento(
    id_forma_pagamento: int,
) -> FormasPagamentosIdFormaPagamentoGetResponse200:
    """Obtém uma forma de pagamento pelo ID."""
    with BlingClient.from_env() as client:
        return client.formas_pagamentos.obter(id_forma_pagamento=id_forma_pagamento)


## ---------------------------------------------------------------------------
## CREATE A PAYMENT METHOD
## ---------------------------------------------------------------------------


def criar_forma_pagamento(
    dados: FormasPagamentosPostRequest,
) -> FormasPagamentosPostResponse201:
    """Cria uma nova forma de pagamento."""
    client = BlingClient.from_env()
    return client.formas_pagamentos.criar(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE A PAYMENT METHOD (PUT)
## ---------------------------------------------------------------------------


def alterar_forma_pagamento(
    id_forma_pagamento: int,
    dados: FormasPagamentosIdFormaPagamentoPutRequest,
) -> FormasPagamentosIdFormaPagamentoPutResponse200:
    """Atualiza uma forma de pagamento por completo (PUT)."""
    with BlingClient.from_env() as client:
        return client.formas_pagamentos.alterar(id_forma_pagamento=id_forma_pagamento, dados=dados)


## ---------------------------------------------------------------------------
## DELETE A PAYMENT METHOD
## ---------------------------------------------------------------------------


def remover_forma_pagamento(id_forma_pagamento: int) -> None:
    """Remove uma forma de pagamento pelo ID."""
    with BlingClient.from_env() as client:
        client.formas_pagamentos.remover(id_forma_pagamento=id_forma_pagamento)


## ---------------------------------------------------------------------------
## CHANGE PAYMENT METHOD STATUS
## ---------------------------------------------------------------------------


def alterar_situacao_forma_pagamento(id_forma_pagamento: int, situacao: int) -> None:
    """Altera a situação de uma forma de pagamento."""
    with BlingClient.from_env() as client:
        client.formas_pagamentos.alterar_situacao(
            id_forma_pagamento=id_forma_pagamento, situacao=situacao
        )


## ---------------------------------------------------------------------------
## SET DEFAULT PAYMENT METHOD
## ---------------------------------------------------------------------------


def alterar_padrao_forma_pagamento(id_forma_pagamento: int, padrao: int) -> None:
    """Define se a forma de pagamento é padrão."""
    with BlingClient.from_env() as client:
        client.formas_pagamentos.alterar_padrao(
            id_forma_pagamento=id_forma_pagamento, padrao=padrao
        )


def main() -> None:
    """Demonstrate payment method operations."""
    payment_method_id = 10  # Exemplo — substitua pelo ID real.

    # Read operations
    result = listar_formas_pagamento(pagina=1, limite=5, situacao=1)
    print(result.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    result = obter_forma_pagamento(payment_method_id)
    print(result.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Write operations (commented out to avoid side effects)
    # payload = FormasPagamentosPostRequest(
    #     descricao="Cartão de Crédito Exemplo",
    #     tipo_pagamento=1,
    #     situacao=1,
    #     fixa=False,
    #     padrao=False,
    #     finalidade=1,
    # )
    # result = criar_forma_pagamento(payload)
    # print(result.model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    #
    # update_payload = FormasPagamentosIdFormaPagamentoPutRequest(
    #     descricao="Cartão de Crédito Atualizado",
    #     tipo_pagamento=1,
    #     situacao=1,
    #     fixa=False,
    #     padrao=False,
    #     finalidade=1,
    # )
    # result = alterar_forma_pagamento(payment_method_id, update_payload)
    # print(result.model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    #
    # alterar_situacao_forma_pagamento(payment_method_id, situacao=0)
    # time.sleep(1)
    #
    # alterar_padrao_forma_pagamento(payment_method_id, padrao=1)
    # time.sleep(1)
    #
    # remover_forma_pagamento(payment_method_id)
    # time.sleep(1)


if __name__ == "__main__":
    main()
