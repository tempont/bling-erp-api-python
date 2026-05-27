"""Modelos para Naturezas de Operações."""

from bling_erp_api.models.base import BlingModel


class NaturezasOperacoesDadosDTO(BlingModel):
    """Dados de uma natureza de operação."""

    id: int | None = None
    situacao: int | None = None
    padrao: int | None = None
    descricao: str | None = None
