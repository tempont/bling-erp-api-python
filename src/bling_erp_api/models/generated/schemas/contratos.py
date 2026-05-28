# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``contratos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse, Data10


class ContratosCategoriaDTO(BlingModel):
    """OpenAPI schema ``ContratosCategoriaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ContratosCobrancaContatoDTO(BlingModel):
    """OpenAPI schema ``ContratosCobrancaContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Deve ser informado apenas quando o contato de cobrança for diferente do contato vinculado ao contrato."""

    id: int | None = Field(default=None, examples=[12345678])


class ContratosCobrancaVencimentoDTO(BlingModel):
    """OpenAPI schema ``ContratosCobrancaVencimentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        tipo: Bling ``tipo``; type ``int | None``; opcional. `1` No mês corrente<br>`2` No mês seguinte<br>`3` Em dois meses
        dia: Bling ``dia``; type ``int | None``; opcional. Caso o dia informado não exista em um determinado mês(29, 30, 31), o vencimento da cobrança utilizará o ultimo dia válido do mês.
        periodicidade: Bling ``periodicidade``; type ``int | None``; opcional. `1` Mensal<br>`2` Bimestral<br>`3` Trimestral<br>`4` Semestral<br>`5` Anual<br>`6` Bianual<br>`7` Trianual"""

    tipo: int | None = Field(default=None, examples=[1])
    dia: int | None = Field(default=None, examples=[10])
    periodicidade: int | None = Field(default=None, examples=[1])


class ContratosContaContabilDTO(BlingModel):
    """OpenAPI schema ``ContratosContaContabilDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])


class ContratosContatoDTO(BlingModel):
    """OpenAPI schema ``ContratosContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ContratosDadosBaseDTO(BlingModel):
    """OpenAPI schema ``ContratosDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        data: Bling ``data``; type ``date``; obrigatório. Data de criação do contrato.
        numero: Bling ``numero``; type ``str``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `0` Inativo<br>`1` Ativo<br>`2` Baixado<br>`3` Isento<br>`4` Em avaliação
        contato: Bling ``contato``; type ``ContratosContatoDTO``; obrigatório."""

    id: int | None = Field(default=None, examples=[123455678])
    descricao: str = Field(..., examples=["Alugel do apartamento A102"])
    data: date = Field(..., examples=["2023-02-19"])
    numero: str = Field(..., examples=["25"])
    valor: float = Field(..., examples=[59.99])
    situacao: int = Field(..., examples=[1])
    contato: ContratosContatoDTO


class ContratosDescontoDTO(BlingModel):
    """OpenAPI schema ``ContratosDescontoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        valor: Bling ``valor``; type ``float``; obrigatório.
        data_fim: Bling ``dataFim``; type ``str``; obrigatório. Formato: YYYY-MM"""

    valor: float = Field(..., examples=[4.99])
    data_fim: str = Field(..., alias="dataFim", examples=["2023-02"])


class ContratosFormaPagamentoDTO(BlingModel):
    """OpenAPI schema ``ContratosFormaPagamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ContratosNotaFiscalISSDTO(BlingModel):
    """OpenAPI schema ``ContratosNotaFiscalISSDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        descontar: Bling ``descontar``; type ``bool | None``; opcional. Reter o ISS e descontar do total da nota.
        aliquota: Bling ``aliquota``; type ``float | None``; opcional. Percentual ISS específico para este contrato. Deixe este campo zerado para utilizar o padrão."""

    descontar: bool | None = Field(default=None, examples=[False])
    aliquota: float | None = Field(default=None, examples=[2.5])


class ContratosNotaFiscalItemProdutoDTO(BlingModel):
    """OpenAPI schema ``ContratosNotaFiscalItemProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do produto do tipo produto ou serviço."""

    id: int | None = Field(default=None, examples=[12345678])


class ContratosVendedorComissaoDTO(BlingModel):
    """OpenAPI schema ``ContratosVendedorComissaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        aliquota: Bling ``aliquota``; type ``float``; obrigatório.
        numero_parcelas: Bling ``numeroParcelas``; type ``int``; obrigatório."""

    aliquota: float = Field(..., examples=[0.5])
    numero_parcelas: int = Field(..., alias="numeroParcelas", examples=[1])


class ContratosVendedorDTO(BlingModel):
    """OpenAPI schema ``ContratosVendedorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        comissao: Bling ``comissao``; type ``ContratosVendedorComissaoDTO``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    comissao: ContratosVendedorComissaoDTO


class ContratosGetResponse200(BlingModel):
    """OpenAPI schema ``ContratosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ContratosDadosBaseDTO] | None``; opcional."""

    data: list[ContratosDadosBaseDTO] | None = None


class ContratosPostResponse201(BlingModel):
    """OpenAPI schema ``ContratosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class ContratosIdContratoPutResponse201(BlingModel):
    """OpenAPI schema ``ContratosIdContratoPutResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class ContratosCobrancaDTO(BlingModel):
    """OpenAPI schema ``ContratosCobrancaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data_base: Bling ``dataBase``; type ``date | None``; opcional.
        contato: Bling ``contato``; type ``ContratosCobrancaContatoDTO | None``; opcional.
        vencimento: Bling ``vencimento``; type ``ContratosCobrancaVencimentoDTO | None``; opcional."""

    data_base: date | None = Field(default=None, alias="dataBase", examples=["2023-02-22"])
    contato: ContratosCobrancaContatoDTO | None = None
    vencimento: ContratosCobrancaVencimentoDTO | None = None


class ContratosNotaFiscalItemDTO(BlingModel):
    """OpenAPI schema ``ContratosNotaFiscalItemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        codigo_servico: Bling ``codigoServico``; type ``str | None``; opcional. Código do serviço conforme tabela de serviços.
        produto: Bling ``produto``; type ``ContratosNotaFiscalItemProdutoDTO | None``; opcional."""

    codigo_servico: str | None = Field(default=None, alias="codigoServico", examples=["14.13"])
    produto: ContratosNotaFiscalItemProdutoDTO | None = None


class ContratosNotaFiscalDTO(BlingModel):
    """OpenAPI schema ``ContratosNotaFiscalDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        mes: Bling ``mes``; type ``int | None``; opcional. `1` Não imprime<br>`2` Mês atual<br>`3` Mês anterior<br>Período de referência da cobrança que será incluído nas informações complementares das notas fiscais e observações da conta...
        gerar: Bling ``gerar``; type ``int | None``; opcional. `1` Não<br>`2` Ao gerar cobrança
        descontar_imposto_renda: Bling ``descontarImpostoRenda``; type ``int | None``; opcional. `1` Sim<br>`2` Não<br>`3` Utilizar padrão da configuração da NFS-e<br>Reter o IR e descontar do total da NFS-e caso ultrapasse R$ 10,00.
        texto: Bling ``texto``; type ``str | None``; opcional. Texto a ser incluído nas informações complementares da NF-e ou como descrição do serviço na NFS-e.
        cfop: Bling ``cfop``; type ``str | None``; opcional. Código fiscal.
        iss: Bling ``iss``; type ``ContratosNotaFiscalISSDTO | None``; opcional.
        item: Bling ``item``; type ``ContratosNotaFiscalItemDTO | None``; opcional."""

    mes: int | None = Field(default=None, examples=[2])
    gerar: int | None = Field(default=None, examples=[1])
    descontar_imposto_renda: int | None = Field(
        default=None, alias="descontarImpostoRenda", examples=[1]
    )
    texto: str | None = Field(default=None, examples=["Exemplo de texto."])
    cfop: str | None = Field(default=None, examples=["5.556"])
    iss: ContratosNotaFiscalISSDTO | None = None
    item: ContratosNotaFiscalItemDTO | None = None


class ContratosDadosDTO(BlingModel):
    """OpenAPI schema ``ContratosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data_fim: Bling ``dataFim``; type ``str``; obrigatório. Formato: YYYY-MM
        tipo_manutencao: Bling ``tipoManutencao``; type ``int``; obrigatório. `1` Valor <br> `2` Indexação
        emitir_ordem_servico: Bling ``emitirOrdemServico``; type ``bool``; obrigatório.
        observacoes: Bling ``observacoes``; type ``str``; obrigatório.
        vendedor: Bling ``vendedor``; type ``ContratosVendedorDTO``; obrigatório.
        categoria: Bling ``categoria``; type ``ContratosCategoriaDTO``; obrigatório.
        desconto: Bling ``desconto``; type ``ContratosDescontoDTO``; obrigatório.
        conta_contabil: Bling ``contaContabil``; type ``ContratosContaContabilDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContratosFormaPagamentoDTO``; obrigatório.
        nota_fiscal: Bling ``notaFiscal``; type ``ContratosNotaFiscalDTO | None``; opcional.
        cobranca: Bling ``cobranca``; type ``ContratosCobrancaDTO``; obrigatório."""

    data_fim: str = Field(..., alias="dataFim", examples=["2024-05"])
    tipo_manutencao: int = Field(..., alias="tipoManutencao", examples=[1])
    emitir_ordem_servico: bool = Field(..., alias="emitirOrdemServico", examples=[False])
    observacoes: str = Field(..., examples=[""])
    vendedor: ContratosVendedorDTO
    categoria: ContratosCategoriaDTO
    desconto: ContratosDescontoDTO
    conta_contabil: ContratosContaContabilDTO = Field(..., alias="contaContabil")
    forma_pagamento: ContratosFormaPagamentoDTO = Field(..., alias="formaPagamento")
    nota_fiscal: ContratosNotaFiscalDTO | None = Field(default=None, alias="notaFiscal")
    cobranca: ContratosCobrancaDTO


class ContratosPostRequest(ContratosDadosBaseDTO, ContratosDadosDTO):
    """OpenAPI schema ``ContratosPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ContratosDadosBaseDTO, ContratosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        data: Bling ``data``; type ``date``; obrigatório. Data de criação do contrato.
        numero: Bling ``numero``; type ``str``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `0` Inativo<br>`1` Ativo<br>`2` Baixado<br>`3` Isento<br>`4` Em avaliação
        contato: Bling ``contato``; type ``ContratosContatoDTO``; obrigatório.
        data_fim: Bling ``dataFim``; type ``str``; obrigatório. Formato: YYYY-MM
        tipo_manutencao: Bling ``tipoManutencao``; type ``int``; obrigatório. `1` Valor <br> `2` Indexação
        emitir_ordem_servico: Bling ``emitirOrdemServico``; type ``bool``; obrigatório.
        observacoes: Bling ``observacoes``; type ``str``; obrigatório.
        vendedor: Bling ``vendedor``; type ``ContratosVendedorDTO``; obrigatório.
        categoria: Bling ``categoria``; type ``ContratosCategoriaDTO``; obrigatório.
        desconto: Bling ``desconto``; type ``ContratosDescontoDTO``; obrigatório.
        conta_contabil: Bling ``contaContabil``; type ``ContratosContaContabilDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContratosFormaPagamentoDTO``; obrigatório.
        nota_fiscal: Bling ``notaFiscal``; type ``ContratosNotaFiscalDTO | None``; opcional.
        cobranca: Bling ``cobranca``; type ``ContratosCobrancaDTO``; obrigatório."""

    pass


class ContratosIdContratoGetResponse200(BlingModel):
    """OpenAPI schema ``ContratosIdContratoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data10 | None``; opcional."""

    data: Data10 | None = None


class ContratosIdContratoPutRequest(ContratosDadosBaseDTO, ContratosDadosDTO):
    """OpenAPI schema ``ContratosIdContratoPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ContratosDadosBaseDTO, ContratosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        data: Bling ``data``; type ``date``; obrigatório. Data de criação do contrato.
        numero: Bling ``numero``; type ``str``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `0` Inativo<br>`1` Ativo<br>`2` Baixado<br>`3` Isento<br>`4` Em avaliação
        contato: Bling ``contato``; type ``ContratosContatoDTO``; obrigatório.
        data_fim: Bling ``dataFim``; type ``str``; obrigatório. Formato: YYYY-MM
        tipo_manutencao: Bling ``tipoManutencao``; type ``int``; obrigatório. `1` Valor <br> `2` Indexação
        emitir_ordem_servico: Bling ``emitirOrdemServico``; type ``bool``; obrigatório.
        observacoes: Bling ``observacoes``; type ``str``; obrigatório.
        vendedor: Bling ``vendedor``; type ``ContratosVendedorDTO``; obrigatório.
        categoria: Bling ``categoria``; type ``ContratosCategoriaDTO``; obrigatório.
        desconto: Bling ``desconto``; type ``ContratosDescontoDTO``; obrigatório.
        conta_contabil: Bling ``contaContabil``; type ``ContratosContaContabilDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContratosFormaPagamentoDTO``; obrigatório.
        nota_fiscal: Bling ``notaFiscal``; type ``ContratosNotaFiscalDTO | None``; opcional.
        cobranca: Bling ``cobranca``; type ``ContratosCobrancaDTO``; obrigatório."""

    pass


__all__ = [
    "ContratosCategoriaDTO",
    "ContratosCobrancaContatoDTO",
    "ContratosCobrancaDTO",
    "ContratosCobrancaVencimentoDTO",
    "ContratosContaContabilDTO",
    "ContratosContatoDTO",
    "ContratosDadosBaseDTO",
    "ContratosDadosDTO",
    "ContratosDescontoDTO",
    "ContratosFormaPagamentoDTO",
    "ContratosGetResponse200",
    "ContratosIdContratoGetResponse200",
    "ContratosIdContratoPutRequest",
    "ContratosIdContratoPutResponse201",
    "ContratosNotaFiscalDTO",
    "ContratosNotaFiscalISSDTO",
    "ContratosNotaFiscalItemDTO",
    "ContratosNotaFiscalItemProdutoDTO",
    "ContratosPostRequest",
    "ContratosPostResponse201",
    "ContratosVendedorComissaoDTO",
    "ContratosVendedorDTO",
]
