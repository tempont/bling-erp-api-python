# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``campos_customizados``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Data1, Data2, Datum, Datum1


class CamposCustomizadosAgrupadorDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosAgrupadorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID do agrupador"""

    id: int = Field(..., examples=[12345678])


class CamposCustomizadosDadosBaseDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório. Ignorado no método PUT
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativo <br> `1` Ativo"""

    id: int = Field(..., examples=[12345678])
    nome: str = Field(..., examples=["Marca"])
    situacao: int | None = Field(default=None, examples=[1])


class CamposCustomizadosModuloBaseDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosModuloBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class CamposCustomizadosOpcaoDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosOpcaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID da opção
        nome: Bling ``nome``; type ``str``; obrigatório. Nome da opção"""

    id: int = Field(..., examples=[12345678])
    nome: str = Field(..., examples=["Opção 1"])


class CamposCustomizadosPermissaoDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosPermissaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str``; obrigatório.
        modulo: Bling ``modulo``; type ``str``; obrigatório.
        autorizado: Bling ``autorizado``; type ``bool``; obrigatório."""

    nome: str = Field(..., examples=["Clientes e Fornecedores"])
    modulo: str = Field(..., examples=["Contatos"])
    autorizado: bool = Field(..., examples=[True])


class CamposCustomizadosTamanhoDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosTamanhoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        minimo: Bling ``minimo``; type ``int | None``; opcional.
        maximo: Bling ``maximo``; type ``int | None``; opcional."""

    minimo: int | None = Field(default=None, examples=[1])
    maximo: int | None = Field(default=None, examples=[10])


class CamposCustomizadosTipoBaseDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosTipoBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class CamposCustomizadosTipoDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosTipoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str | None``; opcional.
        mascara: Bling ``mascara``; type ``str | None``; opcional."""

    nome: str | None = Field(default=None, examples=["Inteiro"])
    mascara: str | None = Field(default=None, examples=[""])


class CamposCustomizadosResponsePOSTPUT(BlingModel):
    """OpenAPI schema ``CamposCustomizadosResponsePOSTPUT``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        ids_vinculos_agrupadores: Bling ``idsVinculosAgrupadores``; type ``list[int] | None``; opcional.
        ids_opcoes: Bling ``idsOpcoes``; type ``list[int] | None``; opcional."""

    ids_vinculos_agrupadores: list[int] | None = Field(
        default=None,
        validation_alias=AliasChoices("ids_vinculos_agrupadores", "idsVinculosAgrupadores"),
        serialization_alias="idsVinculosAgrupadores",
    )
    ids_opcoes: list[int] | None = Field(
        default=None,
        validation_alias=AliasChoices("ids_opcoes", "idsOpcoes"),
        serialization_alias="idsOpcoes",
    )


class CamposCustomizadosTiposGetResponse200(BlingModel):
    """OpenAPI schema ``CamposCustomizadosTiposGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[Datum1] | None``; opcional."""

    data: list[Datum1] | None = None


class CamposCustomizadosModulosIdModuloGetResponse200(BlingModel):
    """OpenAPI schema ``CamposCustomizadosModulosIdModuloGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[CamposCustomizadosDadosBaseDTO] | None``; opcional."""

    data: list[CamposCustomizadosDadosBaseDTO] | None = None


class CamposCustomizadosIdCampoCustomizadoPutResponse200(BlingModel):
    """OpenAPI schema ``CamposCustomizadosIdCampoCustomizadoPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data2 | None``; opcional."""

    data: Data2 | None = None


class CamposCustomizadosPostResponse201(BlingModel):
    """OpenAPI schema ``CamposCustomizadosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data2 | None``; opcional."""

    data: Data2 | None = None


class CamposCustomizadosIdCampoCustomizadoSituacoesPatchRequest(BlingModel):
    """OpenAPI schema ``CamposCustomizadosIdCampoCustomizadoSituacoesPatchRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativo <br> `1` Ativo"""

    situacao: int | None = Field(default=None, examples=[1])


class CamposCustomizadosDadosDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        modulo: Bling ``modulo``; type ``CamposCustomizadosModuloBaseDTO``; obrigatório.
        tipo_campo: Bling ``tipoCampo``; type ``CamposCustomizadosTipoBaseDTO``; obrigatório."""

    modulo: CamposCustomizadosModuloBaseDTO
    tipo_campo: CamposCustomizadosTipoBaseDTO = Field(
        ...,
        validation_alias=AliasChoices("tipo_campo", "tipoCampo"),
        serialization_alias="tipoCampo",
    )


class CamposCustomizadosDadosEdicaoDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosDadosEdicaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        placeholder: Bling ``placeholder``; type ``str | None``; opcional.
        obrigatorio: Bling ``obrigatorio``; type ``bool | None``; opcional.
        opcoes: Bling ``opcoes``; type ``list[CamposCustomizadosOpcaoDTO] | None``; opcional.
        tamanho: Bling ``tamanho``; type ``CamposCustomizadosTamanhoDTO | None``; opcional.
        agrupadores: Bling ``agrupadores``; type ``list[CamposCustomizadosAgrupadorDTO] | None``; opcional."""

    placeholder: str | None = Field(default="", examples=["Informe a marca do produto"])
    obrigatorio: bool | None = Field(default=False, examples=[False])
    opcoes: list[CamposCustomizadosOpcaoDTO] | None = None
    tamanho: CamposCustomizadosTamanhoDTO | None = None
    agrupadores: list[CamposCustomizadosAgrupadorDTO] | None = None


class CamposCustomizadosModuloDTO(BlingModel):
    """OpenAPI schema ``CamposCustomizadosModuloDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str``; obrigatório.
        modulo: Bling ``modulo``; type ``str``; obrigatório.
        agrupador: Bling ``agrupador``; type ``str | None``; opcional. Atributo do cadastro utilizado como agrupador.
        permissoes: Bling ``permissoes``; type ``list[CamposCustomizadosPermissaoDTO]``; obrigatório."""

    nome: str = Field(..., examples=["Clientes e Fornecedores"])
    modulo: str = Field(..., examples=["Contatos"])
    agrupador: str | None = Field(default=None, examples=["Tipo de contato"])
    permissoes: list[CamposCustomizadosPermissaoDTO]


class CamposCustomizadosModulosGetResponse200(BlingModel):
    """OpenAPI schema ``CamposCustomizadosModulosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[Datum] | None``; opcional."""

    data: list[Datum] | None = None


class CamposCustomizadosIdCampoCustomizadoGetResponse200(BlingModel):
    """OpenAPI schema ``CamposCustomizadosIdCampoCustomizadoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data1 | None``; opcional."""

    data: Data1 | None = None


class CamposCustomizadosIdCampoCustomizadoPutRequest(
    CamposCustomizadosDadosBaseDTO, CamposCustomizadosDadosEdicaoDTO
):
    """OpenAPI schema ``CamposCustomizadosIdCampoCustomizadoPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CamposCustomizadosDadosBaseDTO, CamposCustomizadosDadosEdicaoDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório. Ignorado no método PUT
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativo <br> `1` Ativo
        placeholder: Bling ``placeholder``; type ``str | None``; opcional.
        obrigatorio: Bling ``obrigatorio``; type ``bool | None``; opcional.
        opcoes: Bling ``opcoes``; type ``list[CamposCustomizadosOpcaoDTO] | None``; opcional.
        tamanho: Bling ``tamanho``; type ``CamposCustomizadosTamanhoDTO | None``; opcional.
        agrupadores: Bling ``agrupadores``; type ``list[CamposCustomizadosAgrupadorDTO] | None``; opcional."""

    pass


class CamposCustomizadosPostRequest(
    CamposCustomizadosDadosBaseDTO, CamposCustomizadosDadosEdicaoDTO, CamposCustomizadosDadosDTO
):
    """OpenAPI schema ``CamposCustomizadosPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CamposCustomizadosDadosBaseDTO, CamposCustomizadosDadosEdicaoDTO, CamposCustomizadosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório. Ignorado no método PUT
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativo <br> `1` Ativo
        placeholder: Bling ``placeholder``; type ``str | None``; opcional.
        obrigatorio: Bling ``obrigatorio``; type ``bool | None``; opcional.
        opcoes: Bling ``opcoes``; type ``list[CamposCustomizadosOpcaoDTO] | None``; opcional.
        tamanho: Bling ``tamanho``; type ``CamposCustomizadosTamanhoDTO | None``; opcional.
        agrupadores: Bling ``agrupadores``; type ``list[CamposCustomizadosAgrupadorDTO] | None``; opcional.
        modulo: Bling ``modulo``; type ``CamposCustomizadosModuloBaseDTO``; obrigatório.
        tipo_campo: Bling ``tipoCampo``; type ``CamposCustomizadosTipoBaseDTO``; obrigatório."""

    pass


__all__ = [
    "CamposCustomizadosAgrupadorDTO",
    "CamposCustomizadosDadosBaseDTO",
    "CamposCustomizadosDadosDTO",
    "CamposCustomizadosDadosEdicaoDTO",
    "CamposCustomizadosIdCampoCustomizadoGetResponse200",
    "CamposCustomizadosIdCampoCustomizadoPutRequest",
    "CamposCustomizadosIdCampoCustomizadoPutResponse200",
    "CamposCustomizadosIdCampoCustomizadoSituacoesPatchRequest",
    "CamposCustomizadosModuloBaseDTO",
    "CamposCustomizadosModuloDTO",
    "CamposCustomizadosModulosGetResponse200",
    "CamposCustomizadosModulosIdModuloGetResponse200",
    "CamposCustomizadosOpcaoDTO",
    "CamposCustomizadosPermissaoDTO",
    "CamposCustomizadosPostRequest",
    "CamposCustomizadosPostResponse201",
    "CamposCustomizadosResponsePOSTPUT",
    "CamposCustomizadosTamanhoDTO",
    "CamposCustomizadosTipoBaseDTO",
    "CamposCustomizadosTipoDTO",
    "CamposCustomizadosTiposGetResponse200",
]
