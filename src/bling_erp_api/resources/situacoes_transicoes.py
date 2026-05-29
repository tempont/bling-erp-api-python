"""Situacoes Transicoes (Situation Transitions) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class SituacoesTransicoesResource(BaseResource):
    """Situacoes Transicoes API resource. Maps to /situacoes/transicoes endpoints.

    Provides CRUD operations for situation transitions (transicoes de situacoes)
    in the Bling API. Canonical methods are in pt-BR following the official
    Bling documentation; English aliases are available for compatibility.
    """

    BASE_PATH = "/situacoes/transicoes"

    # ------------------------------------------------------------------
    # criar / create
    # ------------------------------------------------------------------

    def criar(self, dados: Any) -> JsonObject:
        """Cria uma nova transição de situação.

        Endpoint: POST /situacoes/transicoes

        Cria uma nova transição de situação no sistema.

        Args:
            dados: Dados da transição. Use ``SituacoesTransicoesPostRequest`` para uso
                tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 201: SituacoesTransicoesPostResponse201;
            400: ErrorResponse
        """
        return self._post(self.BASE_PATH, json=to_json_object(dados))

    def create(self, data: Any) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria uma nova transição de situação.

        Endpoint: POST /situacoes/transicoes

        Args:
            data: Dados da transição. Use ``SituacoesTransicoesPostRequest`` para uso
                tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 201: SituacoesTransicoesPostResponse201;
            400: ErrorResponse
        """
        return self.criar(dados=data)

    # ------------------------------------------------------------------
    # obter / get
    # ------------------------------------------------------------------

    def obter(self, id_transicao: int) -> JsonObject:
        """Obtém uma transição pelo ID.

        Endpoint: GET /situacoes/transicoes/{idTransicao}

        Obtém uma transição de situação pelo ID.

        Args:
            id_transicao: ID da transição (Bling: ``idTransicao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SituacoesTransicoesIdTransicaoGetResponse200;
            404: ErrorResponse
        """
        return self._get(f"{self.BASE_PATH}/{id_transicao}")

    def get(self, transition_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém uma transição pelo ID.

        Endpoint: GET /situacoes/transicoes/{idTransicao}

        Args:
            transition_id: ID da transição (Bling: ``idTransicao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SituacoesTransicoesIdTransicaoGetResponse200;
            404: ErrorResponse
        """
        return self.obter(id_transicao=transition_id)

    # ------------------------------------------------------------------
    # alterar / update
    # ------------------------------------------------------------------

    def alterar(self, id_transicao: int, dados: Any) -> JsonObject:
        """Altera uma transição.

        Endpoint: PUT /situacoes/transicoes/{idTransicao}

        Altera uma transição de situação pelo ID.

        Args:
            id_transicao: ID da transição (Bling: ``idTransicao``, integer, obrigatório)
            dados: Dados atualizados da transição. Use
                ``SituacoesTransicoesIdTransicaoPutRequest`` para uso tipado ou um objeto
                JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 200: SituacoesTransicoesIdTransicaoPutResponse200;
            400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"{self.BASE_PATH}/{id_transicao}", json=to_json_object(dados))

    def update(self, transition_id: int, data: Any) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera uma transição.

        Endpoint: PUT /situacoes/transicoes/{idTransicao}

        Args:
            transition_id: ID da transição (Bling: ``idTransicao``, integer, obrigatório)
            data: Dados atualizados da transição. Use
                ``SituacoesTransicoesIdTransicaoPutRequest`` para uso tipado ou um objeto
                JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 200: SituacoesTransicoesIdTransicaoPutResponse200;
            400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_transicao=transition_id, dados=data)

    # ------------------------------------------------------------------
    # remover / delete
    # ------------------------------------------------------------------

    def remover(self, id_transicao: int) -> JsonObject:
        """Remove uma transição.

        Endpoint: DELETE /situacoes/transicoes/{idTransicao}

        Remove uma transição de situação pelo ID.

        Args:
            id_transicao: ID da transição (Bling: ``idTransicao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse;
            404: ErrorResponse
        """
        return self._delete(f"{self.BASE_PATH}/{id_transicao}")

    def delete(self, transition_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove uma transição.

        Endpoint: DELETE /situacoes/transicoes/{idTransicao}

        Args:
            transition_id: ID da transição (Bling: ``idTransicao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse;
            404: ErrorResponse
        """
        return self.remover(id_transicao=transition_id)
