"""Contatos resource."""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING, Literal

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from bling_erp_api.models.generated.contacts import ContactCreateRequest, ContactUpdateRequest
    from bling_erp_api.types import JsonObject, QueryParams


type DateFilter = date | datetime | str
type ContactListCriterion = Literal[1, 2, 3, 4]
type ContactPersonKind = Literal[1, 2, 3]
type ContactStatus = Literal["A", "I", "E", "S"]


class ContactsResource(BaseResource):
    """Operações em ``/contatos``."""

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
        return self._get(f"/contatos/{id_contato}")

    def obter_consumidor_final(self) -> JsonObject:
        return self._get("/contatos/consumidor-final")

    def criar(self, dados: ContactCreateRequest | JsonObject) -> JsonObject:
        return self._post("/contatos", json=to_json_object(dados))

    def alterar(self, id_contato: int, dados: ContactUpdateRequest | JsonObject) -> JsonObject:
        return self._put(f"/contatos/{id_contato}", json=to_json_object(dados))

    def remover(self, id_contato: int) -> JsonObject:
        return self._delete(f"/contatos/{id_contato}")

    def remover_varios(self, ids_contatos: Sequence[int]) -> JsonObject:
        return self._delete("/contatos", params={"idsContatos[]": list(ids_contatos)})

    def obter_tipo_contato(self, id_contato: int) -> JsonObject:
        return self._get(f"/contatos/{id_contato}/tipos")

    def listar_tipos(self) -> JsonObject:
        return self._get("/contatos/tipos")

    def alterar_situacao(self, id_contato: int, situacao: ContactStatus) -> JsonObject:
        return self._patch(f"/contatos/{id_contato}/situacoes", json={"situacao": situacao})

    def alterar_situacao_varios(
        self, ids_contatos: Sequence[int], situacao: ContactStatus
    ) -> JsonObject:
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
        """Compatibility alias for ``listar()``."""
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
        """Compatibility alias for ``iterar()``."""
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
        """Compatibility alias for ``obter()``."""
        return self.obter(contact_id)

    def get_consumer(self) -> JsonObject:
        """Compatibility alias for ``obter_consumidor_final()``."""
        return self.obter_consumidor_final()

    def create(self, data: ContactCreateRequest | JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``."""
        return self.criar(data)

    def update(self, contact_id: int, data: ContactUpdateRequest | JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``."""
        return self.alterar(contact_id, data)

    def delete(self, contact_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``."""
        return self.remover(contact_id)

    def delete_many(self, contact_ids: Sequence[int]) -> JsonObject:
        """Compatibility alias for ``remover_varios()``."""
        return self.remover_varios(contact_ids)

    def get_contact_types(self, contact_id: int) -> JsonObject:
        """Compatibility alias for ``obter_tipo_contato()``."""
        return self.obter_tipo_contato(contact_id)

    def list_types(self) -> JsonObject:
        """Compatibility alias for ``listar_tipos()``."""
        return self.listar_tipos()

    def update_status(self, contact_id: int, status: ContactStatus) -> JsonObject:
        """Compatibility alias for ``alterar_situacao()``."""
        return self.alterar_situacao(contact_id, status)

    def update_many_status(self, contact_ids: Sequence[int], status: ContactStatus) -> JsonObject:
        """Compatibility alias for ``alterar_situacao_varios()``."""
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
