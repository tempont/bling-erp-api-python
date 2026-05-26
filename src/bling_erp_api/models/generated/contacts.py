"""Semi-generated contact models."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class ContactType(BlingModel):
    """Tipo de contato (``ContatosTipoContatoDTO``)."""

    id: int | None = None
    description: str | None = Field(default=None, alias="descricao")


class Contact(BlingModel):
    """Contato retornado ou enviado na API do Bling."""

    id: int | None = None
    name: str | None = Field(default=None, alias="nome")
    code: str | None = Field(default=None, alias="codigo")
    trade_name: str | None = Field(default=None, alias="fantasia")
    status: str | None = Field(default=None, alias="situacao")
    tax_id: str | None = Field(default=None, alias="numeroDocumento")
    person_type: str | None = Field(default=None, alias="tipo")
    phone: str | None = Field(default=None, alias="telefone")
    cellphone: str | None = Field(default=None, alias="celular")
    email: str | None = Field(default=None, alias="email")
    email_nf: str | None = Field(default=None, alias="emailNotaFiscal")
    state_registration_indicator: int | None = Field(default=None, alias="indicadorIe")
    state_registration: str | None = Field(default=None, alias="ie")
    id_document: str | None = Field(default=None, alias="rg")
    municipal_registration: str | None = Field(default=None, alias="inscricaoMunicipal")
    issuer_org: str | None = Field(default=None, alias="orgaoEmissor")
    public_body: str | None = Field(default=None, alias="orgaoPublico")
    address: dict[str, object] | None = Field(default=None, alias="endereco")
    salesperson: dict[str, object] | None = Field(default=None, alias="vendedor")
    extra_data: dict[str, object] | None = Field(default=None, alias="dadosAdicionais")
    financial: dict[str, object] | None = Field(default=None, alias="financeiro")
    country: dict[str, object] | None = Field(default=None, alias="pais")
    contact_types: list[ContactType] = Field(default_factory=list, alias="tiposContato")
    contact_persons: list[dict[str, object]] = Field(default_factory=list, alias="pessoasContato")


class ContactCreateRequest(Contact):
    """Payload aceito por ``POST /contatos``."""


class ContactUpdateRequest(Contact):
    """Payload aceito por ``PUT /contatos/{idContato}``."""


class ContactListResponse(BlingModel):
    """Response de ``GET /contatos``."""

    data: list[Contact] = Field(default_factory=list)


class ContactResponse(BlingModel):
    """Response de ``GET /contatos/{idContato}`` e afins."""

    data: Contact


class ContactTypeListResponse(BlingModel):
    """Response de listagens de tipo de contato."""

    data: list[ContactType] = Field(default_factory=list)


class ContactAlertsResponse(BlingModel):
    """Alertas em operações em lote."""

    alerts: list[dict[str, object]] = Field(default_factory=list, alias="alertas")


class ContactMutationResult(BlingModel):
    """Resultado típico de ``POST /contatos``."""

    id: int | None = None


class ContactMutationResponse(BlingModel):
    """Response de ``POST /contatos``."""

    data: ContactMutationResult
