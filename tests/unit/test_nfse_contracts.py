"""Contract tests for NFS-e (NFSe) operations."""

from bling_erp_api.contracts.generated.nfse import NFSE_OPERATIONS


def test_nfse_operations_count() -> None:
    """The generated contracts should cover all 8 NFSe operations."""
    assert len(NFSE_OPERATIONS) == 8, f"Expected 8 NFSe operations, got {len(NFSE_OPERATIONS)}"


def test_nfse_list_operation_present() -> None:
    """NFS-e listar (GET /nfse) should be in the generated contracts."""
    assert "listar" in NFSE_OPERATIONS
    op = NFSE_OPERATIONS["listar"]
    assert op.method == "GET"
    assert op.path == "/nfse"


def test_nfse_create_operation_present() -> None:
    """NFS-e criar (POST /nfse) should be in the generated contracts."""
    assert "criar" in NFSE_OPERATIONS
    op = NFSE_OPERATIONS["criar"]
    assert op.method == "POST"
    assert op.path == "/nfse"


def test_nfse_operations_have_required_fields() -> None:
    """Every operation should have method and path."""
    for name, op in NFSE_OPERATIONS.items():
        assert op.method, f"Operation '{name}' missing 'method'"
        assert op.path, f"Operation '{name}' missing 'path'"


def test_key_nfse_operations_present() -> None:
    """Verify key NFSe operations are generated."""
    expected_actions = [
        "obter",
        "remover",
        "autorizar",
        "cancelar",
        "obter_configuracoes",
        "alterar_configuracoes",
    ]
    for action in expected_actions:
        assert action in NFSE_OPERATIONS, (
            f"Expected NFSe action '{action}' in NFSE_OPERATIONS, "
            f"got keys: {list(NFSE_OPERATIONS.keys())}"
        )
