"""Testes de contrato OpenAPI para Notificações."""

from bling_erp_api.contracts.generated.notificacoes import (
    NOTIFICACOES_OPERATIONS,
)


def test_cover_all_notificacoes_operations() -> None:
    """Verifica que todas as operações de Notificações estão cobertas."""
    operations = NOTIFICACOES_OPERATIONS
    assert len(operations) == 3


def test_no_extra_notificacoes_operations() -> None:
    """Verifica que não há operações extras no contrato."""
    actions = {op.action for op in NOTIFICACOES_OPERATIONS.values()}
    assert "ObterMultiplos" in actions
    assert "Alterar" in actions
