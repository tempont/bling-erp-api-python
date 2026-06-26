"""Produtos — Lojas resource."""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from bling_erp_api.models.generated.product_stores import (
    ProdutosLojasDadosDTO,
    ProdutosLojasGetResponse200,
    ProdutosLojasIdProdutoLojaGetResponse200,
    ProdutosLojasIdProdutoLojaPutRequest,
    ProdutosLojasIdProdutoLojaPutResponse200,
    ProdutosLojasPostRequest,
    ProdutosLojasPostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams

type DateFilter = date | datetime | str


class ProductStoresResource(BaseResource):
    """Resource para vínculos de produtos com lojas do Bling.

    Mapeia os endpoints ``/produtos/lojas`` para listagem, consulta, criação,
    alteração e remoção de vínculos de produtos com lojas. Métodos canônicos
    em pt-BR; aliases em inglês disponíveis para compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        id_produto: int | None = None,
        id_loja: int | None = None,
        id_categoria_produto: int | None = None,
        data_alteracao_inicial: DateFilter | None = None,
        data_alteracao_final: DateFilter | None = None,
    ) -> ProdutosLojasGetResponse200:
        """Obtém vínculos de produtos com lojas.

        Endpoint: GET /produtos/lojas

        Obtém vínculos de produtos com lojas paginados.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            id_produto: ID do produto (Bling: ``idProduto``, integer, opcional)
            id_loja: ID da loja (Bling: ``idLoja``, integer, opcional)
            id_categoria_produto: ID da categoria do produto vinculada à loja (Bling: ``idCategoriaProduto``, integer, opcional)
            data_alteracao_inicial: Data de alteração inicial (Bling: ``dataAlteracaoInicial``, string, opcional)
            data_alteracao_final: Data de alteração final (Bling: ``dataAlteracaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: ProdutosLojasDadosDTO; 400: ErrorResponse
        """
        raw = self._get(
            "/produtos/lojas",
            params=_store_list_params(
                pagina=pagina,
                limite=limite,
                id_produto=id_produto,
                id_loja=id_loja,
                id_categoria_produto=id_categoria_produto,
                data_alteracao_inicial=data_alteracao_inicial,
                data_alteracao_final=data_alteracao_final,
            ),
        )
        return self._validate_response(ProdutosLojasGetResponse200, raw)

    def iterar(self, *, pagina: int = 1, limite: int = 100) -> Iterator[ProdutosLojasDadosDTO]:
        """Itera pelos registros página a página, mantendo os mesmos filtros.

        Obtém vínculos de produtos com lojas

        Endpoint: GET /produtos/lojas

        Obtém vínculos de produtos com lojas paginados.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            id_produto: ID do produto (Bling: ``idProduto``, integer, opcional)
            id_loja: ID da loja (Bling: ``idLoja``, integer, opcional)
            id_categoria_produto: ID da categoria do produto vinculada à loja (Bling: ``idCategoriaProduto``, integer, opcional)
            data_alteracao_inicial: Data de alteração inicial (Bling: ``dataAlteracaoInicial``, string, opcional)
            data_alteracao_final: Data de alteração final (Bling: ``dataAlteracaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: ProdutosLojasDadosDTO; 400: ErrorResponse
        """
        for item in self._iterate("/produtos/lojas", page=pagina, limit=limite):
            yield ProdutosLojasDadosDTO.model_validate(item)

    def criar(self, dados: ProdutosLojasPostRequest) -> ProdutosLojasPostResponse201:
        """Cria o vínculo de um produto com uma loja.

        Endpoint: POST /produtos/lojas

        Cria o vínculo de um produto com uma loja.

        Args:
            dados: Dados do vínculo do produto com a loja (Bling: ``ProdutosLojasDadosBaseDTO, ProdutosLojasDadosDTO``, obrigatório)

        Request body schema: ProdutosLojasDadosBaseDTO, ProdutosLojasDadosDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse, ProdutosLojasResponse_POST_PUT; 400: ErrorResponse
        """
        raw = self._post("/produtos/lojas", json=to_json_object(dados))
        return self._validate_response(ProdutosLojasPostResponse201, raw)

    def obter(self, id_produto_loja: int) -> ProdutosLojasIdProdutoLojaGetResponse200:
        """Obtém um vínculo de produto com loja.

        Endpoint: GET /produtos/lojas/{idProdutoLoja}

        Obtém um vínculo de produto com loja pelo ID.

        Args:
            id_produto_loja: ID do vínculo do produto com a loja (Bling: ``idProdutoLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosLojasDadosBaseDTO, ProdutosLojasDadosDTO; 404: ErrorResponse
        """
        raw = self._get(f"/produtos/lojas/{id_produto_loja}")
        return self._validate_response(ProdutosLojasIdProdutoLojaGetResponse200, raw)

    def alterar(
        self, id_produto_loja: int, dados: ProdutosLojasIdProdutoLojaPutRequest
    ) -> ProdutosLojasIdProdutoLojaPutResponse200:
        """Altera o vínculo de um produto com uma loja.

        Endpoint: PUT /produtos/lojas/{idProdutoLoja}

        Altera o vínculo de um produto com uma loja pelo ID.

        Args:
            id_produto_loja: ID do vínculo do produto com a loja (Bling: ``idProdutoLoja``, integer, obrigatório)
            dados: Dados do vínculo do produto com a loja (Bling: ``ProdutosLojasDadosBaseDTO, ProdutosLojasDadosDTO``, obrigatório)

        Request body schema: ProdutosLojasDadosBaseDTO, ProdutosLojasDadosDTO

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse, ProdutosLojasResponse_POST_PUT; 400: ErrorResponse; 404: ErrorResponse
        """
        raw = self._put(f"/produtos/lojas/{id_produto_loja}", json=to_json_object(dados))
        return self._validate_response(ProdutosLojasIdProdutoLojaPutResponse200, raw)

    def remover(self, id_produto_loja: int) -> JsonObject:
        """Remove o vínculo de um produto com uma loja.

        Endpoint: DELETE /produtos/lojas/{idProdutoLoja}

        Remove o vínculo de um produto com uma loja pelo ID.

        Args:
            id_produto_loja: ID do vínculo do produto com a loja (Bling: ``idProdutoLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 404: ErrorResponse
        """
        return self._delete(f"/produtos/lojas/{id_produto_loja}")


def _store_list_params(  # noqa: PLR0913
    *,
    pagina: int,
    limite: int,
    id_produto: int | None,
    id_loja: int | None,
    id_categoria_produto: int | None,
    data_alteracao_inicial: DateFilter | None,
    data_alteracao_final: DateFilter | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "idProduto": id_produto,
            "idLoja": id_loja,
            "idCategoriaProduto": id_categoria_produto,
            "dataAlteracaoInicial": _format_datetime_filter(data_alteracao_inicial),
            "dataAlteracaoFinal": _format_datetime_filter(data_alteracao_final),
        }
    )


def _format_datetime_filter(value: DateFilter | None) -> str | None:
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return value.isoformat()
