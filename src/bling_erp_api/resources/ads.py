"""Anúncios resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.models.generated.ads import (
        AnunciosSaveRequest,
    )
    from bling_erp_api.types import JsonObject, QueryParams


def _ads_list_params(
    *,
    situacao: int | None = None,
    id_produto: int | None = None,
    tipo_integracao: str | None = None,
    id_loja: int | None = None,
) -> QueryParams:
    """Build query params for GET /anuncios from SDK param names."""
    return compact_params(
        {
            "situacao": situacao,
            "idProduto": id_produto,
            "tipoIntegracao": tipo_integracao,
            "idLoja": id_loja,
        }
    )


class AdsResource(BaseResource):
    """Operações de anúncios do Bling.

    Este recurso mapeia os endpoints ``/anuncios``. Os métodos canônicos usam
    português para acompanhar a documentação oficial; os métodos em inglês
    continuam disponíveis como aliases de compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        situacao: int | None = None,
        id_produto: int | None = None,
        tipo_integracao: str,
        id_loja: int,
    ) -> JsonObject:
        """Lista anúncios.

        Endpoint: GET /anuncios

        Obtém lista paginada de anúncios.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            limite: Registros por página (Bling: ``limite``, integer, opcional)
            situacao: Situação do anúncio: 1=Publicado, 2=Rascunho, 3=Com problema, 4=Pausado (Bling: ``situacao``, integer, opcional)
            id_produto: ID do produto (Bling: ``idProduto``, integer, opcional)
            tipo_integracao: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            id_loja: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: AnunciosGetAllResponseDTO; 400: ErrorResponse
        """
        params = _ads_list_params(
            situacao=situacao,
            id_produto=id_produto,
            tipo_integracao=tipo_integracao,
            id_loja=id_loja,
        )
        return self._get(f"/anuncios?pagina={pagina}&limite={limite}", params=params)

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        status: int | None = None,
        product_id: int | None = None,
        integration_type: str,
        store_id: int,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lista anúncios.

        Endpoint: GET /anuncios

        Obtém lista paginada de anúncios.

        Args:
            page: N° da página (Bling: ``pagina``, integer, opcional)
            limit: Registros por página (Bling: ``limite``, integer, opcional)
            status: Situação do anúncio (Bling: ``situacao``, integer, opcional)
            product_id: ID do produto (Bling: ``idProduto``, integer, opcional)
            integration_type: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            store_id: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: AnunciosGetAllResponseDTO; 400: ErrorResponse
        """
        return self.listar(
            pagina=page,
            limite=limit,
            situacao=status,
            id_produto=product_id,
            tipo_integracao=integration_type,
            id_loja=store_id,
        )

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        situacao: int | None = None,
        id_produto: int | None = None,
        tipo_integracao: str,
        id_loja: int,
    ) -> Iterator[JsonObject]:
        """Itera pelos anúncios página a página.

        Endpoint: GET /anuncios (via paginação automática)

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            pagina: N° da página inicial
            limite: Registros por página
            situacao: Situação
            id_produto: ID do produto
            tipo_integracao: Tipo de integração
            id_loja: ID da loja

        Yields:
            Iterator de JsonObject — cada iteração retorna a resposta de uma página
        """
        params = _ads_list_params(
            situacao=situacao,
            id_produto=id_produto,
            tipo_integracao=tipo_integracao,
            id_loja=id_loja,
        )
        return self._iterate("/anuncios", page=pagina, limit=limite, params=params)

    def iterate(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        status: int | None = None,
        product_id: int | None = None,
        integration_type: str,
        store_id: int,
    ) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``.

        Itera pelos anúncios página a página.

        Endpoint: GET /anuncios (via paginação automática)

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            page: N° da página inicial
            limit: Registros por página
            status: Situação
            product_id: ID do produto
            integration_type: Tipo de integração
            store_id: ID da loja

        Yields:
            Iterator de JsonObject — cada iteração retorna a resposta de uma página
        """
        return self.iterar(
            pagina=page,
            limite=limit,
            situacao=status,
            id_produto=product_id,
            tipo_integracao=integration_type,
            id_loja=store_id,
        )

    def obter(self, id_anuncio: int, *, tipo_integracao: str, id_loja: int) -> JsonObject:
        """Obtém um anúncio.

        Endpoint: GET /anuncios/{idAnuncio}

        Obtém os detalhes de um anúncio específico pelo ID.

        Args:
            id_anuncio: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
            tipo_integracao: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            id_loja: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: AnunciosGetByIdResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        params = compact_params(
            {
                "tipoIntegracao": tipo_integracao,
                "idLoja": id_loja,
            }
        )
        return self._get(f"/anuncios/{id_anuncio}", params=params)

    def get(self, ad_id: int, *, integration_type: str, store_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém um anúncio.

        Endpoint: GET /anuncios/{idAnuncio}

        Obtém os detalhes de um anúncio específico pelo ID.

        Args:
            ad_id: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
            integration_type: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            store_id: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: AnunciosGetByIdResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.obter(id_anuncio=ad_id, tipo_integracao=integration_type, id_loja=store_id)

    def criar(
        self,
        dados: AnunciosSaveRequest,
    ) -> JsonObject:
        """Cria um anúncio.

        Endpoint: POST /anuncios

        Cria um novo anúncio.

        Args:
            dados: Dados do anúncio. Request body schema: AnunciosSaveRequest

        Returns:
            Bling API response. Response schemas: 201: AnunciosSaveResponseDTO; 400: ErrorResponse
        """
        return self._post("/anuncios", json=to_json_object(dados))

    def create(self, data: AnunciosSaveRequest) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria um anúncio.

        Endpoint: POST /anuncios

        Cria um novo anúncio.

        Args:
            data: Dados do anúncio. Request body schema: AnunciosSaveRequest

        Returns:
            Bling API response. Response schemas: 201: AnunciosSaveResponseDTO; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(
        self,
        id_anuncio: int,
        dados: AnunciosSaveRequest,
    ) -> JsonObject:
        """Altera um anúncio.

        Endpoint: PUT /anuncios/{idAnuncio}

        Altera um anúncio pelo ID.

        Args:
            id_anuncio: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
            dados: Dados do anúncio para atualização. Request body schema: AnunciosSaveRequest

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/anuncios/{id_anuncio}", json=to_json_object(dados))

    def update(
        self,
        ad_id: int,
        data: AnunciosSaveRequest,
    ) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera um anúncio.

        Endpoint: PUT /anuncios/{idAnuncio}

        Altera um anúncio pelo ID.

        Args:
            ad_id: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
            data: Dados do anúncio para atualização. Request body schema: AnunciosSaveRequest

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_anuncio=ad_id, dados=data)

    def remover(self, id_anuncio: int, *, tipo_integracao: str, id_loja: int) -> JsonObject:
        """Remove um anúncio.

        Endpoint: DELETE /anuncios/{idAnuncio}

        Remove um anúncio pelo ID.

        Args:
            id_anuncio: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
            tipo_integracao: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            id_loja: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        params = compact_params(
            {
                "tipoIntegracao": tipo_integracao,
                "idLoja": id_loja,
            }
        )
        return self._delete(f"/anuncios/{id_anuncio}", params=params)

    def delete(self, ad_id: int, *, integration_type: str, store_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove um anúncio.

        Endpoint: DELETE /anuncios/{idAnuncio}

        Remove um anúncio pelo ID.

        Args:
            ad_id: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
            integration_type: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            store_id: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(id_anuncio=ad_id, tipo_integracao=integration_type, id_loja=store_id)

    def publicar(self, id_anuncio: int, *, tipo_integracao: str, id_loja: int) -> JsonObject:
        """Publica um anúncio.

        Endpoint: POST /anuncios/{idAnuncio}/publicar

        Altera o status do anúncio para publicado.

        Args:
            id_anuncio: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
            tipo_integracao: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            id_loja: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        params = compact_params(
            {
                "tipoIntegracao": tipo_integracao,
                "idLoja": id_loja,
            }
        )
        return self._post(f"/anuncios/{id_anuncio}/publicar", params=params)

    def publish(self, ad_id: int, *, integration_type: str, store_id: int) -> JsonObject:
        """Compatibility alias for ``publicar()``.

        Publica um anúncio.

        Endpoint: POST /anuncios/{idAnuncio}/publicar

        Altera o status do anúncio para publicado.

        Args:
            ad_id: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
            integration_type: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            store_id: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.publicar(id_anuncio=ad_id, tipo_integracao=integration_type, id_loja=store_id)

    def pausar(self, id_anuncio: int, *, tipo_integracao: str, id_loja: int) -> JsonObject:
        """Pausa um anúncio.

        Endpoint: POST /anuncios/{idAnuncio}/pausar

        Altera o status do anúncio para pausado.

        Args:
            id_anuncio: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
            tipo_integracao: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            id_loja: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        params = compact_params(
            {
                "tipoIntegracao": tipo_integracao,
                "idLoja": id_loja,
            }
        )
        return self._post(f"/anuncios/{id_anuncio}/pausar", params=params)

    def pause(self, ad_id: int, *, integration_type: str, store_id: int) -> JsonObject:
        """Compatibility alias for ``pausar()``.

        Pausa um anúncio.

        Endpoint: POST /anuncios/{idAnuncio}/pausar

        Altera o status do anúncio para pausado.

        Args:
            ad_id: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
            integration_type: Tipo de integração (Bling: ``tipoIntegracao``, string, obrigatório)
            store_id: ID da loja (Bling: ``idLoja``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.pausar(id_anuncio=ad_id, tipo_integracao=integration_type, id_loja=store_id)
