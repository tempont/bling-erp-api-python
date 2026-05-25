"""Semi-generated models for Produtos — Variações."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class ProductVariationAttributeOption(BlingModel):
    """Atributo e opções de variação (ProdutosVariacoesAtributoDTO)."""

    nome: str
    opcoes: list[str] = Field(default_factory=list)


class ProductVariationParentDTO(BlingModel):
    """Referência ao produto pai (ProdutosVariacoesProdutoPaiDTO)."""

    id: int | None = None


class ProductVariationCombinationRequest(BlingModel):
    """Corpo POST ``/produtos/variacoes/atributos/gerar-combinacoes``."""

    produto_pai: ProductVariationParentDTO = Field(alias="produtoPai")
    atributos: list[ProductVariationAttributeOption] = Field(default_factory=list)


class ProductVariationAttributeRenameRequest(BlingModel):
    """PATCH atributos (ProdutosVariacoesDadosAtributoDTO)."""

    nome_antigo: str = Field(alias="atributoAntigo")
    nome_novo: str = Field(alias="atributoNovo")
