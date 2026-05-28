"""Categorias - Lojas resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.models.generated.store_categories import CategoriasLojasDadosDTO
    from bling_erp_api.types import JsonObject, QueryParams


def _store_categories_list_params(
    *,
    id_loja: int | None = None,
    id_categoria_produto: int | None = None,
    id_categoria_produto_pai: int | None = None,
) -> QueryParams:
    """Build query params for GET /categorias/lojas."""
    return compact_params(
        {
            "idLoja": id_loja,
            "idCategoriaProduto": id_categoria_produto,
            "idCategoriaProdutoPai": id_categoria_produto_pai,
        }
    )


class StoreCategoriesResource(BaseResource):
    """Operações de categorias de lojas do Bling.

    Este recurso mapeia os endpoints ``/categorias/lojas``. Os métodos canônicos
    usam português para acompanhar a documentação oficial; os métodos em inglês
    continuam disponíveis como aliases de compatibilidade.
    """

    def listar(
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        id_loja: int | None = None,
        id_categoria_produto: int | None = None,
        id_categoria_produto_pai: int | None = None,
    ) -> JsonObject:
        """Lista categorias de lojas.

        Endpoint: GET /categorias/lojas

        Obtém lista paginada de vínculos entre categorias de lojas e produtos.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            id_loja: ID da loja (Bling: ``idLoja``, integer, opcional)
            id_categoria_produto: ID da categoria de produto (Bling: ``idCategoriaProduto``, integer, opcional)
            id_categoria_produto_pai: ID da categoria de produto pai (Bling: ``idCategoriaProdutoPai``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: CategoriasLojasDadosDTO
        """
        params = _store_categories_list_params(
            id_loja=id_loja,
            id_categoria_produto=id_categoria_produto,
            id_categoria_produto_pai=id_categoria_produto_pai,
        )
        return self._get(f"/categorias/lojas?pagina={pagina}&limite={limite}", params=params)

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        store_id: int | None = None,
        product_category_id: int | None = None,
        parent_product_category_id: int | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lista categorias de lojas.

        Endpoint: GET /categorias/lojas

        Obtém lista paginada de vínculos entre categorias de lojas e produtos.

        Args:
            page: N° da página (Bling: ``pagina``, integer, opcional)
            limit: Registros por página (Bling: ``limite``, integer, opcional)
            store_id: ID da loja (Bling: ``idLoja``, integer, opcional)
            product_category_id: ID da categoria de produto (Bling: ``idCategoriaProduto``, integer, opcional)
            parent_product_category_id: ID da categoria de produto pai (Bling: ``idCategoriaProdutoPai``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: CategoriasLojasDadosDTO
        """
        return self.listar(
            pagina=page,
            limite=limit,
            id_loja=store_id,
            id_categoria_produto=product_category_id,
            id_categoria_produto_pai=parent_product_category_id,
        )

    def obter(self, id_categoria_loja: int) -> JsonObject:
        """Obtém uma categoria de loja.

        Endpoint: GET /categorias/lojas/{idCategoriaLoja}

        Obtém o vínculo de uma categoria de loja com a de produto pelo ID.

        Args:
            id_categoria_loja: ID do vínculo (Bling: ``idCategoriaLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: CategoriasLojasDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/categorias/lojas/{id_categoria_loja}")

    def get(self, store_category_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém uma categoria de loja.

        Endpoint: GET /categorias/lojas/{idCategoriaLoja}

        Args:
            store_category_id: ID do vínculo (Bling: ``idCategoriaLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: CategoriasLojasDadosDTO; 404: ErrorResponse
        """
        return self.obter(id_categoria_loja=store_category_id)

    def criar(
        self,
        dados: CategoriasLojasDadosDTO,
    ) -> JsonObject:
        """Cria um vínculo de categoria da loja com a de produto.

        Endpoint: POST /categorias/lojas

        Cria o vínculo de uma categoria da loja com a de produto.

        Args:
            dados: Dados do vínculo. Request body schema: CategoriasLojasDadosDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self._post("/categorias/lojas", json=to_json_object(dados))

    def create(
        self,
        data: CategoriasLojasDadosDTO,
    ) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria um vínculo de categoria da loja com a de produto.

        Endpoint: POST /categorias/lojas

        Args:
            data: Dados do vínculo. Request body schema: CategoriasLojasDadosDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(
        self,
        id_categoria_loja: int,
        dados: CategoriasLojasDadosDTO,
    ) -> JsonObject:
        """Altera um vínculo de categoria da loja com a de produto.

        Endpoint: PUT /categorias/lojas/{idCategoriaLoja}

        Altera o vínculo de uma categoria da loja com a de produto pelo ID.

        Args:
            id_categoria_loja: ID do vínculo (Bling: ``idCategoriaLoja``, integer, obrigatório)
            dados: Dados do vínculo para atualização. Request body schema: CategoriasLojasDadosDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/categorias/lojas/{id_categoria_loja}", json=to_json_object(dados))

    def update(
        self,
        store_category_id: int,
        data: CategoriasLojasDadosDTO,
    ) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera um vínculo de categoria da loja com a de produto.

        Endpoint: PUT /categorias/lojas/{idCategoriaLoja}

        Args:
            store_category_id: ID do vínculo (Bling: ``idCategoriaLoja``, integer, obrigatório)
            data: Dados do vínculo. Request body schema: CategoriasLojasDadosDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_categoria_loja=store_category_id, dados=data)

    def remover(self, id_categoria_loja: int) -> JsonObject:
        """Remove um vínculo de categoria da loja.

        Endpoint: DELETE /categorias/lojas/{idCategoriaLoja}

        Remove o vínculo de uma categoria da loja com a de produto pelo ID.

        Args:
            id_categoria_loja: ID do vínculo (Bling: ``idCategoriaLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 404: ErrorResponse
        """
        return self._delete(f"/categorias/lojas/{id_categoria_loja}")

    def delete(self, store_category_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove um vínculo de categoria da loja.

        Endpoint: DELETE /categorias/lojas/{idCategoriaLoja}

        Args:
            store_category_id: ID do vínculo (Bling: ``idCategoriaLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 404: ErrorResponse
        """
        return self.remover(id_categoria_loja=store_category_id)
