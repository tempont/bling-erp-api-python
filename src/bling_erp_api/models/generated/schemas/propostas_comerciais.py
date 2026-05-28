# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``propostas_comerciais``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

from .orcamentos import OrcamentosDadosBaseDTO, OrcamentosDadosDTO

if TYPE_CHECKING:
    from .common import BasePostResponse, Data24
    from .orcamentos import OrcamentosDadosBaseDTO


class PropostasComerciaisPostResponse201(BlingModel):
    """OpenAPI schema ``PropostasComerciaisPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class PropostasComerciaisGetResponse200(BlingModel):
    """OpenAPI schema ``PropostasComerciaisGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[OrcamentosDadosBaseDTO] | None``; opcional."""

    data: list[OrcamentosDadosBaseDTO] | None = None


class PropostasComerciaisPostRequest(OrcamentosDadosBaseDTO, OrcamentosDadosDTO):
    """OpenAPI schema ``PropostasComerciaisPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: OrcamentosDadosBaseDTO, OrcamentosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        data: Bling ``data``; type ``date | None``; opcional.
        situacao: Bling ``situacao``; type ``str | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        contato: Bling ``contato``; type ``OrcamentosContatoDTO | None``; opcional.
        loja: Bling ``loja``; type ``OrcamentosLojaDTO | None``; opcional.
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

    pass


class PropostasComerciaisIdPropostaComercialGetResponse200(
    OrcamentosDadosBaseDTO, OrcamentosDadosDTO
):
    """OpenAPI schema ``PropostasComerciaisIdPropostaComercialGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: OrcamentosDadosBaseDTO, OrcamentosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        data: Bling ``data``; type ``date | None``; opcional.
        situacao: Bling ``situacao``; type ``str | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        contato: Bling ``contato``; type ``OrcamentosContatoDTO | None``; opcional.
        loja: Bling ``loja``; type ``OrcamentosLojaDTO | None``; opcional.
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

    pass


class PropostasComerciaisIdPropostaComercialPutRequest(OrcamentosDadosBaseDTO, OrcamentosDadosDTO):
    """OpenAPI schema ``PropostasComerciaisIdPropostaComercialPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: OrcamentosDadosBaseDTO, OrcamentosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        data: Bling ``data``; type ``date | None``; opcional.
        situacao: Bling ``situacao``; type ``str | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        contato: Bling ``contato``; type ``OrcamentosContatoDTO | None``; opcional.
        loja: Bling ``loja``; type ``OrcamentosLojaDTO | None``; opcional.
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

    pass


class PropostasComerciaisDeleteResponse200(BlingModel):
    """OpenAPI schema ``PropostasComerciaisDeleteResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data24 | None``; opcional."""

    data: Data24 | None = None


__all__ = [
    "PropostasComerciaisDeleteResponse200",
    "PropostasComerciaisGetResponse200",
    "PropostasComerciaisIdPropostaComercialGetResponse200",
    "PropostasComerciaisIdPropostaComercialPutRequest",
    "PropostasComerciaisPostRequest",
    "PropostasComerciaisPostResponse201",
]
