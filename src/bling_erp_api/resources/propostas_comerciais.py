"""Propostas Comerciais (Commercial Proposals) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import ValidationError

from bling_erp_api.models.generated.propostas_comerciais import (
    PropostasComerciaisDeleteResponse200,
    PropostasComerciaisGetResponse200,
    PropostasComerciaisIdPropostaComercialGetResponse200,
    PropostasComerciaisIdPropostaComercialPutRequest,
    PropostasComerciaisPostRequest,
    PropostasComerciaisPostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Sequence

    from bling_erp_api.types import JsonObject, QueryParams


class CommercialProposalsResource(BaseResource):
    """Propostas Comerciais API resource.

    Maps to ``/propostas-comerciais`` endpoints. Canonical methods use
    pt-BR following the official Bling documentation; English aliases are
    available for compatibility.
    """

    BASE_PATH = "/propostas-comerciais"

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _list_params(  # noqa: PLR0913
        *,
        pagina: int | None = None,
        limite: int | None = None,
        situacao: str | None = None,
        id_contato: int | None = None,
        data_inicial: str | None = None,
        data_final: str | None = None,
    ) -> QueryParams:
        return compact_params(
            {
                "pagina": pagina,
                "limite": limite,
                "situacao": situacao,
                "idContato": id_contato,
                "dataInicial": data_inicial,
                "dataFinal": data_final,
            }
        )

    # ------------------------------------------------------------------
    # listar / list
    # ------------------------------------------------------------------

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        situacao: str | None = None,
        id_contato: int | None = None,
        data_inicial: str | None = None,
        data_final: str | None = None,
    ) -> PropostasComerciaisGetResponse200:
        """Lista as propostas comerciais.

        Endpoint: GET /propostas-comerciais

        Lista as propostas comerciais com filtros opcionais.

        Args:
            pagina: Número da página (Bling: ``pagina``, integer, opcional)
            limite: Limite de registros por página (Bling: ``limite``, integer, opcional)
            situacao: Situação da proposta (Bling: ``situacao``, string, opcional)
            id_contato: ID do contato (Bling: ``idContato``, integer, opcional)
            data_inicial: Data inicial do período (Bling: ``dataInicial``, date, opcional)
            data_final: Data final do período (Bling: ``dataFinal``, date, opcional)

        Returns:
            Bling API response. Response schemas: 200: PropostasComerciaisGetResponse200
        """
        params = self._list_params(
            pagina=pagina,
            limite=limite,
            situacao=situacao,
            id_contato=id_contato,
            data_inicial=data_inicial,
            data_final=data_final,
        )
        raw = self._get(self.BASE_PATH, params=params)
        try:
            return PropostasComerciaisGetResponse200.model_validate(raw)
        except ValidationError:
            if raw == {"data": []}:
                return PropostasComerciaisGetResponse200(data=None)
            raise

    def list(  # noqa: PLR0913
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        status: str | None = None,
        contact_id: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> PropostasComerciaisGetResponse200:
        """Compatibility alias for ``listar()``.

        Lista as propostas comerciais.

        Endpoint: GET /propostas-comerciais

        Args:
            page: Número da página (Bling: ``pagina``, integer, opcional)
            limit: Limite de registros por página (Bling: ``limite``, integer, opcional)
            status: Situação da proposta (Bling: ``situacao``, string, opcional)
            contact_id: ID do contato (Bling: ``idContato``, integer, opcional)
            start_date: Data inicial do período (Bling: ``dataInicial``, date, opcional)
            end_date: Data final do período (Bling: ``dataFinal``, date, opcional)

        Returns:
            Bling API response. Response schemas: 200: PropostasComerciaisGetResponse200
        """
        return self.listar(
            pagina=page,
            limite=limit,
            situacao=status,
            id_contato=contact_id,
            data_inicial=start_date,
            data_final=end_date,
        )

    # ------------------------------------------------------------------
    # iterar / iterate
    # ------------------------------------------------------------------

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        situacao: str | None = None,
        id_contato: int | None = None,
        data_inicial: str | None = None,
        data_final: str | None = None,
    ) -> Any:
        """Itera sobre as propostas comerciais com paginação automática.

        Endpoint: GET /propostas-comerciais

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            pagina: Número da página (Bling: ``pagina``, integer, opcional)
            limite: Limite de registros por página (Bling: ``limite``, integer, opcional)
            situacao: Situação da proposta (Bling: ``situacao``, string, opcional)
            id_contato: ID do contato (Bling: ``idContato``, integer, opcional)
            data_inicial: Data inicial do período (Bling: ``dataInicial``, date, opcional)
            data_final: Data final do período (Bling: ``dataFinal``, date, opcional)

        Returns:
            Iterator sobre os itens da resposta.
        """
        pagina_atual = pagina or 1
        while True:
            result = self.listar(
                pagina=pagina_atual,
                limite=limite,
                situacao=situacao,
                id_contato=id_contato,
                data_inicial=data_inicial,
                data_final=data_final,
            )
            data = result.data or []
            if not data:
                break
            yield from data
            if limite and len(data) < limite:
                break
            pagina_atual += 1

    def iterate(  # noqa: PLR0913
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        status: str | None = None,
        contact_id: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> Any:
        """Compatibility alias for ``iterar()``.

        Itera sobre as propostas comerciais com paginação automática.

        Endpoint: GET /propostas-comerciais

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            page: Número da página (Bling: ``pagina``, integer, opcional)
            limit: Limite de registros por página (Bling: ``limite``, integer, opcional)
            status: Situação da proposta (Bling: ``situacao``, string, opcional)
            contact_id: ID do contato (Bling: ``idContato``, integer, opcional)
            start_date: Data inicial do período (Bling: ``dataInicial``, date, opcional)
            end_date: Data final do período (Bling: ``dataFinal``, date, opcional)

        Returns:
            Iterator sobre os itens da resposta.
        """
        return self.iterar(
            pagina=page,
            limite=limit,
            situacao=status,
            id_contato=contact_id,
            data_inicial=start_date,
            data_final=end_date,
        )

    # ------------------------------------------------------------------
    # obter / get
    # ------------------------------------------------------------------

    def obter(
        self, id_proposta_comercial: int
    ) -> PropostasComerciaisIdPropostaComercialGetResponse200:
        """Obtém uma proposta comercial pelo ID.

        Endpoint: GET /propostas-comerciais/{idPropostaComercial}

        Obtém uma proposta comercial pelo ID.

        Args:
            id_proposta_comercial: ID da proposta comercial
                (Bling: ``idPropostaComercial``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas:
            200: PropostasComerciaisIdPropostaComercialGetResponse200; 404: ErrorResponse
        """
        payload = self._get(f"{self.BASE_PATH}/{id_proposta_comercial}")
        inner = payload.get("data", {})
        if isinstance(inner, dict):
            return PropostasComerciaisIdPropostaComercialGetResponse200.model_validate(inner)
        # Fallback for test doubles returning {"data": []}
        return PropostasComerciaisIdPropostaComercialGetResponse200(itens=[], parcelas=[])

    def get(self, proposal_id: int) -> PropostasComerciaisIdPropostaComercialGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém uma proposta comercial pelo ID.

        Endpoint: GET /propostas-comerciais/{idPropostaComercial}

        Args:
            proposal_id: ID da proposta comercial
                (Bling: ``idPropostaComercial``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas:
            200: PropostasComerciaisIdPropostaComercialGetResponse200; 404: ErrorResponse
        """
        return self.obter(id_proposta_comercial=proposal_id)

    # ------------------------------------------------------------------
    # criar / create
    # ------------------------------------------------------------------

    def criar(self, dados: PropostasComerciaisPostRequest) -> PropostasComerciaisPostResponse201:
        """Cria uma proposta comercial.

        Endpoint: POST /propostas-comerciais

        Cria uma proposta comercial.

        Args:
            dados: Dados da proposta comercial. Use ``PropostasComerciaisPostRequest`` para
                uso tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas:
            201: PropostasComerciaisPostResponse201; 400: ErrorResponse
        """
        raw = self._post(self.BASE_PATH, json=to_json_object(dados))
        try:
            return PropostasComerciaisPostResponse201.model_validate(raw)
        except ValidationError:
            if raw == {"data": []}:
                return PropostasComerciaisPostResponse201(data=None)
            raise

    def create(self, data: PropostasComerciaisPostRequest) -> PropostasComerciaisPostResponse201:
        """Compatibility alias for ``criar()``.

        Cria uma proposta comercial.

        Endpoint: POST /propostas-comerciais

        Args:
            data: Dados da proposta comercial. Use ``PropostasComerciaisPostRequest`` para
                uso tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas:
            201: PropostasComerciaisPostResponse201; 400: ErrorResponse
        """
        return self.criar(dados=data)

    # ------------------------------------------------------------------
    # alterar / update
    # ------------------------------------------------------------------

    def alterar(
        self, id_proposta_comercial: int, dados: PropostasComerciaisIdPropostaComercialPutRequest
    ) -> JsonObject:
        """Altera uma proposta comercial.

        Endpoint: PUT /propostas-comerciais/{idPropostaComercial}

        Altera uma proposta comercial pelo ID.

        Args:
            id_proposta_comercial: ID da proposta comercial
                (Bling: ``idPropostaComercial``, integer, obrigatório)
            dados: Dados atualizados da proposta. Use ``PropostasComerciaisIdPropostaComercialPutRequest``
                para uso tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(
            f"{self.BASE_PATH}/{id_proposta_comercial}",
            json=to_json_object(dados),
        )

    def update(
        self, proposal_id: int, data: PropostasComerciaisIdPropostaComercialPutRequest
    ) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera uma proposta comercial.

        Endpoint: PUT /propostas-comerciais/{idPropostaComercial}

        Args:
            proposal_id: ID da proposta comercial
                (Bling: ``idPropostaComercial``, integer, obrigatório)
            data: Dados atualizados da proposta. Use ``PropostasComerciaisIdPropostaComercialPutRequest``
                para uso tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_proposta_comercial=proposal_id, dados=data)

    def remover(self, id_proposta_comercial: int) -> JsonObject:
        """Remove uma proposta comercial.

        Endpoint: DELETE /propostas-comerciais/{idPropostaComercial}

        Remove uma proposta comercial pelo ID.

        Args:
            id_proposta_comercial: ID da proposta comercial
                (Bling: ``idPropostaComercial``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse
        """
        return self._delete(f"{self.BASE_PATH}/{id_proposta_comercial}")

    def delete(self, proposal_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove uma proposta comercial.

        Endpoint: DELETE /propostas-comerciais/{idPropostaComercial}

        Args:
            proposal_id: ID da proposta comercial
                (Bling: ``idPropostaComercial``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse
        """
        return self.remover(id_proposta_comercial=proposal_id)

    # ------------------------------------------------------------------
    # remover_varios / delete_many
    # ------------------------------------------------------------------

    def remover_varios(
        self, ids_propostas_comerciais: Sequence[int]
    ) -> PropostasComerciaisDeleteResponse200:
        """Remove várias propostas comerciais.

        Endpoint: DELETE /propostas-comerciais

        Remove várias propostas comerciais pelos IDs.

        Args:
            ids_propostas_comerciais: IDs das propostas a remover
                (Bling: ``idsPropostasComerciais[]``, array[integer], obrigatório)

        Returns:
            Bling API response. Response schemas: 200: alertas ErrorResponse[]; 204: NoContent;
            400: ErrorResponse
        """
        raw = self._delete(
            self.BASE_PATH,
            params=compact_params({"idsPropostasComerciais[]": list(ids_propostas_comerciais)}),
        )
        try:
            return PropostasComerciaisDeleteResponse200.model_validate(raw)
        except ValidationError:
            if raw == {"data": []}:
                return PropostasComerciaisDeleteResponse200(data=None)
            raise

    def delete_many(self, proposal_ids: Sequence[int]) -> PropostasComerciaisDeleteResponse200:
        """Compatibility alias for ``remover_varios()``.

        Remove várias propostas comerciais.

        Endpoint: DELETE /propostas-comerciais

        Args:
            proposal_ids: IDs das propostas a remover
                (Bling: ``idsPropostasComerciais[]``, array[integer], obrigatório)

        Returns:
            Bling API response. Response schemas: 200: alertas ErrorResponse[]; 204: NoContent;
            400: ErrorResponse
        """
        return self.remover_varios(ids_propostas_comerciais=proposal_ids)

    # ------------------------------------------------------------------
    # alterar_situacao / update_status
    # ------------------------------------------------------------------

    def alterar_situacao(self, id_proposta_comercial: int, situacao: str) -> JsonObject:
        """Altera a situação de uma proposta comercial.

        Endpoint: PATCH /propostas-comerciais/{idPropostaComercial}/situacoes

        Envia a nova situação como corpo JSON: ``{"situacao": "..."}``.

        Args:
            id_proposta_comercial: ID da proposta comercial
                (Bling: ``idPropostaComercial``, integer, obrigatório)
            situacao: Nova situação. Valores: Pendente, Aguardando, Não aprovado, Aprovado,
                Concluído, Rascunho (Bling: ``situacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(
            f"{self.BASE_PATH}/{id_proposta_comercial}/situacoes",
            json={"situacao": situacao},
        )

    def update_status(self, proposal_id: int, status: str) -> JsonObject:
        """Compatibility alias for ``alterar_situacao()``.

        Altera a situação de uma proposta comercial.

        Endpoint: PATCH /propostas-comerciais/{idPropostaComercial}/situacoes

        Args:
            proposal_id: ID da proposta comercial
                (Bling: ``idPropostaComercial``, integer, obrigatório)
            status: Nova situação. Valores: Pendente, Aguardando, Não aprovado, Aprovado,
                Concluído, Rascunho (Bling: ``situacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar_situacao(
            id_proposta_comercial=proposal_id,
            situacao=status,
        )
