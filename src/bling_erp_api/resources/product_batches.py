"""Produtos — Lotes resource."""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from bling_erp_api.models.generated.product_batches import (
        ProductBatch,
        ProductBatchStatusRequest,
        ProductBatchUpdateRequest,
    )
    from bling_erp_api.types import JsonObject, QueryParams

type DateFilter = date | datetime | str


class ProductBatchesResource(BaseResource):
    """Operações em ``/produtos/lotes`` e rotas relacionadas."""

    def remover_varios(self, ids_lotes: Sequence[int]) -> JsonObject:
        """Remove lotes de produtos.

        Endpoint: DELETE /produtos/lotes

        Remove lotes de produtos pelos IDs.

        Args:
            ids_lotes: IDs dos lotes (Bling: ``idsLotes[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(
            "/produtos/lotes",
            params=compact_params({"idsLotes[]": list(ids_lotes)}),
        )

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        ids_produtos: Sequence[int],
        ids_lotes: Sequence[int] | None = None,
        ids_depositos: Sequence[int] | None = None,
        codigos_lotes: Sequence[str] | None = None,
        status: str | None = None,
        data_validade_inicial: DateFilter | None = None,
        data_validade_final: DateFilter | None = None,
        data_fabricacao_inicial: DateFilter | None = None,
        data_fabricacao_final: DateFilter | None = None,
        data_criacao_inicial: DateFilter | None = None,
        data_criacao_final: DateFilter | None = None,
    ) -> JsonObject:
        """Obtém lotes de produtos.

        Endpoint: GET /produtos/lotes

        Obtém lotes de produtos paginados.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            ids_produtos: IDs dos produtos (Bling: ``idsProdutos[]``, array, obrigatório)
            ids_lotes: IDs dos lotes (Bling: ``idsLotes[]``, array, opcional)
            ids_depositos: IDs dos depósitos (Bling: ``idsDepositos[]``, array, opcional)
            codigos_lotes: Códigos dos lotes (Bling: ``codigosLotes[]``, array, opcional)
            status: Status do lote (Bling: ``status``, string, opcional)
            data_validade_inicial: Data de validade inicial (Bling: ``dataValidadeInicial``, string, opcional)
            data_validade_final: Data de validade final (Bling: ``dataValidadeFinal``, string, opcional)
            data_fabricacao_inicial: Data de fabricação inicial (Bling: ``dataFabricacaoInicial``, string, opcional)
            data_fabricacao_final: Data de fabricação final (Bling: ``dataFabricacaoFinal``, string, opcional)
            data_criacao_inicial: Data de inclusão inicial (Bling: ``dataCriacaoInicial``, string, opcional)
            data_criacao_final: Data de inclusão final (Bling: ``dataCriacaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: LotesDTO; 400: ErrorResponse
        """
        return self._get(
            "/produtos/lotes",
            params=_batch_list_params(
                pagina=pagina,
                limite=limite,
                ids_produtos=ids_produtos,
                ids_lotes=ids_lotes,
                ids_depositos=ids_depositos,
                codigos_lotes=codigos_lotes,
                status=status,
                data_validade_inicial=data_validade_inicial,
                data_validade_final=data_validade_final,
                data_fabricacao_inicial=data_fabricacao_inicial,
                data_fabricacao_final=data_fabricacao_final,
                data_criacao_inicial=data_criacao_inicial,
                data_criacao_final=data_criacao_final,
            ),
        )

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        ids_produtos: Sequence[int],
        ids_lotes: Sequence[int] | None = None,
        ids_depositos: Sequence[int] | None = None,
        codigos_lotes: Sequence[str] | None = None,
        status: str | None = None,
        data_validade_inicial: DateFilter | None = None,
        data_validade_final: DateFilter | None = None,
        data_fabricacao_inicial: DateFilter | None = None,
        data_fabricacao_final: DateFilter | None = None,
        data_criacao_inicial: DateFilter | None = None,
        data_criacao_final: DateFilter | None = None,
    ) -> Iterator[JsonObject]:
        """Itera pelos registros página a página, mantendo os mesmos filtros.

        Obtém lotes de produtos

        Endpoint: GET /produtos/lotes

        Obtém lotes de produtos paginados.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            ids_produtos: IDs dos produtos (Bling: ``idsProdutos[]``, array, obrigatório)
            ids_lotes: IDs dos lotes (Bling: ``idsLotes[]``, array, opcional)
            ids_depositos: IDs dos depósitos (Bling: ``idsDepositos[]``, array, opcional)
            codigos_lotes: Códigos dos lotes (Bling: ``codigosLotes[]``, array, opcional)
            status: Status do lote (Bling: ``status``, string, opcional)
            data_validade_inicial: Data de validade inicial (Bling: ``dataValidadeInicial``, string, opcional)
            data_validade_final: Data de validade final (Bling: ``dataValidadeFinal``, string, opcional)
            data_fabricacao_inicial: Data de fabricação inicial (Bling: ``dataFabricacaoInicial``, string, opcional)
            data_fabricacao_final: Data de fabricação final (Bling: ``dataFabricacaoFinal``, string, opcional)
            data_criacao_inicial: Data de inclusão inicial (Bling: ``dataCriacaoInicial``, string, opcional)
            data_criacao_final: Data de inclusão final (Bling: ``dataCriacaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: LotesDTO; 400: ErrorResponse
        """
        merged = compact_params(
            {
                "idsProdutos[]": list(ids_produtos),
                "idsLotes[]": list(ids_lotes) if ids_lotes is not None else None,
                "idsDepositos[]": list(ids_depositos) if ids_depositos is not None else None,
                "codigosLotes[]": list(codigos_lotes) if codigos_lotes is not None else None,
                "status": status,
                "dataValidadeInicial": _format_date_filter(data_validade_inicial),
                "dataValidadeFinal": _format_date_filter(data_validade_final),
                "dataFabricacaoInicial": _format_date_filter(data_fabricacao_inicial),
                "dataFabricacaoFinal": _format_date_filter(data_fabricacao_final),
                "dataCriacaoInicial": _format_datetime_filter(data_criacao_inicial),
                "dataCriacaoFinal": _format_datetime_filter(data_criacao_final),
            },
        )

        return self._iterate("/produtos/lotes", page=pagina, limit=limite, params=merged or {})

    def criar_varios(self, lotes: Sequence[ProductBatch | JsonObject]) -> JsonObject:
        """Salva lotes de produtos.

        Endpoint: PUT /produtos/lotes

        Cria/altera lotes de produtos.

        Request body schema: LotesDTO

        Returns:
            Bling API response. Response schemas: 200: SaveResponseLotsDTO; 400: ErrorResponse
        """
        payload = [to_json_object(lote) for lote in lotes]
        return self._put("/produtos/lotes", json=payload)

    def listar_produtos_controlam_lote(self, ids_produtos: Sequence[int]) -> JsonObject:
        """Obtém a informação se determinados produtos possuem controle de lote.

        Endpoint: GET /produtos/lotes/controla-lote

        Obtém a informação se determinados produtos possuem controle de lote.

        Args:
            ids_produtos: IDs dos produtos (Bling: ``idsProdutos[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutoControlaLotesDTO; 400: ErrorResponse
        """
        return self._get(
            "/produtos/lotes/controla-lote",
            params=compact_params({"idsProdutos[]": list(ids_produtos)}),
        )

    def obter(self, id_lote: int) -> JsonObject:
        """Obtém um lote de um produto.

        Endpoint: GET /produtos/lotes/{idLote}

        Obtém um lote de um produto pelo ID.

        Args:
            id_lote: ID do lote (Bling: ``idLote``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: LotesDTO; 404: ErrorResponse
        """
        return self._get(f"/produtos/lotes/{id_lote}")

    def alterar(self, id_lote: int, dados: ProductBatchUpdateRequest | JsonObject) -> JsonObject:
        """Altera um lote de um produto.

        Endpoint: PUT /produtos/lotes/{idLote}

        Altera um lote de um produto pelo ID.

        Request body schema: LotePutRequestDTO

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/produtos/lotes/{id_lote}", json=to_json_object(dados))

    def alterar_situacao(
        self, id_lote: int, dados: ProductBatchStatusRequest | JsonObject
    ) -> JsonObject:
        """Altera o status de um lote do produto.

        Endpoint: PATCH /produtos/lotes/{idLote}/status

        Altera o status de um lote do produto pelo ID.

        Request body schema: LoteStatusDTO

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(f"/produtos/lotes/{id_lote}/status", json=to_json_object(dados))

    def alterar_situacao_desativar(self, id_produto: int) -> JsonObject:
        """Desativa controle de lotes para o produto.

        Endpoint: POST /produtos/{idProduto}/lotes/controla-lote/desativar

        Desativa controle de lotes para o produto pelo ID do produto.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/produtos/{id_produto}/lotes/controla-lote/desativar")


def _batch_list_params(  # noqa: PLR0913
    *,
    pagina: int,
    limite: int,
    ids_produtos: Sequence[int],
    ids_lotes: Sequence[int] | None,
    ids_depositos: Sequence[int] | None,
    codigos_lotes: Sequence[str] | None,
    status: str | None,
    data_validade_inicial: DateFilter | None,
    data_validade_final: DateFilter | None,
    data_fabricacao_inicial: DateFilter | None,
    data_fabricacao_final: DateFilter | None,
    data_criacao_inicial: DateFilter | None,
    data_criacao_final: DateFilter | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "idsProdutos[]": list(ids_produtos),
            "idsLotes[]": list(ids_lotes) if ids_lotes is not None else None,
            "idsDepositos[]": list(ids_depositos) if ids_depositos is not None else None,
            "codigosLotes[]": list(codigos_lotes) if codigos_lotes is not None else None,
            "status": status,
            "dataValidadeInicial": _format_date_filter(data_validade_inicial),
            "dataValidadeFinal": _format_date_filter(data_validade_final),
            "dataFabricacaoInicial": _format_date_filter(data_fabricacao_inicial),
            "dataFabricacaoFinal": _format_date_filter(data_fabricacao_final),
            "dataCriacaoInicial": _format_datetime_filter(data_criacao_inicial),
            "dataCriacaoFinal": _format_datetime_filter(data_criacao_final),
        }
    )


def _format_date_filter(value: DateFilter | None) -> str | None:
    if value is None or isinstance(value, str):
        return value
    return value.date().isoformat() if isinstance(value, datetime) else value.isoformat()


def _format_datetime_filter(value: DateFilter | None) -> str | None:
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return value.isoformat()
