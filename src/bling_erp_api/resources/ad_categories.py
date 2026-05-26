"""Anúncios - Categorias resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, QueryParams


def _ad_categories_list_params(
    *,
    id_categoria: int | None = None,
    tipo_produto: str | None = None,
) -> QueryParams:
    """Build query params for GET /anuncios/categorias from SDK param names."""
    return compact_params(
        {
            "idCategoria": id_categoria,
            "tipoProduto": tipo_produto,
        }
    )


class AdCategoriesResource(BaseResource):
    """Operações de categorias de anúncios do Bling.

    Este recurso mapeia os endpoints ``/anuncios/categorias``. Os métodos
    canônicos usam português para acompanhar a documentação oficial; os
    métodos em inglês continuam disponíveis como aliases de compatibilidade.
    """

    def listar(
        self,
        *,
        tipo_integracao: str,
        id_loja: int,
        id_categoria: int | None = None,
        tipo_produto: str | None = None,
    ) -> JsonObject:
        """Lista categorias de anúncios.

        Endpoint: GET /anuncios/categorias

        Obtém categorias de anúncios.

        Args:
            tipo_integracao: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            id_loja: ID da loja (Bling: ``idLoja``, integer, obrigatório)
            id_categoria: ID da categoria (Bling: ``idCategoria``, integer, opcional)
            tipo_produto: Tipo do produto (Bling: ``tipoProduto``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: AnunciosCategoriaDTO; 400: ErrorResponse
        """
        params: QueryParams = {
            "tipoIntegracao": tipo_integracao,
            "idLoja": id_loja,
            **_ad_categories_list_params(id_categoria=id_categoria, tipo_produto=tipo_produto),
        }
        return self._get("/anuncios/categorias", params=params)

    def list(
        self,
        *,
        integration_type: str,
        store_id: int,
        category_id: int | None = None,
        product_type: str | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lista categorias de anúncios.

        Endpoint: GET /anuncios/categorias

        Obtém categorias de anúncios.

        Args:
            integration_type: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            store_id: ID da loja (Bling: ``idLoja``, integer, obrigatório)
            category_id: ID da categoria (Bling: ``idCategoria``, integer, opcional)
            product_type: Tipo do produto (Bling: ``tipoProduto``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: AnunciosCategoriaDTO; 400: ErrorResponse
        """
        return self.listar(
            tipo_integracao=integration_type,
            id_loja=store_id,
            id_categoria=category_id,
            tipo_produto=product_type,
        )

    def obter(
        self,
        id_categoria: str,
        *,
        tipo_integracao: str,
        id_loja: int,
    ) -> JsonObject:
        """Obtém uma categoria de anúncio com atributos.

        Endpoint: GET /anuncios/categorias/{idCategoria}

        Obtém uma categoria de anúncio pelo ID com seus atributos.

        Args:
            id_categoria: ID da categoria no marketplace (Bling: ``idCategoria``, string, obrigatório)
            tipo_integracao: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            id_loja: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: AnunciosGetAttributesFromCategoryResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        params = compact_params(
            {
                "tipoIntegracao": tipo_integracao,
                "idLoja": id_loja,
            }
        )
        return self._get(f"/anuncios/categorias/{id_categoria}", params=params)

    def get(
        self,
        category_id: str,
        *,
        integration_type: str,
        store_id: int,
    ) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém uma categoria de anúncio com atributos.

        Endpoint: GET /anuncios/categorias/{idCategoria}

        Obtém uma categoria de anúncio pelo ID com seus atributos.

        Args:
            category_id: ID da categoria no marketplace (Bling: ``idCategoria``, string, obrigatório)
            integration_type: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            store_id: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: AnunciosGetAttributesFromCategoryResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.obter(
            id_categoria=category_id, tipo_integracao=integration_type, id_loja=store_id
        )
