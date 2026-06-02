# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``categorias_receitas_despesas``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Data5, Data6


class CategoriasReceitasDespesasDadosBaseDTO(BlingModel):
    """OpenAPI schema ``CategoriasReceitasDespesasDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        id_categoria_pai: Bling ``idCategoriaPai``; type ``int | None``; opcional. Id da categoria pai. Se for a categoria raíz será 0.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        tipo: Bling ``tipo``; type ``int``; obrigatório. `1` Despesa<br>`2` Receita<br>`3` Receita e despesa"""

    id: int | None = Field(default=None, examples=[12345678])
    id_categoria_pai: int | None = Field(
        default=None,
        validation_alias=AliasChoices("id_categoria_pai", "idCategoriaPai"),
        examples=[0],
        serialization_alias="idCategoriaPai",
    )
    descricao: str = Field(..., examples=["Vendas de mercadorias"])
    tipo: int = Field(..., examples=[1])


class CategoriasReceitasDespesasDadosDTO(BlingModel):
    """OpenAPI schema ``CategoriasReceitasDespesasDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativa <br> `1` Ativa"""

    situacao: int | None = Field(default=None, examples=[1])


class CategoriasReceitasDespesasDadosPostDTO(BlingModel):
    """OpenAPI schema ``CategoriasReceitasDespesasDadosPostDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        grupo_dre: Bling ``grupoDRE``; type ``int | None``; opcional. `1` Não exibir DRE<br>`2` Receita Operacional Bruta<br>`3` Deduções da Receita Bruta<br>`7` Despesas Operacionais<br>`8` Receita Financeira<br>`9` Despesa Financeira<br>`10` Outra..."""

    grupo_dre: int | None = Field(
        default=1,
        validation_alias=AliasChoices("grupo_dre", "grupoDRE"),
        examples=[1],
        serialization_alias="grupoDRE",
    )


class CategoriasReceitasDespesasGetResponse200(BlingModel):
    """OpenAPI schema ``CategoriasReceitasDespesasGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[CategoriasReceitasDespesasDadosBaseDTO] | None``; opcional."""

    data: list[CategoriasReceitasDespesasDadosBaseDTO] | None = None


class CategoriasReceitasDespesasPostRequest(
    CategoriasReceitasDespesasDadosPostDTO, CategoriasReceitasDespesasDadosBaseDTO
):
    """OpenAPI schema ``CategoriasReceitasDespesasPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CategoriasReceitasDespesasDadosPostDTO, CategoriasReceitasDespesasDadosBaseDTO.

    Fields:
        grupo_dre: Bling ``grupoDRE``; type ``int | None``; opcional. `1` Não exibir DRE<br>`2` Receita Operacional Bruta<br>`3` Deduções da Receita Bruta<br>`7` Despesas Operacionais<br>`8` Receita Financeira<br>`9` Despesa Financeira<br>`10` Outra...
        id: Bling ``id``; type ``int | None``; opcional.
        id_categoria_pai: Bling ``idCategoriaPai``; type ``int | None``; opcional. Id da categoria pai. Se for a categoria raíz será 0.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        tipo: Bling ``tipo``; type ``int``; obrigatório. `1` Despesa<br>`2` Receita<br>`3` Receita e despesa"""

    pass


class CategoriasReceitasDespesasPostResponse201(BlingModel):
    """OpenAPI schema ``CategoriasReceitasDespesasPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``CategoriasReceitasDespesasDadosBaseDTO | None``; opcional."""

    data: CategoriasReceitasDespesasDadosBaseDTO | None = None


class CategoriasReceitasDespesasIdCategoriaGetResponse200(BlingModel):
    """OpenAPI schema ``CategoriasReceitasDespesasIdCategoriaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data6 | None``; opcional."""

    data: Data6 | None = None


class CategoriasReceitasDespesasIdCategoriaPutRequest(
    CategoriasReceitasDespesasDadosPostDTO, CategoriasReceitasDespesasDadosBaseDTO
):
    """OpenAPI schema ``CategoriasReceitasDespesasIdCategoriaPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CategoriasReceitasDespesasDadosPostDTO, CategoriasReceitasDespesasDadosBaseDTO.

    Fields:
        grupo_dre: Bling ``grupoDRE``; type ``int | None``; opcional. `1` Não exibir DRE<br>`2` Receita Operacional Bruta<br>`3` Deduções da Receita Bruta<br>`7` Despesas Operacionais<br>`8` Receita Financeira<br>`9` Despesa Financeira<br>`10` Outra...
        id: Bling ``id``; type ``int | None``; opcional.
        id_categoria_pai: Bling ``idCategoriaPai``; type ``int | None``; opcional. Id da categoria pai. Se for a categoria raíz será 0.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        tipo: Bling ``tipo``; type ``int``; obrigatório. `1` Despesa<br>`2` Receita<br>`3` Receita e despesa"""

    pass


class CategoriasReceitasDespesasIdCategoriaPutResponse200(BlingModel):
    """OpenAPI schema ``CategoriasReceitasDespesasIdCategoriaPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``CategoriasReceitasDespesasDadosBaseDTO | None``; opcional."""

    data: CategoriasReceitasDespesasDadosBaseDTO | None = None


class CategoriasReceitasDespesasDeleteResponse200(BlingModel):
    """OpenAPI schema ``CategoriasReceitasDespesasDeleteResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data5 | None``; opcional."""

    data: Data5 | None = None


__all__ = [
    "CategoriasReceitasDespesasDadosBaseDTO",
    "CategoriasReceitasDespesasDadosDTO",
    "CategoriasReceitasDespesasDadosPostDTO",
    "CategoriasReceitasDespesasDeleteResponse200",
    "CategoriasReceitasDespesasGetResponse200",
    "CategoriasReceitasDespesasIdCategoriaGetResponse200",
    "CategoriasReceitasDespesasIdCategoriaPutRequest",
    "CategoriasReceitasDespesasIdCategoriaPutResponse200",
    "CategoriasReceitasDespesasPostRequest",
    "CategoriasReceitasDespesasPostResponse201",
]
