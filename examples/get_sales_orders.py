"""Exemplo que lista pedidos de venda usando a API de recursos do SDK."""

import json
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


def list_orders() -> None:
    """Busca a primeira página de pedidos de venda."""
    with BlingClient.from_env() as client:
        response: JsonObject = client.pedidos_vendas.listar(
            pagina=1,
            limite=10,
        )
        print(json.dumps(obj=response, indent=2, ensure_ascii=False))


def order_details() -> None:
    """Busca detalhes de um pedido de venda."""
    with BlingClient.from_env() as client:
        response = client.pedidos_vendas.obter(id_pedido_venda=25903217773)
        print(json.dumps(obj=response, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    list_orders()
