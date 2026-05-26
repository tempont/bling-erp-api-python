"""Invoices resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams, QueryParamValue


class InvoicesResource(BaseResource):
    """Operations for Bling invoices."""

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> JsonObject:
        """Obtém notas fiscais.

        Endpoint: GET /notas/fiscais

        Obtém notas fiscais paginadas.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            id_transportador: ID do contato do transportador (Bling: ``idTransportador``, integer, opcional)
            chave_acesso: Chave de acesso (Bling: ``chaveAcesso``, integer, opcional)
            numero: Número da nota fiscal (Bling: ``numero``, integer, opcional)
            serie: Série (Bling: ``serie``, integer, opcional)
            situacao: `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10` Consulta situação<br>`11` Bloqueada (Bling: ``situacao``, integer, opcional)
            data_emissao_inicial: Data e hora inicial de emissão (Bling: ``dataEmissaoInicial``, string, opcional)
            data_emissao_final: Data e hora final de emissão (Bling: ``dataEmissaoFinal``, string, opcional)
            **filters: Filtros adicionais para a listagem.

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosBaseDTO; 404: ErrorResponse
        """
        return self._get("/notas/fiscais", params={"pagina": page, "limite": limit, **filters})

    def iterate(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> Iterator[JsonObject]:
        """Itera pelos registros página a página, mantendo os mesmos filtros.

        Obtém notas fiscais.

        Endpoint: GET /notas/fiscais

        Obtém notas fiscais paginadas.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            id_transportador: ID do contato do transportador (Bling: ``idTransportador``, integer, opcional)
            chave_acesso: Chave de acesso (Bling: ``chaveAcesso``, integer, opcional)
            numero: Número da nota fiscal (Bling: ``numero``, integer, opcional)
            serie: Série (Bling: ``serie``, integer, opcional)
            situacao: `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10` Consulta situação<br>`11` Bloqueada (Bling: ``situacao``, integer, opcional)
            data_emissao_inicial: Data e hora inicial de emissão (Bling: ``dataEmissaoInicial``, string, opcional)
            data_emissao_final: Data e hora final de emissão (Bling: ``dataEmissaoFinal``, string, opcional)
            **filters: Filtros adicionais para a listagem.

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosBaseDTO; 404: ErrorResponse
        """
        params: QueryParams = filters
        return self._iterate("/notas/fiscais", page=page, limit=limit, params=params)

    def get(self, invoice_id: int) -> JsonObject:
        """Obtém uma nota fiscal.

        Endpoint: GET /notas/fiscais/{id}

        Obtém uma nota fiscal pelo ID.

        Args:
            invoice_id: ID da nota fiscal (Bling: ``id``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotasFiscaisDadosBaseDTO, NotasFiscaisDadosGetDTO; 404: ErrorResponse
        """
        return self._get(f"/notas/fiscais/{invoice_id}")
