# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``formas_pagamentos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse, Data11


class FormasPagamentosAlterarSituacaoDTO(BlingModel):
    """OpenAPI schema ``FormasPagamentosAlterarSituacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        situacao: Bling ``situacao``; type ``int``; obrigatório. Situação que será alterada <br> `1` Ativa <br> `0` Inativa"""

    situacao: int = Field(..., examples=[1])


class FormasPagamentosDadosBaseDTO(BlingModel):
    """OpenAPI schema ``FormasPagamentosDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        tipo_pagamento: Bling ``tipoPagamento``; type ``int``; obrigatório. `1` Dinheiro<br>`2` Cheque<br>`3` Cartão de Crédito<br>`4` Cartão de Débito<br>`5` Cartão da Loja (Private Label)<br>`10` Vale Alimentação<br>`11` Vale Refeição<br>`12` Vale Prese...
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativa<br>`1` Ativa<br>
        fixa: Bling ``fixa``; type ``bool | None``; opcional.
        padrao: Bling ``padrao``; type ``int | None``; opcional. `0` Não<br>`1` Padrão<br>`2` Padrão devolução
        finalidade: Bling ``finalidade``; type ``int``; obrigatório. `1` Pagamentos<br>`2` Recebimentos<br>`3` Pagamentos e Recebimentos<br>
        juros: Bling ``juros``; type ``float | None``; opcional. Valor em porcentagem, com até 2 casas decimais.
        multa: Bling ``multa``; type ``float | None``; opcional. Valor em porcentagem, com até 2 casas decimais."""

    id: int | None = Field(default=None, examples=[12345678])
    descricao: str = Field(..., examples=["Dinheiro"])
    tipo_pagamento: int = Field(
        ...,
        validation_alias=AliasChoices("tipo_pagamento", "tipoPagamento"),
        examples=[1],
        serialization_alias="tipoPagamento",
    )
    situacao: int | None = Field(default=None, examples=[1])
    fixa: bool | None = Field(default=None, examples=[False])
    padrao: int | None = Field(default=None, examples=[0])
    finalidade: int = Field(..., examples=[1])
    juros: float | None = Field(default=None, examples=[0])
    multa: float | None = Field(default=None, examples=[0])


class FormasPagamentosDadosCartaoDTO(BlingModel):
    """OpenAPI schema ``FormasPagamentosDadosCartaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        bandeira: Bling ``bandeira``; type ``int``; obrigatório. `1` Visa<br>`2` Mastercard<br>`3` American Express<br>`4` Sorocred<br>`5` Diners Club<br>`6` Elo<br>`7` Hipercard<br>`8` Aura<br>`9` Cabal<br>`99` Outros
        tipo: Bling ``tipo``; type ``int``; obrigatório. `1` TEF<br>`2` POS
        cnpj_credenciadora: Bling ``cnpjCredenciadora``; type ``str | None``; opcional. CNPJ da credenciadora.
        auto_liquidacao: Bling ``autoLiquidacao``; type ``int | None``; opcional. `0` Não<br>`1` Sim - Liquidação automática dos recebíveis"""

    bandeira: int = Field(..., examples=[1])
    tipo: int = Field(..., examples=[1])
    cnpj_credenciadora: str | None = Field(
        default=None,
        validation_alias=AliasChoices("cnpj_credenciadora", "cnpjCredenciadora"),
        examples=["67168564000109"],
        serialization_alias="cnpjCredenciadora",
    )
    auto_liquidacao: int | None = Field(
        default=None,
        validation_alias=AliasChoices("auto_liquidacao", "autoLiquidacao"),
        examples=[1],
        serialization_alias="autoLiquidacao",
    )


class FormasPagamentosDefinirPadraoDTO(BlingModel):
    """OpenAPI schema ``FormasPagamentosDefinirPadraoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        padrao: Bling ``padrao``; type ``int``; obrigatório. `1` Pagamento <br> `2` Devolução<br>`3` Fiado"""

    padrao: int = Field(..., examples=[1])


class FormasPagamentosTaxaDTO(BlingModel):
    """OpenAPI schema ``FormasPagamentosTaxaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        aliquota: Bling ``aliquota``; type ``float | None``; opcional. Valor da alíquota sobre o valor da parcela.
        valor: Bling ``valor``; type ``float | None``; opcional. Valor em Reais somado ao valor total da parcela.
        prazo: Bling ``prazo``; type ``int | None``; opcional. Prazo em dias que o dinheiro é retido antes de estar disponível para movimentação."""

    aliquota: float | None = Field(default=None, examples=[3.5])
    valor: float | None = Field(default=None, examples=[1.99])
    prazo: int | None = Field(default=None, examples=[2])


class FormasPagamentosGetResponse200(BlingModel):
    """OpenAPI schema ``FormasPagamentosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[FormasPagamentosDadosBaseDTO] | None``; opcional."""

    data: list[FormasPagamentosDadosBaseDTO] | None = None


class FormasPagamentosPostResponse201(BlingModel):
    """OpenAPI schema ``FormasPagamentosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class FormasPagamentosIdFormaPagamentoPutResponse200(BlingModel):
    """OpenAPI schema ``FormasPagamentosIdFormaPagamentoPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class FormasPagamentosDadosDTO(BlingModel):
    """OpenAPI schema ``FormasPagamentosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        condicao: Bling ``condicao``; type ``str | None``; opcional. Condição de pagamento padrão.
        destino: Bling ``destino``; type ``int``; obrigatório. `1` Conta a receber/pagar<br>`2` Ficha financeira<br>`3` Caixa e bancos
        utiliza_dias_uteis: Bling ``utilizaDiasUteis``; type ``bool | None``; opcional. Indica se a forma de pagamento utiliza lançamentos em dias úteis.
        taxas: Bling ``taxas``; type ``FormasPagamentosTaxaDTO | None``; opcional.
        dados_cartao: Bling ``dadosCartao``; type ``FormasPagamentosDadosCartaoDTO | None``; opcional."""

    condicao: str | None = Field(default=None, examples=["1x"])
    destino: int = Field(..., examples=[1])
    utiliza_dias_uteis: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("utiliza_dias_uteis", "utilizaDiasUteis"),
        examples=[True],
        serialization_alias="utilizaDiasUteis",
    )
    taxas: FormasPagamentosTaxaDTO | None = None
    dados_cartao: FormasPagamentosDadosCartaoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("dados_cartao", "dadosCartao"),
        serialization_alias="dadosCartao",
    )


class FormasPagamentosPostRequest(FormasPagamentosDadosBaseDTO, FormasPagamentosDadosDTO):
    """OpenAPI schema ``FormasPagamentosPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: FormasPagamentosDadosBaseDTO, FormasPagamentosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        tipo_pagamento: Bling ``tipoPagamento``; type ``int``; obrigatório. `1` Dinheiro<br>`2` Cheque<br>`3` Cartão de Crédito<br>`4` Cartão de Débito<br>`5` Cartão da Loja (Private Label)<br>`10` Vale Alimentação<br>`11` Vale Refeição<br>`12` Vale Prese...
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativa<br>`1` Ativa<br>
        fixa: Bling ``fixa``; type ``bool | None``; opcional.
        padrao: Bling ``padrao``; type ``int | None``; opcional. `0` Não<br>`1` Padrão<br>`2` Padrão devolução
        finalidade: Bling ``finalidade``; type ``int``; obrigatório. `1` Pagamentos<br>`2` Recebimentos<br>`3` Pagamentos e Recebimentos<br>
        juros: Bling ``juros``; type ``float | None``; opcional. Valor em porcentagem, com até 2 casas decimais.
        multa: Bling ``multa``; type ``float | None``; opcional. Valor em porcentagem, com até 2 casas decimais.
        condicao: Bling ``condicao``; type ``str | None``; opcional. Condição de pagamento padrão.
        destino: Bling ``destino``; type ``int``; obrigatório. `1` Conta a receber/pagar<br>`2` Ficha financeira<br>`3` Caixa e bancos
        utiliza_dias_uteis: Bling ``utilizaDiasUteis``; type ``bool | None``; opcional. Indica se a forma de pagamento utiliza lançamentos em dias úteis.
        taxas: Bling ``taxas``; type ``FormasPagamentosTaxaDTO | None``; opcional.
        dados_cartao: Bling ``dadosCartao``; type ``FormasPagamentosDadosCartaoDTO | None``; opcional."""

    pass


class FormasPagamentosIdFormaPagamentoGetResponse200(BlingModel):
    """OpenAPI schema ``FormasPagamentosIdFormaPagamentoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data11 | None``; opcional."""

    data: Data11 | None = None


class FormasPagamentosIdFormaPagamentoPutRequest(
    FormasPagamentosDadosBaseDTO, FormasPagamentosDadosDTO
):
    """OpenAPI schema ``FormasPagamentosIdFormaPagamentoPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: FormasPagamentosDadosBaseDTO, FormasPagamentosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        tipo_pagamento: Bling ``tipoPagamento``; type ``int``; obrigatório. `1` Dinheiro<br>`2` Cheque<br>`3` Cartão de Crédito<br>`4` Cartão de Débito<br>`5` Cartão da Loja (Private Label)<br>`10` Vale Alimentação<br>`11` Vale Refeição<br>`12` Vale Prese...
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativa<br>`1` Ativa<br>
        fixa: Bling ``fixa``; type ``bool | None``; opcional.
        padrao: Bling ``padrao``; type ``int | None``; opcional. `0` Não<br>`1` Padrão<br>`2` Padrão devolução
        finalidade: Bling ``finalidade``; type ``int``; obrigatório. `1` Pagamentos<br>`2` Recebimentos<br>`3` Pagamentos e Recebimentos<br>
        juros: Bling ``juros``; type ``float | None``; opcional. Valor em porcentagem, com até 2 casas decimais.
        multa: Bling ``multa``; type ``float | None``; opcional. Valor em porcentagem, com até 2 casas decimais.
        condicao: Bling ``condicao``; type ``str | None``; opcional. Condição de pagamento padrão.
        destino: Bling ``destino``; type ``int``; obrigatório. `1` Conta a receber/pagar<br>`2` Ficha financeira<br>`3` Caixa e bancos
        utiliza_dias_uteis: Bling ``utilizaDiasUteis``; type ``bool | None``; opcional. Indica se a forma de pagamento utiliza lançamentos em dias úteis.
        taxas: Bling ``taxas``; type ``FormasPagamentosTaxaDTO | None``; opcional.
        dados_cartao: Bling ``dadosCartao``; type ``FormasPagamentosDadosCartaoDTO | None``; opcional."""

    pass


__all__ = [
    "FormasPagamentosAlterarSituacaoDTO",
    "FormasPagamentosDadosBaseDTO",
    "FormasPagamentosDadosCartaoDTO",
    "FormasPagamentosDadosDTO",
    "FormasPagamentosDefinirPadraoDTO",
    "FormasPagamentosGetResponse200",
    "FormasPagamentosIdFormaPagamentoGetResponse200",
    "FormasPagamentosIdFormaPagamentoPutRequest",
    "FormasPagamentosIdFormaPagamentoPutResponse200",
    "FormasPagamentosPostRequest",
    "FormasPagamentosPostResponse201",
    "FormasPagamentosTaxaDTO",
]
