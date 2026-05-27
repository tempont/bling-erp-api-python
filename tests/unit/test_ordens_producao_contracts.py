"""Testes de contrato OpenAPI para Ordens de Produção."""

from bling_erp_api.contracts.generated.ordens_producao import (
    ORDENS_PRODUCAO_OPERATIONS,
)


def test_cover_all_ordens_producao_operations() -> None:
    """Verifica que todas as operações de Ordens de Produção estão cobertas."""
    operations = ORDENS_PRODUCAO_OPERATIONS
    assert len(operations) == 7


def test_no_extra_ordens_producao_operations() -> None:
    """Verifica que não há operações extras no contrato."""
    actions = {op.action for op in ORDENS_PRODUCAO_OPERATIONS.values()}
    expected = {
        "ObterAcaoMultiplos",
        "Criar",
        "Obter",
        "Alterar",
        "Remover",
        "AlterarSituacao",
        "CriarMultiplos",
    }
    assert actions == expected
