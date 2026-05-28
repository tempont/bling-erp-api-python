# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``produtos_lojas``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .categorias_produtos import CategoriasProdutos
    from .common import CategoriasProduto, Data30, Data31


class ProdutosLojasCategoriaDTO(BlingModel):
    """OpenAPI schema ``ProdutosLojasCategoriaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID da categoria de produto"""

    id: int = Field(..., examples=[12345678])


class ProdutosLojasFornecedorLojaDTO(BlingModel):
    """OpenAPI schema ``ProdutosLojasFornecedorLojaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID do fornecedor na loja virtual"""

    id: int = Field(..., examples=[12345678])


class ProdutosLojasLojaDTO(BlingModel):
    """OpenAPI schema ``ProdutosLojasLojaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID da loja no Bling"""

    id: int = Field(..., examples=[12345678])


class ProdutosLojasMarcaLojaDTO(BlingModel):
    """OpenAPI schema ``ProdutosLojasMarcaLojaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID da marca do produto na loja virtual"""

    id: int = Field(..., examples=[12345678])


class ProdutosLojasProdutoDTO(BlingModel):
    """OpenAPI schema ``ProdutosLojasProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID do produto no Bling"""

    id: int = Field(..., examples=[12345678])


class ProdutosLojasResponsePOSTPUT(BlingModel):
    """OpenAPI schema ``ProdutosLojasResponsePOSTPUT``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        categorias_produtos: Bling ``categoriasProdutos``; type ``list[CategoriasProduto] | None``; opcional."""

    categorias_produtos: list[CategoriasProduto] | None = Field(
        default=None,
        validation_alias=AliasChoices("categorias_produtos", "categoriasProdutos"),
        serialization_alias="categoriasProdutos",
    )


class ProdutosLojasPostResponse201(BlingModel):
    """OpenAPI schema ``ProdutosLojasPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data30 | None``; opcional."""

    data: Data30 | None = None


class ProdutosLojasIdProdutoLojaPutResponse200(BlingModel):
    """OpenAPI schema ``ProdutosLojasIdProdutoLojaPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data30 | None``; opcional."""

    data: Data30 | None = None


class ProdutosLojasDadosBaseDTO(BlingModel):
    """OpenAPI schema ``ProdutosLojasDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        codigo: Bling ``codigo``; type ``str``; obrigatório. Código do produto na loja virtual
        preco: Bling ``preco``; type ``float | None``; opcional.
        preco_promocional: Bling ``precoPromocional``; type ``float | None``; opcional.
        produto: Bling ``produto``; type ``ProdutosLojasProdutoDTO``; obrigatório.
        loja: Bling ``loja``; type ``ProdutosLojasLojaDTO``; obrigatório.
        fornecedor_loja: Bling ``fornecedorLoja``; type ``ProdutosLojasFornecedorLojaDTO | None``; opcional.
        marca_loja: Bling ``marcaLoja``; type ``ProdutosLojasMarcaLojaDTO | None``; opcional.
        categorias_produtos: Bling ``categoriasProdutos``; type ``ProdutosLojasCategoriaDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    codigo: str = Field(..., examples=["ASDF1234"])
    preco: float | None = Field(default=None, examples=[25.99])
    preco_promocional: float | None = Field(
        default=None,
        validation_alias=AliasChoices("preco_promocional", "precoPromocional"),
        examples=[22.99],
        serialization_alias="precoPromocional",
    )
    produto: ProdutosLojasProdutoDTO
    loja: ProdutosLojasLojaDTO
    fornecedor_loja: ProdutosLojasFornecedorLojaDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("fornecedor_loja", "fornecedorLoja"),
        serialization_alias="fornecedorLoja",
    )
    marca_loja: ProdutosLojasMarcaLojaDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("marca_loja", "marcaLoja"),
        serialization_alias="marcaLoja",
    )
    categorias_produtos: ProdutosLojasCategoriaDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("categorias_produtos", "categoriasProdutos"),
        serialization_alias="categoriasProdutos",
    )


class ProdutosLojasDadosDTO(ProdutosLojasDadosBaseDTO):
    """OpenAPI schema ``ProdutosLojasDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ProdutosLojasDadosBaseDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        codigo: Bling ``codigo``; type ``str``; obrigatório. Código do produto na loja virtual
        preco: Bling ``preco``; type ``float | None``; opcional.
        preco_promocional: Bling ``precoPromocional``; type ``float | None``; opcional.
        produto: Bling ``produto``; type ``ProdutosLojasProdutoDTO``; obrigatório.
        loja: Bling ``loja``; type ``ProdutosLojasLojaDTO``; obrigatório.
        fornecedor_loja: Bling ``fornecedorLoja``; type ``ProdutosLojasFornecedorLojaDTO | None``; opcional.
        marca_loja: Bling ``marcaLoja``; type ``ProdutosLojasMarcaLojaDTO | None``; opcional.
        categorias_produtos: Bling ``categoriasProdutos``; type ``list[ProdutosLojasCategoriaDTO] | CategoriasProdutos | None``; opcional."""

    categorias_produtos: list[ProdutosLojasCategoriaDTO] | CategoriasProdutos | None = Field(
        default=None,
        validation_alias=AliasChoices("categorias_produtos", "categoriasProdutos"),
        serialization_alias="categoriasProdutos",
    )


class ProdutosLojasGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosLojasGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ProdutosLojasDadosDTO] | None``; opcional."""

    data: list[ProdutosLojasDadosDTO] | None = None


class ProdutosLojasPostRequest(ProdutosLojasDadosDTO, ProdutosLojasDadosBaseDTO):
    """OpenAPI schema ``ProdutosLojasPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ProdutosLojasDadosDTO, ProdutosLojasDadosBaseDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        codigo: Bling ``codigo``; type ``str``; obrigatório. Código do produto na loja virtual
        preco: Bling ``preco``; type ``float | None``; opcional.
        preco_promocional: Bling ``precoPromocional``; type ``float | None``; opcional.
        produto: Bling ``produto``; type ``ProdutosLojasProdutoDTO``; obrigatório.
        loja: Bling ``loja``; type ``ProdutosLojasLojaDTO``; obrigatório.
        fornecedor_loja: Bling ``fornecedorLoja``; type ``ProdutosLojasFornecedorLojaDTO | None``; opcional.
        marca_loja: Bling ``marcaLoja``; type ``ProdutosLojasMarcaLojaDTO | None``; opcional.
        categorias_produtos: Bling ``categoriasProdutos``; type ``list[ProdutosLojasCategoriaDTO] | CategoriasProdutos | None``; opcional."""

    pass


class ProdutosLojasIdProdutoLojaGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosLojasIdProdutoLojaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data31 | None``; opcional."""

    data: Data31 | None = None


class ProdutosLojasIdProdutoLojaPutRequest(ProdutosLojasDadosDTO, ProdutosLojasDadosBaseDTO):
    """OpenAPI schema ``ProdutosLojasIdProdutoLojaPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ProdutosLojasDadosDTO, ProdutosLojasDadosBaseDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        codigo: Bling ``codigo``; type ``str``; obrigatório. Código do produto na loja virtual
        preco: Bling ``preco``; type ``float | None``; opcional.
        preco_promocional: Bling ``precoPromocional``; type ``float | None``; opcional.
        produto: Bling ``produto``; type ``ProdutosLojasProdutoDTO``; obrigatório.
        loja: Bling ``loja``; type ``ProdutosLojasLojaDTO``; obrigatório.
        fornecedor_loja: Bling ``fornecedorLoja``; type ``ProdutosLojasFornecedorLojaDTO | None``; opcional.
        marca_loja: Bling ``marcaLoja``; type ``ProdutosLojasMarcaLojaDTO | None``; opcional.
        categorias_produtos: Bling ``categoriasProdutos``; type ``list[ProdutosLojasCategoriaDTO] | CategoriasProdutos | None``; opcional."""

    pass


__all__ = [
    "ProdutosLojasCategoriaDTO",
    "ProdutosLojasDadosBaseDTO",
    "ProdutosLojasDadosDTO",
    "ProdutosLojasFornecedorLojaDTO",
    "ProdutosLojasGetResponse200",
    "ProdutosLojasIdProdutoLojaGetResponse200",
    "ProdutosLojasIdProdutoLojaPutRequest",
    "ProdutosLojasIdProdutoLojaPutResponse200",
    "ProdutosLojasLojaDTO",
    "ProdutosLojasMarcaLojaDTO",
    "ProdutosLojasPostRequest",
    "ProdutosLojasPostResponse201",
    "ProdutosLojasProdutoDTO",
    "ProdutosLojasResponsePOSTPUT",
]
