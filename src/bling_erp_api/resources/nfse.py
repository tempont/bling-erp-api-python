"""NFS-e (Nota Fiscal de Serviço Eletrônica) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.nfse import NfsePostRequest, NfsePostResponse201
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams


class NfseResource(BaseResource):
    """Operações de notas fiscais de serviço eletrônicas (NFS-e).

    Este recurso mapeia os endpoints ``/nfse``. Os métodos canônicos usam
    português para acompanhar a documentação oficial; os métodos em inglês
    continuam disponíveis como aliases de compatibilidade.
    """

    def listar(
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        situacao: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> JsonObject:
        """Lista notas fiscais de serviço (NFS-e).

        Endpoint: GET /nfse

        Obtém lista paginada de NFS-e.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            situacao: Situação (Bling: ``situacao``, integer, opcional)
            data_emissao_inicial: Data de emissão inicial (Bling: ``dataEmissaoInicial``, string, opcional)
            data_emissao_final: Data de emissão final (Bling: ``dataEmissaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasServicosDadosBaseDTO; 400: ErrorResponse
        """
        return self._get(
            "/nfse",
            params=_nfse_list_params(
                pagina=pagina,
                limite=limite,
                situacao=situacao,
                data_emissao_inicial=data_emissao_inicial,
                data_emissao_final=data_emissao_final,
            ),
        )

    def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        status: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lista notas fiscais de serviço (NFS-e).

        Endpoint: GET /nfse

        Obtém lista paginada de NFS-e.

        Args:
            page: N° da página (Bling: ``pagina``, integer, opcional)
            limit: Registros por página (Bling: ``limite``, integer, opcional)
            status: Situação (Bling: ``situacao``, integer, opcional)
            issued_start: Data de emissão inicial (Bling: ``dataEmissaoInicial``, string, opcional)
            issued_end: Data de emissão final (Bling: ``dataEmissaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotasServicosDadosBaseDTO; 400: ErrorResponse
        """
        return self.listar(
            pagina=page,
            limite=limit,
            situacao=status,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def iterar(
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        situacao: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> Iterator[JsonObject]:
        """Itera pelas NFS-e página a página.

        Endpoint: GET /nfse (via paginação automática)

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            pagina: N° da página inicial
            limite: Registros por página
            situacao: Situação
            data_emissao_inicial: Data de emissão inicial
            data_emissao_final: Data de emissão final

        Yields:
            Iterator de JsonObject — cada iteração retorna a resposta de uma página
        """
        params = _nfse_list_params(
            pagina=pagina,
            limite=limite,
            situacao=situacao,
            data_emissao_inicial=data_emissao_inicial,
            data_emissao_final=data_emissao_final,
        )
        return self._iterate("/nfse", page=pagina or 1, limit=limite or 100, params=params)

    def iterate(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        status: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``.

        Itera pelas NFS-e página a página.

        Endpoint: GET /nfse (via paginação automática)

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            page: N° da página inicial
            limit: Registros por página
            status: Situação
            issued_start: Data de emissão inicial
            issued_end: Data de emissão final

        Yields:
            Iterator de JsonObject — cada iteração retorna a resposta de uma página
        """
        return self.iterar(
            pagina=page,
            limite=limit,
            situacao=status,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def obter(self, id_nota_servico: int) -> JsonObject:
        """Obtém uma NFS-e.

        Endpoint: GET /nfse/{idNotaServico}

        Obtém uma nota fiscal de serviço pelo ID.

        Args:
            id_nota_servico: ID da NFS-e (Bling: ``idNotaServico``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasServicosDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/nfse/{id_nota_servico}")

    def get(self, service_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém uma NFS-e.

        Endpoint: GET /nfse/{idNotaServico}

        Obtém uma nota fiscal de serviço pelo ID.

        Args:
            service_invoice_id: ID da NFS-e (Bling: ``idNotaServico``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasServicosDadosDTO; 404: ErrorResponse
        """
        return self.obter(service_invoice_id)

    def criar(self, dados: NfsePostRequest) -> NfsePostResponse201:
        """Cria uma NFS-e.

        Endpoint: POST /nfse

        Cria uma nova nota fiscal de serviço.

        Args:
            dados: Dados da NFS-e. Request body schema: NfsePostRequest

        Returns:
            Bling API response. Response schemas: 201: NfsePostResponse201; 400: ErrorResponse
        """
        raw = self._post("/nfse", json=to_json_object(dados))
        return self._validate_response(NfsePostResponse201, raw)

    def create(self, data: NfsePostRequest) -> NfsePostResponse201:
        """Compatibility alias for ``criar()``.

        Cria uma NFS-e.

        Endpoint: POST /nfse

        Cria uma nova nota fiscal de serviço.

        Args:
            data: Dados da NFS-e. Request body schema: NfsePostRequest

        Returns:
            Bling API response. Response schemas: 201: NfsePostResponse201; 400: ErrorResponse
        """
        return self.criar(data)

    def remover(self, id_nota_servico: int) -> JsonObject:
        """Remove uma NFS-e.

        Endpoint: DELETE /nfse/{idNotaServico}

        Remove uma nota fiscal de serviço pelo ID.

        Args:
            id_nota_servico: ID da NFS-e (Bling: ``idNotaServico``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/nfse/{id_nota_servico}")

    def delete(self, service_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove uma NFS-e.

        Endpoint: DELETE /nfse/{idNotaServico}

        Remove uma nota fiscal de serviço pelo ID.

        Args:
            service_invoice_id: ID da NFS-e (Bling: ``idNotaServico``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(service_invoice_id)

    def autorizar(self, id_nota_servico: int) -> JsonObject:
        """Autoriza (envia) uma NFS-e.

        Endpoint: POST /nfse/{idNotaServico}/enviar

        Envia uma NFS-e para autorização.

        Args:
            id_nota_servico: ID da NFS-e (Bling: ``idNotaServico``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasServicosDadosDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(f"/nfse/{id_nota_servico}/enviar")

    def authorize(self, service_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``autorizar()``.

        Autoriza (envia) uma NFS-e.

        Endpoint: POST /nfse/{idNotaServico}/enviar

        Envia uma NFS-e para autorização.

        Args:
            service_invoice_id: ID da NFS-e (Bling: ``idNotaServico``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasServicosDadosDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.autorizar(service_invoice_id)

    def cancelar(self, id_nota_servico: int, dados: JsonObject) -> JsonObject:
        """Cancela uma NFS-e.

        Endpoint: POST /nfse/{idNotaServico}/cancelar

        Cancela uma nota fiscal de serviço.

        Args:
            id_nota_servico: ID da NFS-e (Bling: ``idNotaServico``, integer, obrigatório)
            dados: Dados de cancelamento. Request body schema: NotasServicosCancelamentoDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(
            f"/nfse/{id_nota_servico}/cancelar",
            json=to_json_object(dados),
        )

    def cancel(self, service_invoice_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``cancelar()``.

        Cancela uma NFS-e.

        Endpoint: POST /nfse/{idNotaServico}/cancelar

        Cancela uma nota fiscal de serviço.

        Args:
            service_invoice_id: ID da NFS-e (Bling: ``idNotaServico``, integer, obrigatório)
            data: Dados de cancelamento. Request body schema: NotasServicosCancelamentoDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.cancelar(service_invoice_id, data)

    def obter_configuracoes(self) -> JsonObject:
        """Obtém as configurações de NFS-e.

        Endpoint: GET /nfse/configuracoes

        Obtém as configurações atuais de NFS-e da empresa.

        Returns:
            Bling API response. Response schemas: 200: ConfiguracaoNotaServicoDadosBaseDTO
        """
        return self._get("/nfse/configuracoes")

    def get_settings(self) -> JsonObject:
        """Compatibility alias for ``obter_configuracoes()``.

        Obtém as configurações de NFS-e.

        Endpoint: GET /nfse/configuracoes

        Obtém as configurações atuais de NFS-e da empresa.

        Returns:
            Bling API response. Response schemas: 200: ConfiguracaoNotaServicoDadosBaseDTO
        """
        return self.obter_configuracoes()

    def alterar_configuracoes(self, dados: JsonObject) -> JsonObject:
        """Altera as configurações de NFS-e.

        Endpoint: PUT /nfse/configuracoes

        Altera as configurações de NFS-e da empresa.

        Args:
            dados: Dados de configuração. Request body schema: ConfiguracaoNotaServicoDadosBaseDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse
        """
        return self._put("/nfse/configuracoes", json=to_json_object(dados))

    def update_settings(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar_configuracoes()``.

        Altera as configurações de NFS-e.

        Endpoint: PUT /nfse/configuracoes

        Altera as configurações de NFS-e da empresa.

        Args:
            data: Dados de configuração. Request body schema: ConfiguracaoNotaServicoDadosBaseDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse
        """
        return self.alterar_configuracoes(data)


def _nfse_list_params(
    *,
    pagina: int | None,
    limite: int | None,
    situacao: int | None,
    data_emissao_inicial: str | None,
    data_emissao_final: str | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "situacao": situacao,
            "dataEmissaoInicial": data_emissao_inicial,
            "dataEmissaoFinal": data_emissao_final,
        }
    )
