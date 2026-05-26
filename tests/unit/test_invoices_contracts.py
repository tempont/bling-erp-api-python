"""Contract tests for invoice (NotasFiscais) operations."""

from bling_erp_api.contracts.generated.invoices import INVOICE_OPERATIONS


def test_invoice_operations_count() -> None:
    """The generated contracts should cover at least 20 operations."""
    assert len(INVOICE_OPERATIONS) >= 20, (
        f"Expected at least 20 invoice operations, got {len(INVOICE_OPERATIONS)}"
    )


def test_nfe_list_operation_present() -> None:
    """NF-e listar (GET /nfe) should be in the generated contracts."""
    assert "listar_nfe" in INVOICE_OPERATIONS, (
        f"Expected 'listar_nfe' in INVOICE_OPERATIONS, got keys: {list(INVOICE_OPERATIONS.keys())}"
    )
    op = INVOICE_OPERATIONS["listar_nfe"]
    assert op.method == "GET"
    assert op.path == "/nfe"


def test_nfe_create_operation_present() -> None:
    """NF-e criar (POST /nfe) should be in the generated contracts."""
    assert "criar_nfe" in INVOICE_OPERATIONS, (
        f"Expected 'criar_nfe' in INVOICE_OPERATIONS, got keys: {list(INVOICE_OPERATIONS.keys())}"
    )
    op = INVOICE_OPERATIONS["criar_nfe"]
    assert op.method == "POST"
    assert op.path == "/nfe"


def test_nfce_list_operation_present() -> None:
    """NFC-e listar (GET /nfce) should be in the generated contracts."""
    nfce_keys = [k for k, v in INVOICE_OPERATIONS.items() if v.path.startswith("/nfce")]
    assert len(nfce_keys) > 0, (
        f"No NFC-e operations found in INVOICE_OPERATIONS. Keys: {list(INVOICE_OPERATIONS.keys())}"
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
    """Verify key NF-e operations are generated (with suffixed keys)."""
    expected_actions = [
        "obter_id_nota_fiscal",
        "alterar_id_nota_fiscal",
        "remover_varios",
        "autorizar_enviar",
        "lancar_contas_lancar_contas",
        "estornar_contas_estornar_contas",
        "lancar_estoque_lancar_estoque",
        "estornar_estoque_estornar_estoque",
        "obter_documento_nota_fiscal",
    ]
    for action in expected_actions:
        assert action in INVOICE_OPERATIONS, (
            f"Expected NF-e action '{action}' in INVOICE_OPERATIONS, "
            f"got keys: {list(INVOICE_OPERATIONS.keys())}"
        )
