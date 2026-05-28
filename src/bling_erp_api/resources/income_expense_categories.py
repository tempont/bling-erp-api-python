"""Categorias - Receitas e Despesas resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.models.generated.income_expense_categories import (
        CategoriasReceitasDespesasDadosPostDTO,
    )
    from bling_erp_api.types import JsonObject, QueryParams


def _income_expense_list_params(
    *,
    tipo: int | None = None,
    situacao: int | None = None,
) -> QueryParams:
    """Build query params for GET /categorias/receitas-despesas."""
    return compact_params(
        {
            "tipo": tipo,
            "situacao": situacao,
        }
    )


class IncomeExpenseCategoriesResource(BaseResource):
    """Operações de categorias de receitas e despesas do Bling.

    Este recurso mapeia os endpoints ``/categorias/receitas-despesas``.
    Os métodos canônicos usam português para acompanhar a documentação
    oficial; os métodos em inglês continuam disponíveis como aliases de
    compatibilidade.
    """

    def listar(
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        tipo: int | None = None,
        situacao: int | None = None,
    ) -> JsonObject:
        """Lista categorias de receitas e despesas.

        Endpoint: GET /categorias/receitas-despesas

        Obtém lista paginada de categorias de receitas e despesas.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            tipo: 0=Todas, 1=Despesa, 2=Receita, 3=Receita e despesa (Bling: ``tipo``, integer, opcional)
            situacao: 0=Ativas e Inativas, 1=Ativas, 2=Inativas (Bling: ``situacao``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: CategoriasReceitasDespesasDadosBaseDTO
        """
        params = _income_expense_list_params(tipo=tipo, situacao=situacao)
        return self._get(
            f"/categorias/receitas-despesas?pagina={pagina}&limite={limite}", params=params
        )

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        type_: int | None = None,
        status: int | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lista categorias de receitas e despesas.

        Endpoint: GET /categorias/receitas-despesas

        Args:
            page: N° da página (Bling: ``pagina``, integer, opcional)
            limit: Registros por página (Bling: ``limite``, integer, opcional)
            type_: 0=Todas, 1=Despesa, 2=Receita, 3=Receita e despesa (Bling: ``tipo``, integer, opcional)
            status: 0=Ativas e Inativas, 1=Ativas, 2=Inativas (Bling: ``situacao``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: CategoriasReceitasDespesasDadosBaseDTO
        """
        return self.listar(pagina=page, limite=limit, tipo=type_, situacao=status)

    def criar(
        self,
        dados: CategoriasReceitasDespesasDadosPostDTO,
    ) -> JsonObject:
        """Cria uma categoria de receita e despesa.

        Endpoint: POST /categorias/receitas-despesas

        Cria uma categoria de receita e despesa.

        Args:
            dados: Dados da categoria. Request body schema: CategoriasReceitasDespesasDadosPostDTO

        Returns:
            Bling API response. Response schemas: 201: CategoriasReceitasDespesasDadosBaseDTO; 400: ErrorResponse
        """
        return self._post("/categorias/receitas-despesas", json=to_json_object(dados))

    def create(
        self,
        data: CategoriasReceitasDespesasDadosPostDTO,
    ) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria uma categoria de receita e despesa.

        Endpoint: POST /categorias/receitas-despesas

        Args:
            data: Dados da categoria. Request body schema: CategoriasReceitasDespesasDadosPostDTO

        Returns:
            Bling API response. Response schemas: 201: CategoriasReceitasDespesasDadosBaseDTO; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def remover_varios(self, ids_categorias: list[int]) -> JsonObject:
        """Remove múltiplas categorias de receita e despesa.

        Endpoint: DELETE /categorias/receitas-despesas

        Remove múltiplas categorias de receita e despesa a partir de uma lista de IDs.

        Args:
            ids_categorias: IDs das categorias a serem removidas (Bling: ``idsCategorias[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 200: ErrorResponse
        """
        return self._delete(
            "/categorias/receitas-despesas", params={"idsCategorias[]": ids_categorias}
        )

    def delete_multiple(self, category_ids: list[int]) -> JsonObject:
        """Compatibility alias for ``remover_varios()``.

        Remove múltiplas categorias de receita e despesa.

        Endpoint: DELETE /categorias/receitas-despesas

        Args:
            category_ids: IDs das categorias a serem removidas (Bling: ``idsCategorias[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 200: ErrorResponse
        """
        return self.remover_varios(ids_categorias=category_ids)

    def obter(self, id_categoria: int) -> JsonObject:
        """Obtém uma categoria de receita e despesa.

        Endpoint: GET /categorias/receitas-despesas/{idCategoria}

        Obtém uma categoria de receita e despesa pelo ID.

        Args:
            id_categoria: ID da categoria (Bling: ``idCategoria``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: CategoriasReceitasDespesasDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/categorias/receitas-despesas/{id_categoria}")

    def get(self, category_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém uma categoria de receita e despesa.

        Endpoint: GET /categorias/receitas-despesas/{idCategoria}

        Args:
            category_id: ID da categoria (Bling: ``idCategoria``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: CategoriasReceitasDespesasDadosDTO; 404: ErrorResponse
        """
        return self.obter(id_categoria=category_id)

    def alterar(
        self,
        id_categoria: int,
        dados: CategoriasReceitasDespesasDadosPostDTO,
    ) -> JsonObject:
        """Altera uma categoria de receita e despesa.

        Endpoint: PUT /categorias/receitas-despesas/{idCategoria}

        Altera uma categoria de receita e despesa a partir do ID.

        Args:
            id_categoria: ID da categoria (Bling: ``idCategoria``, integer, obrigatório)
            dados: Dados da categoria para atualização. Request body schema: CategoriasReceitasDespesasDadosPostDTO

        Returns:
            Bling API response. Response schemas: 200: CategoriasReceitasDespesasDadosBaseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(
            f"/categorias/receitas-despesas/{id_categoria}", json=to_json_object(dados)
        )

    def update(
        self,
        category_id: int,
        data: CategoriasReceitasDespesasDadosPostDTO,
    ) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera uma categoria de receita e despesa.

        Endpoint: PUT /categorias/receitas-despesas/{idCategoria}

        Args:
            category_id: ID da categoria (Bling: ``idCategoria``, integer, obrigatório)
            data: Dados da categoria. Request body schema: CategoriasReceitasDespesasDadosPostDTO

        Returns:
            Bling API response. Response schemas: 200: CategoriasReceitasDespesasDadosBaseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_categoria=category_id, dados=data)

    def remover(self, id_categoria: int) -> JsonObject:
        """Remove uma categoria de receita e despesa.

        Endpoint: DELETE /categorias/receitas-despesas/{idCategoria}

        Remove uma categoria de receita e despesa pelo ID.

        Args:
            id_categoria: ID da categoria (Bling: ``idCategoria``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/categorias/receitas-despesas/{id_categoria}")

    def delete(self, category_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove uma categoria de receita e despesa.

        Endpoint: DELETE /categorias/receitas-despesas/{idCategoria}

        Args:
            category_id: ID da categoria (Bling: ``idCategoria``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(id_categoria=category_id)
