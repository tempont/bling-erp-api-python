"""Produtos — Fornecedores resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.models.generated.product_suppliers import (
        ProdutosFornecedoresIdProdutoFornecedorPutRequest,
        ProdutosFornecedoresPostRequest,
    )
    from bling_erp_api.types import JsonObject, QueryParams


class ProductSuppliersResource(BaseResource):
    """Operações em ``/produtos/fornecedores``."""

    def listar(
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        id_produto: int | None = None,
        id_fornecedor: int | None = None,
    ) -> JsonObject:
        """Obtém produtos fornecedores.

        Endpoint: GET /produtos/fornecedores

        Obtém produtos fornecedores paginados.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            id_produto: ID do produto (Bling: ``idProduto``, integer, opcional)
            id_fornecedor: ID do contato do tipo fornecedor (Bling: ``idFornecedor``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: ProdutosFornecedoresDadosBaseDTO
        """
        return self._get(
            "/produtos/fornecedores",
            params=_supplier_list_params(
                pagina=pagina,
                limite=limite,
                id_produto=id_produto,
                id_fornecedor=id_fornecedor,
            ),
        )

    def iterar(self, *, pagina: int = 1, limite: int = 100) -> Iterator[JsonObject]:
        """Itera pelos registros página a página, mantendo os mesmos filtros.

        Obtém produtos fornecedores

        Endpoint: GET /produtos/fornecedores

        Obtém produtos fornecedores paginados.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            id_produto: ID do produto (Bling: ``idProduto``, integer, opcional)
            id_fornecedor: ID do contato do tipo fornecedor (Bling: ``idFornecedor``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: ProdutosFornecedoresDadosBaseDTO
        """
        return self._iterate("/produtos/fornecedores", page=pagina, limit=limite)

    def criar(self, dados: ProdutosFornecedoresPostRequest) -> JsonObject:
        """Cria um produto fornecedor.

        Endpoint: POST /produtos/fornecedores

        Cria um produto fornecedor.

        Request body schema: ProdutosFornecedoresDadosBaseDTO, ProdutosFornecedoresDadosDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self._post("/produtos/fornecedores", json=to_json_object(dados))

    def obter(self, id_produto_fornecedor: int) -> JsonObject:
        """Obtém um produto fornecedor.

        Endpoint: GET /produtos/fornecedores/{idProdutoFornecedor}

        Obtém um produto fornecedor pelo ID.

        Args:
            id_produto_fornecedor: ID do produto fornecedor (Bling: ``idProdutoFornecedor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosFornecedoresDadosBaseDTO, ProdutosFornecedoresDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/produtos/fornecedores/{id_produto_fornecedor}")

    def alterar(
        self,
        id_produto_fornecedor: int,
        dados: ProdutosFornecedoresIdProdutoFornecedorPutRequest,
    ) -> JsonObject:
        """Altera um produto fornecedor.

        Endpoint: PUT /produtos/fornecedores/{idProdutoFornecedor}

        Altera um produto fornecedor pelo ID.

        Args:
            id_produto_fornecedor: ID do produto fornecedor (Bling: ``idProdutoFornecedor``, integer, obrigatório)
            dados: Dados do produto fornecedor.

        Request body schema: ProdutosFornecedoresDadosBaseUpdateDTO, ProdutosFornecedoresDadosUpdateDTO

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(
            f"/produtos/fornecedores/{id_produto_fornecedor}",
            json=to_json_object(dados),
        )

    def remover(self, id_produto_fornecedor: int) -> JsonObject:
        """Remove um produto fornecedor.

        Endpoint: DELETE /produtos/fornecedores/{idProdutoFornecedor}

        Remove um produto fornecedor pelo ID.

        Args:
            id_produto_fornecedor: ID do produto fornecedor (Bling: ``idProdutoFornecedor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/produtos/fornecedores/{id_produto_fornecedor}")


def _supplier_list_params(
    *,
    pagina: int,
    limite: int,
    id_produto: int | None,
    id_fornecedor: int | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "idProduto": id_produto,
            "idFornecedor": id_fornecedor,
        }
    )
