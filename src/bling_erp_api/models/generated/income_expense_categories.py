"""Pydantic models for Bling Categorias - Receitas e Despesas endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class CategoriasReceitasDespesasDadosBaseDTO(BlingModel):
    """Base category data (GET list response)."""

    id: int | None = Field(default=None, description="ID da categoria (readOnly)")
    id_categoria_pai: int | None = Field(
        default=None, alias="idCategoriaPai", description="ID da categoria pai (0 = raiz)"
    )
    descricao: str = Field(..., description="Descrição da categoria")
    tipo: int = Field(..., description="1=Despesa, 2=Receita, 3=Receita e despesa")


class CategoriasReceitasDespesasDadosDTO(BlingModel):
    """Extended category data with status (single-item GET response)."""

    id: int | None = Field(default=None, description="ID da categoria")
    id_categoria_pai: int | None = Field(default=None, alias="idCategoriaPai")
    descricao: str | None = Field(default=None, description="Descrição")
    tipo: int | None = Field(default=None, description="1=Despesa, 2=Receita, 3=Receita e despesa")
    situacao: int | None = Field(default=None, description="0=Inativa, 1=Ativa")


class CategoriasReceitasDespesasDadosPostDTO(BlingModel):
    """Create/update payload (POST/PUT /categorias/receitas-despesas).

    The Bling spec uses allOf with CategoriasReceitasDespesasDadosBaseDTO.
    We model as a combined DTO with all fields from both schemas.
    """

    id: int | None = Field(default=None, description="ID da categoria")
    id_categoria_pai: int | None = Field(
        default=None, alias="idCategoriaPai", description="ID da categoria pai (0 = raiz)"
    )
    descricao: str = Field(..., description="Descrição da categoria")
    tipo: int = Field(..., description="1=Despesa, 2=Receita, 3=Receita e despesa")
    grupo_dre: int | None = Field(
        default=None,
        alias="grupoDRE",
        description="Grupo DRE: 1=Não exibir, 2=Receita Op. Bruta, 3=Deduções, 7=Desp. Operacionais, 8=Receita Financeira, 9=Despesa Financeira, 10=Outras Receitas, 11=Outras Despesas, 13=IR e CSLL",
    )
