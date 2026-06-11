"""Example: Production Orders (Ordens de Produção) Workflow Examples.

Demonstrates CRUD and status operations for production orders through the Bling API.

Endpoints:
    - GET /ordens-producao
    - POST /ordens-producao
    - GET /ordens-producao/{idOrdemProducao}
    - PUT /ordens-producao/{idOrdemProducao}
    - DELETE /ordens-producao/{idOrdemProducao}
    - PUT /ordens-producao/{idOrdemProducao}/situacoes
    - POST /ordens-producao/gerar-sob-demanda

Docs:
    - https://developer.bling.com.br/referencia#/Ordens%20de%20Produ%C3%A7%C3%A3o/get_ordens_producao
    - https://developer.bling.com.br/referencia#/Ordens%20de%20Produ%C3%A7%C3%A3o/post_ordens_producao
    - https://developer.bling.com.br/referencia#/Ordens%20de%20Produ%C3%A7%C3%A3o/get_ordens_producao__idOrdemProducao_
    - https://developer.bling.com.br/referencia#/Ordens%20de%20Produ%C3%A7%C3%A3o/put_ordens_producao__idOrdemProducao_
    - https://developer.bling.com.br/referencia#/Ordens%20de%20Produ%C3%A7%C3%A3o/delete_ordens_producao__idOrdemProducao_
    - https://developer.bling.com.br/referencia#/Ordens%20de%20Produ%C3%A7%C3%A3o/put_ordens_producao__idOrdemProducao__situacoes
    - https://developer.bling.com.br/referencia#/Ordens%20de%20Produ%C3%A7%C3%A3o/post_ordens_producao_gerar_sob_demanda

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.ordens_producao import (
    OrdensProducaoGerarSobDemandaPostResponse201,
    OrdensProducaoGetResponse200,
    OrdensProducaoIdOrdemProducaoGetResponse200,
    OrdensProducaoPostResponse201,
)

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject

## ---------------------------------------------------------------------------
## LIST PRODUCTION ORDERS
## ---------------------------------------------------------------------------


def list_production_orders(
    status_ids: list[int] | None = None,
) -> OrdensProducaoGetResponse200:
    """List production orders, optionally filtered by status IDs."""
    with BlingClient.from_env() as client:
        response = client.ordens_producao.listar(
            ids_situacoes=status_ids,
            limite=10,
        )
        return OrdensProducaoGetResponse200.model_validate(response)


## ---------------------------------------------------------------------------
## GET SINGLE PRODUCTION ORDER
## ---------------------------------------------------------------------------


def get_production_order(
    order_id: int,
) -> OrdensProducaoIdOrdemProducaoGetResponse200:
    """Get a single production order by ID."""
    with BlingClient.from_env() as client:
        response = client.ordens_producao.obter(id_ordem_producao=order_id)
        return OrdensProducaoIdOrdemProducaoGetResponse200.model_validate(response)


## ---------------------------------------------------------------------------
## CREATE PRODUCTION ORDER
## ---------------------------------------------------------------------------


def create_production_order(
    payload: JsonObject,
) -> OrdensProducaoPostResponse201:
    """Create a new production order."""
    with BlingClient.from_env() as client:
        response = client.ordens_producao.criar(dados=payload)
        return OrdensProducaoPostResponse201.model_validate(response)


## ---------------------------------------------------------------------------
## UPDATE PRODUCTION ORDER
## ---------------------------------------------------------------------------


def update_production_order(order_id: int, payload: JsonObject) -> None:
    """Update an existing production order."""
    with BlingClient.from_env() as client:
        client.ordens_producao.alterar(
            id_ordem_producao=order_id,
            dados=payload,
        )


## ---------------------------------------------------------------------------
## DELETE PRODUCTION ORDER
## ---------------------------------------------------------------------------


def delete_production_order(order_id: int) -> None:
    """Delete a production order by ID."""
    with BlingClient.from_env() as client:
        client.ordens_producao.remover(id_ordem_producao=order_id)


## ---------------------------------------------------------------------------
## UPDATE PRODUCTION ORDER STATUS
## ---------------------------------------------------------------------------


def update_production_order_status(order_id: int, status_id: int) -> None:
    """Update the status (situacao) of a production order."""
    with BlingClient.from_env() as client:
        client.ordens_producao.alterar_situacao(
            id_ordem_producao=order_id,
            dados={"idSituacao": status_id},
        )


## ---------------------------------------------------------------------------
## GENERATE PRODUCTION ORDERS ON DEMAND
## ---------------------------------------------------------------------------


def generate_production_orders_on_demand() -> OrdensProducaoGerarSobDemandaPostResponse201:
    """Generate production orders automatically based on minimum stock levels."""
    with BlingClient.from_env() as client:
        response = client.ordens_producao.criar_multiplos()
        return OrdensProducaoGerarSobDemandaPostResponse201.model_validate(response)


def main() -> None:
    """Demonstrate production order operations."""
    order_id = 12345  # Exemplo — substitua pelo ID real.

    # List orders
    print("=== List production orders ===")
    response = list_production_orders(status_ids=[1])
    print(response.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Get single order
    print("=== Get single production order ===")
    response = get_production_order(order_id)
    print(response.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Create order
    print("=== Create production order ===")
    payload: JsonObject = {
        "numero": 1001,
        "deposito": {"idOrigem": 10, "idDestino": 20},
        "itens": [{"produto": {"id": 100}, "quantidade": 10.0}],
    }
    response = create_production_order(payload)
    print(response.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Update order
    print("=== Update production order ===")
    update_production_order(order_id, {"numero": 1002})
    print("Updated.")
    time.sleep(1)

    # Update status
    print("=== Update production order status ===")
    update_production_order_status(order_id, status_id=2)
    print("Status updated.")
    time.sleep(1)

    # Generate on demand
    print("=== Generate production orders on demand ===")
    response = generate_production_orders_on_demand()
    print(response.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Delete (commented out for safety)
    # print("=== Delete production order ===")
    # delete_production_order(order_id)
    # print("Deleted.")


if __name__ == "__main__":
    main()
