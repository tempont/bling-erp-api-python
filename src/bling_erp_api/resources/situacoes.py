"""Situacoes (Situations) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import ValidationError

from bling_erp_api.models.generated.situacoes import (
    SituacoesIdSituacaoGetResponse200,
    SituacoesIdSituacaoPutRequest,
    SituacoesIdSituacaoPutResponse200,
    SituacoesPostRequest,
    SituacoesPostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class SituacoesResource(BaseResource):
    """Situacoes API resource. Maps to /situacoes endpoints.

    Provides CRUD operations for situations (situacoes) in the Bling API.
    Canonical methods are in pt-BR following the official Bling documentation;
    English aliases are available for compatibility.
    """

    BASE_PATH = "/situacoes"

    # ------------------------------------------------------------------
    # criar / create
    # ------------------------------------------------------------------

    def criar(self, dados: SituacoesPostRequest) -> SituacoesPostResponse201:
        """Cria uma nova situação.

        Endpoint: POST /situacoes

        Cria uma nova situação no sistema.

        Args:
            dados: Dados da situação. Use ``SituacoesPostRequest`` para uso tipado
                ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 201: SituacoesPostResponse201;
            400: ErrorResponse
        """
        raw = self._post(self.BASE_PATH, json=to_json_object(dados))
        return SituacoesPostResponse201.model_validate(raw)

    def create(self, data: SituacoesPostRequest) -> SituacoesPostResponse201:
        """Compatibility alias for ``criar()``.

        Cria uma nova situação.

        Endpoint: POST /situacoes

        Args:
            data: Dados da situação. Use ``SituacoesPostRequest`` para uso tipado
                ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 201: SituacoesPostResponse201;
            400: ErrorResponse
        """
        return self.criar(dados=data)

    # ------------------------------------------------------------------
    # obter / get
    # ------------------------------------------------------------------

    def obter(self, id_situacao: int) -> SituacoesIdSituacaoGetResponse200:
        """Obtém uma situação pelo ID.

        Endpoint: GET /situacoes/{idSituacao}

        Obtém uma situação pelo ID.

        Args:
            id_situacao: ID da situação (Bling: ``idSituacao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SituacoesIdSituacaoGetResponse200;
            404: ErrorResponse
        """
        raw = self._get(f"{self.BASE_PATH}/{id_situacao}")
        try:
            return SituacoesIdSituacaoGetResponse200.model_validate(raw)
        except ValidationError:
            if raw == {"data": []}:
                return SituacoesIdSituacaoGetResponse200(data=None)
            raise

    def get(self, situation_id: int) -> SituacoesIdSituacaoGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém uma situação pelo ID.

        Endpoint: GET /situacoes/{idSituacao}

        Args:
            situation_id: ID da situação (Bling: ``idSituacao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SituacoesIdSituacaoGetResponse200;
            404: ErrorResponse
        """
        return self.obter(id_situacao=situation_id)

    # ------------------------------------------------------------------
    # alterar / update
    # ------------------------------------------------------------------

    def alterar(
        self, id_situacao: int, dados: SituacoesIdSituacaoPutRequest
    ) -> SituacoesIdSituacaoPutResponse200:
        """Altera uma situação.

        Endpoint: PUT /situacoes/{idSituacao}

        Altera uma situação pelo ID.

        Args:
            id_situacao: ID da situação (Bling: ``idSituacao``, integer, obrigatório)
            dados: Dados atualizados da situação. Use ``SituacoesIdSituacaoPutRequest``
                para uso tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 200: SituacoesIdSituacaoPutResponse200;
            400: ErrorResponse; 404: ErrorResponse
        """
        raw = self._put(f"{self.BASE_PATH}/{id_situacao}", json=to_json_object(dados))
        return SituacoesIdSituacaoPutResponse200.model_validate(raw)

    def update(
        self, situation_id: int, data: SituacoesIdSituacaoPutRequest
    ) -> SituacoesIdSituacaoPutResponse200:
        """Compatibility alias for ``alterar()``.

        Altera uma situação.

        Endpoint: PUT /situacoes/{idSituacao}

        Args:
            situation_id: ID da situação (Bling: ``idSituacao``, integer, obrigatório)
            data: Dados atualizados da situação. Use ``SituacoesIdSituacaoPutRequest``
                para uso tipado ou um objeto JSON com os nomes de campos do Bling.

        Returns:
            Bling API response. Response schemas: 200: SituacoesIdSituacaoPutResponse200;
            400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_situacao=situation_id, dados=data)

    # ------------------------------------------------------------------
    # remover / delete
    # ------------------------------------------------------------------

    def remover(self, id_situacao: int) -> JsonObject:
        """Remove uma situação.

        Endpoint: DELETE /situacoes/{idSituacao}

        Remove uma situação pelo ID.

        Args:
            id_situacao: ID da situação (Bling: ``idSituacao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse;
            404: ErrorResponse
        """
        return self._delete(f"{self.BASE_PATH}/{id_situacao}")

    def delete(self, situation_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove uma situação.

        Endpoint: DELETE /situacoes/{idSituacao}

        Args:
            situation_id: ID da situação (Bling: ``idSituacao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse;
            404: ErrorResponse
        """
        return self.remover(id_situacao=situation_id)
