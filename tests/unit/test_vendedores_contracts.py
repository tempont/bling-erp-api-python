"""Contract tests for vendedores operations."""

from bling_erp_api.contracts.generated.vendedores import VENDEDOR_OPERATIONS


def test_vendedores_operations_count() -> None:
    """Vendedores contract should cover exactly 2 operations (listar, obter)."""
    assert len(VENDEDOR_OPERATIONS) == 2


def test_vendedores_list_operation_present() -> None:
    """Listar operation should map to GET /vendedores."""
    assert "listar" in VENDEDOR_OPERATIONS
    op = VENDEDOR_OPERATIONS["listar"]
    assert op.method == "GET"
    assert op.path == "/vendedores"


def test_vendedores_obter_operation_present() -> None:
    """Obter operation should map to GET /vendedores/{idVendedor}."""
    assert "obter" in VENDEDOR_OPERATIONS
    op = VENDEDOR_OPERATIONS["obter"]
    assert op.method == "GET"
    assert op.path == "/vendedores/{idVendedor}"


def test_vendedores_operations_have_required_fields() -> None:
    """Every Vendedores operation should have method and path."""
    for name, op in VENDEDOR_OPERATIONS.items():
        assert op.method, f"Operation '{name}' missing 'method'"
        assert op.path, f"Operation '{name}' missing 'path'"
