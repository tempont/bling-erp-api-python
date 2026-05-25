"""Produtos — Estruturas (composição) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Sequence

    from bling_erp_api.models.generated.product_structures import (
        ProductStructureComponent,
        ProductStructureUpdateRequest,
    )
    from bling_erp_api.types import JsonObject


class ProductStructuresResource(BaseResource):
    """Operações em ``/produtos/estruturas``."""

    def remover_varios(self, ids_produtos: Sequence[int]) -> JsonObject:
        """Remove estruturas de múltiplos produtos (``DELETE``)."""
        return self._delete(
            "/produtos/estruturas",
            params=compact_params({"idsProdutos[]": list(ids_produtos)}),
        )

    def obter(self, id_produto_estrutura: int) -> JsonObject:
        """Obtém estrutura por ``idProdutoEstrutura``."""
        return self._get(f"/produtos/estruturas/{id_produto_estrutura}")

    def alterar(
        self,
        id_produto_estrutura: int,
        dados: ProductStructureUpdateRequest | JsonObject,
    ) -> JsonObject:
        """Substitui a estrutura do produto (``PUT``)."""
        return self._put(
            f"/produtos/estruturas/{id_produto_estrutura}",
            json=to_json_object(dados),
        )

    def remover_componentes(
        self,
        id_produto_estrutura: int,
        *,
        ids_componentes: Sequence[int],
    ) -> JsonObject:
        """Remove componentes da estrutura (``DELETE``)."""
        return self._delete(
            f"/produtos/estruturas/{id_produto_estrutura}/componentes",
            params=compact_params({"idsComponentes[]": list(ids_componentes)}),
        )

    def vincular_componentes(
        self,
        id_produto_estrutura: int,
        componentes: Sequence[ProductStructureComponent | JsonObject],
    ) -> JsonObject:
        """Adiciona componentes (corpo JSON em array ``ProdutosComponenteDTO``)."""
        payload = [to_json_object(c) for c in componentes]
        return self._post(
            f"/produtos/estruturas/{id_produto_estrutura}/componentes",
            json=payload,
        )

    def alterar_componente(
        self,
        id_produto_estrutura: int,
        id_componente: int,
        dados: ProductStructureComponent | JsonObject,
    ) -> JsonObject:
        """Altera um componente (``PATCH``)."""
        return self._patch(
            f"/produtos/estruturas/{id_produto_estrutura}/componentes/{id_componente}",
            json=to_json_object(dados),
        )
