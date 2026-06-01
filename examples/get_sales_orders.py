"""Exemplo que lista pedidos de venda usando a API de recursos do SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.config import (
    DEFAULT_API_BASE_URL,
    DEFAULT_RATE_LIMIT_MAX_REQUESTS,
    DEFAULT_RATE_LIMIT_MAX_RETRIES,
    DEFAULT_RATE_LIMIT_PERIOD_SECONDS,
    DEFAULT_TIMEOUT_SECONDS,
)
from bling_erp_api.models.generated.sales_orders import (
    PedidosVendasGetResponse200,
    PedidosVendasIdPedidoVendaGetResponse200,
)

bling_client: BlingClient = BlingClient(
    base_url=DEFAULT_API_BASE_URL,
    timeout=DEFAULT_TIMEOUT_SECONDS,
    rate_limit_max_requests=DEFAULT_RATE_LIMIT_MAX_REQUESTS,
    rate_limit_period_seconds=DEFAULT_RATE_LIMIT_PERIOD_SECONDS,
    rate_limit_max_retries=DEFAULT_RATE_LIMIT_MAX_RETRIES,
)


def list_orders() -> None:
    """Busca a primeira página de pedidos de venda."""
    with bling_client as client:
        response = client.pedidos_vendas.listar()
        parsed = PedidosVendasGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


def order_details(id_pedido_venda: int) -> None:
    """Busca detalhes de um pedido de venda."""
    with BlingClient.from_env() as client:
        response = client.pedidos_vendas.obter(id_pedido_venda=id_pedido_venda)
        parsed = PedidosVendasIdPedidoVendaGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    # list_orders()
    # order_details(id_pedido_venda=1)
    print("Done.")
