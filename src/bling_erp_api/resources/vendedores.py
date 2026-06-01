"""Vendedores (Sellers) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import ValidationError

from bling_erp_api.models.aliases import (
    VendedoresGetResponse200,
    VendedoresIdVendedorGetResponse200,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params

if TYPE_CHECKING:
    from bling_erp_api.types import QueryParams


def _vendedores_list_params(  # noqa: PLR0913
    *,
    pagina: int | None = None,
    limite: int | None = None,
    nome_contato: str | None = None,
    situacao_contato: str | None = None,
    id_contato: int | None = None,
    id_loja: int | None = None,
    data_alteracao_inicial: str | None = None,
    data_alteracao_final: str | None = None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "nomeContato": nome_contato,
            "situacaoContato": situacao_contato,
            "idContato": id_contato,
            "idLoja": id_loja,
            "dataAlteracaoInicial": data_alteracao_inicial,
            "dataAlteracaoFinal": data_alteracao_final,
        }
    )


class VendedoresResource(BaseResource):
    """Vendedores API resource. Maps to /vendedores endpoints.

    Provides operations for sellers (vendedores) in the Bling API.
    Canonical methods are in pt-BR following the official Bling documentation;
    English aliases are available for compatibility.
    """

    BASE_PATH = "/vendedores"

    # ------------------------------------------------------------------
    # listar / list
    # ------------------------------------------------------------------

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        nome_contato: str | None = None,
        situacao_contato: str | None = None,
        id_contato: int | None = None,
        id_loja: int | None = None,
        data_alteracao_inicial: str | None = None,
        data_alteracao_final: str | None = None,
    ) -> VendedoresGetResponse200:
        """Lista os vendedores.

        Endpoint: GET /vendedores

        Obtém uma lista paginada de vendedores cadastrados. Aceita filtros
        opcionais para refinar a consulta.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros por página (Bling: ``limite``, integer, opcional)
            nome_contato: Nome do contato para filtro (Bling: ``nomeContato``, string, opcional)
            situacao_contato: Situação do contato para filtro (Bling: ``situacaoContato``, string, opcional, [`A` Ativo, `I` Inativo, `S` Sem movimento, `E` Excluído, `T` Todos])
            id_contato: ID do contato para filtro (Bling: ``idContato``, integer, opcional)
            id_loja: ID da loja para filtro (Bling: ``idLoja``, integer, opcional)
            data_alteracao_inicial: Data de alteração inicial (Bling: ``dataAlteracaoInicial``, string, opcional)
            data_alteracao_final: Data de alteração final (Bling: ``dataAlteracaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: VendedoresGetResponse200; 404: ErrorResponse
        """
        params = _vendedores_list_params(
            pagina=pagina,
            limite=limite,
            nome_contato=nome_contato,
            situacao_contato=situacao_contato,
            id_contato=id_contato,
            id_loja=id_loja,
            data_alteracao_inicial=data_alteracao_inicial,
            data_alteracao_final=data_alteracao_final,
        )
        raw = self._get(self.BASE_PATH, params=params)
        return VendedoresGetResponse200.model_validate(raw)

    def list(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        nome_contato: str | None = None,
        situacao_contato: str | None = None,
        id_contato: int | None = None,
        id_loja: int | None = None,
        data_alteracao_inicial: str | None = None,
        data_alteracao_final: str | None = None,
    ) -> VendedoresGetResponse200:
        """Compatibility alias for ``listar()``.

        Lista os vendedores.

        Endpoint: GET /vendedores

        Obtém uma lista paginada de vendedores cadastrados. Aceita filtros
        opcionais para refinar a consulta.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros por página (Bling: ``limite``, integer, opcional)
            nome_contato: Nome do contato para filtro (Bling: ``nomeContato``, string, opcional)
            situacao_contato: Situação do contato para filtro (Bling: ``situacaoContato``, string, opcional)
            id_contato: ID do contato para filtro (Bling: ``idContato``, integer, opcional)
            id_loja: ID da loja para filtro (Bling: ``idLoja``, integer, opcional)
            data_alteracao_inicial: Data de alteração inicial (Bling: ``dataAlteracaoInicial``, string, opcional)
            data_alteracao_final: Data de alteração final (Bling: ``dataAlteracaoFinal``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: VendedoresGetResponse200; 404: ErrorResponse
        """
        return self.listar(
            pagina=pagina,
            limite=limite,
            nome_contato=nome_contato,
            situacao_contato=situacao_contato,
            id_contato=id_contato,
            id_loja=id_loja,
            data_alteracao_inicial=data_alteracao_inicial,
            data_alteracao_final=data_alteracao_final,
        )

    # ------------------------------------------------------------------
    # obter / get
    # ------------------------------------------------------------------

    def obter(self, id_vendedor: int) -> VendedoresIdVendedorGetResponse200:
        """Obtém um vendedor pelo ID.

        Endpoint: GET /vendedores/{idVendedor}

        Obtém os dados de um vendedor específico pelo seu ID.

        Args:
            id_vendedor: ID do vendedor (Bling: ``idVendedor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: VendedoresIdVendedorGetResponse200;
            404: ErrorResponse
        """
        raw = self._get(f"{self.BASE_PATH}/{id_vendedor}")
        try:
            return VendedoresIdVendedorGetResponse200.model_validate(raw)
        except ValidationError:
            if raw == {"data": []}:
                return VendedoresIdVendedorGetResponse200(data=None)
            raise

    def get(self, seller_id: int) -> VendedoresIdVendedorGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém um vendedor pelo ID.

        Endpoint: GET /vendedores/{idVendedor}

        Obtém os dados de um vendedor específico pelo seu ID.

        Args:
            seller_id: ID do vendedor (Bling: ``idVendedor``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: VendedoresIdVendedorGetResponse200;
            404: ErrorResponse
        """
        return self.obter(id_vendedor=seller_id)
