"""Produtos resource."""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING, Literal

from bling_erp_api.models.generated.products import (
    ProdutosDadosBaseDTO,
    ProdutosDadosDTO,
    ProdutosDadosPatchDTO,
    ProdutosDeleteResponse200,
    ProdutosGetResponse200,
    ProdutosIdProdutoGetResponse200,
    ProdutosResponsePOSTPUT,
    ProdutosSituacoesPostResponse200,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from bling_erp_api.types import JsonObject, QueryParams

type DateFilter = date | datetime | str
type ProductListCriterion = Literal[1, 2, 3, 4, 5]
type ProductListType = Literal["T", "P", "S", "E", "PS", "C", "V"]
type ProductStockBalanceFilter = Literal[0, 1, 2]
type ProductStatus = Literal["A", "I", "E"]


class ProductsResource(BaseResource):
    """Resource for Bling product endpoints.

    Maps the main ``/produtos`` endpoints, including listing, retrieval,
    creation, full and partial updates, removal, and status changes. Canonical
    methods use pt-BR names aligned with the official Bling documentation;
    English methods are thin compatibility aliases.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        criterio: ProductListCriterion | None = None,
        tipo: ProductListType | None = None,
        id_componente: int | None = None,
        data_inclusao_inicial: DateFilter | None = None,
        data_inclusao_final: DateFilter | None = None,
        data_alteracao_inicial: DateFilter | None = None,
        data_alteracao_final: DateFilter | None = None,
        id_categoria: int | None = None,
        id_loja: int | None = None,
        nome: str | None = None,
        ids_produtos: Sequence[int] | None = None,
        codigos: Sequence[str] | None = None,
        gtins: Sequence[str] | None = None,
        filtro_saldo_estoque: ProductStockBalanceFilter | None = None,
        filtro_saldo_estoque_deposito: int | None = None,
    ) -> ProdutosGetResponse200:
        """Lista produtos.

        Endpoint: GET /produtos

        Obtém produtos paginados.

        Args:
            pagina: Parâmetro ``pagina`` do Bling.
            limite: Parâmetro ``limite`` do Bling.
            criterio: Critério de listagem, enviado como ``criterio``.
            tipo: Tipo de produto, enviado como ``tipo``.
            id_componente: Componente para composições, enviado como ``idComponente``.
            data_inclusao_inicial: Data/hora inicial de inclusão.
            data_inclusao_final: Data/hora final de inclusão.
            data_alteracao_inicial: Data/hora inicial de alteração.
            data_alteracao_final: Data/hora final de alteração.
            id_categoria: Categoria, enviada como ``idCategoria``.
            id_loja: Loja, enviada como ``idLoja``.
            nome: Nome do produto, enviado como ``nome``.
            ids_produtos: IDs, enviados como ``idsProdutos[]``.
            codigos: SKUs, enviados como ``codigos[]``.
            gtins: GTINs/EANs, enviados como ``gtins[]``.
            filtro_saldo_estoque: Filtro de saldo, enviado como ``filtroSaldoEstoque``.
            filtro_saldo_estoque_deposito: Depósito para filtro de saldo.

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosBaseDTO
        """
        raw = self._get(
            "/produtos",
            params=_product_list_params(
                pagina=pagina,
                limite=limite,
                criterio=criterio,
                tipo=tipo,
                id_componente=id_componente,
                data_inclusao_inicial=data_inclusao_inicial,
                data_inclusao_final=data_inclusao_final,
                data_alteracao_inicial=data_alteracao_inicial,
                data_alteracao_final=data_alteracao_final,
                id_categoria=id_categoria,
                id_loja=id_loja,
                nome=nome,
                ids_produtos=ids_produtos,
                codigos=codigos,
                gtins=gtins,
                filtro_saldo_estoque=filtro_saldo_estoque,
                filtro_saldo_estoque_deposito=filtro_saldo_estoque_deposito,
            ),
        )
        return self._validate_response(ProdutosGetResponse200, raw)

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        criterion: ProductListCriterion | None = None,
        product_type: ProductListType | None = None,
        component_id: int | None = None,
        created_start: DateFilter | None = None,
        created_end: DateFilter | None = None,
        updated_start: DateFilter | None = None,
        updated_end: DateFilter | None = None,
        category_id: int | None = None,
        store_id: int | None = None,
        name: str | None = None,
        product_ids: Sequence[int] | None = None,
        codes: Sequence[str] | None = None,
        gtins: Sequence[str] | None = None,
        stock_balance_filter: ProductStockBalanceFilter | None = None,
        stock_balance_deposit_id: int | None = None,
    ) -> ProdutosGetResponse200:
        """Compatibility alias for ``listar()``.

        Obtém produtos

        Endpoint: GET /produtos

        Obtém produtos paginados.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            criterion: Critério de listagem <br> `1` Últimos incluídos <br> `2` Ativos <br> `3` Inativos <br> `4` Excluídos <br> `5` Todos (Bling: ``criterio``, integer, opcional)
            product_type: `T` Todos <br> `P` Produtos <br> `S` Serviços <br> `E` Composições <br> `PS` Produtos simples <br> `C` Com variações <br> `V` Variações (Bling: ``tipo``, string, opcional)
            component_id: ID do componente. Utilizado quando o filtro **tipo** for `E`. (Bling: ``idComponente``, integer, opcional)
            created_start: Data de inclusão inicial (Bling: ``dataInclusaoInicial``, string, opcional)
            created_end: Data de inclusão final (Bling: ``dataInclusaoFinal``, string, opcional)
            updated_start: Data de alteração inicial (Bling: ``dataAlteracaoInicial``, string, opcional)
            updated_end: Data de alteração final (Bling: ``dataAlteracaoFinal``, string, opcional)
            category_id: ID da categoria do produto (Bling: ``idCategoria``, integer, opcional)
            store_id: ID da loja (Bling: ``idLoja``, integer, opcional)
            name: Nome do produto (Bling: ``nome``, string, opcional)
            product_ids: IDs dos produtos (Bling: ``idsProdutos[]``, array, opcional)
            codes: Códigos (SKU) dos produtos (Bling: ``codigos[]``, array, opcional)
            gtins: GTINs/EANs dos produtos (Bling: ``gtins[]``, array, opcional)
            stock_balance_filter: Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> `2` negativo (Bling: ``filtroSaldoEstoque``, integer, opcional)
            stock_balance_deposit_id: ID do depósito para considerar no filtro de saldo em estoque. Se omitido, considera todos os depósitos. (Bling: ``filtroSaldoEstoqueDeposito``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosBaseDTO
        """
        return self.listar(
            pagina=page,
            limite=limit,
            criterio=criterion,
            tipo=product_type,
            id_componente=component_id,
            data_inclusao_inicial=created_start,
            data_inclusao_final=created_end,
            data_alteracao_inicial=updated_start,
            data_alteracao_final=updated_end,
            id_categoria=category_id,
            id_loja=store_id,
            nome=name,
            ids_produtos=product_ids,
            codigos=codes,
            gtins=gtins,
            filtro_saldo_estoque=stock_balance_filter,
            filtro_saldo_estoque_deposito=stock_balance_deposit_id,
        )

    def iterar(self, *, pagina: int = 1, limite: int = 100) -> Iterator[ProdutosDadosBaseDTO]:
        """Itera pelos produtos página a página.

        Endpoint: GET /produtos

        Itera pelos produtos, página a página, retornando um iterador de itens.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros por página (Bling: ``limite``, integer, opcional)

        Returns:
            Iterator sobre os itens da resposta. Cada item é um ``ProdutosDadosBaseDTO``.
        """
        for item in self._iterate("/produtos", page=pagina, limit=limite):
            yield ProdutosDadosBaseDTO.model_validate(item)

    def iterate(self, *, page: int = 1, limit: int = 100) -> Iterator[ProdutosDadosBaseDTO]:
        """Compatibility alias for ``iterar()``.

        Itera pelos produtos página a página.

        Endpoint: GET /produtos

        Itera pelos produtos, página a página, retornando um iterador de itens.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros por página (Bling: ``limite``, integer, opcional)

        Returns:
            Iterator sobre os itens da resposta. Cada item é um ``ProdutosDadosBaseDTO``.
        """
        return self.iterar(pagina=page, limite=limit)

    def obter(self, id_produto: int) -> ProdutosIdProdutoGetResponse200:
        """Obtém um produto.

        Endpoint: GET /produtos/{idProduto}

        Obtém um produto pelo ID.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosDTO; 403: ErrorResponse; 404: ErrorResponse
        """
        raw = self._get(f"/produtos/{id_produto}")
        return self._validate_response(ProdutosIdProdutoGetResponse200, raw)

    def get(self, product_id: int) -> ProdutosIdProdutoGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém um produto

        Endpoint: GET /produtos/{idProduto}

        Obtém um produto pelo ID.

        Args:
            product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosDTO; 403: ErrorResponse; 404: ErrorResponse
        """
        return self.obter(product_id)

    def criar(self, dados: ProdutosDadosDTO) -> ProdutosResponsePOSTPUT:
        """Cria um produto.

        Endpoint: POST /produtos

        Cria um produto.

        Args:
            dados: Dados do produto (Bling: request body, ``ProdutosDadosDTO``, obrigatório)

        Request body schema: ProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 201: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        raw = self._post("/produtos", json=to_json_object(dados))
        return self._validate_response(ProdutosResponsePOSTPUT, raw)

    def create(self, data: ProdutosDadosDTO) -> ProdutosResponsePOSTPUT:
        """Compatibility alias for ``criar()``.

        Cria um produto

        Endpoint: POST /produtos

        Cria um produto.

        Args:
            data: Dados do produto (Bling: request body, ``ProdutosDadosDTO``, obrigatório)

        Request body schema: ProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 201: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        return self.criar(data)

    def alterar(self, id_produto: int, dados: ProdutosDadosDTO) -> ProdutosResponsePOSTPUT:
        """Altera um produto.

        Endpoint: PUT /produtos/{idProduto}

        Altera um produto pelo ID.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            dados: Dados do produto para atualização.

        Request body schema: ProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 200: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        raw = self._put(f"/produtos/{id_produto}", json=to_json_object(dados))
        return self._validate_response(ProdutosResponsePOSTPUT, raw)

    def update(self, product_id: int, data: ProdutosDadosDTO) -> ProdutosResponsePOSTPUT:
        """Compatibility alias for ``alterar()``.

        Altera um produto

        Endpoint: PUT /produtos/{idProduto}

        Altera um produto pelo ID.

        Args:
            product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            data: Dados do produto para atualização.

        Request body schema: ProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 200: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        return self.alterar(product_id, data)

    def alterar_parcialmente(
        self, id_produto: int, dados: ProdutosDadosPatchDTO
    ) -> ProdutosResponsePOSTPUT:
        """Altera parcialmente um produto.

        Endpoint: PATCH /produtos/{idProduto}

        Altera parcialmente um produto pelo ID. Somente os campos informados terão o valor alterado.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            dados: Dados parciais do produto para atualização.

        Request body schema: ProdutosDadosPatchDTO

        Returns:
            Bling API response. Response schemas: 200: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        raw = self._patch(f"/produtos/{id_produto}", json=to_json_object(dados))
        return self._validate_response(ProdutosResponsePOSTPUT, raw)

    def patch(self, product_id: int, data: ProdutosDadosPatchDTO) -> ProdutosResponsePOSTPUT:
        """Compatibility alias for ``alterar_parcialmente()``.

        Altera parcialmente um produto

        Endpoint: PATCH /produtos/{idProduto}

        Altera parcialmente um produto pelo ID. Somente os campos informados terão o valor alterado.

        Args:
            product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            data: Dados parciais do produto para atualização.

        Request body schema: ProdutosDadosPatchDTO

        Returns:
            Bling API response. Response schemas: 200: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        return self.alterar_parcialmente(product_id, data)

    def remover(self, id_produto: int) -> JsonObject:
        """Remove um produto.

        Endpoint: DELETE /produtos/{idProduto}

        Remove um produto pelo ID.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 404: ErrorResponse
        """
        return self._delete(f"/produtos/{id_produto}")

    def delete(self, product_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove um produto

        Endpoint: DELETE /produtos/{idProduto}

        Remove um produto pelo ID.

        Args:
            product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 404: ErrorResponse
        """
        return self.remover(product_id)

    def remover_varios(self, ids_produtos: Sequence[int]) -> ProdutosDeleteResponse200:
        """Remove múltiplos produtos.

        Endpoint: DELETE /produtos

        Remove múltiplos produtos pelos IDs.

        Args:
            ids_produtos: IDs dos produtos (Bling: ``idsProdutos[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosAlertasResponse; 400: ErrorResponse
        """
        raw = self._delete("/produtos", params={"idsProdutos[]": list(ids_produtos)})
        return self._validate_response(ProdutosDeleteResponse200, raw)

    def delete_many(self, product_ids: Sequence[int]) -> ProdutosDeleteResponse200:
        """Compatibility alias for ``remover_varios()``.

        Remove múltiplos produtos

        Endpoint: DELETE /produtos

        Remove múltiplos produtos pelos IDs.

        Args:
            product_ids: IDs dos produtos (Bling: ``idsProdutos[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosAlertasResponse; 400: ErrorResponse
        """
        return self.remover_varios(product_ids)

    def alterar_situacao(self, id_produto: int, situacao: ProductStatus) -> JsonObject:
        """Altera a situação de um produto.

        Endpoint: PATCH /produtos/{idProduto}/situacoes

        Altera a situação de um produto pelo ID.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            situacao: Situação do produto.

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(f"/produtos/{id_produto}/situacoes", json={"situacao": situacao})

    def update_status(self, product_id: int, status: ProductStatus) -> JsonObject:
        """Compatibility alias for ``alterar_situacao()``.

        Altera a situação de um produto

        Endpoint: PATCH /produtos/{idProduto}/situacoes

        Altera a situação de um produto pelo ID.

        Args:
            product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            status: Situação do produto.

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar_situacao(product_id, status)

    def alterar_situacao_varios(
        self, ids_produtos: Sequence[int], situacao: ProductStatus
    ) -> ProdutosSituacoesPostResponse200:
        """Altera a situação de múltiplos produtos.

        Endpoint: POST /produtos/situacoes

        Altera a situação de múltiplos produtos pelos IDs.

        Args:
            ids_produtos: IDs dos produtos (Bling: ``idsProdutos``, array, obrigatório)
            situacao: Situação do produto (Bling: ``situacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosAlertasResponse; 400: ErrorResponse
        """
        raw = self._post(
            "/produtos/situacoes",
            json={"idsProdutos": list(ids_produtos), "situacao": situacao},
        )
        return self._validate_response(ProdutosSituacoesPostResponse200, raw)

    def update_many_status(
        self, product_ids: Sequence[int], status: ProductStatus
    ) -> ProdutosSituacoesPostResponse200:
        """Compatibility alias for ``alterar_situacao_varios()``.

        Altera a situação de múltiplos produtos

        Endpoint: POST /produtos/situacoes

        Altera a situação de múltiplos produtos pelos IDs.

        Args:
            product_ids: IDs dos produtos (Bling: ``idsProdutos``, array, obrigatório)
            status: Situação do produto (Bling: ``situacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosAlertasResponse; 400: ErrorResponse
        """
        return self.alterar_situacao_varios(product_ids, status)


def _product_list_params(  # noqa: PLR0913
    *,
    pagina: int,
    limite: int,
    criterio: ProductListCriterion | None,
    tipo: ProductListType | None,
    id_componente: int | None,
    data_inclusao_inicial: DateFilter | None,
    data_inclusao_final: DateFilter | None,
    data_alteracao_inicial: DateFilter | None,
    data_alteracao_final: DateFilter | None,
    id_categoria: int | None,
    id_loja: int | None,
    nome: str | None,
    ids_produtos: Sequence[int] | None,
    codigos: Sequence[str] | None,
    gtins: Sequence[str] | None,
    filtro_saldo_estoque: ProductStockBalanceFilter | None,
    filtro_saldo_estoque_deposito: int | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "criterio": criterio,
            "tipo": tipo,
            "idComponente": id_componente,
            "dataInclusaoInicial": _format_datetime_filter(data_inclusao_inicial),
            "dataInclusaoFinal": _format_datetime_filter(data_inclusao_final),
            "dataAlteracaoInicial": _format_datetime_filter(data_alteracao_inicial),
            "dataAlteracaoFinal": _format_datetime_filter(data_alteracao_final),
            "idCategoria": id_categoria,
            "idLoja": id_loja,
            "nome": nome,
            "idsProdutos[]": list(ids_produtos) if ids_produtos is not None else None,
            "codigos[]": list(codigos) if codigos is not None else None,
            "gtins[]": list(gtins) if gtins is not None else None,
            "filtroSaldoEstoque": filtro_saldo_estoque,
            "filtroSaldoEstoqueDeposito": filtro_saldo_estoque_deposito,
        }
    )


def _format_datetime_filter(value: DateFilter | None) -> str | None:
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return value.isoformat()
