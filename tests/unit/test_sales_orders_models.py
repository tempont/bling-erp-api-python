"""Model tests for PedidosVendas (Sales Orders) models."""

import json
from pathlib import Path
from typing import cast

from bling_erp_api.models.generated.sales_orders import (
    PedidosVendasGetResponse200,
    PedidosVendasIdPedidoVendaGetResponse200,
    PedidosVendasPostRequest,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def _load_fixture(name: str) -> dict[str, object]:
    return json.loads((FIXTURES_DIR / name).read_text())


class TestSalesOrdersListResponse:
    """Tests for the sales order list response model (PedidosVendasGetResponse200)."""

    def test_deserialize_sales_orders_list(self) -> None:
        """Should deserialize list fixture with two items."""
        data = _load_fixture("sales_order_list.json")
        response = PedidosVendasGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        assert len(response.data) == 2
        item = response.data[0]
        assert item.id == 12345678
        assert item.numero == 42
        assert item.total == 23.5
        assert item.contato is not None
        assert item.contato.nome == "Cliente Teste"

    def test_deserialize_sales_orders_list_contato(self) -> None:
        """Should deserialize contato sub-object with aliased fields."""
        data = _load_fixture("sales_order_list.json")
        response = PedidosVendasGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        contato = response.data[0].contato
        assert contato.id == 87654321
        assert contato.tipo_pessoa == "J"
        assert contato.numero_documento == "30188025000121"

    def test_deserialize_sales_orders_list_situacao(self) -> None:
        """Should deserialize situacao sub-object."""
        data = _load_fixture("sales_order_list.json")
        response = PedidosVendasGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        situacao = response.data[0].situacao
        assert situacao is not None
        assert situacao.id == 111
        assert situacao.valor == 1

    def test_deserialize_sales_orders_list_itens(self) -> None:
        """Itens are extra fields on VendasDadosBaseDTO; accessed as dict."""
        data = _load_fixture("sales_order_list.json")
        response = PedidosVendasGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        # itens is an extra field (not on VendasDadosBaseDTO), accessed via __getattr__
        itens = cast("list[dict[str, object]]", response.data[0].itens)  # pyright: ignore[reportAttributeAccessIssue]
        assert len(itens) == 1
        assert itens[0]["codigo"] == "SKU-1"
        assert itens[0]["quantidade"] == 2

    def test_deserialize_sales_orders_list_extra_allowed(self) -> None:
        """Extra fields should be preserved."""
        data = _load_fixture("sales_order_list.json")
        response = PedidosVendasGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        # pyright doesn't know about extra fields on Pydantic models with extra="allow"
        assert getattr(response.data[0], "campoNovoBling", None) == "mantido"  # pyright: ignore[reportAttributeAccessIssue]


class TestSalesOrdersGetResponse:
    """Tests for the sales order detail response model (PedidosVendasIdPedidoVendaGetResponse200)."""

    def test_deserialize_sales_orders_get(self) -> None:
        """Should deserialize get fixture with base and detail fields."""
        data = _load_fixture("sales_orders_get.json")
        response = PedidosVendasIdPedidoVendaGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        item = response.data
        assert item is not None
        assert item.id == 12345678
        assert item.numero == 42
        assert item.total == 23.5

    def test_deserialize_sales_orders_get_itens(self) -> None:
        """Get response itens are typed VendasItemDTO instances."""
        data = _load_fixture("sales_orders_get.json")
        response = PedidosVendasIdPedidoVendaGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        item = response.data
        assert item is not None
        assert item.itens is not None
        assert len(item.itens) == 1
        assert item.itens[0].codigo == "SKU-1"
        assert item.itens[0].quantidade == 2.0

    def test_deserialize_sales_orders_get_ids_present(self) -> None:
        """Itens and parcelas with ids keep parsing them (Bug 7 regression guard)."""
        data = _load_fixture("sales_orders_get.json")
        response = PedidosVendasIdPedidoVendaGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        item = response.data
        assert item is not None
        assert item.itens is not None
        assert item.itens[0].id == 333
        assert item.parcelas is not None
        assert item.parcelas[0].id == 555


class TestSalesOrdersGetMinimalResponse:
    """Tests for minimal sales order detail payloads (Bug 7 class)."""

    def test_deserialize_sales_orders_get_minimal(self) -> None:
        """Detail fixture without item/parcela ids should parse with id=None."""
        data = _load_fixture("sales_order_get_minimal.json")
        response = PedidosVendasIdPedidoVendaGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        item = response.data
        assert item is not None
        assert item.id == 12345678
        assert item.data is not None
        assert item.data_saida is not None
        assert item.data_prevista is not None
        assert item.situacao is not None
        assert item.situacao.id == 111

    def test_deserialize_sales_orders_get_minimal_itens_without_id(self) -> None:
        """Minimal itens without id/codigo/produto/desconto/aliquotaIPI parse with None."""
        data = _load_fixture("sales_order_get_minimal.json")
        response = PedidosVendasIdPedidoVendaGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        item = response.data
        assert item is not None
        assert item.itens is not None
        assert len(item.itens) == 1
        pedido_item = item.itens[0]
        assert pedido_item.id is None
        assert pedido_item.codigo is None
        assert pedido_item.produto is None
        assert pedido_item.desconto is None
        assert pedido_item.aliquota_ipi is None
        assert pedido_item.quantidade == 2.0
        assert pedido_item.valor == 10.5
        assert pedido_item.descricao == "Produto Teste"

    def test_deserialize_sales_orders_get_minimal_parcelas_without_id(self) -> None:
        """Minimal parcelas without id parse with id=None."""
        data = _load_fixture("sales_order_get_minimal.json")
        response = PedidosVendasIdPedidoVendaGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        item = response.data
        assert item is not None
        assert item.parcelas is not None
        assert len(item.parcelas) == 1
        parcela = item.parcelas[0]
        assert parcela.id is None
        assert parcela.data_vencimento is not None
        assert parcela.valor == 23.5
        assert parcela.forma_pagamento.id == 666


class TestSalesOrdersRequestModels:
    """Tests for sales order request models (PedidosVendasPostRequest)."""

    def test_post_request_accepts_snake_case(self) -> None:
        """Should construct PedidosVendasPostRequest with snake_case fields."""
        model = PedidosVendasPostRequest.model_validate(  # type: ignore[reportUnknownMemberType]
            {
                "data": "2024-01-01",
                "data_saida": "2024-01-01",
                "data_prevista": "2024-01-05",
                "contato": {"id": 1, "nome": "Cliente"},
                "itens": [
                    {
                        "id": 1,
                        "codigo": "P1",
                        "descricao": "Produto",
                        "quantidade": 1,
                        "valor": 10.0,
                    }
                ],
                "parcelas": [
                    {
                        "id": 1,
                        "dataVencimento": "2024-01-01",
                        "valor": 10.0,
                        "formaPagamento": {"id": 1},
                    }
                ],
                "desconto": {"valor": 0, "unidade": "REAL"},
            }
        )
        assert model.contato is not None
        assert model.contato.id == 1
        assert model.contato.nome == "Cliente"
        assert len(model.itens) == 1
        assert model.itens[0].codigo == "P1"
