"""Sales orders resource."""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from bling_erp_api.models.generated.sales_orders import (
        PedidosVendasIdPedidoVendaPutRequest,
        PedidosVendasPostRequest,
    )
    from bling_erp_api.types import JsonObject, QueryParams

type DateFilter = date | datetime | str


class SalesOrdersResource(BaseResource):
    """Operações de pedidos de venda do Bling.

    Este recurso mapeia os endpoints ``/pedidos/vendas``. Os métodos canônicos
    usam português para acompanhar a documentação oficial do Bling; os métodos em
    inglês continuam disponíveis como aliases de compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        id_contato: int | None = None,
        ids_situacoes: Sequence[int] | None = None,
        data_inicial: DateFilter | None = None,
        data_final: DateFilter | None = None,
        data_alteracao_inicial: DateFilter | None = None,
        data_alteracao_final: DateFilter | None = None,
        data_prevista_inicial: DateFilter | None = None,
        data_prevista_final: DateFilter | None = None,
        numero: int | None = None,
        id_loja: int | None = None,
        id_vendedor: int | None = None,
        id_controle_caixa: int | None = None,
        numeros_lojas: Sequence[str] | None = None,
        id_unidade_negocio: int | None = None,
    ) -> JsonObject:
        """Lista pedidos de venda.

        Endpoint: GET /pedidos/vendas

        Lista pedidos de venda paginados.

        Args:
            pagina: Parâmetro ``pagina`` do Bling.
            limite: Parâmetro ``limite`` do Bling.
            id_contato: Filtra por contato, enviado como ``idContato``.
            ids_situacoes: Filtra por situações, enviado como ``idsSituacoes[]``.
            data_inicial: Data inicial do pedido, enviada como ``dataInicial``.
            data_final: Data final do pedido, enviada como ``dataFinal``.
            data_alteracao_inicial: Data inicial de alteração, enviada como
                ``dataAlteracaoInicial``.
            data_alteracao_final: Data final de alteração, enviada como
                ``dataAlteracaoFinal``.
            data_prevista_inicial: Data prevista inicial, enviada como
                ``dataPrevistaInicial``.
            data_prevista_final: Data prevista final, enviada como
                ``dataPrevistaFinal``.
            numero: Número do pedido, enviado como ``numero``.
            id_loja: Loja, enviada como ``idLoja``.
            id_vendedor: Vendedor, enviado como ``idVendedor``.
            id_controle_caixa: Controle de caixa, enviado como ``idControleCaixa``.
            numeros_lojas: Números dos pedidos nas lojas, enviados como
                ``numerosLojas[]``.
            id_unidade_negocio: Unidade de negócio, enviada como
                ``idUnidadeNegocio``.

        Datas aceitam ``str``, ``datetime.date`` ou ``datetime.datetime``.
        Filtros de data/hora são formatados como ``YYYY-MM-DD HH:MM:SS``.

        Returns:
            Bling API response. Response schemas: 200: VendasDadosBaseDTO
        """
        return self._get(
            "/pedidos/vendas",
            params=_sales_order_list_params(
                pagina=pagina,
                limite=limite,
                id_contato=id_contato,
                ids_situacoes=ids_situacoes,
                data_inicial=data_inicial,
                data_final=data_final,
                data_alteracao_inicial=data_alteracao_inicial,
                data_alteracao_final=data_alteracao_final,
                data_prevista_inicial=data_prevista_inicial,
                data_prevista_final=data_prevista_final,
                numero=numero,
                id_loja=id_loja,
                id_vendedor=id_vendedor,
                id_controle_caixa=id_controle_caixa,
                numeros_lojas=numeros_lojas,
                id_unidade_negocio=id_unidade_negocio,
            ),
        )

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        contact_id: int | None = None,
        status_ids: Sequence[int] | None = None,
        start_date: DateFilter | None = None,
        end_date: DateFilter | None = None,
        updated_start: DateFilter | None = None,
        updated_end: DateFilter | None = None,
        expected_start_date: DateFilter | None = None,
        expected_end_date: DateFilter | None = None,
        number: int | None = None,
        store_id: int | None = None,
        seller_id: int | None = None,
        cash_register_id: int | None = None,
        store_numbers: Sequence[str] | None = None,
        business_unit_id: int | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lista pedidos de venda.

        Endpoint: GET /pedidos/vendas

        Lista pedidos de venda paginados.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            contact_id: ID do contato (Bling: ``idContato``, integer, opcional)
            status_ids: IDs das situações (Bling: ``idsSituacoes[]``, array, opcional)
            start_date: Data inicial (Bling: ``dataInicial``, string, opcional)
            end_date: Data final (Bling: ``dataFinal``, string, opcional)
            updated_start: Data inicial da alteração (Bling: ``dataAlteracaoInicial``, string, opcional)
            updated_end: Data final da alteração (Bling: ``dataAlteracaoFinal``, string, opcional)
            expected_start_date: Data prevista inicial (Bling: ``dataPrevistaInicial``, string, opcional)
            expected_end_date: Data prevista final (Bling: ``dataPrevistaFinal``, string, opcional)
            number: Número do pedido de venda (Bling: ``numero``, integer, opcional)
            store_id: ID da loja (Bling: ``idLoja``, integer, opcional)
            seller_id: ID do vendedor (Bling: ``idVendedor``, integer, opcional)
            cash_register_id: ID do controle de caixa (Bling: ``idControleCaixa``, integer, opcional)
            store_numbers: Números dos pedidos nas lojas (Bling: ``numerosLojas[]``, array, opcional)
            business_unit_id: ID da unidade de negócio (Bling: ``idUnidadeNegocio``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: VendasDadosBaseDTO
        """
        return self.listar(
            pagina=page,
            limite=limit,
            id_contato=contact_id,
            ids_situacoes=status_ids,
            data_inicial=start_date,
            data_final=end_date,
            data_alteracao_inicial=updated_start,
            data_alteracao_final=updated_end,
            data_prevista_inicial=expected_start_date,
            data_prevista_final=expected_end_date,
            numero=number,
            id_loja=store_id,
            id_vendedor=seller_id,
            id_controle_caixa=cash_register_id,
            numeros_lojas=store_numbers,
            id_unidade_negocio=business_unit_id,
        )

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        id_contato: int | None = None,
        ids_situacoes: Sequence[int] | None = None,
        data_inicial: DateFilter | None = None,
        data_final: DateFilter | None = None,
        data_alteracao_inicial: DateFilter | None = None,
        data_alteracao_final: DateFilter | None = None,
        data_prevista_inicial: DateFilter | None = None,
        data_prevista_final: DateFilter | None = None,
        numero: int | None = None,
        id_loja: int | None = None,
        id_vendedor: int | None = None,
        id_controle_caixa: int | None = None,
        numeros_lojas: Sequence[str] | None = None,
        id_unidade_negocio: int | None = None,
    ) -> Iterator[JsonObject]:
        """Itera pelos pedidos de venda página a página.

        Endpoint: GET /pedidos/vendas

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Returns:
            Bling API response. Response schemas: 200: VendasDadosBaseDTO
        """
        params = _sales_order_list_params(
            pagina=pagina,
            limite=limite,
            id_contato=id_contato,
            ids_situacoes=ids_situacoes,
            data_inicial=data_inicial,
            data_final=data_final,
            data_alteracao_inicial=data_alteracao_inicial,
            data_alteracao_final=data_alteracao_final,
            data_prevista_inicial=data_prevista_inicial,
            data_prevista_final=data_prevista_final,
            numero=numero,
            id_loja=id_loja,
            id_vendedor=id_vendedor,
            id_controle_caixa=id_controle_caixa,
            numeros_lojas=numeros_lojas,
            id_unidade_negocio=id_unidade_negocio,
        )
        return self._iterate("/pedidos/vendas", page=pagina, limit=limite, params=params)

    def iterate(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        contact_id: int | None = None,
        status_ids: Sequence[int] | None = None,
        start_date: DateFilter | None = None,
        end_date: DateFilter | None = None,
        updated_start: DateFilter | None = None,
        updated_end: DateFilter | None = None,
        expected_start_date: DateFilter | None = None,
        expected_end_date: DateFilter | None = None,
        number: int | None = None,
        store_id: int | None = None,
        seller_id: int | None = None,
        cash_register_id: int | None = None,
        store_numbers: Sequence[str] | None = None,
        business_unit_id: int | None = None,
    ) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``.

        Itera pelos pedidos de venda página a página.

        Endpoint: GET /pedidos/vendas

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            contact_id: ID do contato (Bling: ``idContato``, integer, opcional)
            status_ids: IDs das situações (Bling: ``idsSituacoes[]``, array, opcional)
            start_date: Data inicial (Bling: ``dataInicial``, string, opcional)
            end_date: Data final (Bling: ``dataFinal``, string, opcional)
            updated_start: Data inicial da alteração (Bling: ``dataAlteracaoInicial``, string, opcional)
            updated_end: Data final da alteração (Bling: ``dataAlteracaoFinal``, string, opcional)
            expected_start_date: Data prevista inicial (Bling: ``dataPrevistaInicial``, string, opcional)
            expected_end_date: Data prevista final (Bling: ``dataPrevistaFinal``, string, opcional)
            number: Número do pedido de venda (Bling: ``numero``, integer, opcional)
            store_id: ID da loja (Bling: ``idLoja``, integer, opcional)
            seller_id: ID do vendedor (Bling: ``idVendedor``, integer, opcional)
            cash_register_id: ID do controle de caixa (Bling: ``idControleCaixa``, integer, opcional)
            store_numbers: Números dos pedidos nas lojas (Bling: ``numerosLojas[]``, array, opcional)
            business_unit_id: ID da unidade de negócio (Bling: ``idUnidadeNegocio``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: VendasDadosBaseDTO
        """
        return self.iterar(
            pagina=page,
            limite=limit,
            id_contato=contact_id,
            ids_situacoes=status_ids,
            data_inicial=start_date,
            data_final=end_date,
            data_alteracao_inicial=updated_start,
            data_alteracao_final=updated_end,
            data_prevista_inicial=expected_start_date,
            data_prevista_final=expected_end_date,
            numero=number,
            id_loja=store_id,
            id_vendedor=seller_id,
            id_controle_caixa=cash_register_id,
            numeros_lojas=store_numbers,
            id_unidade_negocio=business_unit_id,
        )

    def obter(self, id_pedido_venda: int) -> JsonObject:
        """Obtém um pedido de venda.

        Endpoint: GET /pedidos/vendas/{idPedidoVenda}

        Obtém um pedido de venda pelo ID.

        Args:
            id_pedido_venda: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: VendasDadosBaseDTO, VendasDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/pedidos/vendas/{id_pedido_venda}")

    def get(self, order_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém um pedido de venda.

        Endpoint: GET /pedidos/vendas/{idPedidoVenda}

        Obtém um pedido de venda pelo ID.

        Args:
            order_id: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: VendasDadosBaseDTO, VendasDadosDTO; 404: ErrorResponse
        """
        return self.obter(order_id)

    def criar(self, dados: PedidosVendasPostRequest) -> JsonObject:
        """Cria um pedido de venda.

        Endpoint: POST /pedidos/vendas

        Cria um pedido de venda.

        Args:
            dados: Payload do pedido. Use ``PedidosVendasPostRequest`` para uso
                tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse, VendasResponse_POST_PUT; 400: ErrorResponse
        """
        return self._post("/pedidos/vendas", json=to_json_object(dados))

    def create(self, data: PedidosVendasPostRequest) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria um pedido de venda.

        Endpoint: POST /pedidos/vendas

        Cria um pedido de venda.

        Args:
            data: Payload do pedido. Use ``PedidosVendasPostRequest`` para uso
                tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse, VendasResponse_POST_PUT; 400: ErrorResponse
        """
        return self.criar(data)

    def alterar(
        self, id_pedido_venda: int, dados: PedidosVendasIdPedidoVendaPutRequest
    ) -> JsonObject:
        """Altera um pedido de venda.

        Endpoint: PUT /pedidos/vendas/{idPedidoVenda}

        Altera um pedido de venda pelo ID.

        Args:
            id_pedido_venda: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)
            dados: Payload do pedido. Use ``PedidosVendasIdPedidoVendaPutRequest`` para uso
                tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse, VendasResponse_POST_PUT; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/pedidos/vendas/{id_pedido_venda}", json=to_json_object(dados))

    def update(self, order_id: int, data: PedidosVendasIdPedidoVendaPutRequest) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera um pedido de venda.

        Endpoint: PUT /pedidos/vendas/{idPedidoVenda}

        Altera um pedido de venda pelo ID.

        Args:
            order_id: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)
            data: Payload do pedido. Use ``PedidosVendasIdPedidoVendaPutRequest`` para uso
                tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse, VendasResponse_POST_PUT; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(order_id, data)

    def remover(self, id_pedido_venda: int) -> JsonObject:
        """Remove um pedido de venda.

        Endpoint: DELETE /pedidos/vendas/{idPedidoVenda}

        Remove um pedido de venda pelo ID.

        Args:
            id_pedido_venda: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/pedidos/vendas/{id_pedido_venda}")

    def delete(self, order_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove um pedido de venda.

        Endpoint: DELETE /pedidos/vendas/{idPedidoVenda}

        Remove um pedido de venda pelo ID.

        Args:
            order_id: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(order_id)

    def remover_varios(self, ids_pedidos_vendas: Sequence[int]) -> JsonObject:
        """Remove vários pedidos de venda.

        Endpoint: DELETE /pedidos/vendas

        Remove vários pedidos de venda pelos IDs.

        Args:
            ids_pedidos_vendas: IDs dos pedidos de venda (Bling: ``idsPedidosVendas[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(
            "/pedidos/vendas", params={"idsPedidosVendas[]": list(ids_pedidos_vendas)}
        )

    def delete_many(self, order_ids: Sequence[int]) -> JsonObject:
        """Compatibility alias for ``remover_varios()``.

        Remove vários pedidos de venda.

        Endpoint: DELETE /pedidos/vendas

        Remove vários pedidos de venda pelos IDs.

        Args:
            order_ids: IDs dos pedidos de venda (Bling: ``idsPedidosVendas[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover_varios(order_ids)

    def alterar_situacao(self, id_pedido_venda: int, id_situacao: int) -> JsonObject:
        """Altera a situação de um pedido de venda.

        Endpoint: PATCH /pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}

        Altera a situação de um pedido de venda pelo ID.

        Args:
            id_pedido_venda: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)
            id_situacao: ID da situação do pedido de venda (Bling: ``idSituacao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(f"/pedidos/vendas/{id_pedido_venda}/situacoes/{id_situacao}")

    def update_status(self, order_id: int, status_id: int) -> JsonObject:
        """Compatibility alias for ``alterar_situacao()``.

        Altera a situação de um pedido de venda.

        Endpoint: PATCH /pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}

        Altera a situação de um pedido de venda pelo ID.

        Args:
            order_id: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)
            status_id: ID da situação do pedido de venda (Bling: ``idSituacao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar_situacao(order_id, status_id)

    def lancar_estoque(self, id_pedido_venda: int, *, id_deposito: int | None = None) -> JsonObject:
        """Lança estoque de um pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/lancar-estoque

        Lança o estoque de um pedido de venda pelo ID, no depósito padrão ou
        em um depósito específico se ``idDeposito`` for informado.

        Args:
            id_pedido_venda: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)
            id_deposito: ID do depósito de estoque (Bling: ``idDeposito``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        if id_deposito is None:
            return self._post(f"/pedidos/vendas/{id_pedido_venda}/lancar-estoque")
        return self._post(f"/pedidos/vendas/{id_pedido_venda}/lancar-estoque/{id_deposito}")

    def post_stock(self, order_id: int, *, deposit_id: int | None = None) -> JsonObject:
        """Compatibility alias for ``lancar_estoque()``.

        Lança estoque de um pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/lancar-estoque

        Lança o estoque de um pedido de venda pelo ID, no depósito padrão ou
        em um depósito específico se ``deposit_id`` for informado.

        Args:
            order_id: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)
            deposit_id: ID do depósito de estoque (Bling: ``idDeposito``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.lancar_estoque(order_id, id_deposito=deposit_id)

    def estornar_estoque(self, id_pedido_venda: int) -> JsonObject:
        """Estorna o estoque de um pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/estornar-estoque

        Estorna o estoque de um pedido de venda pelo ID.

        Args:
            id_pedido_venda: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 404: ErrorResponse
        """
        return self._post(f"/pedidos/vendas/{id_pedido_venda}/estornar-estoque")

    def reverse_stock(self, order_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_estoque()``.

        Estorna o estoque de um pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/estornar-estoque

        Estorna o estoque de um pedido de venda pelo ID.

        Args:
            order_id: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 404: ErrorResponse
        """
        return self.estornar_estoque(order_id)

    def lancar_contas(self, id_pedido_venda: int) -> JsonObject:
        """Lança as contas de um pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/lancar-contas

        Lança as contas de um pedido de venda pelo ID.

        Args:
            id_pedido_venda: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/pedidos/vendas/{id_pedido_venda}/lancar-contas")

    def post_accounts(self, order_id: int) -> JsonObject:
        """Compatibility alias for ``lancar_contas()``.

        Lança as contas de um pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/lancar-contas

        Lança as contas de um pedido de venda pelo ID.

        Args:
            order_id: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.lancar_contas(order_id)

    def estornar_contas(self, id_pedido_venda: int) -> JsonObject:
        """Estorna as contas de um pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/estornar-contas

        Estorna as contas de um pedido de venda pelo ID.

        Args:
            id_pedido_venda: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/pedidos/vendas/{id_pedido_venda}/estornar-contas")

    def reverse_accounts(self, order_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_contas()``.

        Estorna as contas de um pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/estornar-contas

        Estorna as contas de um pedido de venda pelo ID.

        Args:
            order_id: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.estornar_contas(order_id)

    def gerar_nota_fiscal(self, id_pedido_venda: int) -> JsonObject:
        """Gera nota fiscal eletrônica a partir do pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/gerar-nfe

        Gera nota fiscal eletrônica a partir do pedido de venda pelo ID.

        Args:
            id_pedido_venda: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: VendasCreateInvoiceResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/pedidos/vendas/{id_pedido_venda}/gerar-nfe")

    def generate_invoice(self, order_id: int) -> JsonObject:
        """Compatibility alias for ``gerar_nota_fiscal()``.

        Gera nota fiscal eletrônica a partir do pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/gerar-nfe

        Gera nota fiscal eletrônica a partir do pedido de venda pelo ID.

        Args:
            order_id: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: VendasCreateInvoiceResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.gerar_nota_fiscal(order_id)

    def gerar_nota_fiscal_consumidor(self, id_pedido_venda: int) -> JsonObject:
        """Gera nota fiscal de consumidor eletrônica a partir do pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/gerar-nfce

        Gera nota fiscal de consumidor eletrônica a partir do pedido de venda pelo ID.

        Args:
            id_pedido_venda: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: VendasCreateInvoiceResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/pedidos/vendas/{id_pedido_venda}/gerar-nfce")

    def generate_consumer_invoice(self, order_id: int) -> JsonObject:
        """Compatibility alias for ``gerar_nota_fiscal_consumidor()``.

        Gera nota fiscal de consumidor eletrônica a partir do pedido de venda.

        Endpoint: POST /pedidos/vendas/{idPedidoVenda}/gerar-nfce

        Gera nota fiscal de consumidor eletrônica a partir do pedido de venda pelo ID.

        Args:
            order_id: ID do pedido de venda (Bling: ``idPedidoVenda``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: VendasCreateInvoiceResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.gerar_nota_fiscal_consumidor(order_id)


def _sales_order_list_params(  # noqa: PLR0913
    *,
    pagina: int,
    limite: int,
    id_contato: int | None,
    ids_situacoes: Sequence[int] | None,
    data_inicial: DateFilter | None,
    data_final: DateFilter | None,
    data_alteracao_inicial: DateFilter | None,
    data_alteracao_final: DateFilter | None,
    data_prevista_inicial: DateFilter | None,
    data_prevista_final: DateFilter | None,
    numero: int | None,
    id_loja: int | None,
    id_vendedor: int | None,
    id_controle_caixa: int | None,
    numeros_lojas: Sequence[str] | None,
    id_unidade_negocio: int | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "idContato": id_contato,
            "idsSituacoes[]": list(ids_situacoes) if ids_situacoes is not None else None,
            "dataInicial": _format_date_filter(data_inicial),
            "dataFinal": _format_date_filter(data_final),
            "dataAlteracaoInicial": _format_datetime_filter(data_alteracao_inicial),
            "dataAlteracaoFinal": _format_datetime_filter(data_alteracao_final),
            "dataPrevistaInicial": _format_date_filter(data_prevista_inicial),
            "dataPrevistaFinal": _format_date_filter(data_prevista_final),
            "numero": numero,
            "idLoja": id_loja,
            "idVendedor": id_vendedor,
            "idControleCaixa": id_controle_caixa,
            "numerosLojas[]": list(numeros_lojas) if numeros_lojas is not None else None,
            "idUnidadeNegocio": id_unidade_negocio,
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
