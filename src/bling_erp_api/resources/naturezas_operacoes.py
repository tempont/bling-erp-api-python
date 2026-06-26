"""Resource para Naturezas de Operações.

Mapeia os endpoints da API Bling:
- GET /naturezas-operacoes — listar naturezas (ObterMultiplos)
- POST /naturezas-operacoes/{idNaturezaOperacao}/obter-tributacao — obter tributação (ObterTributacao)

Canonical methods are in pt-BR. English aliases available for compatibility.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from bling_erp_api.models.generated.naturezas_operacoes import (
    NaturezasOperacoesGetResponse200,
    NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class NaturezasOperacoesResource(BaseResource):
    """Naturezas de Operações.

    Endpoints mapeados:
    - GET /naturezas-operacoes
    - POST /naturezas-operacoes/{idNaturezaOperacao}/obter-tributacao

    Métodos canônicos em pt-BR; aliases em inglês disponíveis para compatibilidade.
    """

    def listar(
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        situacao: int | None = None,
        descricao: str | None = None,
    ) -> NaturezasOperacoesGetResponse200:
        """Lista naturezas de operação.

        Endpoint: GET /naturezas-operacoes

        Lista naturezas de operação com paginação e filtros opcionais.

        Args:
            pagina: Nº da página (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros por página (Bling: ``limite``, integer, opcional)
            situacao: Situação da natureza (0=Inativo, 1=Ativo) (Bling: ``situacao``, integer, opcional)
            descricao: Descrição da natureza (Bling: ``descricao``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NaturezasOperacoesDadosDTO[]; 400: ErrorResponse
        """
        params = compact_params(
            {"pagina": pagina, "limite": limite, "situacao": situacao, "descricao": descricao}
        )
        raw = self._get("/naturezas-operacoes", params=params)
        return self._validate_response(NaturezasOperacoesGetResponse200, raw)

    def obter_tributacao(
        self,
        id_natureza_operacao: int,
        calculo: JsonObject,
    ) -> NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200:
        """Obtém regras de tributação para uma natureza de operação.

        Endpoint: POST /naturezas-operacoes/{idNaturezaOperacao}/obter-tributacao

        Obtém as regras de tributação que incidem sobre o item,
        dada uma natureza de operação.

        Args:
            id_natureza_operacao: ID da natureza de operação (Bling: ``idNaturezaOperacao``, integer, obrigatório)
            calculo: Dados para cálculo da tributação (Bling: ``CalculosImpostosCalculoDTO``, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: CalculosImpostosDadosDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        raw = self._post(
            f"/naturezas-operacoes/{id_natureza_operacao}/obter-tributacao",
            json=to_json_object(calculo),
        )
        return self._validate_response(
            NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200, raw
        )

    # --- English aliases ---

    def list(self, **kwargs: Any) -> NaturezasOperacoesGetResponse200:
        """Compatibility alias for ``listar()``.

        Lista naturezas de operação.

        Endpoint: GET /naturezas-operacoes

        Aceita os mesmos argumentos de ``listar()``.

        Returns:
            Bling API response. Response schemas: 200: NaturezasOperacoesDadosDTO[]; 400: ErrorResponse
        """
        return self.listar(**kwargs)

    def get_taxation(
        self,
        nature_of_operation_id: int,
        calculation: JsonObject,
    ) -> NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200:
        """Compatibility alias for ``obter_tributacao()``.

        Obtém regras de tributação para uma natureza de operação.

        Endpoint: POST /naturezas-operacoes/{idNaturezaOperacao}/obter-tributacao

        Args:
            nature_of_operation_id: ID da natureza de operação (Bling: ``idNaturezaOperacao``, integer, obrigatório)
            calculation: Dados para cálculo da tributação (Bling: ``CalculosImpostosCalculoDTO``, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: CalculosImpostosDadosDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.obter_tributacao(
            id_natureza_operacao=nature_of_operation_id, calculo=calculation
        )
