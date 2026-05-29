"""Purchase orders resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from bling_erp_api.models.generated.purchase_orders import (
        PedidosComprasIdPedidoCompraPutRequest,
        PedidosComprasPostRequest,
    )
    from bling_erp_api.types import JsonObject, QueryParams


class PurchaseOrdersResource(BaseResource):
    """Operações de pedidos de compra do Bling.

    Este recurso mapeia os endpoints ``/pedidos/compras``. Os métodos canônicos
    usam português para acompanhar a documentação oficial do Bling; os métodos em
    inglês continuam disponíveis como aliases de compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        id_fornecedor: int | None = None,
        valor_situacao: int | None = None,
        id_situacao: int | None = None,
        data_inicial: str | None = None,
        data_final: str | None = None,
        ids_notas_fiscais: Sequence[int] | None = None,
    ) -> JsonObject:
        """Obtém pedidos de compras.

        Endpoint: GET /pedidos/compras

        Obtém pedidos de compras paginados.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            id_fornecedor: ID do contato do tipo fornecedor (Bling: ``idFornecedor``, integer, opcional)
            valor_situacao: Valor da situação (Bling: ``valorSituacao``, integer, opcional)
            id_situacao: ID da situação (Bling: ``idSituacao``, integer, opcional)
            data_inicial: Data inicial do período da compra (Bling: ``dataInicial``, string, opcional)
            data_final: Data final do período da compra (Bling: ``dataFinal``, string, opcional)
            ids_notas_fiscais: IDs das notas fiscais de entrada (Bling: ``idsNotasFiscais[]``, array, opcional)

        Returns:
            Bling API response. Response schemas: 200: PedidosComprasDadosBaseDTO
        """
        return self._get(
            "/pedidos/compras",
            params=_purchase_order_list_params(
                pagina=pagina,
                limite=limite,
                id_fornecedor=id_fornecedor,
                valor_situacao=valor_situacao,
                id_situacao=id_situacao,
                data_inicial=data_inicial,
                data_final=data_final,
                ids_notas_fiscais=ids_notas_fiscais,
            ),
        )

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        supplier_id: int | None = None,
        status_value: int | None = None,
        status_id: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        invoice_ids: Sequence[int] | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``."""
        return self.listar(
            pagina=page,
            limite=limit,
            id_fornecedor=supplier_id,
            valor_situacao=status_value,
            id_situacao=status_id,
            data_inicial=start_date,
            data_final=end_date,
            ids_notas_fiscais=invoice_ids,
        )

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        id_fornecedor: int | None = None,
        valor_situacao: int | None = None,
        id_situacao: int | None = None,
        data_inicial: str | None = None,
        data_final: str | None = None,
        ids_notas_fiscais: Sequence[int] | None = None,
    ) -> Iterator[JsonObject]:
        """Itera pelos pedidos de compra página a página.

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.
        """
        params = _purchase_order_list_params(
            pagina=pagina,
            limite=limite,
            id_fornecedor=id_fornecedor,
            valor_situacao=valor_situacao,
            id_situacao=id_situacao,
            data_inicial=data_inicial,
            data_final=data_final,
            ids_notas_fiscais=ids_notas_fiscais,
        )
        return self._iterate("/pedidos/compras", page=pagina, limit=limite, params=params)

    def iterate(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        supplier_id: int | None = None,
        status_value: int | None = None,
        status_id: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        invoice_ids: Sequence[int] | None = None,
    ) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``."""
        return self.iterar(
            pagina=page,
            limite=limit,
            id_fornecedor=supplier_id,
            valor_situacao=status_value,
            id_situacao=status_id,
            data_inicial=start_date,
            data_final=end_date,
            ids_notas_fiscais=invoice_ids,
        )

    def obter(self, id_pedido_compra: int) -> JsonObject:
        """Obtém um pedido de compra.

        Endpoint: GET /pedidos/compras/{idPedidoCompra}

        Obtém um pedido de compra pelo ID.

        Args:
            id_pedido_compra: ID do pedido de compra (Bling: ``idPedidoCompra``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: PedidosComprasDadosBaseDTO, PedidosComprasDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/pedidos/compras/{id_pedido_compra}")

    def get(self, purchase_order_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``."""
        return self.obter(purchase_order_id)

    def criar(self, dados: PedidosComprasPostRequest) -> JsonObject:
        """Cria um pedido de compra.

        Endpoint: POST /pedidos/compras

        Cria um pedido de compra.

        Args:
            dados: Payload do pedido. Use ``PedidosComprasPostRequest`` para uso
                tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse, PedidosCompraResponsePOSTPUT; 400: ErrorResponse
        """
        return self._post("/pedidos/compras", json=to_json_object(dados))

    def create(self, data: PedidosComprasPostRequest) -> JsonObject:
        """Compatibility alias for ``criar()``."""
        return self.criar(data)

    def alterar(
        self,
        id_pedido_compra: int,
        dados: PedidosComprasIdPedidoCompraPutRequest,
    ) -> JsonObject:
        """Altera um pedido de compra.

        Endpoint: PUT /pedidos/compras/{idPedidoCompra}

        Altera um pedido de compra pelo ID.

        Args:
            id_pedido_compra: ID do pedido de compra (Bling: ``idPedidoCompra``, integer, obrigatório)
            dados: Payload do pedido. Use ``PedidosComprasIdPedidoCompraPutRequest`` para uso
                tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse, PedidosCompraResponsePOSTPUT; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/pedidos/compras/{id_pedido_compra}", json=to_json_object(dados))

    def update(
        self,
        purchase_order_id: int,
        data: PedidosComprasIdPedidoCompraPutRequest,
    ) -> JsonObject:
        """Compatibility alias for ``alterar()``."""
        return self.alterar(purchase_order_id, data)

    def remover(self, id_pedido_compra: int) -> JsonObject:
        """Remove um pedido de compra.

        Endpoint: DELETE /pedidos/compras/{idPedidoCompra}

        Remove um pedido de compra pelo ID.

        Args:
            id_pedido_compra: ID do pedido de compra (Bling: ``idPedidoCompra``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 404: ErrorResponse
        """
        return self._delete(f"/pedidos/compras/{id_pedido_compra}")

    def delete(self, purchase_order_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``."""
        return self.remover(purchase_order_id)

    def alterar_situacao(self, id_pedido_compra: int, id_situacao: int) -> JsonObject:
        """Altera a situação de um pedido de compra.

        Endpoint: PATCH /pedidos/compras/{idPedidoCompra}/situacoes/{idSituacao}

        Altera a situação de um pedido de compra pelo ID.

        Args:
            id_pedido_compra: ID do pedido de compra (Bling: ``idPedidoCompra``, integer, obrigatório)
            id_situacao: ID da situação do pedido de compra (Bling: ``idSituacao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(f"/pedidos/compras/{id_pedido_compra}/situacoes/{id_situacao}")

    def update_status(self, purchase_order_id: int, status_id: int) -> JsonObject:
        """Compatibility alias for ``alterar_situacao()``."""
        return self.alterar_situacao(purchase_order_id, status_id)

    def lancar_contas(self, id_pedido_compra: int) -> JsonObject:
        """Lança as contas de um pedido de compra.

        Endpoint: POST /pedidos/compras/{idPedidoCompra}/lancar-contas

        Lança as contas de um pedido de compra pelo ID.

        Args:
            id_pedido_compra: ID do pedido de compra (Bling: ``idPedidoCompra``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/pedidos/compras/{id_pedido_compra}/lancar-contas")

    def post_accounts(self, purchase_order_id: int) -> JsonObject:
        """Compatibility alias for ``lancar_contas()``."""
        return self.lancar_contas(purchase_order_id)

    def estornar_contas(self, id_pedido_compra: int) -> JsonObject:
        """Estorna as contas de um pedido de compra.

        Endpoint: POST /pedidos/compras/{idPedidoCompra}/estornar-contas

        Estorna as contas de um pedido de compra pelo ID.

        Args:
            id_pedido_compra: ID do pedido de compra (Bling: ``idPedidoCompra``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/pedidos/compras/{id_pedido_compra}/estornar-contas")

    def reverse_accounts(self, purchase_order_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_contas()``."""
        return self.estornar_contas(purchase_order_id)

    def lancar_estoque(self, id_pedido_compra: int) -> JsonObject:
        """Lança o estoque de um pedido de compra.

        Endpoint: POST /pedidos/compras/{idPedidoCompra}/lancar-estoque

        Lança o estoque de um pedido de compra pelo ID.

        Args:
            id_pedido_compra: ID do pedido de compra (Bling: ``idPedidoCompra``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/pedidos/compras/{id_pedido_compra}/lancar-estoque")

    def post_stock(self, purchase_order_id: int) -> JsonObject:
        """Compatibility alias for ``lancar_estoque()``."""
        return self.lancar_estoque(purchase_order_id)

    def estornar_estoque(self, id_pedido_compra: int) -> JsonObject:
        """Estorna o estoque de um pedido de compra.

        Endpoint: POST /pedidos/compras/{idPedidoCompra}/estornar-estoque

        Estorna o estoque de um pedido de compra pelo ID.

        Args:
            id_pedido_compra: ID do pedido de compra (Bling: ``idPedidoCompra``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/pedidos/compras/{id_pedido_compra}/estornar-estoque")

    def reverse_stock(self, purchase_order_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_estoque()``."""
        return self.estornar_estoque(purchase_order_id)


def _purchase_order_list_params(  # noqa: PLR0913
    *,
    pagina: int,
    limite: int,
    id_fornecedor: int | None,
    valor_situacao: int | None,
    id_situacao: int | None,
    data_inicial: str | None,
    data_final: str | None,
    ids_notas_fiscais: Sequence[int] | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "idFornecedor": id_fornecedor,
            "valorSituacao": valor_situacao,
            "idSituacao": id_situacao,
            "dataInicial": data_inicial,
            "dataFinal": data_final,
            "idsNotasFiscais[]": list(ids_notas_fiscais) if ids_notas_fiscais is not None else None,
        }
    )
