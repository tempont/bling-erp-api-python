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
        """Remove a estrutura de múltiplos produtos.

        Endpoint: DELETE /produtos/estruturas

        Remove a estrutura de múltiplos produtos com composição pelos IDs.

        Args:
            ids_produtos: IDs dos produtos (Bling: ``idsProdutos[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: Error; 400: ErrorResponse
        """
        return self._delete(
            "/produtos/estruturas",
            params=compact_params({"idsProdutos[]": list(ids_produtos)}),
        )

    def obter(self, id_produto_estrutura: int) -> JsonObject:
        """Obtém a estrutura de um produto com composição.

        Endpoint: GET /produtos/estruturas/{idProdutoEstrutura}

        Obtém a estrutura de um produto com composição pelo ID.

        Args:
            id_produto_estrutura: ID do produto com composição (Bling: ``idProdutoEstrutura``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosEstruturaDTO; 404: ErrorResponse
        """
        return self._get(f"/produtos/estruturas/{id_produto_estrutura}")

    def alterar(
        self,
        id_produto_estrutura: int,
        dados: ProductStructureUpdateRequest | JsonObject,
    ) -> JsonObject:
        """Altera a estrutura de um produto com composição.

        Endpoint: PUT /produtos/estruturas/{idProdutoEstrutura}

        Altera a estrutura de um produto com composição pelo ID.

        Args:
            id_produto_estrutura: ID do produto com composição (Bling: ``idProdutoEstrutura``, integer, obrigatório)
            dados: Dados da estrutura do produto.

        Request body schema: ProdutosEstruturaDTO

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
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
        """Remove componentes específicos de um produto com composição.

        Endpoint: DELETE /produtos/estruturas/{idProdutoEstrutura}/componentes

        Remove os componentes de um produto com composição pelos IDs dos componentes.

        Args:
            id_produto_estrutura: ID do produto com composição (Bling: ``idProdutoEstrutura``, integer, obrigatório)
            ids_componentes: IDs dos produtos (Bling: ``idsComponentes[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(
            f"/produtos/estruturas/{id_produto_estrutura}/componentes",
            params=compact_params({"idsComponentes[]": list(ids_componentes)}),
        )

    def vincular_componentes(
        self,
        id_produto_estrutura: int,
        componentes: Sequence[ProductStructureComponent | JsonObject],
    ) -> JsonObject:
        """Adiciona componente(s) a uma estrutura.

        Endpoint: POST /produtos/estruturas/{idProdutoEstrutura}/componentes

        Adiciona múltiplos componentes a uma estrutura pelo ID.

        Args:
            id_produto_estrutura: ID do produto com composição (Bling: ``idProdutoEstrutura``, integer, obrigatório)
            componentes: Dados dos componentes a serem vinculados.

        Request body schema: ProdutosComponenteDTO

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
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
        """Altera um componente de uma estrutura.

        Endpoint: PATCH /produtos/estruturas/{idProdutoEstrutura}/componentes/{idComponente}

        Altera um componente de uma estrutura pelo ID.

        Args:
            id_produto_estrutura: ID do produto com composição (Bling: ``idProdutoEstrutura``, integer, obrigatório)
            id_componente: ID do componente (Bling: ``idComponente``, integer, obrigatório)
            dados: Dados do componente a serem alterados.

        Request body schema: ProdutosComponenteDTO

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(
            f"/produtos/estruturas/{id_produto_estrutura}/componentes/{id_componente}",
            json=to_json_object(dados),
        )
