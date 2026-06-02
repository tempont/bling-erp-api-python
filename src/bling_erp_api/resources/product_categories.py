"""Categorias - Produtos resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.product_categories import (
    CategoriasProdutosGetResponse200,
    CategoriasProdutosIdCategoriaProdutoGetResponse200,
    CategoriasProdutosPostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.models.generated.product_categories import (
        CategoriasProdutosDadosDTO,
    )
    from bling_erp_api.types import JsonObject


class ProductCategoriesResource(BaseResource):
    """Resource for Bling product category endpoints.

    Maps ``/categorias/produtos`` operations for product category listing,
    retrieval, creation, update, and removal. Canonical methods use pt-BR names
    aligned with the official API; English methods remain compatibility aliases.
    """

    def listar(
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
    ) -> CategoriasProdutosGetResponse200:
        """Lista categorias de produtos.

        Endpoint: GET /categorias/produtos

        Obtém lista paginada de categorias de produtos.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: CategoriasProdutosDadosDTO
        """
        raw = self._get(f"/categorias/produtos?pagina={pagina}&limite={limite}")
        return self._validate_response(CategoriasProdutosGetResponse200, raw)

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
    ) -> CategoriasProdutosGetResponse200:
        """Compatibility alias for ``listar()``.

        Lista categorias de produtos.

        Endpoint: GET /categorias/produtos

        Args:
            page: N° da página (Bling: ``pagina``, integer, opcional)
            limit: Registros por página (Bling: ``limite``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: CategoriasProdutosDadosDTO
        """
        return self.listar(pagina=page, limite=limit)

    def obter(
        self, id_categoria_produto: int
    ) -> CategoriasProdutosIdCategoriaProdutoGetResponse200:
        """Obtém uma categoria de produto.

        Endpoint: GET /categorias/produtos/{idCategoriaProduto}

        Obtém uma categoria de produto pelo ID.

        Args:
            id_categoria_produto: ID da categoria de produto (Bling: ``idCategoriaProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: CategoriasProdutosDadosDTO; 404: ErrorResponse
        """
        raw = self._get(f"/categorias/produtos/{id_categoria_produto}")
        return self._validate_response(CategoriasProdutosIdCategoriaProdutoGetResponse200, raw)

    def get(self, product_category_id: int) -> CategoriasProdutosIdCategoriaProdutoGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém uma categoria de produto.

        Endpoint: GET /categorias/produtos/{idCategoriaProduto}

        Args:
            product_category_id: ID da categoria de produto (Bling: ``idCategoriaProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: CategoriasProdutosDadosDTO; 404: ErrorResponse
        """
        return self.obter(id_categoria_produto=product_category_id)

    def criar(
        self,
        dados: CategoriasProdutosDadosDTO,
    ) -> CategoriasProdutosPostResponse201:
        """Cria uma categoria de produto.

        Endpoint: POST /categorias/produtos

        Cria uma categoria de produto.

        Args:
            dados: Dados da categoria. Request body schema: CategoriasProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        raw = self._post("/categorias/produtos", json=to_json_object(dados))
        return self._validate_response(CategoriasProdutosPostResponse201, raw)

    def create(
        self,
        data: CategoriasProdutosDadosDTO,
    ) -> CategoriasProdutosPostResponse201:
        """Compatibility alias for ``criar()``.

        Cria uma categoria de produto.

        Endpoint: POST /categorias/produtos

        Args:
            data: Dados da categoria. Request body schema: CategoriasProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(
        self,
        id_categoria_produto: int,
        dados: CategoriasProdutosDadosDTO,
    ) -> JsonObject:
        """Altera uma categoria de produto.

        Endpoint: PUT /categorias/produtos/{idCategoriaProduto}

        Altera uma categoria de produto pelo ID.

        Args:
            id_categoria_produto: ID da categoria de produto (Bling: ``idCategoriaProduto``, integer, obrigatório)
            dados: Dados da categoria para atualização. Request body schema: CategoriasProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/categorias/produtos/{id_categoria_produto}", json=to_json_object(dados))

    def update(
        self,
        product_category_id: int,
        data: CategoriasProdutosDadosDTO,
    ) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera uma categoria de produto.

        Endpoint: PUT /categorias/produtos/{idCategoriaProduto}

        Args:
            product_category_id: ID da categoria de produto (Bling: ``idCategoriaProduto``, integer, obrigatório)
            data: Dados da categoria. Request body schema: CategoriasProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_categoria_produto=product_category_id, dados=data)

    def remover(self, id_categoria_produto: int) -> JsonObject:
        """Remove uma categoria de produto.

        Endpoint: DELETE /categorias/produtos/{idCategoriaProduto}

        Remove uma categoria de produto pelo ID.

        Args:
            id_categoria_produto: ID da categoria de produto (Bling: ``idCategoriaProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/categorias/produtos/{id_categoria_produto}")

    def delete(self, product_category_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove uma categoria de produto.

        Endpoint: DELETE /categorias/produtos/{idCategoriaProduto}

        Args:
            product_category_id: ID da categoria de produto (Bling: ``idCategoriaProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(id_categoria_produto=product_category_id)
