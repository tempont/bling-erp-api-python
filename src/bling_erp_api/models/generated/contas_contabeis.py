"""Pydantic models for Bling Contas Financeiras endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class ContasContabeisDadosDTO(BlingModel):
    """Financial account data (GET /contas-contabeis)."""

    id: int | None = Field(default=None, description="ID da conta financeira")
    descricao: str | None = Field(default=None, description="Descrição da conta financeira")
    tipo: str | None = Field(
        default=None, description="Tipo: banco, caixa, conta-bancaria, integracao-pagamento"
    )
    alias_integracao: str | None = Field(default=None, alias="aliasIntegracao")
