"""Contract tests for purchase order (PedidosCompra) operations."""

from bling_erp_api.contracts.generated.purchase_orders import PURCHASE_ORDER_OPERATIONS


def test_purchase_order_operations_count() -> None:
    """The generated contracts should cover all purchase order operations."""
    assert len(PURCHASE_ORDER_OPERATIONS) == 10, (
        f"Expected 10 operations, got {len(PURCHASE_ORDER_OPERATIONS)}"
    )


def test_purchase_order_list_operation_present() -> None:
    """List operation should be present."""
    assert "listar" in PURCHASE_ORDER_OPERATIONS
    op = PURCHASE_ORDER_OPERATIONS["listar"]
    assert op.method == "GET"
    assert op.path == "/pedidos/compras"


def test_purchase_order_create_operation_present() -> None:
    """Create operation should be present."""
    assert "criar" in PURCHASE_ORDER_OPERATIONS
    op = PURCHASE_ORDER_OPERATIONS["criar"]
    assert op.method == "POST"
    assert op.path == "/pedidos/compras"


def test_purchase_order_operations_have_required_fields() -> None:
    """Every operation should have method and path."""
    for name, op in PURCHASE_ORDER_OPERATIONS.items():
        assert op.method, f"Operation '{name}' missing 'method'"
        assert op.path, f"Operation '{name}' missing 'path'"
        assert op.method in ("GET", "POST", "PUT", "DELETE", "PATCH"), (
            f"Operation '{name}' has invalid method: {op.method}"
        )


def test_key_purchase_order_operations_present() -> None:
    """Verify key purchase order operations are generated."""
    expected_actions = [
        "obter",
        "alterar",
        "remover",
        "alterar_situacao",
        "lancar_contas",
        "estornar_contas",
        "lancar_estoque",
        "estornar_estoque",
    ]
    for action in expected_actions:
        assert action in PURCHASE_ORDER_OPERATIONS, (
            f"Expected action '{action}' in PURCHASE_ORDER_OPERATIONS, "
            f"got keys: {list(PURCHASE_ORDER_OPERATIONS.keys())}"
        )
