"""Pydantic models for Bling Estoques endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class EstoquesDepositoBaseDTO(BlingModel):
    """Deposit reference for stock."""

    id: int = Field(..., description="ID do depósito")


class EstoquesDepositoDTO(BlingModel):
    """Deposit with stock balances."""

    saldo_fisico: float | None = Field(
        default=None, alias="saldoFisico", description="Saldo físico do produto"
    )
    saldo_virtual: float | None = Field(
        default=None, alias="saldoVirtual", description="Saldo desconsiderando produtos reservados"
    )


class EstoquesProdutoDTO(BlingModel):
    """Product reference for stock."""

    id: int = Field(..., description="ID do produto")
    codigo: str | None = Field(default=None, description="Código do produto (readOnly)")


class EstoquesDadosBaseDTO(BlingModel):
    """Base stock entry data."""

    operacao: str = Field(..., description="B=Balanço, E=Entrada, S=Saída")
    preco: float | None = Field(default=None, description="Preço unitário")
    custo: float | None = Field(default=None, description="Custo unitário")
    quantidade: float = Field(...)
    observacoes: str | None = Field(default=None, description="Observações")


class EstoquesSalvarDTO(BlingModel):
    """Create payload for POST /estoques (allOf composition)."""

    produto: EstoquesProdutoDTO = Field(...)
    deposito: EstoquesDepositoBaseDTO = Field(...)
    operacao: str = Field(..., description="B=Balanço, E=Entrada, S=Saída")
    preco: float | None = Field(default=None)
    custo: float | None = Field(default=None)
    quantidade: float = Field(...)
    observacoes: str | None = Field(default=None)


class EstoquesSaldosBaseDTO(BlingModel):
    """Stock balance summary."""

    produto: EstoquesProdutoDTO | None = Field(default=None)
    saldo_fisico_total: float | None = Field(default=None, alias="saldoFisicoTotal")
    saldo_virtual_total: float | None = Field(default=None, alias="saldoVirtualTotal")
