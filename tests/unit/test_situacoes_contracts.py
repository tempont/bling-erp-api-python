"""Contract tests for situation-related operations."""

from bling_erp_api.contracts.generated.situacoes import SITUATION_OPERATIONS
from bling_erp_api.contracts.generated.situacoes_modulos import (
    SITUATION_MODULE_OPERATIONS,
)
from bling_erp_api.contracts.generated.situacoes_transicoes import (
    SITUATION_TRANSITION_OPERATIONS,
)


def test_situation_operations_count() -> None:
    """Situacoes contract should cover exactly 4 operations (criar, obter, alterar, remover)."""
    assert len(SITUATION_OPERATIONS) == 4


def test_situation_module_operations_count() -> None:
    """SituacoesModulos contract should cover exactly 4 operations."""
    assert len(SITUATION_MODULE_OPERATIONS) == 4


def test_situation_transition_operations_count() -> None:
    """SituacoesTransicoes contract should cover exactly 4 operations."""
    assert len(SITUATION_TRANSITION_OPERATIONS) == 4


def test_situation_operations_have_required_fields() -> None:
    """Every Situacoes operation should have method and path."""
    for name, op in SITUATION_OPERATIONS.items():
        assert op.method, f"Operation '{name}' missing 'method'"
        assert op.path, f"Operation '{name}' missing 'path'"


def test_module_operations_have_required_fields() -> None:
    """Every SituacoesModulos operation should have method and path."""
    for name, op in SITUATION_MODULE_OPERATIONS.items():
        assert op.method, f"Operation '{name}' missing 'method'"
        assert op.path, f"Operation '{name}' missing 'path'"


def test_transition_operations_have_required_fields() -> None:
    """Every SituacoesTransicoes operation should have method and path."""
    for name, op in SITUATION_TRANSITION_OPERATIONS.items():
        assert op.method, f"Operation '{name}' missing 'method'"
        assert op.path, f"Operation '{name}' missing 'path'"


def test_situation_listar_not_present() -> None:
    """Situacoes resource does NOT have a list endpoint."""
    assert "listar" not in SITUATION_OPERATIONS


def test_key_module_operations_present() -> None:
    """SituacoesModulos contract should contain listar, obter, listar_acoes, listar_transicoes."""
    for action in ["listar", "obter", "listar_acoes", "listar_transicoes"]:
        assert action in SITUATION_MODULE_OPERATIONS


def test_key_transition_operations_present() -> None:
    """SituacoesTransicoes contract should contain criar, obter, alterar, remover."""
    for action in ["criar", "obter", "alterar", "remover"]:
        assert action in SITUATION_TRANSITION_OPERATIONS
