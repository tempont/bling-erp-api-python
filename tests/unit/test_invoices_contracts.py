"""Contract tests for NF-e (NotasFiscais) operations."""

from bling_erp_api.contracts.generated.invoices import INVOICE_OPERATIONS
from bling_erp_api.contracts.generated.nfce import NFCE_OPERATIONS


def test_invoice_operations_count() -> None:
    """NF-e generated contracts should cover at least 10 operations."""
    assert len(INVOICE_OPERATIONS) >= 10, (
        f"Expected at least 10 NF-e operations, got {len(INVOICE_OPERATIONS)}"
    )


def test_nfe_list_operation_present() -> None:
    """NF-e listar (GET /nfe) should be in the generated contracts."""
    assert "listar" in INVOICE_OPERATIONS, (
        f"Expected 'listar' in INVOICE_OPERATIONS, got keys: {list(INVOICE_OPERATIONS.keys())}"
    )
    op = INVOICE_OPERATIONS["listar"]
    assert op.method == "GET"
    assert op.path == "/nfe"


def test_nfe_create_operation_present() -> None:
    """NF-e criar (POST /nfe) should be in the generated contracts."""
    assert "criar" in INVOICE_OPERATIONS, (
        f"Expected 'criar' in INVOICE_OPERATIONS, got keys: {list(INVOICE_OPERATIONS.keys())}"
    )
    op = INVOICE_OPERATIONS["criar"]
    assert op.method == "POST"
    assert op.path == "/nfe"


def test_nfce_contracts_generated() -> None:
    """NFC-e should have its own generated contract module."""
    assert len(NFCE_OPERATIONS) >= 5, (
        f"Expected at least 5 NFC-e operations, got {len(NFCE_OPERATIONS)}"
    )


def test_invoice_operations_have_required_fields() -> None:
    """Every operation should have method and path."""
    for name, op in INVOICE_OPERATIONS.items():
        assert op.method, f"Operation '{name}' missing 'method'"
        assert op.path, f"Operation '{name}' missing 'path'"
        assert op.method in ("GET", "POST", "PUT", "DELETE", "PATCH"), (
            f"Operation '{name}' has invalid method: {op.method}"
        )


def test_key_nfe_operations_present() -> None:
    """Verify key NF-e operations are generated (clean keys after NF-e/NFC-e split)."""
    expected_actions = [
        "listar",
        "criar",
        "obter",
        "alterar",
        "remover_varios",
        "obter_documento_nota_fiscal",
        "autorizar",
        "lancar_contas",
        "estornar_contas",
        "lancar_estoque",
        "estornar_estoque",
    ]
    for action in expected_actions:
        assert action in INVOICE_OPERATIONS, (
            f"Expected NF-e action '{action}' in INVOICE_OPERATIONS, "
            f"got keys: {list(INVOICE_OPERATIONS.keys())}"
        )
