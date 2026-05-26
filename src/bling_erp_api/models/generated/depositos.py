"""Pydantic models for Bling Depósitos endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class DepositosDadosDTO(BlingModel):
    """Deposit data (GET/POST/PUT /depositos)."""

    id: int | None = Field(default=None, description="ID do depósito (readOnly)")
    descricao: str = Field(..., description="Descrição do depósito")
    situacao: int = Field(..., description="0=Inativo, 1=Ativo")
    padrao: bool = Field(..., description="Depósito padrão")
    desconsiderar_saldo: bool = Field(..., alias="desconsiderarSaldo")
