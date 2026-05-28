# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``caixas_bancos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .contas_financeiras import ContasFinanceirasDadosBasicosDTO


class CaixasBancosDadosBasicoContatoDTO(BlingModel):
    """OpenAPI schema ``CaixasBancosDadosBasicoContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str | None``; opcional.
        cnpj: Bling ``cnpj``; type ``str | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    nome: str | None = Field(default=None, examples=["Pedro Silva"])
    cnpj: str | None = Field(default=None, examples=["30188025000121"])


class CaixasBancosDadosBasicosCategoriaDTO(BlingModel):
    """OpenAPI schema ``CaixasBancosDadosBasicosCategoriaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    descricao: str | None = Field(default=None, examples=["Vendas"])


class CaixasBancosDadosBasicosOrigemDTO(BlingModel):
    """OpenAPI schema ``CaixasBancosDadosBasicosOrigemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        tipo: Bling ``tipo``; type ``str | None``; opcional. Tipo da origem do lançamento <br> 'caixa' para lançamento de caixas e bancos <br> 'duplicata' para contas a receber/pagar <br> 'bordero' para pagamento/recebimento <br> 'estoque'..."""

    id: int | None = Field(default=None, examples=[12345678])
    tipo: str | None = Field(default=None, examples=["bordero"])


class CaixasBancosLancamentoConciliacaoMovimentacaoDTO(BlingModel):
    """OpenAPI schema ``CaixasBancosLancamentoConciliacaoMovimentacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Id da conciliação da movimentação"""

    id: int | None = Field(default=None, examples=[12345678])


class CaixasBancosLancamentoParcelaDTO(BlingModel):
    """OpenAPI schema ``CaixasBancosLancamentoParcelaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Id da parcela do lançamento"""

    id: int | None = Field(default=None, examples=[12345678])


class CaixasBancosSalvarLancamentoResponseDTO(BlingModel):
    """OpenAPI schema ``CaixasBancosSalvarLancamentoResponseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do lançamento criado"""

    id: int | None = Field(default=None, examples=[12345678])


class CaixasBancosItemLancamentoDTO(BlingModel):
    """OpenAPI schema ``CaixasBancosItemLancamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``str | None``; opcional. ID do lançamento de caixas e bancos
        deb_cred: Bling ``debCred``; type ``str | None``; opcional. Débito ou crédito
        situacao: Bling ``situacao``; type ``str | None``; opcional. Situação
        valor: Bling ``valor``; type ``float | None``; opcional. Valor
        data: Bling ``data``; type ``str | None``; opcional. Data
        observacoes: Bling ``observacoes``; type ``str | None``; opcional. Observações
        descricao: Bling ``descricao``; type ``str | None``; opcional. Descrição
        origem: Bling ``origem``; type ``CaixasBancosDadosBasicosOrigemDTO | None``; opcional.
        contato: Bling ``contato``; type ``CaixasBancosDadosBasicoContatoDTO | None``; opcional.
        conta_financeira: Bling ``contaFinanceira``; type ``ContasFinanceirasDadosBasicosDTO | None``; opcional."""

    id: str | None = Field(default=None, examples=["1234567"])
    deb_cred: str | None = Field(
        default=None,
        validation_alias=AliasChoices("deb_cred", "debCred"),
        examples=["D"],
        serialization_alias="debCred",
    )
    situacao: str | None = Field(default=None, examples=["R"])
    valor: float | None = Field(default=None, examples=[100])
    data: str | None = Field(default=None, examples=["2025-01-01"])
    observacoes: str | None = Field(default=None, examples=["Observações do lançamento"])
    descricao: str | None = Field(default=None, examples=["Descrição do lançamento"])
    origem: CaixasBancosDadosBasicosOrigemDTO | None = None
    contato: CaixasBancosDadosBasicoContatoDTO | None = None
    conta_financeira: ContasFinanceirasDadosBasicosDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("conta_financeira", "contaFinanceira"),
        serialization_alias="contaFinanceira",
    )


class CaixasBancosLancamentoDTO(BlingModel):
    """OpenAPI schema ``CaixasBancosLancamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Id do lançamento
        deb_cred: Bling ``debCred``; type ``str | None``; opcional. Tipo de lançamento <br> `D` - Débito <br> `C` - Crédito
        saldo: Bling ``saldo``; type ``str | None``; opcional. É ajuste de saldo após o lançamento <br> `S` - Sim <br> `N` - Não
        situacao: Bling ``situacao``; type ``str | None``; opcional. Situação do lançamento <br> `R` - Registrado <br> `E` - Excluído <br> `H` - Escondido <br> `N` - Não registrado <br> `P` - Processando (externa) <br> `C` - Cancelado (externa)
        transferencia: Bling ``transferencia``; type ``str | None``; opcional. Indica se o lançamento é uma transferência <br> `1` - Sim <br> `0` - Não
        tipo_lancamento: Bling ``tipoLancamento``; type ``str | None``; opcional. Tipo do lançamento <br> `1` - Débito <br> `2` - Crédito
        data: Bling ``data``; type ``date | None``; opcional. Data do lançamento
        competencia: Bling ``competencia``; type ``date | None``; opcional. Data de competência do lançamento
        valor: Bling ``valor``; type ``float | None``; opcional. Valor do lançamento
        observacoes: Bling ``observacoes``; type ``str | None``; opcional. Observações adicionais sobre o lançamento
        parcela: Bling ``parcela``; type ``CaixasBancosLancamentoParcelaDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``CaixasBancosDadosBasicosCategoriaDTO | None``; opcional.
        conciliacao_movimentacao: Bling ``conciliacaoMovimentacao``; type ``CaixasBancosLancamentoConciliacaoMovimentacaoDTO | None``; opcional.
        contato: Bling ``contato``; type ``CaixasBancosDadosBasicoContatoDTO | None``; opcional.
        origem: Bling ``origem``; type ``CaixasBancosDadosBasicosOrigemDTO | None``; opcional.
        conta_financeira: Bling ``contaFinanceira``; type ``ContasFinanceirasDadosBasicosDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    deb_cred: str | None = Field(
        default=None,
        validation_alias=AliasChoices("deb_cred", "debCred"),
        examples=["D"],
        serialization_alias="debCred",
    )
    saldo: str | None = Field(default=None, examples=["S"])
    situacao: str | None = Field(default=None, examples=["R"])
    transferencia: str | None = Field(default=None, examples=["1"])
    tipo_lancamento: str | None = Field(
        default=None,
        validation_alias=AliasChoices("tipo_lancamento", "tipoLancamento"),
        examples=["1"],
        serialization_alias="tipoLancamento",
    )
    data: date | None = Field(default=None, examples=["2025-01-01"])
    competencia: date | None = Field(default=None, examples=["2025-01-01"])
    valor: float | None = Field(default=None, examples=[100])
    observacoes: str | None = Field(default=None, examples=["Observações"])
    parcela: CaixasBancosLancamentoParcelaDTO | None = None
    categoria: CaixasBancosDadosBasicosCategoriaDTO | None = None
    conciliacao_movimentacao: CaixasBancosLancamentoConciliacaoMovimentacaoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("conciliacao_movimentacao", "conciliacaoMovimentacao"),
        serialization_alias="conciliacaoMovimentacao",
    )
    contato: CaixasBancosDadosBasicoContatoDTO | None = None
    origem: CaixasBancosDadosBasicosOrigemDTO | None = None
    conta_financeira: ContasFinanceirasDadosBasicosDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("conta_financeira", "contaFinanceira"),
        serialization_alias="contaFinanceira",
    )


class CaixasBancosSalvarLancamentoDTO(BlingModel):
    """OpenAPI schema ``CaixasBancosSalvarLancamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do lançamento (deve corresponder ao ID da URL)
        data: Bling ``data``; type ``date``; obrigatório. Data do lançamento
        valor: Bling ``valor``; type ``float``; obrigatório. Valor do lançamento
        deb_cred: Bling ``debCred``; type ``str``; obrigatório. Tipo de lançamento: <br> `C` - Crédito <br> `D` - Débito
        competencia: Bling ``competencia``; type ``date``; obrigatório. Data de competência
        observacoes: Bling ``observacoes``; type ``str``; obrigatório. Observações do lançamento
        transferencia: Bling ``transferencia``; type ``str | None``; opcional. Indica se é uma transferência
        conta_financeira: Bling ``contaFinanceira``; type ``ContasFinanceirasDadosBasicosDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``CaixasBancosDadosBasicosCategoriaDTO | None``; opcional.
        origem: Bling ``origem``; type ``CaixasBancosDadosBasicosOrigemDTO | None``; opcional.
        contato: Bling ``contato``; type ``CaixasBancosDadosBasicoContatoDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    data: date = Field(..., examples=["2025-01-01"])
    valor: float = Field(..., examples=["123.00"])
    deb_cred: str = Field(
        ...,
        validation_alias=AliasChoices("deb_cred", "debCred"),
        examples=["C"],
        serialization_alias="debCred",
    )
    competencia: date = Field(..., examples=["2025-01-01"])
    observacoes: str = Field(..., examples=["Lançamento atualizado"])
    transferencia: str | None = Field(default=None, examples=[""])
    conta_financeira: ContasFinanceirasDadosBasicosDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("conta_financeira", "contaFinanceira"),
        serialization_alias="contaFinanceira",
    )
    categoria: CaixasBancosDadosBasicosCategoriaDTO | None = None
    origem: CaixasBancosDadosBasicosOrigemDTO | None = None
    contato: CaixasBancosDadosBasicoContatoDTO | None = None


class CaixasGetResponse200(BlingModel):
    """OpenAPI schema ``CaixasGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[CaixasBancosItemLancamentoDTO] | None``; opcional."""

    data: list[CaixasBancosItemLancamentoDTO] | None = None


__all__ = [
    "CaixasBancosDadosBasicoContatoDTO",
    "CaixasBancosDadosBasicosCategoriaDTO",
    "CaixasBancosDadosBasicosOrigemDTO",
    "CaixasBancosItemLancamentoDTO",
    "CaixasBancosLancamentoConciliacaoMovimentacaoDTO",
    "CaixasBancosLancamentoDTO",
    "CaixasBancosLancamentoParcelaDTO",
    "CaixasBancosSalvarLancamentoDTO",
    "CaixasBancosSalvarLancamentoResponseDTO",
    "CaixasGetResponse200",
]
