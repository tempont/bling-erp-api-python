# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``orcamentos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import LojaUnidadeNegocioDTO


class OrcamentosContatoDTO(BlingModel):
    """OpenAPI schema ``OrcamentosContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])


class OrcamentosFormaPagamentoDTO(BlingModel):
    """OpenAPI schema ``OrcamentosFormaPagamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])


class OrcamentosParcelaDTO(BlingModel):
    """OpenAPI schema ``OrcamentosParcelaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        numero_dias: Bling ``numeroDias``; type ``int | None``; opcional.
        data_vencimento: Bling ``dataVencimento``; type ``date | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        forma_pagamento: Bling ``formaPagamento``; type ``OrcamentosFormaPagamentoDTO | None``; opcional."""

    numero_dias: int | None = Field(default=None, alias="numeroDias", examples=[10])
    data_vencimento: date | None = Field(
        default=None, alias="dataVencimento", examples=["2024-04-29"]
    )
    valor: float | None = Field(default=None, examples=[10.55])
    observacoes: str | None = Field(default=None, examples=["Observacao da forma de pagamento"])
    forma_pagamento: OrcamentosFormaPagamentoDTO | None = Field(
        default=None, alias="formaPagamento"
    )


class OrcamentosProdutoDTO(BlingModel):
    """OpenAPI schema ``OrcamentosProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    descricao: str | None = Field(default=None, examples=["Bolo"])


class OrcamentosSituacaoDTO(BlingModel):
    """OpenAPI schema ``OrcamentosSituacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        situacao: Bling ``situacao``; type ``str | None``; opcional."""

    situacao: str | None = Field(default=None, examples=["Aguardando"])


class OrcamentosTransporteContatoDTO(BlingModel):
    """OpenAPI schema ``OrcamentosTransporteContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    nome: str | None = Field(default=None, examples=["Nome do transportador"])


class OrcamentosTransporteVolumeDTO(BlingModel):
    """OpenAPI schema ``OrcamentosTransporteVolumeDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        servico: Bling ``servico``; type ``str | None``; opcional.
        codigo_rastreamento: Bling ``codigoRastreamento``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    servico: str | None = Field(default=None, examples=["Correios PAC"])
    codigo_rastreamento: str | None = Field(
        default=None, alias="codigoRastreamento", examples=["R56563A"]
    )


class OrcamentosVendedorDTO(BlingModel):
    """OpenAPI schema ``OrcamentosVendedorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])


class OrcamentosItemDTO(BlingModel):
    """OpenAPI schema ``OrcamentosItemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        produto: Bling ``produto``; type ``OrcamentosProdutoDTO | None``; opcional.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        unidade: Bling ``unidade``; type ``str | None``; opcional.
        quantidade: Bling ``quantidade``; type ``float | None``; opcional.
        desconto: Bling ``desconto``; type ``float | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional.
        descricao_detalhada: Bling ``descricaoDetalhada``; type ``str | None``; opcional."""

    produto: OrcamentosProdutoDTO | None = None
    codigo: str | None = Field(default=None, examples=["BLG-5"])
    unidade: str | None = Field(default=None, examples=["UN"])
    quantidade: float | None = Field(default=None, examples=[1.1])
    desconto: float | None = Field(default=None, examples=[1.2])
    valor: float | None = Field(default=None, examples=[3.1])
    descricao_detalhada: str | None = Field(
        default=None, alias="descricaoDetalhada", examples=["Descrição detalhada do produto"]
    )


class OrcamentosLojaDTO(BlingModel):
    """OpenAPI schema ``OrcamentosLojaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        unidade_negocio: Bling ``unidadeNegocio``; type ``LojaUnidadeNegocioDTO | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    unidade_negocio: LojaUnidadeNegocioDTO | None = Field(default=None, alias="unidadeNegocio")


class OrcamentosTransporteDTO(BlingModel):
    """OpenAPI schema ``OrcamentosTransporteDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        frete_modalidade: Bling ``freteModalidade``; type ``int | None``; opcional. `0` Contratação do Frete por conta do Remetente (CIF)<br> `1` Contratação do Frete por conta do Destinatário (FOB)<br> `2` Contratação do Frete por conta de Terceiros<br> `3` Tran...
        frete: Bling ``frete``; type ``float | None``; opcional.
        quantidade_volumes: Bling ``quantidadeVolumes``; type ``float | None``; opcional.
        prazo_entrega: Bling ``prazoEntrega``; type ``int | None``; opcional.
        peso_bruto: Bling ``pesoBruto``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``OrcamentosTransporteContatoDTO | None``; opcional.
        volumes: Bling ``volumes``; type ``OrcamentosTransporteVolumeDTO | None``; opcional."""

    frete_modalidade: int | None = Field(default=None, alias="freteModalidade", examples=[0])
    frete: float | None = Field(default=None, examples=[2.34])
    quantidade_volumes: float | None = Field(
        default=None, alias="quantidadeVolumes", examples=[2.33]
    )
    prazo_entrega: int | None = Field(default=None, alias="prazoEntrega", examples=[2])
    peso_bruto: float | None = Field(default=None, alias="pesoBruto", examples=[2.4])
    contato: OrcamentosTransporteContatoDTO | None = None
    volumes: OrcamentosTransporteVolumeDTO | None = None


class OrcamentosDadosBaseDTO(BlingModel):
    """OpenAPI schema ``OrcamentosDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        data: Bling ``data``; type ``date | None``; opcional.
        situacao: Bling ``situacao``; type ``str | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        contato: Bling ``contato``; type ``OrcamentosContatoDTO | None``; opcional.
        loja: Bling ``loja``; type ``OrcamentosLojaDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[123456789])
    data: date | None = Field(default=None, examples=["2024-04-29"])
    situacao: str | None = Field(default=None, examples=["Concluído"])
    total: float | None = Field(default=None, examples=[251])
    total_produtos: float | None = Field(default=None, alias="totalProdutos", examples=[500])
    numero: int | None = Field(default=None, examples=[13])
    contato: OrcamentosContatoDTO | None = None
    loja: OrcamentosLojaDTO | None = None


class OrcamentosDadosDTO(BlingModel):
    """OpenAPI schema ``OrcamentosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        desconto: Bling ``desconto``; type ``float | None``; opcional.
        outras_despesas: Bling ``outrasDespesas``; type ``float | None``; opcional.
        garantia: Bling ``garantia``; type ``int | None``; opcional.
        data_proximo_contato: Bling ``dataProximoContato``; type ``str | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        observacao_interna: Bling ``observacaoInterna``; type ``str | None``; opcional.
        total_outros_itens: Bling ``totalOutrosItens``; type ``int | None``; opcional.
        aos_cuidados_de: Bling ``aosCuidadosDe``; type ``str | None``; opcional.
        introducao: Bling ``introducao``; type ``str | None``; opcional.
        prazo_entrega: Bling ``prazoEntrega``; type ``str | None``; opcional.
        itens: Bling ``itens``; type ``list[OrcamentosItemDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[OrcamentosParcelaDTO]``; obrigatório.
        vendedor: Bling ``vendedor``; type ``OrcamentosVendedorDTO | None``; opcional.
        transporte: Bling ``transporte``; type ``OrcamentosTransporteDTO | None``; opcional."""

    desconto: float | None = Field(default=None, examples=[10])
    outras_despesas: float | None = Field(default=None, alias="outrasDespesas", examples=[11])
    garantia: int | None = Field(default=None, examples=[3])
    data_proximo_contato: str | None = Field(
        default=None, alias="dataProximoContato", examples=["2024-05-01"]
    )
    observacoes: str | None = Field(default=None, examples=["Observações da proposta comercial"])
    observacao_interna: str | None = Field(
        default=None,
        alias="observacaoInterna",
        examples=["Observações internas da proposta comercial"],
    )
    total_outros_itens: int | None = Field(default=None, alias="totalOutrosItens", examples=[1])
    aos_cuidados_de: str | None = Field(
        default=None, alias="aosCuidadosDe", examples=["Nome do Contato"]
    )
    introducao: str | None = Field(default=None, examples=["Introdução da proposta comercial"])
    prazo_entrega: str | None = Field(
        default=None, alias="prazoEntrega", examples=["Prazo de entrega proposta comercial"]
    )
    itens: list[OrcamentosItemDTO]
    parcelas: list[OrcamentosParcelaDTO]
    vendedor: OrcamentosVendedorDTO | None = None
    transporte: OrcamentosTransporteDTO | None = None


__all__ = [
    "OrcamentosContatoDTO",
    "OrcamentosDadosBaseDTO",
    "OrcamentosDadosDTO",
    "OrcamentosFormaPagamentoDTO",
    "OrcamentosItemDTO",
    "OrcamentosLojaDTO",
    "OrcamentosParcelaDTO",
    "OrcamentosProdutoDTO",
    "OrcamentosSituacaoDTO",
    "OrcamentosTransporteContatoDTO",
    "OrcamentosTransporteDTO",
    "OrcamentosTransporteVolumeDTO",
    "OrcamentosVendedorDTO",
]
