"""NFC-e (Nota Fiscal do Consumidor Eletrônica) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.models.generated.schemas.notas_fiscais_consumidor import (
        NfceIdNotaFiscalConsumidorPutRequest,
        NfcePostRequest,
    )
    from bling_erp_api.types import JsonObject, QueryParams


class NfceResource(BaseResource):
    """Operações de notas fiscais do consumidor eletrônicas (NFC-e).

    Este recurso mapeia os endpoints ``/nfce``. Os métodos canônicos usam
    português para acompanhar a documentação oficial; os métodos em inglês
    continuam disponíveis como aliases de compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        id_transportador: int | None = None,
        chave_acesso: str | None = None,
        numero: str | None = None,
        serie: str | None = None,
        situacao: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> JsonObject:
        """Lista notas fiscais do consumidor (NFC-e).

        Endpoint: GET /nfce

        Obtém lista paginada de NFC-e.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            id_transportador: ID do transportador (Bling: ``idTransportador``, integer, opcional)
            chave_acesso: Chave de acesso (Bling: ``chaveAcesso``, string, opcional)
            numero: N° da nota (Bling: ``numero``, string, opcional)
            serie: Série (Bling: ``serie``, string, opcional)
            situacao: Situação (Bling: ``situacao``, integer, opcional)
            data_emissao_inicial: Data de emissão inicial (Bling: ``dataEmissaoInicial``, string, opcional)
            data_emissao_final: Data de emissão final (Bling: ``dataEmissaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosBaseDTO; 404: ErrorResponse
        """
        return self._get(
            "/nfce",
            params=_nfce_list_params(
                pagina=pagina,
                limite=limite,
                id_transportador=id_transportador,
                chave_acesso=chave_acesso,
                numero=numero,
                serie=serie,
                situacao=situacao,
                data_emissao_inicial=data_emissao_inicial,
                data_emissao_final=data_emissao_final,
            ),
        )

    def list(  # noqa: PLR0913
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        carrier_id: int | None = None,
        access_key: str | None = None,
        number: str | None = None,
        series: str | None = None,
        status: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lista notas fiscais do consumidor (NFC-e).

        Endpoint: GET /nfce

        Obtém lista paginada de NFC-e.

        Args:
            page: N° da página (Bling: ``pagina``, integer, opcional)
            limit: Registros por página (Bling: ``limite``, integer, opcional)
            carrier_id: ID do transportador (Bling: ``idTransportador``, integer, opcional)
            access_key: Chave de acesso (Bling: ``chaveAcesso``, string, opcional)
            number: N° da nota (Bling: ``numero``, string, opcional)
            series: Série (Bling: ``serie``, string, opcional)
            status: Situação (Bling: ``situacao``, integer, opcional)
            issued_start: Data de emissão inicial (Bling: ``dataEmissaoInicial``, string, opcional)
            issued_end: Data de emissão final (Bling: ``dataEmissaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosBaseDTO; 404: ErrorResponse
        """
        return self.listar(
            pagina=page,
            limite=limit,
            id_transportador=carrier_id,
            chave_acesso=access_key,
            numero=number,
            serie=series,
            situacao=status,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        id_transportador: int | None = None,
        chave_acesso: str | None = None,
        numero: str | None = None,
        serie: str | None = None,
        situacao: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> Iterator[JsonObject]:
        """Itera pelas NFC-e página a página.

        Endpoint: GET /nfce (via paginação automática)

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            id_transportador: ID do transportador (Bling: ``idTransportador``, integer, opcional)
            chave_acesso: Chave de acesso (Bling: ``chaveAcesso``, string, opcional)
            numero: N° da nota (Bling: ``numero``, string, opcional)
            serie: Série (Bling: ``serie``, string, opcional)
            situacao: Situação (Bling: ``situacao``, integer, opcional)
            data_emissao_inicial: Data de emissão inicial (Bling: ``dataEmissaoInicial``, string, opcional)
            data_emissao_final: Data de emissão final (Bling: ``dataEmissaoFinal``, string, opcional)

        Returns:
            Iterator sobre os itens da resposta.
        """
        params = _nfce_list_params(
            pagina=pagina,
            limite=limite,
            id_transportador=id_transportador,
            chave_acesso=chave_acesso,
            numero=numero,
            serie=serie,
            situacao=situacao,
            data_emissao_inicial=data_emissao_inicial,
            data_emissao_final=data_emissao_final,
        )
        return self._iterate("/nfce", page=pagina or 1, limit=limite or 100, params=params)

    def iterate(  # noqa: PLR0913
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        carrier_id: int | None = None,
        access_key: str | None = None,
        number: str | None = None,
        series: str | None = None,
        status: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``.

        Itera pelas NFC-e página a página.

        Endpoint: GET /nfce (via paginação automática)

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            page: N° da página (Bling: ``pagina``, integer, opcional)
            limit: Registros por página (Bling: ``limite``, integer, opcional)
            carrier_id: ID do transportador (Bling: ``idTransportador``, integer, opcional)
            access_key: Chave de acesso (Bling: ``chaveAcesso``, string, opcional)
            number: N° da nota (Bling: ``numero``, string, opcional)
            series: Série (Bling: ``serie``, string, opcional)
            status: Situação (Bling: ``situacao``, integer, opcional)
            issued_start: Data de emissão inicial (Bling: ``dataEmissaoInicial``, string, opcional)
            issued_end: Data de emissão final (Bling: ``dataEmissaoFinal``, string, opcional)

        Returns:
            Iterator sobre os itens da resposta.
        """
        return self.iterar(
            pagina=page,
            limite=limit,
            id_transportador=carrier_id,
            chave_acesso=access_key,
            numero=number,
            serie=series,
            situacao=status,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def obter(self, id_nota_fiscal_consumidor: int) -> JsonObject:
        """Obtém uma NFC-e.

        Endpoint: GET /nfce/{idNotaFiscalConsumidor}

        Obtém uma nota fiscal do consumidor pelo ID.

        Args:
            id_nota_fiscal_consumidor: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 404: ErrorResponse
        """
        return self._get(f"/nfce/{id_nota_fiscal_consumidor}")

    def get(self, consumer_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém uma NFC-e.

        Endpoint: GET /nfce/{idNotaFiscalConsumidor}

        Obtém uma nota fiscal do consumidor pelo ID.

        Args:
            consumer_invoice_id: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 404: ErrorResponse
        """
        return self.obter(consumer_invoice_id)

    def criar(self, dados: NfcePostRequest) -> JsonObject:
        """Cria uma NFC-e.

        Endpoint: POST /nfce

        Cria uma nova nota fiscal do consumidor eletrônica.

        Args:
            dados: Dados da NFC-e. Use ``NfcePostRequest`` para uso tipado
                ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self._post("/nfce", json=to_json_object(dados))

    def create(self, data: NfcePostRequest) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria uma NFC-e.

        Endpoint: POST /nfce

        Cria uma nova nota fiscal do consumidor eletrônica.

        Args:
            data: Dados da NFC-e. Use ``NfcePostRequest`` para uso tipado
                ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self.criar(data)

    def alterar(
        self, id_nota_fiscal_consumidor: int, dados: NfceIdNotaFiscalConsumidorPutRequest
    ) -> JsonObject:
        """Altera uma NFC-e.

        Endpoint: PUT /nfce/{idNotaFiscalConsumidor}

        Altera uma nota fiscal do consumidor pelo ID.

        Args:
            id_nota_fiscal_consumidor: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)
            dados: Dados da NFC-e para atualização. Use ``NfceIdNotaFiscalConsumidorPutRequest``
                para uso tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/nfce/{id_nota_fiscal_consumidor}", json=to_json_object(dados))

    def update(
        self, consumer_invoice_id: int, data: NfceIdNotaFiscalConsumidorPutRequest
    ) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera uma NFC-e.

        Endpoint: PUT /nfce/{idNotaFiscalConsumidor}

        Altera uma nota fiscal do consumidor pelo ID.

        Args:
            consumer_invoice_id: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)
            data: Dados da NFC-e para atualização. Use ``NfceIdNotaFiscalConsumidorPutRequest``
                para uso tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(consumer_invoice_id, data)

    def autorizar(
        self, id_nota_fiscal_consumidor: int, *, enviar_email: bool | None = None
    ) -> JsonObject:
        """Autoriza (envia para a SEFAZ) uma NFC-e.

        Endpoint: POST /nfce/{idNotaFiscalConsumidor}/enviar

        Envia uma NFC-e para autorização da SEFAZ.

        Args:
            id_nota_fiscal_consumidor: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)
            enviar_email: Enviar e-mail após autorização (Bling: ``enviarEmail``, boolean, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        params = compact_params({"enviarEmail": enviar_email})
        return self._post(f"/nfce/{id_nota_fiscal_consumidor}/enviar", params=params)

    def authorize(self, consumer_invoice_id: int, *, send_email: bool | None = None) -> JsonObject:
        """Compatibility alias for ``autorizar()``.

        Autoriza (envia para a SEFAZ) uma NFC-e.

        Endpoint: POST /nfce/{idNotaFiscalConsumidor}/enviar

        Envia uma NFC-e para autorização da SEFAZ.

        Args:
            consumer_invoice_id: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)
            send_email: Enviar e-mail após autorização (Bling: ``enviarEmail``, boolean, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.autorizar(consumer_invoice_id, enviar_email=send_email)

    def lancar_contas(self, id_nota_fiscal_consumidor: int) -> JsonObject:
        """Lança as contas de uma NFC-e.

        Endpoint: POST /nfce/{idNotaFiscalConsumidor}/lancar-contas

        Lança as contas a pagar/receber geradas a partir de uma NFC-e.

        Args:
            id_nota_fiscal_consumidor: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/nfce/{id_nota_fiscal_consumidor}/lancar-contas")

    def post_accounts(self, consumer_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``lancar_contas()``.

        Lança as contas de uma NFC-e.

        Endpoint: POST /nfce/{idNotaFiscalConsumidor}/lancar-contas

        Lança as contas a pagar/receber geradas a partir de uma NFC-e.

        Args:
            consumer_invoice_id: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.lancar_contas(consumer_invoice_id)

    def estornar_contas(self, id_nota_fiscal_consumidor: int) -> JsonObject:
        """Estorna as contas de uma NFC-e.

        Endpoint: POST /nfce/{idNotaFiscalConsumidor}/estornar-contas

        Estorna as contas vinculadas a uma NFC-e.

        Args:
            id_nota_fiscal_consumidor: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/nfce/{id_nota_fiscal_consumidor}/estornar-contas")

    def reverse_accounts(self, consumer_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_contas()``.

        Estorna as contas de uma NFC-e.

        Endpoint: POST /nfce/{idNotaFiscalConsumidor}/estornar-contas

        Estorna as contas vinculadas a uma NFC-e.

        Args:
            consumer_invoice_id: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.estornar_contas(consumer_invoice_id)

    def lancar_estoque(
        self, id_nota_fiscal_consumidor: int, *, id_deposito: int | None = None
    ) -> JsonObject:
        """Lança o estoque de uma NFC-e.

        Endpoint: POST /nfce/{idNotaFiscalConsumidor}/lancar-estoque[/{idDeposito}]

        Lança o estoque de uma NFC-e, opcionalmente em um depósito específico.

        Args:
            id_nota_fiscal_consumidor: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)
            id_deposito: ID do depósito (Bling: ``idDeposito``, integer, opcional). Se
                omitido, usa o depósito padrão.

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        if id_deposito is not None:
            return self._post(f"/nfce/{id_nota_fiscal_consumidor}/lancar-estoque/{id_deposito}")
        return self._post(f"/nfce/{id_nota_fiscal_consumidor}/lancar-estoque")

    def post_stock(self, consumer_invoice_id: int, *, deposit_id: int | None = None) -> JsonObject:
        """Compatibility alias for ``lancar_estoque()``.

        Lança o estoque de uma NFC-e.

        Endpoint: POST /nfce/{idNotaFiscalConsumidor}/lancar-estoque[/{idDeposito}]

        Lança o estoque de uma NFC-e, opcionalmente em um depósito específico.

        Args:
            consumer_invoice_id: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)
            deposit_id: ID do depósito (Bling: ``idDeposito``, integer, opcional). Se
                omitido, usa o depósito padrão.

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.lancar_estoque(consumer_invoice_id, id_deposito=deposit_id)

    def estornar_estoque(self, id_nota_fiscal_consumidor: int) -> JsonObject:
        """Estorna o estoque de uma NFC-e.

        Endpoint: POST /nfce/{idNotaFiscalConsumidor}/estornar-estoque

        Estorna o estoque lançado de uma NFC-e.

        Args:
            id_nota_fiscal_consumidor: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 404: ErrorResponse
        """
        return self._post(f"/nfce/{id_nota_fiscal_consumidor}/estornar-estoque")

    def reverse_stock(self, consumer_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_estoque()``.

        Estorna o estoque de uma NFC-e.

        Endpoint: POST /nfce/{idNotaFiscalConsumidor}/estornar-estoque

        Estorna o estoque lançado de uma NFC-e.

        Args:
            consumer_invoice_id: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 404: ErrorResponse
        """
        return self.estornar_estoque(consumer_invoice_id)


def _nfce_list_params(  # noqa: PLR0913
    *,
    pagina: int | None,
    limite: int | None,
    id_transportador: int | None,
    chave_acesso: str | None,
    numero: str | None,
    serie: str | None,
    situacao: int | None,
    data_emissao_inicial: str | None,
    data_emissao_final: str | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "idTransportador": id_transportador,
            "chaveAcesso": chave_acesso,
            "numero": numero,
            "serie": serie,
            "situacao": situacao,
            "dataEmissaoInicial": data_emissao_inicial,
            "dataEmissaoFinal": data_emissao_final,
        }
    )
