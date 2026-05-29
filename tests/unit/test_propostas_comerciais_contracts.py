"""Contract tests for commercial proposal (PropostasComerciais) operations."""

from bling_erp_api.contracts.generated.propostas_comerciais import COMMERCIAL_PROPOSAL_OPERATIONS


def test_commercial_proposal_operations_count() -> None:
    """The generated contracts should cover all commercial proposal operations."""
    assert len(COMMERCIAL_PROPOSAL_OPERATIONS) == 7, (
        f"Expected 7 operations, got {len(COMMERCIAL_PROPOSAL_OPERATIONS)}"
    )


def test_commercial_proposal_list_operation_present() -> None:
    """List operation should be present."""
    assert "listar" in COMMERCIAL_PROPOSAL_OPERATIONS
    op = COMMERCIAL_PROPOSAL_OPERATIONS["listar"]
    assert op.method == "GET"
    assert op.path == "/propostas-comerciais"


def test_commercial_proposal_create_operation_present() -> None:
    """Create operation should be present."""
    assert "criar" in COMMERCIAL_PROPOSAL_OPERATIONS
    op = COMMERCIAL_PROPOSAL_OPERATIONS["criar"]
    assert op.method == "POST"
    assert op.path == "/propostas-comerciais"


def test_commercial_proposal_operations_have_required_fields() -> None:
    """Every operation should have method and path."""
    for name, op in COMMERCIAL_PROPOSAL_OPERATIONS.items():
        assert op.method, f"Operation '{name}' missing 'method'"
        assert op.path, f"Operation '{name}' missing 'path'"
        assert op.method in ("GET", "POST", "PUT", "DELETE", "PATCH"), (
            f"Operation '{name}' has invalid method: {op.method}"
        )


def test_key_commercial_proposal_operations_present() -> None:
    """Verify key commercial proposal operations are generated."""
    expected_actions = [
        "obter",
        "alterar",
        "remover",
        "remover_varios",
        "alterar_situacao",
    ]
    for action in expected_actions:
        assert action in COMMERCIAL_PROPOSAL_OPERATIONS, (
            f"Expected action '{action}' in COMMERCIAL_PROPOSAL_OPERATIONS, "
            f"got keys: {list(COMMERCIAL_PROPOSAL_OPERATIONS.keys())}"
        )
