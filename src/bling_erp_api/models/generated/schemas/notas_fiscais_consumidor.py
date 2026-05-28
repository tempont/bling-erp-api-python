# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``notas_fiscais_consumidor``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

from .notas_fiscais import NotasFiscaisDadosBaseDTO, NotasFiscaisDadosPostDTO

if TYPE_CHECKING:
    from .common import Data13, Data14, Data16
    from .notas_fiscais import NotasFiscaisDadosBaseDTO


class NfcePostResponse201(BlingModel):
    """OpenAPI schema ``NfcePostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data13 | None``; opcional."""

    data: Data13 | None = None


class NfceIdNotaFiscalConsumidorPutResponse200(BlingModel):
    """OpenAPI schema ``NfceIdNotaFiscalConsumidorPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data13 | None``; opcional."""

    data: Data13 | None = None


class NfceIdNotaFiscalConsumidorEnviarPostResponse200(BlingModel):
    """OpenAPI schema ``NfceIdNotaFiscalConsumidorEnviarPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data16 | None``; opcional."""

    data: Data16 | None = None


class NfceGetResponse200(BlingModel):
    """OpenAPI schema ``NfceGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[NotasFiscaisDadosBaseDTO] | None``; opcional."""

    data: list[NotasFiscaisDadosBaseDTO] | None = None


class NfcePostRequest(NotasFiscaisDadosBaseDTO, NotasFiscaisDadosPostDTO):
    """OpenAPI schema ``NfcePostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasFiscaisDadosBaseDTO, NotasFiscaisDadosPostDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        tipo: Bling ``tipo``; type ``int``; obrigatório. `0` Entrada <br> `1` Saída
        situacao: Bling ``situacao``; type ``int | None``; opcional. `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10...
        numero: Bling ``numero``; type ``str``; obrigatório.
        data_emissao: Bling ``dataEmissao``; type ``str | None``; opcional. Data e hora da emissão.
        data_operacao: Bling ``dataOperacao``; type ``str``; obrigatório. Data de saída/entrada de acordo com o tipo da nota.
        chave_acesso: Bling ``chaveAcesso``; type ``str | None``; opcional.
        contato: Bling ``contato``; type ``NotasFiscaisContatoDTO``; obrigatório.
        natureza_operacao: Bling ``naturezaOperacao``; type ``NotasFiscaisNaturezaOperacaoDTO``; obrigatório.
        loja: Bling ``loja``; type ``NotasFiscaisLojaDTO | None``; opcional.
        finalidade: Bling ``finalidade``; type ``int | None``; opcional. `1` Normal <br>`2` Complementar <br>`3` Ajuste <br>`4` Devolução <br>`5` Crédito <br>`6` Débito
        tipo_nota: Bling ``tipoNota``; type ``str | None``; opcional. Obrigatório quando finalidade for 5 (Crédito) ou 6 (Débito). <br><br>**Crédito (finalidade 5):** <br>`01` Multa e juros <br>`02` Apropriação de crédito presumido de IBS sobre o sa...
        seguro: Bling ``seguro``; type ``float | None``; opcional.
        despesas: Bling ``despesas``; type ``float | None``; opcional.
        desconto: Bling ``desconto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        xml: Bling ``xml``; type ``str | None``; opcional.
        link_danfe: Bling ``linkDanfe``; type ``str | None``; opcional.
        link_pdf: Bling ``linkPDF``; type ``str | None``; opcional.
        documento_referenciado: Bling ``documentoReferenciado``; type ``NotasFiscaisDocumentoReferenciadoDTO | None``; opcional.
        documentos_referenciados: Bling ``documentosReferenciados``; type ``list[NotasFiscaisDocumentoReferenciadoDTO] | None``; opcional.
        itens: Bling ``itens``; type ``list[NotasFiscaisItemDTO] | None``; opcional.
        parcelas: Bling ``parcelas``; type ``list[NotasFiscaisParcelaDTO] | None``; opcional.
        transporte: Bling ``transporte``; type ``NotasFiscaisTransportePostDTO | None``; opcional.
        nota_fiscal_produtor_rural_referenciada: Bling ``notaFiscalProdutorRuralReferenciada``; type ``NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO | None``; opcional.
        intermediador: Bling ``intermediador``; type ``NotasFiscaisIntermediadorDTO | None``; opcional."""

    pass


class NfceIdNotaFiscalConsumidorGetResponse200(BlingModel):
    """OpenAPI schema ``NfceIdNotaFiscalConsumidorGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data14 | None``; opcional."""

    data: Data14 | None = None


class NfceIdNotaFiscalConsumidorPutRequest(NotasFiscaisDadosBaseDTO, NotasFiscaisDadosPostDTO):
    """OpenAPI schema ``NfceIdNotaFiscalConsumidorPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasFiscaisDadosBaseDTO, NotasFiscaisDadosPostDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        tipo: Bling ``tipo``; type ``int``; obrigatório. `0` Entrada <br> `1` Saída
        situacao: Bling ``situacao``; type ``int | None``; opcional. `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10...
        numero: Bling ``numero``; type ``str``; obrigatório.
        data_emissao: Bling ``dataEmissao``; type ``str | None``; opcional. Data e hora da emissão.
        data_operacao: Bling ``dataOperacao``; type ``str``; obrigatório. Data de saída/entrada de acordo com o tipo da nota.
        chave_acesso: Bling ``chaveAcesso``; type ``str | None``; opcional.
        contato: Bling ``contato``; type ``NotasFiscaisContatoDTO``; obrigatório.
        natureza_operacao: Bling ``naturezaOperacao``; type ``NotasFiscaisNaturezaOperacaoDTO``; obrigatório.
        loja: Bling ``loja``; type ``NotasFiscaisLojaDTO | None``; opcional.
        finalidade: Bling ``finalidade``; type ``int | None``; opcional. `1` Normal <br>`2` Complementar <br>`3` Ajuste <br>`4` Devolução <br>`5` Crédito <br>`6` Débito
        tipo_nota: Bling ``tipoNota``; type ``str | None``; opcional. Obrigatório quando finalidade for 5 (Crédito) ou 6 (Débito). <br><br>**Crédito (finalidade 5):** <br>`01` Multa e juros <br>`02` Apropriação de crédito presumido de IBS sobre o sa...
        seguro: Bling ``seguro``; type ``float | None``; opcional.
        despesas: Bling ``despesas``; type ``float | None``; opcional.
        desconto: Bling ``desconto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        xml: Bling ``xml``; type ``str | None``; opcional.
        link_danfe: Bling ``linkDanfe``; type ``str | None``; opcional.
        link_pdf: Bling ``linkPDF``; type ``str | None``; opcional.
        documento_referenciado: Bling ``documentoReferenciado``; type ``NotasFiscaisDocumentoReferenciadoDTO | None``; opcional.
        documentos_referenciados: Bling ``documentosReferenciados``; type ``list[NotasFiscaisDocumentoReferenciadoDTO] | None``; opcional.
        itens: Bling ``itens``; type ``list[NotasFiscaisItemDTO] | None``; opcional.
        parcelas: Bling ``parcelas``; type ``list[NotasFiscaisParcelaDTO] | None``; opcional.
        transporte: Bling ``transporte``; type ``NotasFiscaisTransportePostDTO | None``; opcional.
        nota_fiscal_produtor_rural_referenciada: Bling ``notaFiscalProdutorRuralReferenciada``; type ``NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO | None``; opcional.
        intermediador: Bling ``intermediador``; type ``NotasFiscaisIntermediadorDTO | None``; opcional."""

    pass


__all__ = [
    "NfceGetResponse200",
    "NfceIdNotaFiscalConsumidorEnviarPostResponse200",
    "NfceIdNotaFiscalConsumidorGetResponse200",
    "NfceIdNotaFiscalConsumidorPutRequest",
    "NfceIdNotaFiscalConsumidorPutResponse200",
    "NfcePostRequest",
    "NfcePostResponse201",
]
