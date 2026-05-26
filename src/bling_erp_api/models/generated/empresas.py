"""Pydantic models for Bling Empresas endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class EmpresasDadosBasicosDTO(BlingModel):
    """Basic company data (GET /empresas/me/dados-basicos)."""

    id: str | None = Field(default=None, description="ID da empresa")
    nome: str | None = Field(default=None, description="Nome da empresa")
    cnpj: str | None = Field(default=None, description="CNPJ da empresa")
    email: str | None = Field(default=None, description="Email da empresa")
    data_contrato: str | None = Field(
        default=None, alias="dataContrato", description="Data de início do contrato"
    )
