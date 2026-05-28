"""Contatos resource."""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING, Literal

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from bling_erp_api.models.generated.contacts import (
        ContatosIdContatoPutRequest,
        ContatosPostRequest,
    )
    from bling_erp_api.types import JsonObject, QueryParams


type DateFilter = date | datetime | str
type ContactListCriterion = Literal[1, 2, 3, 4]
type ContactPersonKind = Literal[1, 2, 3]
type ContactStatus = Literal["A", "I", "E", "S"]


class ContactsResource(BaseResource):
    """Operações de contatos do Bling.

    Este recurso mapeia os endpoints ``/contatos``. Os métodos canônicos usam
    português para acompanhar a documentação oficial; os métodos em inglês
    continuam disponíveis como aliases de compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        pesquisa: str | None = None,
        criterio: ContactListCriterion | None = None,
        data_inclusao_inicial: DateFilter | None = None,
        data_inclusao_final: DateFilter | None = None,
        data_alteracao_inicial: DateFilter | None = None,
        data_alteracao_final: DateFilter | None = None,
        id_tipo_contato: int | None = None,
        id_vendedor: int | None = None,
        uf: str | None = None,
        telefone: str | None = None,
        ids_contatos: Sequence[int] | None = None,
        numero_documento: str | None = None,
        tipo_pessoa: ContactPersonKind | None = None,
    ) -> JsonObject:
        """Lista contatos.

        Endpoint: GET /contatos

        Obtém lista paginada de contatos.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros por página (Bling: ``limite``, integer, opcional)
            pesquisa: Termo de pesquisa (Bling: ``pesquisa``, string, opcional)
            criterio: Critério de listagem: 1=Todos, 2=Ativos, 3=Inativos, 4=Excluídos (Bling: ``criterio``, integer, opcional)
            data_inclusao_inicial: Data de inclusão inicial (Bling: ``dataInclusaoInicial``, string, opcional)
            data_inclusao_final: Data de inclusão final (Bling: ``dataInclusaoFinal``, string, opcional)
            data_alteracao_inicial: Data de alteração inicial (Bling: ``dataAlteracaoInicial``, string, opcional)
            data_alteracao_final: Data de alteração final (Bling: ``dataAlteracaoFinal``, string, opcional)
            id_tipo_contato: ID do tipo de contato (Bling: ``idTipoContato``, integer, opcional)
            id_vendedor: ID do vendedor (Bling: ``idVendedor``, integer, opcional)
            uf: Sigla da UF (Bling: ``uf``, string, opcional)
            telefone: Telefone do contato (Bling: ``telefone``, string, opcional)
            ids_contatos: IDs dos contatos (Bling: ``idsContatos[]``, array, opcional)
            numero_documento: N° do documento (Bling: ``numeroDocumento``, string, opcional)
            tipo_pessoa: Tipo de pessoa: 1=Pessoa Física, 2=Pessoa Jurídica, 3=Outros (Bling: ``tipoPessoa``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: ContatosDadosBaseDTO; 404: ErrorResponse
        """
        return self._get(
            "/contatos",
            params=_contact_list_params(
                pagina=pagina,
                limite=limite,
                pesquisa=pesquisa,
                criterio=criterio,
                data_inclusao_inicial=data_inclusao_inicial,
                data_inclusao_final=data_inclusao_final,
                data_alteracao_inicial=data_alteracao_inicial,
                data_alteracao_final=data_alteracao_final,
                id_tipo_contato=id_tipo_contato,
                id_vendedor=id_vendedor,
                uf=uf,
                telefone=telefone,
                ids_contatos=ids_contatos,
                numero_documento=numero_documento,
                tipo_pessoa=tipo_pessoa,
            ),
        )

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        pesquisa: str | None = None,
        criterio: ContactListCriterion | None = None,
        data_inclusao_inicial: DateFilter | None = None,
        data_inclusao_final: DateFilter | None = None,
        data_alteracao_inicial: DateFilter | None = None,
        data_alteracao_final: DateFilter | None = None,
        id_tipo_contato: int | None = None,
        id_vendedor: int | None = None,
        uf: str | None = None,
        telefone: str | None = None,
        ids_contatos: Sequence[int] | None = None,
        numero_documento: str | None = None,
        tipo_pessoa: ContactPersonKind | None = None,
    ) -> Iterator[JsonObject]:
        """Itera pelos contatos página a página.

        Endpoint: GET /contatos (via paginação automática)

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            pagina: N° da página inicial
            limite: Registros por página
            pesquisa: Termo de pesquisa
            criterio: Critério de listagem
            data_inclusao_inicial: Data de inclusão inicial
            data_inclusao_final: Data de inclusão final
            data_alteracao_inicial: Data de alteração inicial
            data_alteracao_final: Data de alteração final
            id_tipo_contato: ID do tipo de contato
            id_vendedor: ID do vendedor
            uf: UF
            telefone: Telefone
            ids_contatos: IDs dos contatos
            numero_documento: N° do documento
            tipo_pessoa: Tipo de pessoa

        Yields:
            Iterator de JsonObject — cada iteração retorna a resposta de uma página
        """
        params: QueryParams = _contact_list_params(
            pagina=pagina,
            limite=limite,
            pesquisa=pesquisa,
            criterio=criterio,
            data_inclusao_inicial=data_inclusao_inicial,
            data_inclusao_final=data_inclusao_final,
            data_alteracao_inicial=data_alteracao_inicial,
            data_alteracao_final=data_alteracao_final,
            id_tipo_contato=id_tipo_contato,
            id_vendedor=id_vendedor,
            uf=uf,
            telefone=telefone,
            ids_contatos=ids_contatos,
            numero_documento=numero_documento,
            tipo_pessoa=tipo_pessoa,
        )
        return self._iterate("/contatos", page=pagina, limit=limite, params=params)

    def obter(self, id_contato: int) -> JsonObject:
        """Obtém um contato.

        Endpoint: GET /contatos/{idContato}

        Obtém um contato pelo ID.

        Args:
            id_contato: ID do contato (Bling: ``idContato``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContatosDadosBaseDTO; 404: ErrorResponse
        """
        return self._get(f"/contatos/{id_contato}")

    def obter_consumidor_final(self) -> JsonObject:
        """Obtém o contato Consumidor Final.

        Endpoint: GET /contatos/consumidor-final

        Obtém os dados do contato Consumidor Final pré-definido.

        Returns:
            Bling API response. Response schemas: 200: ContatosDadosBaseDTO
        """
        return self._get("/contatos/consumidor-final")

    def criar(self, dados: ContatosPostRequest) -> JsonObject:
        """Cria um contato.

        Endpoint: POST /contatos

        Cria um novo contato.

        Args:
            dados: Dados do contato. Request body schema: ContatosDadosDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self._post("/contatos", json=to_json_object(dados))

    def alterar(self, id_contato: int, dados: ContatosIdContatoPutRequest) -> JsonObject:
        """Altera um contato.

        Endpoint: PUT /contatos/{idContato}

        Altera um contato pelo ID.

        Args:
            id_contato: ID do contato (Bling: ``idContato``, integer, obrigatório)
            dados: Dados do contato para atualização. Request body schema: ContatosDadosDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/contatos/{id_contato}", json=to_json_object(dados))

    def remover(self, id_contato: int) -> JsonObject:
        """Remove um contato.

        Endpoint: DELETE /contatos/{idContato}

        Remove um contato pelo ID.

        Args:
            id_contato: ID do contato (Bling: ``idContato``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/contatos/{id_contato}")

    def remover_varios(self, ids_contatos: Sequence[int]) -> JsonObject:
        """Remove múltiplos contatos.

        Endpoint: DELETE /contatos

        Remove múltiplos contatos pelos IDs.

        Args:
            ids_contatos: IDs dos contatos (Bling: ``idsContatos[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContatosAlertasResponse; 204: NoContent; 400: ErrorResponse
        """
        return self._delete("/contatos", params={"idsContatos[]": list(ids_contatos)})

    def obter_tipo_contato(self, id_contato: int) -> JsonObject:
        """Obtém os tipos de contato de um contato.

        Endpoint: GET /contatos/{idContato}/tipos

        Obtém os tipos de contato associados a um contato.

        Args:
            id_contato: ID do contato (Bling: ``idContato``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContatosTipoContatoDTO; 404: ErrorResponse
        """
        return self._get(f"/contatos/{id_contato}/tipos")

    def listar_tipos(self) -> JsonObject:
        """Lista tipos de contato.

        Endpoint: GET /contatos/tipos

        Obtém todos os tipos de contato disponíveis.

        Returns:
            Bling API response. Response schemas: 200: ContatosTipoContatoDTO
        """
        return self._get("/contatos/tipos")

    def alterar_situacao(self, id_contato: int, situacao: ContactStatus) -> JsonObject:
        """Altera a situação de um contato.

        Endpoint: PATCH /contatos/{idContato}/situacoes

        Altera a situação de um contato pelo ID.

        Args:
            id_contato: ID do contato (Bling: ``idContato``, integer, obrigatório)
            situacao: Situação do contato: A=Ativo, I=Inativo, E=Excluído, S=Sem cobrança (Bling: ``situacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(f"/contatos/{id_contato}/situacoes", json={"situacao": situacao})

    def alterar_situacao_varios(
        self, ids_contatos: Sequence[int], situacao: ContactStatus
    ) -> JsonObject:
        """Altera a situação de múltiplos contatos.

        Endpoint: POST /contatos/situacoes

        Altera a situação de múltiplos contatos pelos IDs.

        Args:
            ids_contatos: IDs dos contatos (Bling: ``idsContatos``, array, obrigatório)
            situacao: Situação: A=Ativo, I=Inativo, E=Excluído, S=Sem cobrança (Bling: ``situacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContatosAlertasResponse; 204: NoContent; 400: ErrorResponse
        """
        return self._post(
            "/contatos/situacoes",
            json={"idsContatos": list(ids_contatos), "situacao": situacao},
        )

    # -- Aliases em inglês (compatibilidade) --

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        search: str | None = None,
        criterion: ContactListCriterion | None = None,
        created_start: DateFilter | None = None,
        created_end: DateFilter | None = None,
        updated_start: DateFilter | None = None,
        updated_end: DateFilter | None = None,
        contact_type_id: int | None = None,
        seller_id: int | None = None,
        uf: str | None = None,
        phone: str | None = None,
        contact_ids: Sequence[int] | None = None,
        tax_id: str | None = None,
        person_kind: ContactPersonKind | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lista contatos.

        Endpoint: GET /contatos

        Obtém lista paginada de contatos.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros por página (Bling: ``limite``, integer, opcional)
            search: Termo de pesquisa (Bling: ``pesquisa``, string, opcional)
            criterion: Critério de listagem (Bling: ``criterio``, integer, opcional)
            created_start: Data de inclusão inicial (Bling: ``dataInclusaoInicial``, string, opcional)
            created_end: Data de inclusão final (Bling: ``dataInclusaoFinal``, string, opcional)
            updated_start: Data de alteração inicial (Bling: ``dataAlteracaoInicial``, string, opcional)
            updated_end: Data de alteração final (Bling: ``dataAlteracaoFinal``, string, opcional)
            contact_type_id: ID do tipo de contato (Bling: ``idTipoContato``, integer, opcional)
            seller_id: ID do vendedor (Bling: ``idVendedor``, integer, opcional)
            uf: Sigla da UF (Bling: ``uf``, string, opcional)
            phone: Telefone do contato (Bling: ``telefone``, string, opcional)
            contact_ids: IDs dos contatos (Bling: ``idsContatos[]``, array, opcional)
            tax_id: N° do documento (Bling: ``numeroDocumento``, string, opcional)
            person_kind: Tipo de pessoa (Bling: ``tipoPessoa``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: ContatosDadosBaseDTO; 404: ErrorResponse
        """
        return self.listar(
            pagina=page,
            limite=limit,
            pesquisa=search,
            criterio=criterion,
            data_inclusao_inicial=created_start,
            data_inclusao_final=created_end,
            data_alteracao_inicial=updated_start,
            data_alteracao_final=updated_end,
            id_tipo_contato=contact_type_id,
            id_vendedor=seller_id,
            uf=uf,
            telefone=phone,
            ids_contatos=contact_ids,
            numero_documento=tax_id,
            tipo_pessoa=person_kind,
        )

    def iterate(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        search: str | None = None,
        criterion: ContactListCriterion | None = None,
        created_start: DateFilter | None = None,
        created_end: DateFilter | None = None,
        updated_start: DateFilter | None = None,
        updated_end: DateFilter | None = None,
        contact_type_id: int | None = None,
        seller_id: int | None = None,
        uf: str | None = None,
        phone: str | None = None,
        contact_ids: Sequence[int] | None = None,
        tax_id: str | None = None,
        person_kind: ContactPersonKind | None = None,
    ) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``.

        Itera pelos contatos página a página.

        Endpoint: GET /contatos (via paginação automática)

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.

        Args:
            page: N° da página inicial
            limit: Registros por página
            search: Termo de pesquisa
            criterion: Critério
            created_start: Data de inclusão inicial
            created_end: Data de inclusão final
            updated_start: Data de alteração inicial
            updated_end: Data de alteração final
            contact_type_id: ID do tipo de contato
            seller_id: ID do vendedor
            uf: UF
            phone: Telefone
            contact_ids: IDs dos contatos
            tax_id: N° do documento
            person_kind: Tipo de pessoa

        Yields:
            Iterator de JsonObject — cada iteração retorna a resposta de uma página
        """
        return self.iterar(
            pagina=page,
            limite=limit,
            pesquisa=search,
            criterio=criterion,
            data_inclusao_inicial=created_start,
            data_inclusao_final=created_end,
            data_alteracao_inicial=updated_start,
            data_alteracao_final=updated_end,
            id_tipo_contato=contact_type_id,
            id_vendedor=seller_id,
            uf=uf,
            telefone=phone,
            ids_contatos=contact_ids,
            numero_documento=tax_id,
            tipo_pessoa=person_kind,
        )

    def get(self, contact_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém um contato.

        Endpoint: GET /contatos/{idContato}

        Obtém um contato pelo ID.

        Args:
            contact_id: ID do contato (Bling: ``idContato``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContatosDadosBaseDTO; 404: ErrorResponse
        """
        return self.obter(contact_id)

    def get_consumer(self) -> JsonObject:
        """Compatibility alias for ``obter_consumidor_final()``.

        Obtém o contato Consumidor Final.

        Endpoint: GET /contatos/consumidor-final

        Obtém os dados do contato Consumidor Final pré-definido.

        Returns:
            Bling API response. Response schemas: 200: ContatosDadosBaseDTO
        """
        return self.obter_consumidor_final()

    def create(self, data: ContatosPostRequest) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria um contato.

        Endpoint: POST /contatos

        Cria um novo contato.

        Args:
            data: Dados do contato. Request body schema: ContatosDadosDTO

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self.criar(data)

    def update(self, contact_id: int, data: ContatosIdContatoPutRequest) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera um contato.

        Endpoint: PUT /contatos/{idContato}

        Altera um contato pelo ID.

        Args:
            contact_id: ID do contato (Bling: ``idContato``, integer, obrigatório)
            data: Dados do contato para atualização. Request body schema: ContatosDadosDTO

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(contact_id, data)

    def delete(self, contact_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove um contato.

        Endpoint: DELETE /contatos/{idContato}

        Remove um contato pelo ID.

        Args:
            contact_id: ID do contato (Bling: ``idContato``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(contact_id)

    def delete_many(self, contact_ids: Sequence[int]) -> JsonObject:
        """Compatibility alias for ``remover_varios()``.

        Remove múltiplos contatos.

        Endpoint: DELETE /contatos

        Remove múltiplos contatos pelos IDs.

        Args:
            contact_ids: IDs dos contatos (Bling: ``idsContatos[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContatosAlertasResponse; 204: NoContent; 400: ErrorResponse
        """
        return self.remover_varios(contact_ids)

    def get_contact_types(self, contact_id: int) -> JsonObject:
        """Compatibility alias for ``obter_tipo_contato()``.

        Obtém os tipos de contato de um contato.

        Endpoint: GET /contatos/{idContato}/tipos

        Obtém os tipos de contato associados a um contato.

        Args:
            contact_id: ID do contato (Bling: ``idContato``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContatosTipoContatoDTO; 404: ErrorResponse
        """
        return self.obter_tipo_contato(contact_id)

    def list_types(self) -> JsonObject:
        """Compatibility alias for ``listar_tipos()``.

        Lista tipos de contato.

        Endpoint: GET /contatos/tipos

        Obtém todos os tipos de contato disponíveis.

        Returns:
            Bling API response. Response schemas: 200: ContatosTipoContatoDTO
        """
        return self.listar_tipos()

    def update_status(self, contact_id: int, status: ContactStatus) -> JsonObject:
        """Compatibility alias for ``alterar_situacao()``.

        Altera a situação de um contato.

        Endpoint: PATCH /contatos/{idContato}/situacoes

        Altera a situação de um contato pelo ID.

        Args:
            contact_id: ID do contato (Bling: ``idContato``, integer, obrigatório)
            status: Situação do contato: A=Ativo, I=Inativo, E=Excluído, S=Sem cobrança (Bling: ``situacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar_situacao(contact_id, status)

    def update_many_status(self, contact_ids: Sequence[int], status: ContactStatus) -> JsonObject:
        """Compatibility alias for ``alterar_situacao_varios()``.

        Altera a situação de múltiplos contatos.

        Endpoint: POST /contatos/situacoes

        Altera a situação de múltiplos contatos pelos IDs.

        Args:
            contact_ids: IDs dos contatos (Bling: ``idsContatos``, array, obrigatório)
            status: Situação: A=Ativo, I=Inativo, E=Excluído, S=Sem cobrança (Bling: ``situacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ContatosAlertasResponse; 204: NoContent; 400: ErrorResponse
        """
        return self.alterar_situacao_varios(contact_ids, status)


def _contact_list_params(  # noqa: PLR0913
    *,
    pagina: int,
    limite: int,
    pesquisa: str | None,
    criterio: ContactListCriterion | None,
    data_inclusao_inicial: DateFilter | None,
    data_inclusao_final: DateFilter | None,
    data_alteracao_inicial: DateFilter | None,
    data_alteracao_final: DateFilter | None,
    id_tipo_contato: int | None,
    id_vendedor: int | None,
    uf: str | None,
    telefone: str | None,
    ids_contatos: Sequence[int] | None,
    numero_documento: str | None,
    tipo_pessoa: ContactPersonKind | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "pesquisa": pesquisa,
            "criterio": criterio,
            "dataInclusaoInicial": _format_datetime_filter(data_inclusao_inicial),
            "dataInclusaoFinal": _format_datetime_filter(data_inclusao_final),
            "dataAlteracaoInicial": _format_datetime_filter(data_alteracao_inicial),
            "dataAlteracaoFinal": _format_datetime_filter(data_alteracao_final),
            "idTipoContato": id_tipo_contato,
            "idVendedor": id_vendedor,
            "uf": uf,
            "telefone": telefone,
            "idsContatos[]": list(ids_contatos) if ids_contatos is not None else None,
            "numeroDocumento": numero_documento,
            "tipoPessoa": tipo_pessoa,
        }
    )


def _format_date_filter(value: DateFilter | None) -> str | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    return value


def _format_datetime_filter(value: DateFilter | None) -> str | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return _format_date_filter(value)
