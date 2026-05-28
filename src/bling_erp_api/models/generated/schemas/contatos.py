# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``contatos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse, Data8, ErrorResponse


class ContatosDadoAdicionalDTO(BlingModel):
    """OpenAPI schema ``ContatosDadoAdicionalDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data_nascimento: Bling ``dataNascimento``; type ``date | None``; opcional.
        sexo: Bling ``sexo``; type ``str | None``; opcional. `M` Masculino <br> `F` Feminino
        naturalidade: Bling ``naturalidade``; type ``str | None``; opcional."""

    data_nascimento: date | None = Field(
        default=None,
        validation_alias=AliasChoices("data_nascimento", "dataNascimento"),
        examples=["1990-08-24"],
        serialization_alias="dataNascimento",
    )
    sexo: str | None = Field(default=None, examples=["M"])
    naturalidade: str | None = Field(default=None, examples=["Brasileira"])


class ContatosDadosBaseDTO(BlingModel):
    """OpenAPI schema ``ContatosDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação do contato <br> `A` Ativo <br> `E` Excluído <br> `I` Inativo <br> `S` Sem movimentação
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. CPF ou CNPJ do contato
        telefone: Bling ``telefone``; type ``str | None``; opcional.
        celular: Bling ``celular``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    nome: str = Field(..., examples=["Contato"])
    codigo: str | None = Field(default=None, examples=["ASD001"])
    situacao: str = Field(..., examples=["A"])
    numero_documento: str | None = Field(
        default=None,
        validation_alias=AliasChoices("numero_documento", "numeroDocumento"),
        examples=["123.456.789-10"],
        serialization_alias="numeroDocumento",
    )
    telefone: str | None = Field(default=None, examples=["(54) 3333-4444"])
    celular: str | None = Field(default=None, examples=["(54) 99999-8888"])


class ContatosEnderecoDadosDTO(BlingModel):
    """OpenAPI schema ``ContatosEnderecoDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        endereco: Bling ``endereco``; type ``str | None``; opcional.
        cep: Bling ``cep``; type ``str | None``; opcional.
        bairro: Bling ``bairro``; type ``str | None``; opcional.
        municipio: Bling ``municipio``; type ``str | None``; opcional.
        uf: Bling ``uf``; type ``str | None``; opcional.
        numero: Bling ``numero``; type ``str | None``; opcional.
        complemento: Bling ``complemento``; type ``str | None``; opcional."""

    endereco: str | None = Field(default=None, examples=["R. Olavo Bilac"])
    cep: str | None = Field(default=None, examples=["95702-000"])
    bairro: str | None = Field(default=None, examples=["Imigrante"])
    municipio: str | None = Field(default=None, examples=["Bento Gonçalves"])
    uf: str | None = Field(default=None, examples=["RS"])
    numero: str | None = Field(default=None, examples=["914"])
    complemento: str | None = Field(default=None, examples=["Sede 101"])


class ContatosFinanceiroCategoriaDTO(BlingModel):
    """OpenAPI schema ``ContatosFinanceiroCategoriaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ContatosFinanceiroDTO(BlingModel):
    """OpenAPI schema ``ContatosFinanceiroDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        limite_credito: Bling ``limiteCredito``; type ``float | None``; opcional. Limite de crédito do cliente
        condicao_pagamento: Bling ``condicaoPagamento``; type ``str | None``; opcional. Número de parcelas ou prazos
        categoria: Bling ``categoria``; type ``ContatosFinanceiroCategoriaDTO | None``; opcional."""

    limite_credito: float | None = Field(
        default=0,
        validation_alias=AliasChoices("limite_credito", "limiteCredito"),
        examples=[0],
        serialization_alias="limiteCredito",
    )
    condicao_pagamento: str | None = Field(
        default=None,
        validation_alias=AliasChoices("condicao_pagamento", "condicaoPagamento"),
        examples=["30"],
        serialization_alias="condicaoPagamento",
    )
    categoria: ContatosFinanceiroCategoriaDTO | None = None


class ContatosPaisDTO(BlingModel):
    """OpenAPI schema ``ContatosPaisDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str | None``; opcional. Nome do país do contato estrangeiro"""

    nome: str | None = Field(default=None, examples=["ESTADOS UNIDOS"])


class ContatosPessoaContatoDTO(BlingModel):
    """OpenAPI schema ``ContatosPessoaContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        descricao: Bling ``descricao``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    descricao: str | None = Field(default=None, examples=["Fornecedor Fulano"])


class ContatosTipoContatoDTO(BlingModel):
    """OpenAPI schema ``ContatosTipoContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        descricao: Bling ``descricao``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    descricao: str | None = Field(default=None, examples=["Fornecedor"])


class ContatosVendedorDTO(BlingModel):
    """OpenAPI schema ``ContatosVendedorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ContatosGetResponse200(BlingModel):
    """OpenAPI schema ``ContatosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ContatosDadosBaseDTO] | None``; opcional."""

    data: list[ContatosDadosBaseDTO] | None = None


class ContatosPostResponse201(BlingModel):
    """OpenAPI schema ``ContatosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class ContatosIdContatoTiposGetResponse200(BlingModel):
    """OpenAPI schema ``ContatosIdContatoTiposGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ContatosTipoContatoDTO] | None``; opcional."""

    data: list[ContatosTipoContatoDTO] | None = None


class ContatosIdContatoSituacoesPatchRequest(BlingModel):
    """OpenAPI schema ``ContatosIdContatoSituacoesPatchRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        situacao: Bling ``situacao``; type ``str | None``; opcional."""

    situacao: str | None = Field(default=None, examples=["A"])


class ContatosSituacoesPostRequest(BlingModel):
    """OpenAPI schema ``ContatosSituacoesPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        ids_contatos: Bling ``idsContatos``; type ``list[int] | None``; opcional.
        situacao: Bling ``situacao``; type ``str | None``; opcional."""

    ids_contatos: list[int] | None = Field(
        default=None,
        validation_alias=AliasChoices("ids_contatos", "idsContatos"),
        serialization_alias="idsContatos",
    )
    situacao: str | None = Field(default=None, examples=["A"])


class ContatosTiposGetResponse200(BlingModel):
    """OpenAPI schema ``ContatosTiposGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ContatosTipoContatoDTO] | None``; opcional."""

    data: list[ContatosTipoContatoDTO] | None = None


class ContatosEnderecoDTO(BlingModel):
    """OpenAPI schema ``ContatosEnderecoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        geral: Bling ``geral``; type ``ContatosEnderecoDadosDTO | None``; opcional.
        cobranca: Bling ``cobranca``; type ``ContatosEnderecoDadosDTO | None``; opcional."""

    geral: ContatosEnderecoDadosDTO | None = None
    cobranca: ContatosEnderecoDadosDTO | None = None


class ContatosPostRequest(BlingModel):
    """OpenAPI schema ``ContatosPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação do contato <br> `A` Ativo <br> `E` Excluído <br> `I` Inativo <br> `S` Sem movimentação
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. CPF ou CNPJ do contato
        telefone: Bling ``telefone``; type ``str | None``; opcional.
        celular: Bling ``celular``; type ``str | None``; opcional.
        fantasia: Bling ``fantasia``; type ``str | None``; opcional.
        tipo: Bling ``tipo``; type ``str``; obrigatório. Tipo da pessoa <br> `J` Jurídica <br> `F` Física <br> `E` Estrangeira
        indicador_ie: Bling ``indicadorIe``; type ``int | None``; opcional. Indicador de inscrição estadual <br> `1` Contribuinte ICMS <br> `2` Contribuinte isento de Inscrição no cadastro de Contribuintes <br> `9` Não Contribuinte
        ie: Bling ``ie``; type ``str | None``; opcional. Inscrição estadual
        rg: Bling ``rg``; type ``str | None``; opcional. RG do contato caso for pessoa física
        inscricao_municipal: Bling ``inscricaoMunicipal``; type ``str | None``; opcional. Inscrição Municipal da empresa. Apenas para pessoa jurídica
        orgao_emissor: Bling ``orgaoEmissor``; type ``str | None``; opcional. Órgão emissor caso for pessoa física
        email: Bling ``email``; type ``str | None``; opcional.
        email_nota_fiscal: Bling ``emailNotaFiscal``; type ``str | None``; opcional. E-mail para envio da NF-e
        orgao_publico: Bling ``orgaoPublico``; type ``str | None``; opcional. Órgão público? <br> `N` Não <br> `M` Municipal <br> `E` Estadual <br> `F` Federal
        endereco: Bling ``endereco``; type ``ContatosEnderecoDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``ContatosVendedorDTO | None``; opcional.
        dados_adicionais: Bling ``dadosAdicionais``; type ``ContatosDadoAdicionalDTO | None``; opcional.
        financeiro: Bling ``financeiro``; type ``ContatosFinanceiroDTO | None``; opcional.
        pais: Bling ``pais``; type ``ContatosPaisDTO | None``; opcional.
        tipos_contato: Bling ``tiposContato``; type ``list[ContatosTipoContatoDTO] | None``; opcional.
        pessoas_contato: Bling ``pessoasContato``; type ``list[ContatosPessoaContatoDTO] | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    nome: str = Field(..., examples=["Contato"])
    codigo: str | None = Field(default=None, examples=["ASD001"])
    situacao: str = Field(..., examples=["A"])
    numero_documento: str | None = Field(
        default=None,
        validation_alias=AliasChoices("numero_documento", "numeroDocumento"),
        examples=["12345678910"],
        serialization_alias="numeroDocumento",
    )
    telefone: str | None = Field(default=None, examples=["(54) 3333-4444"])
    celular: str | None = Field(default=None, examples=["(54) 99999-8888"])
    fantasia: str | None = Field(default=None, examples=["Nome fantasia"])
    tipo: str = Field(..., examples=["J"])
    indicador_ie: int | None = Field(
        default=None,
        validation_alias=AliasChoices("indicador_ie", "indicadorIe"),
        examples=[1],
        serialization_alias="indicadorIe",
    )
    ie: str | None = Field(default=None, examples=["123.456.789.101"])
    rg: str | None = Field(default=None, examples=["1234567890"])
    inscricao_municipal: str | None = Field(
        default=None,
        validation_alias=AliasChoices("inscricao_municipal", "inscricaoMunicipal"),
        examples=["123456789012"],
        serialization_alias="inscricaoMunicipal",
    )
    orgao_emissor: str | None = Field(
        default=None,
        validation_alias=AliasChoices("orgao_emissor", "orgaoEmissor"),
        examples=["1234567890"],
        serialization_alias="orgaoEmissor",
    )
    email: str | None = Field(default=None, examples=["contato@email.com"])
    email_nota_fiscal: str | None = Field(
        default=None,
        validation_alias=AliasChoices("email_nota_fiscal", "emailNotaFiscal"),
        examples=["fiscal@email.com"],
        serialization_alias="emailNotaFiscal",
    )
    orgao_publico: str | None = Field(
        default=None,
        validation_alias=AliasChoices("orgao_publico", "orgaoPublico"),
        examples=["N"],
        serialization_alias="orgaoPublico",
    )
    endereco: ContatosEnderecoDTO | None = None
    vendedor: ContatosVendedorDTO | None = None
    dados_adicionais: ContatosDadoAdicionalDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("dados_adicionais", "dadosAdicionais"),
        serialization_alias="dadosAdicionais",
    )
    financeiro: ContatosFinanceiroDTO | None = None
    pais: ContatosPaisDTO | None = None
    tipos_contato: list[ContatosTipoContatoDTO] | None = Field(
        default=None,
        validation_alias=AliasChoices("tipos_contato", "tiposContato"),
        serialization_alias="tiposContato",
    )
    pessoas_contato: list[ContatosPessoaContatoDTO] | None = Field(
        default=None,
        validation_alias=AliasChoices("pessoas_contato", "pessoasContato"),
        serialization_alias="pessoasContato",
    )


class ContatosIdContatoGetResponse200(BlingModel):
    """OpenAPI schema ``ContatosIdContatoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data8 | None``; opcional."""

    data: Data8 | None = None


class ContatosIdContatoPutRequest(BlingModel):
    """OpenAPI schema ``ContatosIdContatoPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação do contato <br> `A` Ativo <br> `E` Excluído <br> `I` Inativo <br> `S` Sem movimentação
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. CPF ou CNPJ do contato
        telefone: Bling ``telefone``; type ``str | None``; opcional.
        celular: Bling ``celular``; type ``str | None``; opcional.
        fantasia: Bling ``fantasia``; type ``str | None``; opcional.
        tipo: Bling ``tipo``; type ``str``; obrigatório. Tipo da pessoa <br> `J` Jurídica <br> `F` Física <br> `E` Estrangeira
        indicador_ie: Bling ``indicadorIe``; type ``int | None``; opcional. Indicador de inscrição estadual <br> `1` Contribuinte ICMS <br> `2` Contribuinte isento de Inscrição no cadastro de Contribuintes <br> `9` Não Contribuinte
        ie: Bling ``ie``; type ``str | None``; opcional. Inscrição estadual
        rg: Bling ``rg``; type ``str | None``; opcional. RG do contato caso for pessoa física
        inscricao_municipal: Bling ``inscricaoMunicipal``; type ``str | None``; opcional. Inscrição Municipal da empresa. Apenas para pessoa jurídica
        orgao_emissor: Bling ``orgaoEmissor``; type ``str | None``; opcional. Órgão emissor caso for pessoa física
        email: Bling ``email``; type ``str | None``; opcional.
        email_nota_fiscal: Bling ``emailNotaFiscal``; type ``str | None``; opcional. E-mail para envio da NF-e
        orgao_publico: Bling ``orgaoPublico``; type ``str | None``; opcional. Órgão público? <br> `N` Não <br> `M` Municipal <br> `E` Estadual <br> `F` Federal
        endereco: Bling ``endereco``; type ``ContatosEnderecoDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``ContatosVendedorDTO | None``; opcional.
        dados_adicionais: Bling ``dadosAdicionais``; type ``ContatosDadoAdicionalDTO | None``; opcional.
        financeiro: Bling ``financeiro``; type ``ContatosFinanceiroDTO | None``; opcional.
        pais: Bling ``pais``; type ``ContatosPaisDTO | None``; opcional.
        tipos_contato: Bling ``tiposContato``; type ``list[ContatosTipoContatoDTO] | None``; opcional.
        pessoas_contato: Bling ``pessoasContato``; type ``list[ContatosPessoaContatoDTO] | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    nome: str = Field(..., examples=["Contato"])
    codigo: str | None = Field(default=None, examples=["ASD001"])
    situacao: str = Field(..., examples=["A"])
    numero_documento: str | None = Field(
        default=None,
        validation_alias=AliasChoices("numero_documento", "numeroDocumento"),
        examples=["12345678910"],
        serialization_alias="numeroDocumento",
    )
    telefone: str | None = Field(default=None, examples=["(54) 3333-4444"])
    celular: str | None = Field(default=None, examples=["(54) 99999-8888"])
    fantasia: str | None = Field(default=None, examples=["Nome fantasia"])
    tipo: str = Field(..., examples=["J"])
    indicador_ie: int | None = Field(
        default=None,
        validation_alias=AliasChoices("indicador_ie", "indicadorIe"),
        examples=[1],
        serialization_alias="indicadorIe",
    )
    ie: str | None = Field(default=None, examples=["123.456.789.101"])
    rg: str | None = Field(default=None, examples=["1234567890"])
    inscricao_municipal: str | None = Field(
        default=None,
        validation_alias=AliasChoices("inscricao_municipal", "inscricaoMunicipal"),
        examples=["123456789012"],
        serialization_alias="inscricaoMunicipal",
    )
    orgao_emissor: str | None = Field(
        default=None,
        validation_alias=AliasChoices("orgao_emissor", "orgaoEmissor"),
        examples=["1234567890"],
        serialization_alias="orgaoEmissor",
    )
    email: str | None = Field(default=None, examples=["contato@email.com"])
    email_nota_fiscal: str | None = Field(
        default=None,
        validation_alias=AliasChoices("email_nota_fiscal", "emailNotaFiscal"),
        examples=["fiscal@email.com"],
        serialization_alias="emailNotaFiscal",
    )
    orgao_publico: str | None = Field(
        default=None,
        validation_alias=AliasChoices("orgao_publico", "orgaoPublico"),
        examples=["N"],
        serialization_alias="orgaoPublico",
    )
    endereco: ContatosEnderecoDTO | None = None
    vendedor: ContatosVendedorDTO | None = None
    dados_adicionais: ContatosDadoAdicionalDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("dados_adicionais", "dadosAdicionais"),
        serialization_alias="dadosAdicionais",
    )
    financeiro: ContatosFinanceiroDTO | None = None
    pais: ContatosPaisDTO | None = None
    tipos_contato: list[ContatosTipoContatoDTO] | None = Field(
        default=None,
        validation_alias=AliasChoices("tipos_contato", "tiposContato"),
        serialization_alias="tiposContato",
    )
    pessoas_contato: list[ContatosPessoaContatoDTO] | None = Field(
        default=None,
        validation_alias=AliasChoices("pessoas_contato", "pessoasContato"),
        serialization_alias="pessoasContato",
    )


class ContatosConsumidorFinalGetResponse200(BlingModel):
    """OpenAPI schema ``ContatosConsumidorFinalGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data8 | None``; opcional."""

    data: Data8 | None = None


class ContatosDadosDTO(BlingModel):
    """OpenAPI schema ``ContatosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        fantasia: Bling ``fantasia``; type ``str | None``; opcional.
        tipo: Bling ``tipo``; type ``str``; obrigatório. Tipo da pessoa <br> `J` Jurídica <br> `F` Física <br> `E` Estrangeira
        indicador_ie: Bling ``indicadorIe``; type ``int | None``; opcional. Indicador de inscrição estadual <br> `1` Contribuinte ICMS <br> `2` Contribuinte isento de Inscrição no cadastro de Contribuintes <br> `9` Não Contribuinte
        ie: Bling ``ie``; type ``str | None``; opcional. Inscrição estadual
        rg: Bling ``rg``; type ``str | None``; opcional. RG do contato caso for pessoa física
        inscricao_municipal: Bling ``inscricaoMunicipal``; type ``str | None``; opcional. Inscrição Municipal da empresa. Apenas para pessoa jurídica
        orgao_emissor: Bling ``orgaoEmissor``; type ``str | None``; opcional. Órgão emissor caso for pessoa física
        email: Bling ``email``; type ``str | None``; opcional.
        email_nota_fiscal: Bling ``emailNotaFiscal``; type ``str | None``; opcional. E-mail para envio da NF-e
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. CPF ou CNPJ do contato
        orgao_publico: Bling ``orgaoPublico``; type ``str | None``; opcional. Órgão público? <br> `N` Não <br> `M` Municipal <br> `E` Estadual <br> `F` Federal
        endereco: Bling ``endereco``; type ``ContatosEnderecoDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``ContatosVendedorDTO | None``; opcional.
        dados_adicionais: Bling ``dadosAdicionais``; type ``ContatosDadoAdicionalDTO | None``; opcional.
        financeiro: Bling ``financeiro``; type ``ContatosFinanceiroDTO | None``; opcional.
        pais: Bling ``pais``; type ``ContatosPaisDTO | None``; opcional.
        tipos_contato: Bling ``tiposContato``; type ``list[ContatosTipoContatoDTO] | None``; opcional.
        pessoas_contato: Bling ``pessoasContato``; type ``list[ContatosPessoaContatoDTO] | None``; opcional."""

    fantasia: str | None = Field(default=None, examples=["Nome fantasia"])
    tipo: str = Field(..., examples=["J"])
    indicador_ie: int | None = Field(
        default=None,
        validation_alias=AliasChoices("indicador_ie", "indicadorIe"),
        examples=[1],
        serialization_alias="indicadorIe",
    )
    ie: str | None = Field(default=None, examples=["123.456.789.101"])
    rg: str | None = Field(default=None, examples=["1234567890"])
    inscricao_municipal: str | None = Field(
        default=None,
        validation_alias=AliasChoices("inscricao_municipal", "inscricaoMunicipal"),
        examples=["123456789012"],
        serialization_alias="inscricaoMunicipal",
    )
    orgao_emissor: str | None = Field(
        default=None,
        validation_alias=AliasChoices("orgao_emissor", "orgaoEmissor"),
        examples=["1234567890"],
        serialization_alias="orgaoEmissor",
    )
    email: str | None = Field(default=None, examples=["contato@email.com"])
    email_nota_fiscal: str | None = Field(
        default=None,
        validation_alias=AliasChoices("email_nota_fiscal", "emailNotaFiscal"),
        examples=["fiscal@email.com"],
        serialization_alias="emailNotaFiscal",
    )
    numero_documento: str | None = Field(
        default=None,
        validation_alias=AliasChoices("numero_documento", "numeroDocumento"),
        examples=["12345678910"],
        serialization_alias="numeroDocumento",
    )
    orgao_publico: str | None = Field(
        default=None,
        validation_alias=AliasChoices("orgao_publico", "orgaoPublico"),
        examples=["N"],
        serialization_alias="orgaoPublico",
    )
    endereco: ContatosEnderecoDTO | None = None
    vendedor: ContatosVendedorDTO | None = None
    dados_adicionais: ContatosDadoAdicionalDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("dados_adicionais", "dadosAdicionais"),
        serialization_alias="dadosAdicionais",
    )
    financeiro: ContatosFinanceiroDTO | None = None
    pais: ContatosPaisDTO | None = None
    tipos_contato: list[ContatosTipoContatoDTO] | None = Field(
        default=None,
        validation_alias=AliasChoices("tipos_contato", "tiposContato"),
        serialization_alias="tiposContato",
    )
    pessoas_contato: list[ContatosPessoaContatoDTO] | None = Field(
        default=None,
        validation_alias=AliasChoices("pessoas_contato", "pessoasContato"),
        serialization_alias="pessoasContato",
    )


class ContatosAlertasResponse(BlingModel):
    """OpenAPI schema ``ContatosAlertasResponse``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        alertas: Bling ``alertas``; type ``list[ErrorResponse]``; obrigatório."""

    alertas: list[ErrorResponse]


class ContatosDeleteResponse200(BlingModel):
    """OpenAPI schema ``ContatosDeleteResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``ContatosAlertasResponse | None``; opcional."""

    data: ContatosAlertasResponse | None = None


class ContatosSituacoesPostResponse200(BlingModel):
    """OpenAPI schema ``ContatosSituacoesPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``ContatosAlertasResponse | None``; opcional."""

    data: ContatosAlertasResponse | None = None


__all__ = [
    "ContatosAlertasResponse",
    "ContatosConsumidorFinalGetResponse200",
    "ContatosDadoAdicionalDTO",
    "ContatosDadosBaseDTO",
    "ContatosDadosDTO",
    "ContatosDeleteResponse200",
    "ContatosEnderecoDTO",
    "ContatosEnderecoDadosDTO",
    "ContatosFinanceiroCategoriaDTO",
    "ContatosFinanceiroDTO",
    "ContatosGetResponse200",
    "ContatosIdContatoGetResponse200",
    "ContatosIdContatoPutRequest",
    "ContatosIdContatoSituacoesPatchRequest",
    "ContatosIdContatoTiposGetResponse200",
    "ContatosPaisDTO",
    "ContatosPessoaContatoDTO",
    "ContatosPostRequest",
    "ContatosPostResponse201",
    "ContatosSituacoesPostRequest",
    "ContatosSituacoesPostResponse200",
    "ContatosTipoContatoDTO",
    "ContatosTiposGetResponse200",
    "ContatosVendedorDTO",
]
