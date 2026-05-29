"""Model tests for PedidosCompras (Purchase Orders) models."""

import json
from pathlib import Path

from bling_erp_api.models.generated.purchase_orders import (
    PedidosComprasGetResponse200,
    PedidosComprasIdPedidoCompraGetResponse200,
    PedidosComprasPostRequest,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def _load_fixture(name: str) -> dict[str, object]:
    return json.loads((FIXTURES_DIR / name).read_text())


class TestPurchaseOrdersListResponse:
    """Tests for the purchase orders list response model (PedidosComprasGetResponse200)."""

    def test_deserialize_purchase_orders_list(self) -> None:
        """Should deserialize list fixture with two items."""
        data = _load_fixture("purchase_orders_list.json")
        response = PedidosComprasGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        assert len(response.data) == 2
        item = response.data[0]
        assert item.id == 1001
        assert item.numero == 55
        assert item.total == 1650.0
        assert item.fornecedor is not None
        assert item.fornecedor.id == 500

    def test_deserialize_purchase_orders_list_situacao(self) -> None:
        """Should deserialize situacao sub-object."""
        data = _load_fixture("purchase_orders_list.json")
        response = PedidosComprasGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        situacao = response.data[0].situacao
        assert situacao is not None
        assert situacao.id == 1
        assert situacao.valor == 0

    def test_deserialize_purchase_orders_list_extra_allowed(self) -> None:
        """Extra fields (campoNovoBling) should be preserved."""
        data = _load_fixture("purchase_orders_list.json")
        response = PedidosComprasGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        # pyright doesn't know about extra fields on Pydantic models with extra="allow"
        assert getattr(response.data[0], "campoNovoBling", None) == "mantido"  # pyright: ignore[reportAttributeAccessIssue]


class TestPurchaseOrdersGetResponse:
    """Tests for the purchase order detail response model (PedidosComprasIdPedidoCompraGetResponse200)."""

    def test_deserialize_purchase_orders_get(self) -> None:
        """Should deserialize get fixture with base and detail fields."""
        data = _load_fixture("purchase_orders_get.json")
        response = PedidosComprasIdPedidoCompraGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        item = response.data
        assert item is not None
        assert item.id == 1001
        assert item.numero == 55
        assert item.total == 1650.0
        assert item.ordem_compra == "OC-2024-001"
        assert item.observacoes == "Pedido urgente"

    def test_deserialize_purchase_orders_get_itens(self) -> None:
        """Should deserialize itens as typed PedidosComprasItemDTO instances."""
        data = _load_fixture("purchase_orders_get.json")
        response = PedidosComprasIdPedidoCompraGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        item = response.data
        assert item is not None
        itens = item.itens
        assert len(itens) == 1
        assert itens[0].descricao == "Matéria-prima A"
        assert itens[0].valor == 750.0
        assert itens[0].produto is not None
        assert itens[0].produto.id == 200

    def test_deserialize_purchase_orders_get_parcelas(self) -> None:
        """Should deserialize parcelas as typed PedidosComprasParcelaDTO instances."""
        data = _load_fixture("purchase_orders_get.json")
        response = PedidosComprasIdPedidoCompraGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        item = response.data
        assert item is not None
        parcelas = item.parcelas
        assert parcelas is not None
        assert len(parcelas) == 1
        assert parcelas[0].valor == 1650.0
        assert parcelas[0].data_vencimento is not None


class TestPurchaseOrdersRequestModels:
    """Tests for purchase order request models (PedidosComprasPostRequest)."""

    def test_post_request_accepts_fields(self) -> None:
        """Should construct PedidosComprasPostRequest with snake_case fields."""
        model = PedidosComprasPostRequest.model_validate(  # type: ignore[reportUnknownMemberType]
            {
                "fornecedor": {"id": 500},
                "itens": [{"descricao": "Item A", "valor": 100.0}],
                "parcelas": [
                    {
                        "dataVencimento": "2024-04-01",
                        "valor": 100.0,
                        "formaPagamento": {"id": 1},
                    }
                ],
            }
        )
        assert model.fornecedor is not None
        assert model.fornecedor.id == 500
        assert len(model.itens) == 1
        assert model.itens[0].descricao == "Item A"
