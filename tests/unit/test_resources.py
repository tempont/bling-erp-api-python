"""Tests for resource request mapping."""

from __future__ import annotations

from datetime import UTC, date, datetime
from typing import TYPE_CHECKING

from bling_erp_api.models.generated.sales_orders import SalesOrderCreateRequest
from bling_erp_api.resources.contacts import ContactsResource
from bling_erp_api.resources.sales_orders import SalesOrdersResource

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, QueryParams


class RecordingTransport:
    """Transport test double that records the latest request."""

    def __init__(self) -> None:
        """Create an empty recorder."""
        self.calls: list[tuple[str, str, QueryParams | None, JsonObject | None]] = []

    def request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonObject | None = None,
    ) -> JsonObject:
        """Record a request and return a simple response."""
        self.calls.append((method, path, params, json))
        return {"data": []}


def test_contacts_list_maps_to_bling_endpoint() -> None:
    """Contacts listing should use the Portuguese Bling API path."""
    transport = RecordingTransport()
    resource = ContactsResource(transport)

    response = resource.list(page=2, limit=50, name="Ana")

    assert response == {"data": []}
    assert transport.calls == [
        ("GET", "/contatos", {"pagina": 2, "limite": 50, "name": "Ana"}, None)
    ]


def test_sales_orders_list_maps_to_bling_endpoint() -> None:
    """Sales order listing should use Portuguese SDK names and Bling query names."""
    transport = RecordingTransport()
    resource = SalesOrdersResource(transport)

    response = resource.listar(
        pagina=2,
        limite=50,
        id_contato=123,
        ids_situacoes=[1, 2],
        data_inicial=date(2024, 1, 1),
        data_alteracao_inicial=datetime(2024, 1, 2, 10, 30, 45, tzinfo=UTC),
        numeros_lojas=["WEB-1", "WEB-2"],
    )

    assert response == {"data": []}
    assert transport.calls == [
        (
            "GET",
            "/pedidos/vendas",
            {
                "pagina": 2,
                "limite": 50,
                "idContato": 123,
                "idsSituacoes[]": [1, 2],
                "dataInicial": "2024-01-01",
                "dataAlteracaoInicial": "2024-01-02 10:30:45",
                "numerosLojas[]": ["WEB-1", "WEB-2"],
            },
            None,
        )
    ]


def test_sales_orders_english_list_alias_still_maps_to_bling_endpoint() -> None:
    """English alias should keep compatibility while Portuguese is canonical."""
    transport = RecordingTransport()
    resource = SalesOrdersResource(transport)

    resource.list(page=2, limit=50, contact_id=123)

    assert transport.calls == [
        ("GET", "/pedidos/vendas", {"pagina": 2, "limite": 50, "idContato": 123}, None)
    ]


def test_sales_orders_create_serializes_model_with_api_aliases() -> None:
    """Sales order creation should serialize Pydantic payloads using Bling aliases."""
    transport = RecordingTransport()
    resource = SalesOrdersResource(transport)
    order = SalesOrderCreateRequest.model_validate(
        {
            "data": "2024-01-10",
            "dataSaida": "2024-01-10",
            "dataPrevista": "2024-01-12",
            "contato": {"id": 123, "nome": "Ana"},
            "itens": [
                {
                    "codigo": "SKU-1",
                    "quantidade": 2,
                    "valor": 10.5,
                    "descricao": "Produto",
                    "produto": {"id": 456},
                }
            ],
            "parcelas": [
                {
                    "dataVencimento": "2024-01-20",
                    "valor": 21,
                    "formaPagamento": {"id": 789},
                }
            ],
        }
    )

    response = resource.create(order)

    assert response == {"data": []}
    assert transport.calls == [
        (
            "POST",
            "/pedidos/vendas",
            None,
            {
                "data": "2024-01-10",
                "dataSaida": "2024-01-10",
                "dataPrevista": "2024-01-12",
                "contato": {"id": 123, "nome": "Ana"},
                "itens": [
                    {
                        "codigo": "SKU-1",
                        "quantidade": 2.0,
                        "valor": 10.5,
                        "descricao": "Produto",
                        "produto": {"id": 456},
                    }
                ],
                "parcelas": [
                    {
                        "dataVencimento": "2024-01-20",
                        "valor": 21.0,
                        "formaPagamento": {"id": 789},
                    }
                ],
            },
        )
    ]


def test_sales_orders_write_operations_map_to_bling_endpoints() -> None:
    """Sales order write operations should map to the expected Bling paths."""
    transport = RecordingTransport()
    resource = SalesOrdersResource(transport)

    resource.alterar(123, {"numeroLoja": "WEB-123"})
    resource.remover(123)
    resource.remover_varios([123, 456])
    resource.alterar_situacao(123, 9)

    assert transport.calls == [
        ("PUT", "/pedidos/vendas/123", None, {"numeroLoja": "WEB-123"}),
        ("DELETE", "/pedidos/vendas/123", None, None),
        ("DELETE", "/pedidos/vendas", {"idsPedidosVendas[]": [123, 456]}, None),
        ("PATCH", "/pedidos/vendas/123/situacoes/9", None, None),
    ]


def test_sales_orders_posting_operations_map_to_bling_endpoints() -> None:
    """Sales order post actions should map to their action endpoints."""
    transport = RecordingTransport()
    resource = SalesOrdersResource(transport)

    resource.lancar_estoque(123)
    resource.lancar_estoque(123, id_deposito=456)
    resource.estornar_estoque(123)
    resource.lancar_contas(123)
    resource.estornar_contas(123)
    resource.gerar_nota_fiscal(123)
    resource.gerar_nota_fiscal_consumidor(123)

    assert transport.calls == [
        ("POST", "/pedidos/vendas/123/lancar-estoque", None, None),
        ("POST", "/pedidos/vendas/123/lancar-estoque/456", None, None),
        ("POST", "/pedidos/vendas/123/estornar-estoque", None, None),
        ("POST", "/pedidos/vendas/123/lancar-contas", None, None),
        ("POST", "/pedidos/vendas/123/estornar-contas", None, None),
        ("POST", "/pedidos/vendas/123/gerar-nfe", None, None),
        ("POST", "/pedidos/vendas/123/gerar-nfce", None, None),
    ]
