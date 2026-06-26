"""Resource para Ordens de Produção.

Mapeia os endpoints da API Bling:
- GET /ordens-producao — listar ordens (ObterAcaoMultiplos)
- POST /ordens-producao — criar ordem (Criar)
- GET /ordens-producao/{idOrdemProducao} — obter ordem (Obter)
- PUT /ordens-producao/{idOrdemProducao} — alterar ordem (Alterar)
- DELETE /ordens-producao/{idOrdemProducao} — remover ordem (Remover)
- PUT /ordens-producao/{idOrdemProducao}/situacoes — alterar situação (AlterarSituacao)
- POST /ordens-producao/gerar-sob-demanda — gerar sob demanda (CriarMultiplos)

Canonical methods are in pt-BR. English aliases available for compatibility.
"""

from __future__ import annotations

from bling_erp_api.models.generated.ordens_producao import (
    OrdensProducaoGerarSobDemandaPostResponse201,
    OrdensProducaoGetResponse200,
    OrdensProducaoIdOrdemProducaoGetResponse200,
    OrdensProducaoPostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.types import JsonObject
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object


class OrdensProducaoResource(BaseResource):
    """Ordens de Produção.

    Endpoints mapeados:
    - GET /ordens-producao
    - POST /ordens-producao
    - GET /ordens-producao/{idOrdemProducao}
    - PUT /ordens-producao/{idOrdemProducao}
    - DELETE /ordens-producao/{idOrdemProducao}
    - PUT /ordens-producao/{idOrdemProducao}/situacoes
    - POST /ordens-producao/gerar-sob-demanda

    Métodos canônicos em pt-BR; aliases em inglês disponíveis para compatibilidade.
    """

    def listar(
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        ids_situacoes: list[int] | None = None,
    ) -> OrdensProducaoGetResponse200:
        """Lista ordens de produção.

        Endpoint: GET /ordens-producao

        Lista ordens de produção com paginação e filtro de situações.

        Args:
            pagina: Nº da página (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros por página (Bling: ``limite``, integer, opcional)
            ids_situacoes: IDs das situações para filtrar (Bling: ``idsSituacoes[]``, array de integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: OrdensProducaoDadosBaseDTO[]; 400: ErrorResponse
        """
        params = compact_params(
            {
                "pagina": pagina,
                "limite": limite,
                "idsSituacoes[]": ids_situacoes,
            }
        )
        raw = self._get("/ordens-producao", params=params)
        return self._validate_response(OrdensProducaoGetResponse200, raw)

    def criar(self, dados: JsonObject) -> OrdensProducaoPostResponse201:
        """Cria uma ordem de produção.

        Endpoint: POST /ordens-producao

        Cria uma nova ordem de produção.

        Args:
            dados: Dados da ordem de produção (Bling: ``OrdensProducaoCreateRequestDTO``, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        raw = self._post("/ordens-producao", json=to_json_object(dados))
        return self._validate_response(OrdensProducaoPostResponse201, raw)

    def obter(self, id_ordem_producao: int) -> OrdensProducaoIdOrdemProducaoGetResponse200:
        """Obtém uma ordem de produção.

        Endpoint: GET /ordens-producao/{idOrdemProducao}

        Obtém uma ordem de produção pelo ID.

        Args:
            id_ordem_producao: ID da ordem de produção (Bling: ``idOrdemProducao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: OrdensProducaoDetailResponseDTO; 404: ErrorResponse
        """
        raw = self._get(f"/ordens-producao/{id_ordem_producao}")
        return self._validate_response(OrdensProducaoIdOrdemProducaoGetResponse200, raw)

    def alterar(self, id_ordem_producao: int, dados: JsonObject) -> JsonObject:
        """Altera uma ordem de produção.

        Endpoint: PUT /ordens-producao/{idOrdemProducao}

        Altera integralmente uma ordem de produção.

        Args:
            id_ordem_producao: ID da ordem de produção (Bling: ``idOrdemProducao``, integer, obrigatório)
            dados: Dados da ordem de produção (Bling: ``OrdensProducaoCreateRequestDTO``, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(
            f"/ordens-producao/{id_ordem_producao}",
            json=to_json_object(dados),
        )

    def remover(self, id_ordem_producao: int) -> JsonObject:
        """Remove uma ordem de produção.

        Endpoint: DELETE /ordens-producao/{idOrdemProducao}

        Remove uma ordem de produção pelo ID.

        Args:
            id_ordem_producao: ID da ordem de produção (Bling: ``idOrdemProducao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 404: ErrorResponse
        """
        return self._delete(f"/ordens-producao/{id_ordem_producao}")

    def alterar_situacao(
        self,
        id_ordem_producao: int,
        dados: JsonObject,
    ) -> JsonObject:
        """Altera a situação de uma ordem de produção.

        Endpoint: PUT /ordens-producao/{idOrdemProducao}/situacoes

        Altera a situação de uma ordem de produção (ex: finalizar, cancelar).

        Args:
            id_ordem_producao: ID da ordem de produção (Bling: ``idOrdemProducao``, integer, obrigatório)
            dados: Dados da situação (Bling: ``OrdensProducaoSituacaoDadosDTO``, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(
            f"/ordens-producao/{id_ordem_producao}/situacoes",
            json=to_json_object(dados),
        )

    def criar_multiplos(self) -> OrdensProducaoGerarSobDemandaPostResponse201:
        """Gera ordens de produção sob demanda.

        Endpoint: POST /ordens-producao/gerar-sob-demanda

        Gera ordens de produção automaticamente com base no estoque mínimo.

        Returns:
            Bling API response. Response schemas: 201: OrdensProducaoDadosGeradosPorDemandaDTO[]; 400: ErrorResponse
        """
        raw = self._post("/ordens-producao/gerar-sob-demanda")
        return self._validate_response(OrdensProducaoGerarSobDemandaPostResponse201, raw)

    # --- English aliases ---

    def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        status_ids: list[int] | None = None,
    ) -> OrdensProducaoGetResponse200:
        """Compatibility alias for ``listar()``.

        Lista ordens de produção.

        Endpoint: GET /ordens-producao

        Args:
            page: Nº da página (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros por página (Bling: ``limite``, integer, opcional)
            status_ids: IDs das situações para filtrar (Bling: ``idsSituacoes[]``, array de integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: OrdensProducaoDadosBaseDTO[]; 400: ErrorResponse
        """
        return self.listar(pagina=page, limite=limit, ids_situacoes=status_ids)

    def create(self, data: JsonObject) -> OrdensProducaoPostResponse201:
        """Compatibility alias for ``criar()``.

        Cria uma ordem de produção.

        Endpoint: POST /ordens-producao

        Args:
            data: Dados da ordem de produção (Bling: ``OrdensProducaoCreateRequestDTO``, obrigatório)

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def get(self, production_order_id: int) -> OrdensProducaoIdOrdemProducaoGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém uma ordem de produção.

        Endpoint: GET /ordens-producao/{idOrdemProducao}

        Args:
            production_order_id: ID da ordem de produção (Bling: ``idOrdemProducao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: OrdensProducaoDetailResponseDTO; 404: ErrorResponse
        """
        return self.obter(id_ordem_producao=production_order_id)

    def update(self, production_order_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera uma ordem de produção.

        Endpoint: PUT /ordens-producao/{idOrdemProducao}

        Args:
            production_order_id: ID da ordem de produção (Bling: ``idOrdemProducao``, integer, obrigatório)
            data: Dados da ordem de produção (Bling: ``OrdensProducaoCreateRequestDTO``, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_ordem_producao=production_order_id, dados=data)

    def delete(self, production_order_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove uma ordem de produção.

        Endpoint: DELETE /ordens-producao/{idOrdemProducao}

        Args:
            production_order_id: ID da ordem de produção (Bling: ``idOrdemProducao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 404: ErrorResponse
        """
        return self.remover(id_ordem_producao=production_order_id)

    def set_status(self, production_order_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar_situacao()``.

        Altera a situação de uma ordem de produção.

        Endpoint: PUT /ordens-producao/{idOrdemProducao}/situacoes

        Args:
            production_order_id: ID da ordem de produção (Bling: ``idOrdemProducao``, integer, obrigatório)
            data: Dados da situação (Bling: ``OrdensProducaoSituacaoDadosDTO``, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar_situacao(id_ordem_producao=production_order_id, dados=data)

    def generate_on_demand(self) -> OrdensProducaoGerarSobDemandaPostResponse201:
        """Compatibility alias for ``criar_multiplos()``.

        Gera ordens de produção sob demanda.

        Endpoint: POST /ordens-producao/gerar-sob-demanda

        Returns:
            Bling API response. Response schemas: 201: OrdensProducaoDadosGeradosPorDemandaDTO[]; 400: ErrorResponse
        """
        return self.criar_multiplos()
