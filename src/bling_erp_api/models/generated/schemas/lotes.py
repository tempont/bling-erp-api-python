# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``lotes``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import ErrorResponse, LotResponseDTO
    from .lotes_lancamentos import LoteLancamentoDTO


class LotesDepositoDTO(BlingModel):
    """OpenAPI schema ``LotesDepositoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LotePutRequestDTO(BlingModel):
    """OpenAPI schema ``LotePutRequestDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        codigo_lote: Bling ``codigoLote``; type ``str | None``; opcional.
        data_fabricacao: Bling ``dataFabricacao``; type ``str | None``; opcional.
        data_validade: Bling ``dataValidade``; type ``str | None``; opcional.
        dias_permitido_venda: Bling ``diasPermitidoVenda``; type ``int | None``; opcional.
        codigo_agregacao: Bling ``codigoAgregacao``; type ``str | None``; opcional."""

    codigo_lote: str | None = Field(default=None, alias="codigoLote", examples=["Lote 1"])
    data_fabricacao: str | None = Field(
        default=None, alias="dataFabricacao", examples=["2021-01-01"]
    )
    data_validade: str | None = Field(default=None, alias="dataValidade", examples=["2021-01-01"])
    dias_permitido_venda: int | None = Field(
        default=None, alias="diasPermitidoVenda", examples=[10]
    )
    codigo_agregacao: str | None = Field(
        default=None, alias="codigoAgregacao", examples=["12345678"]
    )


class LoteStatusDTO(BlingModel):
    """OpenAPI schema ``LoteStatusDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        status: Bling ``status``; type ``int``; obrigatório. `1` Ativo <br> `2` Inativo"""

    status: int = Field(..., examples=[1])


class ProdutoControlaLotesDTO(BlingModel):
    """OpenAPI schema ``ProdutoControlaLotesDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id_produto: Bling ``idProduto``; type ``int``; obrigatório. ID do produto
        controla_lote: Bling ``controlaLote``; type ``bool | None``; opcional. Indica se o produto controla lote"""

    id_produto: int = Field(..., alias="idProduto", examples=[12345678])
    controla_lote: bool | None = Field(default=None, alias="controlaLote", examples=[True])


class LotesProdutoDTO(BlingModel):
    """OpenAPI schema ``LotesProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ProdutosLotesControlaLoteGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosLotesControlaLoteGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ProdutoControlaLotesDTO] | None``; opcional."""

    data: list[ProdutoControlaLotesDTO] | None = None


class ProdutosLotesIdLoteLancamentosGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosLotesIdLoteLancamentosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[LoteLancamentoDTO] | None``; opcional."""

    data: list[LoteLancamentoDTO] | None = None


class ProdutosLotesIdLoteLancamentosPostResponse200(BlingModel):
    """OpenAPI schema ``ProdutosLotesIdLoteLancamentosPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LoteLancamentoDTO | None``; opcional."""

    data: LoteLancamentoDTO | None = None


class ProdutosLotesLancamentosIdLancamentoGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosLotesLancamentosIdLancamentoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LoteLancamentoDTO | None``; opcional."""

    data: LoteLancamentoDTO | None = None


class LotesDTO(BlingModel):
    """OpenAPI schema ``LotesDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id_lote: Bling ``idLote``; type ``int``; obrigatório.
        codigo_lote: Bling ``codigoLote``; type ``str | None``; opcional.
        data_fabricacao: Bling ``dataFabricacao``; type ``str``; obrigatório.
        data_validade: Bling ``dataValidade``; type ``str``; obrigatório.
        dias_permitido_venda: Bling ``diasPermitidoVenda``; type ``int | None``; opcional.
        codigo_agregacao: Bling ``codigoAgregacao``; type ``str | None``; opcional.
        produto: Bling ``produto``; type ``LotesProdutoDTO``; obrigatório.
        deposito: Bling ``deposito``; type ``LotesDepositoDTO``; obrigatório.
        status: Bling ``status``; type ``int | None``; opcional. `1` Ativo <br> `2` Inativo"""

    id_lote: int = Field(..., alias="idLote", examples=["12345678"])
    codigo_lote: str | None = Field(default=None, alias="codigoLote", examples=["Lote 1"])
    data_fabricacao: str = Field(..., alias="dataFabricacao", examples=["2021-01-01"])
    data_validade: str = Field(..., alias="dataValidade", examples=["2021-01-01"])
    dias_permitido_venda: int | None = Field(
        default=None, alias="diasPermitidoVenda", examples=[10]
    )
    codigo_agregacao: str | None = Field(
        default=None, alias="codigoAgregacao", examples=["12345678"]
    )
    produto: LotesProdutoDTO
    deposito: LotesDepositoDTO
    status: int | None = Field(default=None, examples=[1])


class ProdutosLotesGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosLotesGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[LotesDTO] | None``; opcional."""

    data: list[LotesDTO] | None = None


class ProdutosLotesPutRequest(RootModel[list[LotesDTO]]):
    """OpenAPI schema ``ProdutosLotesPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        root: Bling ``root``; type ``list[LotesDTO]``; obrigatório."""

    root: list[LotesDTO]


class ProdutosLotesIdLoteGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosLotesIdLoteGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LotesDTO | None``; opcional."""

    data: LotesDTO | None = None


class SaveResponseLotsDTO(BlingModel):
    """OpenAPI schema ``SaveResponseLotsDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        saved: Bling ``saved``; type ``list[LotResponseDTO] | None``; opcional.
        errors: Bling ``errors``; type ``list[ErrorResponse] | None``; opcional."""

    saved: list[LotResponseDTO] | None = None
    errors: list[ErrorResponse] | None = None


class ProdutosLotesPutResponse200(BlingModel):
    """OpenAPI schema ``ProdutosLotesPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``SaveResponseLotsDTO | None``; opcional."""

    data: SaveResponseLotsDTO | None = None


__all__ = [
    "LotePutRequestDTO",
    "LoteStatusDTO",
    "LotesDTO",
    "LotesDepositoDTO",
    "LotesProdutoDTO",
    "ProdutoControlaLotesDTO",
    "ProdutosLotesControlaLoteGetResponse200",
    "ProdutosLotesGetResponse200",
    "ProdutosLotesIdLoteGetResponse200",
    "ProdutosLotesIdLoteLancamentosGetResponse200",
    "ProdutosLotesIdLoteLancamentosPostResponse200",
    "ProdutosLotesLancamentosIdLancamentoGetResponse200",
    "ProdutosLotesPutRequest",
    "ProdutosLotesPutResponse200",
    "SaveResponseLotsDTO",
]
