"""NF-e (Nota Fiscal Eletrônica) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.invoices import (
    NfeDeleteResponse200,
    NfeDocumentoChaveAcessoGetResponse200,
    NfeGetResponse200,
    NfeIdNotaFiscalEnviarPostResponse200,
    NfeIdNotaFiscalGetResponse200,
    NfeIdNotaFiscalPutRequest,
    NfeIdNotaFiscalPutResponse200,
    NfePostRequest,
    NfePostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from bling_erp_api.types import JsonObject, QueryParams


class NfeResource(BaseResource):
    """Operações de notas fiscais eletrônicas (NF-e).

    Este recurso mapeia os endpoints ``/nfe``. Os métodos canônicos usam
    português para acompanhar a documentação oficial; os métodos em inglês
    continuam disponíveis como aliases de compatibilidade.

    Para NFC-e use ``NfceResource`` (``client.notas_fiscais_consumidor``).
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        numero_loja: int | None = None,
        id_transportador: int | None = None,
        chave_acesso: str | None = None,
        numero: str | None = None,
        serie: str | None = None,
        situacao: int | None = None,
        tipo: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> NfeGetResponse200:
        """Lista notas fiscais eletrônicas (NF-e).

        Endpoint: GET /nfe

        Obtém lista paginada de NF-e.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            numero_loja: N° da loja (Bling: ``numeroLoja``, integer, opcional)
            id_transportador: ID do transportador (Bling: ``idTransportador``, integer, opcional)
            chave_acesso: Chave de acesso da NF-e (Bling: ``chaveAcesso``, string, opcional)
            numero: N° da nota fiscal (Bling: ``numero``, string, opcional)
            serie: Série da nota fiscal (Bling: ``serie``, string, opcional)
            situacao: Situação (Bling: ``situacao``, integer, opcional)
            tipo: Tipo (Bling: ``tipo``, integer, opcional)
            data_emissao_inicial: Data de emissão inicial (Bling: ``dataEmissaoInicial``, string, opcional)
            data_emissao_final: Data de emissão final (Bling: ``dataEmissaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosBaseDTO; 404: ErrorResponse
        """
        raw = self._get(
            "/nfe",
            params=_nfe_list_params(
                pagina=pagina,
                limite=limite,
                numero_loja=numero_loja,
                id_transportador=id_transportador,
                chave_acesso=chave_acesso,
                numero=numero,
                serie=serie,
                situacao=situacao,
                tipo=tipo,
                data_emissao_inicial=data_emissao_inicial,
                data_emissao_final=data_emissao_final,
            ),
        )
        return self._validate_response(NfeGetResponse200, raw)

    def list(  # noqa: PLR0913
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        store_number: int | None = None,
        carrier_id: int | None = None,
        access_key: str | None = None,
        number: str | None = None,
        series: str | None = None,
        status: int | None = None,
        kind: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> NfeGetResponse200:
        """Compatibility alias for ``listar()``.

        Lista notas fiscais eletrônicas (NF-e).

        Endpoint: GET /nfe

        Obtém lista paginada de NF-e.

        Args:
            page: N° da página (Bling: ``pagina``, integer, opcional)
            limit: Registros por página (Bling: ``limite``, integer, opcional)
            store_number: N° da loja (Bling: ``numeroLoja``, integer, opcional)
            carrier_id: ID do transportador (Bling: ``idTransportador``, integer, opcional)
            access_key: Chave de acesso da NF-e (Bling: ``chaveAcesso``, string, opcional)
            number: N° da nota fiscal (Bling: ``numero``, string, opcional)
            series: Série da nota fiscal (Bling: ``serie``, string, opcional)
            status: Situação (Bling: ``situacao``, integer, opcional)
            kind: Tipo (Bling: ``tipo``, integer, opcional)
            issued_start: Data de emissão inicial (Bling: ``dataEmissaoInicial``, string, opcional)
            issued_end: Data de emissão final (Bling: ``dataEmissaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosBaseDTO; 404: ErrorResponse
        """
        return self.listar(
            pagina=page,
            limite=limit,
            numero_loja=store_number,
            id_transportador=carrier_id,
            chave_acesso=access_key,
            numero=number,
            serie=series,
            situacao=status,
            tipo=kind,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        numero_loja: int | None = None,
        id_transportador: int | None = None,
        chave_acesso: str | None = None,
        numero: str | None = None,
        serie: str | None = None,
        situacao: int | None = None,
        tipo: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> Iterator[JsonObject]:
        """Itera pelas NF-e página a página.

        Endpoint: GET /nfe (via paginação automática)

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            pagina: N° da página inicial
            limite: Registros por página
            numero_loja: N° da loja
            id_transportador: ID do transportador
            chave_acesso: Chave de acesso
            numero: N° da nota
            serie: Série
            situacao: Situação
            tipo: Tipo
            data_emissao_inicial: Data de emissão inicial
            data_emissao_final: Data de emissão final

        Yields:
            Iterator de JsonObject — cada iteração retorna a resposta de uma página
        """
        params = _nfe_list_params(
            pagina=pagina,
            limite=limite,
            numero_loja=numero_loja,
            id_transportador=id_transportador,
            chave_acesso=chave_acesso,
            numero=numero,
            serie=serie,
            situacao=situacao,
            tipo=tipo,
            data_emissao_inicial=data_emissao_inicial,
            data_emissao_final=data_emissao_final,
        )
        return self._iterate("/nfe", page=pagina or 1, limit=limite or 100, params=params)

    def iterate(  # noqa: PLR0913
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        store_number: int | None = None,
        carrier_id: int | None = None,
        access_key: str | None = None,
        number: str | None = None,
        series: str | None = None,
        status: int | None = None,
        kind: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``.

        Itera pelas NF-e página a página.

        Endpoint: GET /nfe (via paginação automática)

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            page: N° da página inicial
            limit: Registros por página
            store_number: N° da loja
            carrier_id: ID do transportador
            access_key: Chave de acesso
            number: N° da nota
            series: Série
            status: Situação
            kind: Tipo
            issued_start: Data de emissão inicial
            issued_end: Data de emissão final

        Yields:
            Iterator de JsonObject — cada iteração retorna a resposta de uma página
        """
        return self.iterar(
            pagina=page,
            limite=limit,
            numero_loja=store_number,
            id_transportador=carrier_id,
            chave_acesso=access_key,
            numero=number,
            serie=series,
            situacao=status,
            tipo=kind,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def obter(self, id_nota_fiscal: int) -> NfeIdNotaFiscalGetResponse200:
        """Obtém uma NF-e.

        Endpoint: GET /nfe/{idNotaFiscal}

        Obtém uma nota fiscal eletrônica pelo ID.

        Args:
            id_nota_fiscal: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 404: ErrorResponse
        """
        raw = self._get(f"/nfe/{id_nota_fiscal}")
        return self._validate_response(NfeIdNotaFiscalGetResponse200, raw)

    def get(self, invoice_id: int) -> NfeIdNotaFiscalGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém uma NF-e.

        Endpoint: GET /nfe/{idNotaFiscal}

        Obtém uma nota fiscal eletrônica pelo ID.

        Args:
            invoice_id: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 404: ErrorResponse
        """
        return self.obter(invoice_id)

    def criar(self, dados: NfePostRequest) -> NfePostResponse201:
        """Cria uma NF-e.

        Endpoint: POST /nfe

        Cria uma nova nota fiscal eletrônica.

        Args:
            dados: Dados da NF-e. Request body schema: NotasFiscaisDadosPostDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        raw = self._post("/nfe", json=to_json_object(dados))
        return self._validate_response(NfePostResponse201, raw)

    def create(self, data: NfePostRequest) -> NfePostResponse201:
        """Compatibility alias for ``criar()``.

        Cria uma NF-e.

        Endpoint: POST /nfe

        Cria uma nova nota fiscal eletrônica.

        Args:
            data: Dados da NF-e. Request body schema: NotasFiscaisDadosPostDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self.criar(data)

    def alterar(
        self, id_nota_fiscal: int, dados: NfeIdNotaFiscalPutRequest
    ) -> NfeIdNotaFiscalPutResponse200:
        """Altera uma NF-e.

        Endpoint: PUT /nfe/{idNotaFiscal}

        Altera uma nota fiscal eletrônica pelo ID.

        Args:
            id_nota_fiscal: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)
            dados: Dados da NF-e para atualização. Request body schema: NotasFiscaisDadosPostDTO

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        raw = self._put(f"/nfe/{id_nota_fiscal}", json=to_json_object(dados))
        return self._validate_response(NfeIdNotaFiscalPutResponse200, raw)

    def update(
        self, invoice_id: int, data: NfeIdNotaFiscalPutRequest
    ) -> NfeIdNotaFiscalPutResponse200:
        """Compatibility alias for ``alterar()``.

        Altera uma NF-e.

        Endpoint: PUT /nfe/{idNotaFiscal}

        Altera uma nota fiscal eletrônica pelo ID.

        Args:
            invoice_id: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)
            data: Dados da NF-e para atualização. Request body schema: NotasFiscaisDadosPostDTO

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(invoice_id, data)

    def remover_varios(self, ids_notas: Sequence[int]) -> NfeDeleteResponse200:
        """Remove múltiplas NF-e.

        Endpoint: DELETE /nfe

        Remove múltiplas notas fiscais eletrônicas pelos IDs.

        Args:
            ids_notas: IDs das notas fiscais (Bling: ``idsNotas[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisExclusaoDTO; 204: NoContent; 400: ErrorResponse
        """
        raw = self._delete("/nfe", params={"idsNotas[]": list(ids_notas)})
        return self._validate_response(NfeDeleteResponse200, raw)

    def delete_many(self, invoice_ids: Sequence[int]) -> NfeDeleteResponse200:
        """Compatibility alias for ``remover_varios()``.

        Remove múltiplas NF-e.

        Endpoint: DELETE /nfe

        Remove múltiplas notas fiscais eletrônicas pelos IDs.

        Args:
            invoice_ids: IDs das notas fiscais (Bling: ``idsNotas[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisExclusaoDTO; 204: NoContent; 400: ErrorResponse
        """
        return self.remover_varios(invoice_ids)

    def autorizar(
        self, id_nota_fiscal: int, *, enviar_email: bool | None = None
    ) -> NfeIdNotaFiscalEnviarPostResponse200:
        """Autoriza (envia para a SEFAZ) uma NF-e.

        Endpoint: POST /nfe/{idNotaFiscal}/enviar

        Envia uma NF-e para autorização da SEFAZ.

        Args:
            id_nota_fiscal: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)
            enviar_email: Enviar e-mail após autorização (Bling: ``enviarEmail``, boolean, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        params = compact_params({"enviarEmail": enviar_email})
        raw = self._post(f"/nfe/{id_nota_fiscal}/enviar", params=params)
        return self._validate_response(NfeIdNotaFiscalEnviarPostResponse200, raw)

    def authorize(
        self, invoice_id: int, *, send_email: bool | None = None
    ) -> NfeIdNotaFiscalEnviarPostResponse200:
        """Compatibility alias for ``autorizar()``.

        Autoriza (envia para a SEFAZ) uma NF-e.

        Endpoint: POST /nfe/{idNotaFiscal}/enviar

        Envia uma NF-e para autorização da SEFAZ.

        Args:
            invoice_id: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)
            send_email: Enviar e-mail após autorização (Bling: ``enviarEmail``, boolean, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosGetDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.autorizar(invoice_id, enviar_email=send_email)

    def lancar_contas(self, id_nota_fiscal: int) -> JsonObject:
        """Lança as contas de uma NF-e.

        Endpoint: POST /nfe/{idNotaFiscal}/lancar-contas

        Lança as contas a pagar/receber geradas a partir de uma NF-e.

        Args:
            id_nota_fiscal: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/nfe/{id_nota_fiscal}/lancar-contas")

    def post_accounts(self, invoice_id: int) -> JsonObject:
        """Compatibility alias for ``lancar_contas()``.

        Lança as contas de uma NF-e.

        Endpoint: POST /nfe/{idNotaFiscal}/lancar-contas

        Lança as contas a pagar/receber geradas a partir de uma NF-e.

        Args:
            invoice_id: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.lancar_contas(invoice_id)

    def estornar_contas(self, id_nota_fiscal: int) -> JsonObject:
        """Estorna as contas de uma NF-e.

        Endpoint: POST /nfe/{idNotaFiscal}/estornar-contas

        Estorna as contas a pagar/receber vinculadas a uma NF-e.

        Args:
            id_nota_fiscal: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/nfe/{id_nota_fiscal}/estornar-contas")

    def reverse_accounts(self, invoice_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_contas()``.

        Estorna as contas de uma NF-e.

        Endpoint: POST /nfe/{idNotaFiscal}/estornar-contas

        Estorna as contas a pagar/receber vinculadas a uma NF-e.

        Args:
            invoice_id: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.estornar_contas(invoice_id)

    def lancar_estoque(self, id_nota_fiscal: int, *, id_deposito: int | None = None) -> JsonObject:
        """Lança o estoque de uma NF-e.

        Endpoint: POST /nfe/{idNotaFiscal}/lancar-estoque[/{idDeposito}]

        Lança o estoque de uma NF-e, opcionalmente em um depósito específico.

        Args:
            id_nota_fiscal: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)
            id_deposito: ID do depósito (Bling: ``idDeposito``, integer, opcional). Se
                omitido, usa o depósito padrão.

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        if id_deposito is not None:
            return self._post(f"/nfe/{id_nota_fiscal}/lancar-estoque/{id_deposito}")
        return self._post(f"/nfe/{id_nota_fiscal}/lancar-estoque")

    def post_stock(self, invoice_id: int, *, deposit_id: int | None = None) -> JsonObject:
        """Compatibility alias for ``lancar_estoque()``.

        Lança o estoque de uma NF-e.

        Endpoint: POST /nfe/{idNotaFiscal}/lancar-estoque[/{idDeposito}]

        Lança o estoque de uma NF-e, opcionalmente em um depósito específico.

        Args:
            invoice_id: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)
            deposit_id: ID do depósito (Bling: ``idDeposito``, integer, opcional). Se
                omitido, usa o depósito padrão.

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.lancar_estoque(invoice_id, id_deposito=deposit_id)

    def estornar_estoque(self, id_nota_fiscal: int) -> JsonObject:
        """Estorna o estoque de uma NF-e.

        Endpoint: POST /nfe/{idNotaFiscal}/estornar-estoque

        Estorna o estoque lançado de uma NF-e.

        Args:
            id_nota_fiscal: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 404: ErrorResponse
        """
        return self._post(f"/nfe/{id_nota_fiscal}/estornar-estoque")

    def reverse_stock(self, invoice_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_estoque()``.

        Estorna o estoque de uma NF-e.

        Endpoint: POST /nfe/{idNotaFiscal}/estornar-estoque

        Estorna o estoque lançado de uma NF-e.

        Args:
            invoice_id: ID da nota fiscal (Bling: ``idNotaFiscal``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 404: ErrorResponse
        """
        return self.estornar_estoque(invoice_id)

    def obter_documento_nota_fiscal(
        self, chave_acesso: str, *, formato: str | None = None
    ) -> NfeDocumentoChaveAcessoGetResponse200:
        """Obtém o documento (XML/DANFE) de uma NF-e.

        Endpoint: GET /nfe/documento/{chaveAcesso}

        Obtém o documento de uma NF-e pela chave de acesso.

        Args:
            chave_acesso: Chave de acesso da NF-e (Bling: ``chaveAcesso``, string, obrigatório)
            formato: Formato do documento: pdf ou xml (Bling: ``formato``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDocumentoDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        params = compact_params({"formato": formato})
        raw = self._get(f"/nfe/documento/{chave_acesso}", params=params)
        return self._validate_response(NfeDocumentoChaveAcessoGetResponse200, raw)

    def get_document(
        self, access_key: str, *, output_format: str | None = None
    ) -> NfeDocumentoChaveAcessoGetResponse200:
        """Compatibility alias for ``obter_documento_nota_fiscal()``.

        Obtém o documento (XML/DANFE) de uma NF-e.

        Endpoint: GET /nfe/documento/{chaveAcesso}

        Obtém o documento de uma NF-e pela chave de acesso.

        Args:
            access_key: Chave de acesso da NF-e (Bling: ``chaveAcesso``, string, obrigatório)
            output_format: Formato do documento: pdf ou xml (Bling: ``formato``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDocumentoDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.obter_documento_nota_fiscal(access_key, formato=output_format)


def _nfe_list_params(  # noqa: PLR0913
    *,
    pagina: int | None,
    limite: int | None,
    numero_loja: int | None,
    id_transportador: int | None,
    chave_acesso: str | None,
    numero: str | None,
    serie: str | None,
    situacao: int | None,
    tipo: int | None,
    data_emissao_inicial: str | None,
    data_emissao_final: str | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "numeroLoja": numero_loja,
            "idTransportador": id_transportador,
            "chaveAcesso": chave_acesso,
            "numero": numero,
            "serie": serie,
            "situacao": situacao,
            "tipo": tipo,
            "dataEmissaoInicial": data_emissao_inicial,
            "dataEmissaoFinal": data_emissao_final,
        }
    )
