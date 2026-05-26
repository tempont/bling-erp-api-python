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
        """Retorna o produto pai com combinações de novas variações.

        Endpoint: POST /produtos/variacoes/atributos/gerar-combinacoes

        Ação responsável por retornar o produto pai com combinação de novas variações a partir dos atributos. Esta ação não persistirá os dados.

        Request body schema: ProdutosVariacoesCombinacaoDadosDTO

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosDTO; 400: ErrorResponse
        """
        return self._post(
            "/produtos/variacoes/atributos/gerar-combinacoes",
            json=to_json_object(dados),
        )

    def listar(self, id_produto_pai: int) -> JsonObject:
        """Obtém o produto e variações.

        Endpoint: GET /produtos/variacoes/{idProdutoPai}

        Obtém o produto e variações pelo ID do produto pai.

        Args:
            id_produto_pai: ID do produto pai (Bling: ``idProdutoPai``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/produtos/variacoes/{id_produto_pai}")

    def alterar_atributo(
        self,
        id_produto_pai: int,
        dados: ProductVariationAttributeRenameRequest | JsonObject,
    ) -> JsonObject:
        """Altera o nome do atributo nas variações.

        Endpoint: PATCH /produtos/variacoes/{idProdutoPai}/atributos

        Altera o nome do atributo nas variações de um produto pai.

        Args:
            id_produto_pai: ID do produto pai (Bling: ``idProdutoPai``, integer, obrigatório)
            dados: Dados do atributo a ser alterado.

        Request body schema: ProdutosVariacoesDadosAtributoDTO

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse; 400: ErrorResponse
        """
        return self._patch(
            f"/produtos/variacoes/{id_produto_pai}/atributos",
            json=to_json_object(dados),
        )
