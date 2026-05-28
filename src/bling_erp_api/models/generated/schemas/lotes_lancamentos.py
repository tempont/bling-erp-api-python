# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``lotes_lancamentos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .lotes import LotesDepositoDTO, LotesProdutoDTO


class LoteLancamentoDTO(BlingModel):
    """OpenAPI schema ``LoteLancamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do lancamento do lote
        id_lote: Bling ``idLote``; type ``int``; obrigatório. ID do lote
        quantidade: Bling ``quantidade``; type ``int | None``; opcional. Quantidade do lote
        tipo_lancamento: Bling ``tipoLancamento``; type ``int | None``; opcional. Tipo de lançamento <br> `1` Entrada <br> `2` Saída <br> `3` Balanço
        data: Bling ``data``; type ``str | None``; opcional. Data de lançamento
        id_origem: Bling ``idOrigem``; type ``int | None``; opcional. ID da origem
        observacao: Bling ``observacao``; type ``str``; obrigatório. Observação do lote"""

    id: int | None = Field(default=None, examples=[12345678])
    id_lote: int = Field(..., alias="idLote", examples=[12345678])
    quantidade: int | None = Field(default=None, examples=[12345678])
    tipo_lancamento: int | None = Field(default=None, alias="tipoLancamento", examples=["1"])
    data: str | None = Field(default=None, examples=["2021-01-01 00:00:00"])
    id_origem: int | None = Field(default=None, alias="idOrigem", examples=[12345678])
    observacao: str = Field(..., examples=["Observação do lote"])


class LoteLancamentoObservacaoDTO(BlingModel):
    """OpenAPI schema ``LoteLancamentoObservacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        observacao: Bling ``observacao``; type ``str``; obrigatório. Observação do lote"""

    observacao: str = Field(..., examples=["Observação do lote"])


class SaldoLoteDTO(BlingModel):
    """OpenAPI schema ``SaldoLoteDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id_lote: Bling ``idLote``; type ``int | None``; opcional. ID do lote
        produto: Bling ``produto``; type ``LotesProdutoDTO | None``; opcional.
        deposito: Bling ``deposito``; type ``LotesDepositoDTO | None``; opcional.
        saldo_atual: Bling ``saldoAtual``; type ``float | None``; opcional. Saldo atual do lote"""

    id_lote: int | None = Field(default=None, alias="idLote", examples=[12345678])
    produto: LotesProdutoDTO | None = None
    deposito: LotesDepositoDTO | None = None
    saldo_atual: float | None = Field(default=None, alias="saldoAtual", examples=[12345678.12])


class SaldoSomaLotesDTO(BlingModel):
    """OpenAPI schema ``SaldoSomaLotesDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        produto: Bling ``produto``; type ``LotesProdutoDTO | None``; opcional.
        deposito: Bling ``deposito``; type ``LotesDepositoDTO | None``; opcional.
        saldo_total: Bling ``saldoTotal``; type ``float | None``; opcional. Soma dos saldos de lotes"""

    produto: LotesProdutoDTO | None = None
    deposito: LotesDepositoDTO | None = None
    saldo_total: float | None = Field(default=None, alias="saldoTotal", examples=[12345678.12])


class SaldoSomaLotesTodosDepositosDTO(BlingModel):
    """OpenAPI schema ``SaldoSomaLotesTodosDepositosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        produto: Bling ``produto``; type ``LotesProdutoDTO | None``; opcional.
        saldo_total: Bling ``saldoTotal``; type ``float | None``; opcional. Soma dos saldos de lotes"""

    produto: LotesProdutoDTO | None = None
    saldo_total: float | None = Field(default=None, alias="saldoTotal", examples=[12345678.12])


__all__ = [
    "LoteLancamentoDTO",
    "LoteLancamentoObservacaoDTO",
    "SaldoLoteDTO",
    "SaldoSomaLotesDTO",
    "SaldoSomaLotesTodosDepositosDTO",
]
