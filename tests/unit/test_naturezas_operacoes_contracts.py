"""Testes de contrato OpenAPI para Naturezas de Operações."""

from bling_erp_api.contracts.generated.naturezas_operacoes import (
    NATUREZAS_OPERACOES_OPERATIONS,
)


def test_cover_all_naturezas_operacoes_operations():
    """Todas as operações em NATUREZAS_OPERACOES_OPERATIONS devem corresponder ao OpenAPI."""
    operations = NATUREZAS_OPERACOES_OPERATIONS
    assert len(operations) == 2
    assert operations["listar"].action == "ObterMultiplos"
    assert operations["obter_tributacao"].action == "ObterTributacao"


def test_no_extra_operations():
    """Garante que não há operações extras no contrato."""
    actions = {op.action for op in NATUREZAS_OPERACOES_OPERATIONS.values()}
    assert actions == {"ObterMultiplos", "ObterTributacao"}
