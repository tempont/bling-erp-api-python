"""Produtos — Fornecedores resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.product_suppliers import (
    ProdutosFornecedoresDadosBaseDTO,
    ProdutosFornecedoresGetResponse200,
    ProdutosFornecedoresIdProdutoFornecedorGetResponse200,
    ProdutosFornecedoresIdProdutoFornecedorPutRequest,
    ProdutosFornecedoresIdProdutoFornecedorPutResponse200,
    ProdutosFornecedoresPostRequest,
    ProdutosFornecedoresPostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams


class ProductSuppliersResource(BaseResource):
    """Resource for Bling product-supplier endpoints.

    Maps ``/produtos/fornecedores`` operations for listing, retrieving,
    creating, updating, and removing product supplier links.
    """

    def listar(
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        id_produto: int | None = None,
        id_fornecedor: int | None = None,
    ) -> ProdutosFornecedoresGetResponse200:
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
        raw = self._get(
            "/produtos/fornecedores",
            params=_supplier_list_params(
                pagina=pagina,
                limite=limite,
                id_produto=id_produto,
                id_fornecedor=id_fornecedor,
            ),
        )
        return self._validate_response(ProdutosFornecedoresGetResponse200, raw)

    def iterar(
        self, *, pagina: int = 1, limite: int = 100
    ) -> Iterator[ProdutosFornecedoresDadosBaseDTO]:
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
        for item in self._iterate("/produtos/fornecedores", page=pagina, limit=limite):
            yield ProdutosFornecedoresDadosBaseDTO.model_validate(item)

    def criar(self, dados: ProdutosFornecedoresPostRequest) -> ProdutosFornecedoresPostResponse201:
        """Cria um produto fornecedor.

        Endpoint: POST /produtos/fornecedores

        Cria um produto fornecedor.

        Request body schema: ProdutosFornecedoresDadosBaseDTO, ProdutosFornecedoresDadosDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        raw = self._post("/produtos/fornecedores", json=to_json_object(dados))
        return self._validate_response(ProdutosFornecedoresPostResponse201, raw)

    def obter(
        self, id_produto_fornecedor: int
    ) -> ProdutosFornecedoresIdProdutoFornecedorGetResponse200:
        """Obtém um produto fornecedor.

        Endpoint: GET /produtos/fornecedores/{idProdutoFornecedor}

        Obtém um produto fornecedor pelo ID.

        Args:
            id_produto_fornecedor: ID do produto fornecedor (Bling: ``idProdutoFornecedor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosFornecedoresDadosBaseDTO, ProdutosFornecedoresDadosDTO; 404: ErrorResponse
        """
        raw = self._get(f"/produtos/fornecedores/{id_produto_fornecedor}")
        return self._validate_response(ProdutosFornecedoresIdProdutoFornecedorGetResponse200, raw)

    def alterar(
        self,
        id_produto_fornecedor: int,
        dados: ProdutosFornecedoresIdProdutoFornecedorPutRequest,
    ) -> ProdutosFornecedoresIdProdutoFornecedorPutResponse200:
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
        raw = self._put(
            f"/produtos/fornecedores/{id_produto_fornecedor}",
            json=to_json_object(dados),
        )
        return self._validate_response(ProdutosFornecedoresIdProdutoFornecedorPutResponse200, raw)

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
