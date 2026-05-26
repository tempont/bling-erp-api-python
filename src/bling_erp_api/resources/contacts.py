"""Contacts resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams, QueryParamValue


class ContactsResource(BaseResource):
    """Operations for Bling contacts."""

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> JsonObject:
        """Obtém contatos.

        Endpoint: GET /contatos

        Obtém contatos paginados.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            pesquisa: Nome, CPF/CNPJ, fantasia, e-mail ou código do contato (Bling: ``pesquisa``, string, opcional)
            criterio: Criterio de listagem <br> `1` Todos <br> `2` Excluídos <br> `3` Últimos incluídos <br> `4` Sem movimento (Bling: ``criterio``, integer, opcional)
            data_inclusao_inicial: Data de inclusão inicial (Bling: ``dataInclusaoInicial``, string, opcional)
            data_inclusao_final: Data de inclusão final (Bling: ``dataInclusaoFinal``, string, opcional)
            data_alteracao_inicial: Data de alteração inicial (Bling: ``dataAlteracaoInicial``, string, opcional)
            data_alteracao_final: Data de alteração final (Bling: ``dataAlteracaoFinal``, string, opcional)
            id_tipo_contato: ID do tipo do contato (Bling: ``idTipoContato``, integer, opcional)
            id_vendedor: ID do vendedor relacionado ao contato (Bling: ``idVendedor``, integer, opcional)
            uf: UF do contato (Bling: ``uf``, string, opcional)
            telefone: Telefone do contato (Bling: ``telefone``, string, opcional)
            ids_contatos: IDs dos contatos (Bling: ``idsContatos[]``, array, opcional)
            numero_documento:  CPF/CNPJ, desconsiderando a pontuação (Bling: ``numeroDocumento``, string, opcional)
            tipo_pessoa: Tipo de pessoa <br> `1` Física <br> `2` Jurídica <br> `3` Estrangeiro (Bling: ``tipoPessoa``, integer, opcional)
            **filters: Filtros adicionais para a listagem.

        Returns:
            Bling API response. Response schemas: 200: ContatosDadosBaseDTO
        """
        return self._get(
            "/contatos",
            params={"pagina": page, "limite": limit, **filters},
        )

    def iterate(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> Iterator[JsonObject]:
        """Itera pelos registros página a página, mantendo os mesmos filtros.

        Obtém contatos

        Endpoint: GET /contatos

        Obtém contatos paginados.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            pesquisa: Nome, CPF/CNPJ, fantasia, e-mail ou código do contato (Bling: ``pesquisa``, string, opcional)
            criterio: Criterio de listagem <br> `1` Todos <br> `2` Excluídos <br> `3` Últimos incluídos <br> `4` Sem movimento (Bling: ``criterio``, integer, opcional)
            data_inclusao_inicial: Data de inclusão inicial (Bling: ``dataInclusaoInicial``, string, opcional)
            data_inclusao_final: Data de inclusão final (Bling: ``dataInclusaoFinal``, string, opcional)
            data_alteracao_inicial: Data de alteração inicial (Bling: ``dataAlteracaoInicial``, string, opcional)
            data_alteracao_final: Data de alteração final (Bling: ``dataAlteracaoFinal``, string, opcional)
            id_tipo_contato: ID do tipo do contato (Bling: ``idTipoContato``, integer, opcional)
            id_vendedor: ID do vendedor relacionado ao contato (Bling: ``idVendedor``, integer, opcional)
            uf: UF do contato (Bling: ``uf``, string, opcional)
            telefone: Telefone do contato (Bling: ``telefone``, string, opcional)
            ids_contatos: IDs dos contatos (Bling: ``idsContatos[]``, array, opcional)
            numero_documento:  CPF/CNPJ, desconsiderando a pontuação (Bling: ``numeroDocumento``, string, opcional)
            tipo_pessoa: Tipo de pessoa <br> `1` Física <br> `2` Jurídica <br> `3` Estrangeiro (Bling: ``tipoPessoa``, integer, opcional)
            **filters: Filtros adicionais para a listagem.

        Returns:
            Bling API response. Response schemas: 200: ContatosDadosBaseDTO
        """
        params: QueryParams = filters
        return self._iterate("/contatos", page=page, limit=limit, params=params)

    def get(self, contact_id: int) -> JsonObject:
        """Obtém um contato.

        Endpoint: GET /contatos/{idContato}

        Obtém um contato pelo ID.

        Args:
            contact_id: ID do contato (Bling: ``idContato``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContatosDadosBaseDTO, ContatosDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/contatos/{contact_id}")

    def create(self, data: JsonObject) -> JsonObject:
        """Cria um contato.

        Endpoint: POST /contatos

        Cria um contato.

        Request body schema: ContatosDadosBaseDTO, ContatosDadosDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self._post("/contatos", json=data)

    def update(self, contact_id: int, data: JsonObject) -> JsonObject:
        """Altera um contato.

        Endpoint: PUT /contatos/{idContato}

        Altera um contato pelo ID.

        Args:
            contact_id: ID do contato (Bling: ``idContato``, integer, obrigatório)
            data: Dados do contato para atualização.

        Request body schema: ContatosDadosBaseDTO, ContatosDadosDTO

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/contatos/{contact_id}", json=data)

    def delete(self, contact_id: int) -> JsonObject:
        """Remove um contato.

        Endpoint: DELETE /contatos/{idContato}

        Remove um contato pelo ID.

        Args:
            contact_id: ID do contato (Bling: ``idContato``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/contatos/{contact_id}")
