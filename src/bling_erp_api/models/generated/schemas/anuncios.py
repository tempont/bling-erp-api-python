# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``anuncios``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import (
        AnuncioLoja,
        Atributo,
        Categoria,
        Imagen,
        Integracao,
        Loja,
        MercadoLivre,
        Preco,
    )
    from .estoques import Estoques
    from .produtos import Produto, Produto1


class AnunciosGetAllResponseDTO(BlingModel):
    """OpenAPI schema ``AnunciosGetAllResponseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do anúncio.
        titulo: Bling ``titulo``; type ``str | None``; opcional. Título do anúncio.
        situacao: Bling ``situacao``; type ``int | None``; opcional. Situação do anúncio."""

    id: int | None = Field(default=None, examples=[1])
    titulo: str | None = Field(default=None, examples=["Anúncio 1"])
    situacao: int | None = Field(default=None, examples=[1])


class AnunciosGetAttributesFromCategoryResponseDTO(BlingModel):
    """OpenAPI schema ``AnunciosGetAttributesFromCategoryResponseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do atributo.
        nome: Bling ``nome``; type ``str | None``; opcional. Nome do atributo.
        obrigatorio: Bling ``obrigatorio``; type ``bool | None``; opcional. Se o atributo é obrigatório.
        tipo: Bling ``tipo``; type ``str | None``; opcional. Tipo do atributo.
        unidade_padrao: Bling ``unidadePadrao``; type ``str | None``; opcional. Unidade padrão do atributo.
        minimo: Bling ``minimo``; type ``int | None``; opcional. Mínimo do atributo.
        maximo: Bling ``maximo``; type ``int | None``; opcional. Máximo do atributo."""

    id: int | None = Field(default=None, examples=[1])
    nome: str | None = Field(default=None, examples=["Atributo 1"])
    obrigatorio: bool | None = Field(default=None, examples=[True])
    tipo: str | None = Field(default=None, examples=["string"])
    unidade_padrao: str | None = Field(
        default=None,
        validation_alias=AliasChoices("unidade_padrao", "unidadePadrao"),
        examples=["unidade"],
        serialization_alias="unidadePadrao",
    )
    minimo: int | None = Field(default=None, examples=[1])
    maximo: int | None = Field(default=None, examples=[10])


class AnunciosAtributoDTO(BlingModel):
    """OpenAPI schema ``AnunciosAtributoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do atributo.
        id_externo: Bling ``id_externo``; type ``str | None``; opcional. ID externo do atributo.
        nome: Bling ``nome``; type ``str | None``; opcional. Nome do atributo.
        tipo: Bling ``tipo``; type ``str | None``; opcional. Tipo do atributo.
        valor: Bling ``valor``; type ``str | None``; opcional. Valor do atributo.
        unidade: Bling ``unidade``; type ``str | None``; opcional. Unidade do atributo, se aplicável."""

    id: int | None = Field(default=None, examples=[123])
    id_externo: str | None = Field(default=None, examples=["COR"])
    nome: str | None = Field(default=None, examples=["Cor"])
    tipo: str | None = Field(default=None, examples=["string"])
    valor: str | None = Field(default=None, examples=["Azul"])
    unidade: str | None = Field(default=None, examples=["cm"])


class AnunciosImagemDTO(BlingModel):
    """OpenAPI schema ``AnunciosImagemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID da imagem.
        url: Bling ``url``; type ``str | None``; opcional. URL da imagem.
        ordem: Bling ``ordem``; type ``int | None``; opcional. Ordem da imagem.
        tipo: Bling ``tipo``; type ``str | None``; opcional. Tipo da imagem."""

    id: int | None = Field(default=None, examples=[456])
    url: str | None = Field(default=None, examples=["https://exemplo.com/imagem.jpg"])
    ordem: int | None = Field(default=None, examples=[1])
    tipo: str | None = Field(default=None, examples=["principal"])


class AnunciosVariacaoDTO(BlingModel):
    """OpenAPI schema ``AnunciosVariacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID da variação.
        nome: Bling ``nome``; type ``str | None``; opcional. Nome da variação."""

    id: int | None = Field(default=None, examples=[789])
    nome: str | None = Field(default=None, examples=["Vermelho / P"])


class AnunciosGetByIdResponseDTO(BlingModel):
    """OpenAPI schema ``AnunciosGetByIdResponseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do anúncio.
        produto: Bling ``produto``; type ``Produto | None``; opcional.
        titulo: Bling ``titulo``; type ``str | None``; opcional. Título do anúncio.
        descricao: Bling ``descricao``; type ``str | None``; opcional. Descrição do anúncio.
        status: Bling ``status``; type ``int | None``; opcional. Situação do anúncio.
        atributos: Bling ``atributos``; type ``list[AnunciosAtributoDTO] | None``; opcional.
        imagens: Bling ``imagens``; type ``list[AnunciosImagemDTO] | None``; opcional.
        variacoes: Bling ``variacoes``; type ``list[AnunciosVariacaoDTO] | None``; opcional."""

    id: int | None = Field(default=None, examples=[1])
    produto: Produto | None = None
    titulo: str | None = Field(default=None, examples=["Anúncio 1"])
    descricao: str | None = Field(default=None, examples=["Descrição do anúncio."])
    status: int | None = Field(default=None, examples=[1])
    atributos: list[AnunciosAtributoDTO] | None = None
    imagens: list[AnunciosImagemDTO] | None = None
    variacoes: list[AnunciosVariacaoDTO] | None = None


class AnunciosCategoriaDTO(BlingModel):
    """OpenAPI schema ``AnunciosCategoriaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID da categoria.
        nome: Bling ``nome``; type ``str | None``; opcional. Nome da categoria."""

    id: int | None = Field(default=None, examples=[101])
    nome: str | None = Field(default=None, examples=["Roupas"])


class AnunciosSaveRequestBase(BlingModel):
    """OpenAPI schema ``AnunciosSaveRequestBase``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        produto: Bling ``produto``; type ``Produto1``; obrigatório.
        integracao: Bling ``integracao``; type ``Integracao``; obrigatório.
        loja: Bling ``loja``; type ``Loja``; obrigatório.
        nome: Bling ``nome``; type ``str | None``; opcional.
        descricao: Bling ``descricao``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``Preco | None``; opcional.
        anuncio_loja: Bling ``anuncioLoja``; type ``AnuncioLoja | None``; opcional.
        estoques: Bling ``estoques``; type ``Estoques | None``; opcional.
        categoria: Bling ``categoria``; type ``Categoria | None``; opcional.
        atributos: Bling ``atributos``; type ``list[Atributo] | None``; opcional.
        imagens: Bling ``imagens``; type ``list[Imagen] | None``; opcional.
        mercado_livre: Bling ``mercadoLivre``; type ``MercadoLivre | None``; opcional."""

    produto: Produto1
    integracao: Integracao
    loja: Loja
    nome: str | None = Field(default=None, examples=["Nome do anúncio"])
    descricao: str | None = Field(default=None, examples=["Descrição do anúncio"])
    preco: Preco | None = None
    anuncio_loja: AnuncioLoja | None = Field(
        default=None,
        validation_alias=AliasChoices("anuncio_loja", "anuncioLoja"),
        serialization_alias="anuncioLoja",
    )
    estoques: Estoques | None = None
    categoria: Categoria | None = None
    atributos: list[Atributo] | None = None
    imagens: list[Imagen] | None = None
    mercado_livre: MercadoLivre | None = Field(
        default=None,
        validation_alias=AliasChoices("mercado_livre", "mercadoLivre"),
        serialization_alias="mercadoLivre",
    )


class AnunciosSaveRequest(AnunciosSaveRequestBase):
    """OpenAPI schema ``AnunciosSaveRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: AnunciosSaveRequestBase.

    Fields:
        produto: Bling ``produto``; type ``Produto1``; obrigatório.
        integracao: Bling ``integracao``; type ``Integracao``; obrigatório.
        loja: Bling ``loja``; type ``Loja``; obrigatório.
        nome: Bling ``nome``; type ``str | None``; opcional.
        descricao: Bling ``descricao``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``Preco | None``; opcional.
        anuncio_loja: Bling ``anuncioLoja``; type ``AnuncioLoja | None``; opcional.
        estoques: Bling ``estoques``; type ``Estoques | None``; opcional.
        categoria: Bling ``categoria``; type ``Categoria | None``; opcional.
        atributos: Bling ``atributos``; type ``list[Atributo] | None``; opcional.
        imagens: Bling ``imagens``; type ``list[Imagen] | None``; opcional.
        mercado_livre: Bling ``mercadoLivre``; type ``MercadoLivre | None``; opcional.
        variacoes: Bling ``variacoes``; type ``list[AnunciosSaveRequestBase] | None``; opcional."""

    variacoes: list[AnunciosSaveRequestBase] | None = None


class AnunciosSaveResponseDTO(BlingModel):
    """OpenAPI schema ``AnunciosSaveResponseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do anúncio salvo.
        ids_variacoes: Bling ``idsVariacoes``; type ``list[int] | None``; opcional. Lista de IDs das variações associadas ao anúncio."""

    id: int | None = Field(default=None, examples=[123])
    ids_variacoes: list[int] | None = Field(
        default=None,
        validation_alias=AliasChoices("ids_variacoes", "idsVariacoes"),
        serialization_alias="idsVariacoes",
    )


class AnunciosGetResponse200(BlingModel):
    """OpenAPI schema ``AnunciosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``AnunciosGetAllResponseDTO | None``; opcional."""

    data: AnunciosGetAllResponseDTO | None = None


class AnunciosPostResponse201(BlingModel):
    """OpenAPI schema ``AnunciosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``AnunciosSaveResponseDTO | None``; opcional."""

    data: AnunciosSaveResponseDTO | None = None


class AnunciosIdAnuncioGetResponse200(BlingModel):
    """OpenAPI schema ``AnunciosIdAnuncioGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``AnunciosGetByIdResponseDTO | None``; opcional."""

    data: AnunciosGetByIdResponseDTO | None = None


__all__ = [
    "AnunciosAtributoDTO",
    "AnunciosCategoriaDTO",
    "AnunciosGetAllResponseDTO",
    "AnunciosGetAttributesFromCategoryResponseDTO",
    "AnunciosGetByIdResponseDTO",
    "AnunciosGetResponse200",
    "AnunciosIdAnuncioGetResponse200",
    "AnunciosImagemDTO",
    "AnunciosPostResponse201",
    "AnunciosSaveRequest",
    "AnunciosSaveRequestBase",
    "AnunciosSaveResponseDTO",
    "AnunciosVariacaoDTO",
]
