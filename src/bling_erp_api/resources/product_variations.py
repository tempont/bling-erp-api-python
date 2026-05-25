"""Produtos — Variações resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.models.generated.product_variations import (
        ProductVariationAttributeRenameRequest,
        ProductVariationCombinationRequest,
    )
    from bling_erp_api.types import JsonObject


class ProductVariationsResource(BaseResource):
    """Operações em ``/produtos/variacoes``."""

    def gerar_combinacoes(
        self, dados: ProductVariationCombinationRequest | JsonObject
    ) -> JsonObject:
        """Calcula combinações de variações (não persiste)."""
        return self._post(
            "/produtos/variacoes/atributos/gerar-combinacoes",
            json=to_json_object(dados),
        )

    def listar(self, id_produto_pai: int) -> JsonObject:
        """Obtém produto pai e suas variações."""
        return self._get(f"/produtos/variacoes/{id_produto_pai}")

    def alterar_atributo(
        self,
        id_produto_pai: int,
        dados: ProductVariationAttributeRenameRequest | JsonObject,
    ) -> JsonObject:
        """Renomeia atributos nas variações."""
        return self._patch(
            f"/produtos/variacoes/{id_produto_pai}/atributos",
            json=to_json_object(dados),
        )
