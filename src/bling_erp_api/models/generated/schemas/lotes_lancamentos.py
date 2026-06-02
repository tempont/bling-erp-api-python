# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``lotes_lancamentos``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

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
    id_lote: int = Field(
        ...,
        validation_alias=AliasChoices("id_lote", "idLote"),
        examples=[12345678],
        serialization_alias="idLote",
    )
    quantidade: int | None = Field(default=None, examples=[12345678])
    tipo_lancamento: int | None = Field(
        default=None,
        validation_alias=AliasChoices("tipo_lancamento", "tipoLancamento"),
        examples=["1"],
        serialization_alias="tipoLancamento",
    )
    data: str | None = Field(default=None, examples=["2021-01-01 00:00:00"])
    id_origem: int | None = Field(
        default=None,
        validation_alias=AliasChoices("id_origem", "idOrigem"),
        examples=[12345678],
        serialization_alias="idOrigem",
    )
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

    id_lote: int | None = Field(
        default=None,
        validation_alias=AliasChoices("id_lote", "idLote"),
        examples=[12345678],
        serialization_alias="idLote",
    )
    produto: LotesProdutoDTO | None = None
    deposito: LotesDepositoDTO | None = None
    saldo_atual: float | None = Field(
        default=None,
        validation_alias=AliasChoices("saldo_atual", "saldoAtual"),
        examples=[12345678.12],
        serialization_alias="saldoAtual",
    )


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
    saldo_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("saldo_total", "saldoTotal"),
        examples=[12345678.12],
        serialization_alias="saldoTotal",
    )


class SaldoSomaLotesTodosDepositosDTO(BlingModel):
    """OpenAPI schema ``SaldoSomaLotesTodosDepositosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        produto: Bling ``produto``; type ``LotesProdutoDTO | None``; opcional.
        saldo_total: Bling ``saldoTotal``; type ``float | None``; opcional. Soma dos saldos de lotes"""

    produto: LotesProdutoDTO | None = None
    saldo_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("saldo_total", "saldoTotal"),
        examples=[12345678.12],
        serialization_alias="saldoTotal",
    )


__all__ = [
    "LoteLancamentoDTO",
    "LoteLancamentoObservacaoDTO",
    "SaldoLoteDTO",
    "SaldoSomaLotesDTO",
    "SaldoSomaLotesTodosDepositosDTO",
]
