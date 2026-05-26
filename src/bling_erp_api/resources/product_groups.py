"""Grupos de Produtos resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, QueryParams


def _product_groups_list_params(
    *,
    nome: str | None = None,
    nome_pai: str | None = None,
) -> QueryParams:
    return compact_params({"nome": nome, "nomePai": nome_pai})


class ProductGroupsResource(BaseResource):
    """Operações de grupos de produtos do Bling.

    Este recurso mapeia os endpoints ``/grupos-produtos``. Os métodos canônicos usam
    português para acompanhar a documentação oficial. Aliases em inglês estão disponíveis
    para compatibilidade.
    """

    def listar(
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        nome: str | None = None,
        nome_pai: str | None = None,
    ) -> JsonObject:
        """Obtém grupos de produtos paginados.

        Endpoint: GET /grupos-produtos

        Obtém grupos de produtos paginados.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            nome: O nome do grupo (Bling: ``nome``, string, opcional)
            nome_pai: O nome do grupo pai (Bling: ``nomePai``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: GruposProdutosDadosDTO
        """
        params = _product_groups_list_params(nome=nome, nome_pai=nome_pai)
        return self._get(f"/grupos-produtos?pagina={pagina}&limite={limite}", params=params)

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        name: str | None = None,
        parent_name: str | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Obtém grupos de produtos paginados.

        Endpoint: GET /grupos-produtos

        Obtém grupos de produtos paginados.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            name: O nome do grupo (Bling: ``nome``, string, opcional)
            parent_name: O nome do grupo pai (Bling: ``nomePai``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: GruposProdutosDadosDTO
        """
        return self.listar(pagina=page, limite=limit, nome=name, nome_pai=parent_name)

    def obter(self, id_grupo_produto: int) -> JsonObject:
        """Obtém um grupo de produtos.

        Endpoint: GET /grupos-produtos/{idGrupoProduto}

        Obtém um grupo de produtos pelo ID.

        Args:
            id_grupo_produto: ID do grupo de produto (Bling: ``idGrupoProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: GruposProdutosDadosDTO, GruposProdutosGrupoProdutoPaiDTO; 404: ErrorResponse
        """
        return self._get(f"/grupos-produtos/{id_grupo_produto}")

    def get(self, product_group_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém um grupo de produtos.

        Endpoint: GET /grupos-produtos/{idGrupoProduto}

        Obtém um grupo de produtos pelo ID.

        Args:
            product_group_id: ID do grupo de produto (Bling: ``idGrupoProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: GruposProdutosDadosDTO, GruposProdutosGrupoProdutoPaiDTO; 404: ErrorResponse
        """
        return self.obter(id_grupo_produto=product_group_id)

    def criar(self, dados: JsonObject) -> JsonObject:
        """Cria um grupo de produtos.

        Endpoint: POST /grupos-produtos

        Cria um grupo de produtos.

        Args:
            dados: Dados do grupo de produtos (Bling: request body)

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self._post("/grupos-produtos", json=to_json_object(dados))

    def create(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria um grupo de produtos.

        Endpoint: POST /grupos-produtos

        Cria um grupo de produtos.

        Args:
            data: Dados do grupo de produtos (Bling: request body)

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(self, id_grupo_produto: int, dados: JsonObject) -> JsonObject:
        """Altera um grupo de produtos.

        Endpoint: PUT /grupos-produtos/{idGrupoProduto}

        Altera um grupo de produtos pelo ID.

        Args:
            id_grupo_produto: ID do grupo de produto (Bling: ``idGrupoProduto``, integer, obrigatório)
            dados: Dados do grupo de produtos (Bling: request body)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(
            f"/grupos-produtos/{id_grupo_produto}",
            json=to_json_object(dados),
        )

    def update(self, product_group_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera um grupo de produtos.

        Endpoint: PUT /grupos-produtos/{idGrupoProduto}

        Altera um grupo de produtos pelo ID.

        Args:
            product_group_id: ID do grupo de produto (Bling: ``idGrupoProduto``, integer, obrigatório)
            data: Dados do grupo de produtos (Bling: request body)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_grupo_produto=product_group_id, dados=data)

    def remover(self, id_grupo_produto: int) -> JsonObject:
        """Remove um grupo de produtos.

        Endpoint: DELETE /grupos-produtos/{idGrupoProduto}

        Remove um grupo de produtos pelo ID.

        Args:
            id_grupo_produto: ID do grupo de produto (Bling: ``idGrupoProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/grupos-produtos/{id_grupo_produto}")

    def delete(self, product_group_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove um grupo de produtos.

        Endpoint: DELETE /grupos-produtos/{idGrupoProduto}

        Remove um grupo de produtos pelo ID.

        Args:
            product_group_id: ID do grupo de produto (Bling: ``idGrupoProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(id_grupo_produto=product_group_id)

    def remover_varios(self, ids_grupos_produtos: list[int]) -> JsonObject:
        """Remove múltiplos grupos de produtos.

        Endpoint: DELETE /grupos-produtos

        Remove múltiplos grupos de produtos pelos IDs.

        Args:
            ids_grupos_produtos: IDs dos grupos de produtos (Bling: ``idsGruposProdutos[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ErrorResponse; 400: ErrorResponse
        """
        return self._delete(
            "/grupos-produtos",
            params={"idsGruposProdutos[]": ids_grupos_produtos},
        )

    def delete_multiple(self, product_group_ids: list[int]) -> JsonObject:
        """Compatibility alias for ``remover_varios()``.

        Remove múltiplos grupos de produtos.

        Endpoint: DELETE /grupos-produtos

        Remove múltiplos grupos de produtos pelos IDs.

        Args:
            product_group_ids: IDs dos grupos de produtos (Bling: ``idsGruposProdutos[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ErrorResponse; 400: ErrorResponse
        """
        return self.remover_varios(ids_grupos_produtos=product_group_ids)
