"""Pydantic models for Bling Ads (Anúncios) endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class AnunciosCategoriaDTO(BlingModel):
    """Category reference for an ad."""

    id: int = Field(..., description="ID da categoria")
    nome: str = Field(..., description="Nome da categoria")


class AnunciosAtributoDTO(BlingModel):
    """Attribute of an ad."""

    id: int | None = Field(default=None, alias="id")
    id_externo: str | None = Field(
        default=None, alias="id_externo", description="ID externo do atributo"
    )
    nome: str | None = Field(default=None, description="Nome do atributo")
    tipo: str | None = Field(default=None, description="Tipo do atributo")
    valor: str | None = Field(default=None, description="Valor do atributo")
    unidade: str | None = Field(default=None, description="Unidade do atributo")


class AnunciosImagemDTO(BlingModel):
    """Image of an ad."""

    id: int | None = Field(default=None, description="ID da imagem")
    url: str | None = Field(default=None, description="URL da imagem")
    ordem: int | None = Field(default=None, description="Ordem da imagem")
    tipo: str | None = Field(default=None, description="Tipo da imagem")


class AnunciosVariacaoDTO(BlingModel):
    """Variation of an ad."""

    id: int | None = Field(default=None, description="ID da variação")
    nome: str | None = Field(default=None, description="Nome da variação")


class AnunciosGetAllResponseDTO(BlingModel):
    """Response for listing ads (GET /anuncios)."""

    id: int | None = Field(default=None, description="ID do anúncio")
    titulo: str | None = Field(default=None, description="Título do anúncio")
    situacao: int | None = Field(default=None, description="Situação do anúncio")


class AdsProductRef(BlingModel):
    """Product reference inside ad."""

    id: int | None = Field(default=None, description="ID do produto")


class AnunciosGetByIdResponseDTO(BlingModel):
    """Response for getting a single ad (GET /anuncios/{idAnuncio})."""

    id: int | None = Field(default=None, description="ID do anúncio")
    produto: AdsProductRef | None = Field(default=None)
    titulo: str | None = Field(default=None, description="Título do anúncio")
    descricao: str | None = Field(default=None, description="Descrição do anúncio")
    status: int | None = Field(default=None, description="Situação do anúncio")
    atributos: list[AnunciosAtributoDTO] | None = Field(default=None)
    imagens: list[AnunciosImagemDTO] | None = Field(default=None)
    variacoes: list[AnunciosVariacaoDTO] | None = Field(default=None)


class AdsProdutoRef(BlingModel):
    """Product reference (required) for ad save request."""

    id: int = Field(..., description="ID do produto pai")


class AdsIntegracaoRef(BlingModel):
    """Integration reference (required) for ad save request."""

    tipo: str = Field(..., description="Tipo da integração")


class AdsLojaRef(BlingModel):
    """Store reference (required) for ad save request."""

    id: int = Field(..., description="ID da loja")


class AdsPreco(BlingModel):
    """Price object for ad save request."""

    valor: float | None = Field(default=None, description="Valor do preço")
    promocional: float | None = Field(default=None, description="Preço promocional")


class AdsAnuncioLoja(BlingModel):
    """Store ad reference."""

    id: int | None = Field(default=None)


class AdsEstoques(BlingModel):
    """Stock configuration."""

    itens: list[int] | None = Field(default=None, description="IDs dos depósitos")


class AdsCategoria(BlingModel):
    """Category reference."""

    id: str | None = Field(default=None, description="ID da categoria no marketplace")


class AdsAtributoItem(BlingModel):
    """Attribute key-value pair for ad save request."""

    id: str | None = Field(default=None, description="ID do atributo")
    valor: str | None = Field(default=None, description="Valor do atributo")


class AdsImagemItem(BlingModel):
    """Image reference for ad save request."""

    url: str | None = Field(default=None, description="URL da imagem")
    ordem: int | None = Field(default=None, description="Ordem da imagem")


class AdsMercadoLivreCatalogo(BlingModel):
    """Mercado Livre catalog reference."""

    id: int | None = Field(default=None)


class AdsMercadoLivreGrade(BlingModel):
    """Mercado Livre grade reference."""

    id: int | None = Field(default=None)


class AdsMercadoLivreFrete(BlingModel):
    """Mercado Livre shipping info."""

    gratis: bool | None = Field(default=None, description="Frete grátis")
    tipo: int | None = Field(default=None, description="Tipo de frete")


class AdsMercadoLivreProdutoUsuario(BlingModel):
    """Mercado Livre user product reference."""

    id: int | None = Field(default=None)
    ativo: bool | None = Field(default=None)


class AdsMercadoLivre(BlingModel):
    """Mercado Livre-specific ad configuration."""

    modalidade: str | None = Field(default=None)
    catalogo: AdsMercadoLivreCatalogo | None = Field(default=None)
    grade: AdsMercadoLivreGrade | None = Field(default=None)
    frete: AdsMercadoLivreFrete | None = Field(default=None)
    produto_usuario: AdsMercadoLivreProdutoUsuario | None = Field(
        default=None, alias="produtoUsuario"
    )


class AnunciosSaveRequestBase(BlingModel):
    """Base request body for create/update ad (POST/PUT /anuncios)."""

    produto: AdsProdutoRef = Field(...)
    integracao: AdsIntegracaoRef = Field(...)
    loja: AdsLojaRef = Field(...)
    nome: str | None = Field(default=None, description="Nome do anúncio")
    descricao: str | None = Field(default=None, description="Descrição do anúncio")
    preco: AdsPreco | None = Field(default=None)
    anuncio_loja: AdsAnuncioLoja | None = Field(default=None, alias="anuncioLoja")
    estoques: AdsEstoques | None = Field(default=None)
    categoria: AdsCategoria | None = Field(default=None)
    atributos: list[AdsAtributoItem] | None = Field(default=None)
    imagens: list[AdsImagemItem] | None = Field(default=None)
    mercado_livre: AdsMercadoLivre | None = Field(default=None, alias="mercadoLivre")


class AnunciosSaveRequest(BlingModel):
    """Full request body for create/update ad, including variations."""

    produto: AdsProdutoRef = Field(...)
    integracao: AdsIntegracaoRef = Field(...)
    loja: AdsLojaRef = Field(...)
    nome: str | None = Field(default=None)
    descricao: str | None = Field(default=None)
    preco: AdsPreco | None = Field(default=None)
    anuncio_loja: AdsAnuncioLoja | None = Field(default=None, alias="anuncioLoja")
    estoques: AdsEstoques | None = Field(default=None)
    categoria: AdsCategoria | None = Field(default=None)
    atributos: list[AdsAtributoItem] | None = Field(default=None)
    imagens: list[AdsImagemItem] | None = Field(default=None)
    mercado_livre: AdsMercadoLivre | None = Field(default=None, alias="mercadoLivre")
    variacoes: list[AnunciosSaveRequestBase] | None = Field(default=None)


class AnunciosSaveResponseDTO(BlingModel):
    """Response when creating/updating an ad."""

    id: int | None = Field(default=None, description="ID do anúncio salvo")
    ids_variacoes: list[int] | None = Field(
        default=None,
        alias="idsVariacoes",
        description="IDs das variações",
    )
