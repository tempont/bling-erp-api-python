# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``produtos_fornecedores``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse, Data29


class FornecedorContatoDTO(BlingModel):
    """OpenAPI schema ``FornecedorContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do contato
        nome: Bling ``nome``; type ``str | None``; opcional. Nome do contato"""

    id: int | None = Field(default=None, examples=[123456789])
    nome: str | None = Field(default=None, examples=["Fornecedor padrão"])


class ProdutoFornecedorDTO(BlingModel):
    """OpenAPI schema ``ProdutoFornecedorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do vínculo entre Produto e Fornecedor
        contato: Bling ``contato``; type ``FornecedorContatoDTO | None``; opcional.
        codigo: Bling ``codigo``; type ``str | None``; opcional. Código do produto no fornecedor
        preco_custo: Bling ``precoCusto``; type ``float | None``; opcional. Preço de custo do produto no fornecedor
        preco_compra: Bling ``precoCompra``; type ``float | None``; opcional. Preço de compra do produto no fornecedor"""

    id: int | None = Field(default=None, examples=[123456789])
    contato: FornecedorContatoDTO | None = None
    codigo: str | None = Field(default=None, examples=["SKU-FORNECEDOR"])
    preco_custo: float | None = Field(default=None, alias="precoCusto", examples=[55.55])
    preco_compra: float | None = Field(default=None, alias="precoCompra", examples=[55.55])


class ProdutosFornecedoresDadosDTO(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        garantia: Bling ``garantia``; type ``int | None``; opcional. Quantidade de meses de garantia."""

    garantia: int | None = Field(default=None, examples=[3])


class ProdutosFornecedoresDadosUpdateDTO(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresDadosUpdateDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        garantia: Bling ``garantia``; type ``int | None``; opcional. Quantidade de meses de garantia."""

    garantia: int | None = Field(default=None, examples=[3])


class ProdutosFornecedoresFornecedorDTO(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresFornecedorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ProdutosFornecedoresFornecedorUpdateDTO(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresFornecedorUpdateDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])


class ProdutosFornecedoresProdutoDTO(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ProdutosFornecedoresPostResponse201(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class ProdutosFornecedoresIdProdutoFornecedorPutResponse200(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresIdProdutoFornecedorPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class ProdutosFornecedoresDadosBaseDTO(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Utilizado no GET.
        descricao: Bling ``descricao``; type ``str | None``; opcional. Descrição do produto no fornecedor.
        codigo: Bling ``codigo``; type ``str | None``; opcional. Código do produto no fornecedor.
        preco_custo: Bling ``precoCusto``; type ``float | None``; opcional. Valor de compra do produto com rateio de frete, descontos e impostos.
        preco_compra: Bling ``precoCompra``; type ``float | None``; opcional. Valor de compra do produto.
        padrao: Bling ``padrao``; type ``bool | None``; opcional. Indica se é o fornecedor padrão do produto.
        produto: Bling ``produto``; type ``ProdutosFornecedoresProdutoDTO | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``ProdutosFornecedoresFornecedorDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    descricao: str | None = Field(default=None, examples=["Copo do Bling"])
    codigo: str | None = Field(default=None, examples=["COD-123"])
    preco_custo: float | None = Field(default=None, alias="precoCusto", examples=[5.9])
    preco_compra: float | None = Field(default=None, alias="precoCompra", examples=[3.5])
    padrao: bool | None = Field(default=None, examples=[False])
    produto: ProdutosFornecedoresProdutoDTO | None = None
    fornecedor: ProdutosFornecedoresFornecedorDTO | None = None


class ProdutosFornecedoresDadosBaseUpdateDTO(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresDadosBaseUpdateDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Utilizado no GET.
        descricao: Bling ``descricao``; type ``str | None``; opcional. Descrição do produto no fornecedor.
        codigo: Bling ``codigo``; type ``str | None``; opcional. Código do produto no fornecedor.
        preco_custo: Bling ``precoCusto``; type ``float | None``; opcional. Valor de compra do produto com rateio de frete, descontos e impostos.
        preco_compra: Bling ``precoCompra``; type ``float | None``; opcional. Valor de compra do produto.
        padrao: Bling ``padrao``; type ``bool | None``; opcional. Indica se é o fornecedor padrão do produto.
        produto: Bling ``produto``; type ``ProdutosFornecedoresProdutoDTO | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``ProdutosFornecedoresFornecedorUpdateDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    descricao: str | None = Field(default=None, examples=["Copo do Bling"])
    codigo: str | None = Field(default=None, examples=["COD-123"])
    preco_custo: float | None = Field(default=None, alias="precoCusto", examples=[5.9])
    preco_compra: float | None = Field(default=None, alias="precoCompra", examples=[3.5])
    padrao: bool | None = Field(default=None, examples=[False])
    produto: ProdutosFornecedoresProdutoDTO | None = None
    fornecedor: ProdutosFornecedoresFornecedorUpdateDTO | None = None


class ProdutosFornecedoresGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ProdutosFornecedoresDadosBaseDTO] | None``; opcional."""

    data: list[ProdutosFornecedoresDadosBaseDTO] | None = None


class ProdutosFornecedoresPostRequest(
    ProdutosFornecedoresDadosBaseDTO, ProdutosFornecedoresDadosDTO
):
    """OpenAPI schema ``ProdutosFornecedoresPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ProdutosFornecedoresDadosBaseDTO, ProdutosFornecedoresDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Utilizado no GET.
        descricao: Bling ``descricao``; type ``str | None``; opcional. Descrição do produto no fornecedor.
        codigo: Bling ``codigo``; type ``str | None``; opcional. Código do produto no fornecedor.
        preco_custo: Bling ``precoCusto``; type ``float | None``; opcional. Valor de compra do produto com rateio de frete, descontos e impostos.
        preco_compra: Bling ``precoCompra``; type ``float | None``; opcional. Valor de compra do produto.
        padrao: Bling ``padrao``; type ``bool | None``; opcional. Indica se é o fornecedor padrão do produto.
        produto: Bling ``produto``; type ``ProdutosFornecedoresProdutoDTO | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``ProdutosFornecedoresFornecedorDTO | None``; opcional.
        garantia: Bling ``garantia``; type ``int | None``; opcional. Quantidade de meses de garantia."""

    pass


class ProdutosFornecedoresIdProdutoFornecedorGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosFornecedoresIdProdutoFornecedorGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data29 | None``; opcional."""

    data: Data29 | None = None


class ProdutosFornecedoresIdProdutoFornecedorPutRequest(
    ProdutosFornecedoresDadosBaseUpdateDTO, ProdutosFornecedoresDadosUpdateDTO
):
    """OpenAPI schema ``ProdutosFornecedoresIdProdutoFornecedorPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ProdutosFornecedoresDadosBaseUpdateDTO, ProdutosFornecedoresDadosUpdateDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Utilizado no GET.
        descricao: Bling ``descricao``; type ``str | None``; opcional. Descrição do produto no fornecedor.
        codigo: Bling ``codigo``; type ``str | None``; opcional. Código do produto no fornecedor.
        preco_custo: Bling ``precoCusto``; type ``float | None``; opcional. Valor de compra do produto com rateio de frete, descontos e impostos.
        preco_compra: Bling ``precoCompra``; type ``float | None``; opcional. Valor de compra do produto.
        padrao: Bling ``padrao``; type ``bool | None``; opcional. Indica se é o fornecedor padrão do produto.
        produto: Bling ``produto``; type ``ProdutosFornecedoresProdutoDTO | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``ProdutosFornecedoresFornecedorUpdateDTO | None``; opcional.
        garantia: Bling ``garantia``; type ``int | None``; opcional. Quantidade de meses de garantia."""

    pass


__all__ = [
    "FornecedorContatoDTO",
    "ProdutoFornecedorDTO",
    "ProdutosFornecedoresDadosBaseDTO",
    "ProdutosFornecedoresDadosBaseUpdateDTO",
    "ProdutosFornecedoresDadosDTO",
    "ProdutosFornecedoresDadosUpdateDTO",
    "ProdutosFornecedoresFornecedorDTO",
    "ProdutosFornecedoresFornecedorUpdateDTO",
    "ProdutosFornecedoresGetResponse200",
    "ProdutosFornecedoresIdProdutoFornecedorGetResponse200",
    "ProdutosFornecedoresIdProdutoFornecedorPutRequest",
    "ProdutosFornecedoresIdProdutoFornecedorPutResponse200",
    "ProdutosFornecedoresPostRequest",
    "ProdutosFornecedoresPostResponse201",
    "ProdutosFornecedoresProdutoDTO",
]
