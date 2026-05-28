# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``common``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

from .campos_customizados import (
    CamposCustomizadosDadosBaseDTO,
    CamposCustomizadosDadosDTO,
    CamposCustomizadosDadosEdicaoDTO,
    CamposCustomizadosModuloBaseDTO,
    CamposCustomizadosModuloDTO,
    CamposCustomizadosResponsePOSTPUT,
    CamposCustomizadosTipoBaseDTO,
    CamposCustomizadosTipoDTO,
)
from .categorias_produtos import CategoriasProdutosDadosDTO
from .categorias_receitas_despesas import (
    CategoriasReceitasDespesasDadosBaseDTO,
    CategoriasReceitasDespesasDadosDTO,
)
from .contas import ContasDadosBaseDTO
from .contas_pagar import ContasPagarDadosDTO
from .contas_receber import (
    ContasReceberDadosBaseDTO,
    ContasReceberDadosDTO,
    ContasReceberDadosListDTO,
)
from .contratos import ContratosDadosBaseDTO, ContratosDadosDTO
from .estoques import EstoquesSaldosBaseDTO, EstoquesSaldosDTO
from .formas_pagamentos import FormasPagamentosDadosBaseDTO, FormasPagamentosDadosDTO
from .homologacao import HomologacaoDadosBaseDTO, HomologacaoDadosDTO
from .notas_fiscais import NotaFiscalResponsePOST, NotasFiscaisDadosBaseDTO, NotasFiscaisDadosGetDTO
from .notas_servicos import (
    NotasServicosContatoBaseDTO,
    NotasServicosContatoDTO,
    NotasServicosDadosBaseDTO,
    NotasServicosDadosDTO,
    NotasServicosResponsePOSTPUT,
)
from .notificacoes import NotificacoesDadosBaseDTO, NotificacoesUlidsDTO
from .pedidos_compras import (
    PedidosCompraResponsePOSTPUT,
    PedidosComprasDadosBaseDTO,
    PedidosComprasDadosDTO,
)
from .pedidos_vendas import VendasDadosBaseDTO, VendasDadosDTO, VendasResponsePOSTPUT
from .produtos_fornecedores import ProdutosFornecedoresDadosBaseDTO, ProdutosFornecedoresDadosDTO
from .produtos_lojas import (
    ProdutosLojasDadosBaseDTO,
    ProdutosLojasDadosDTO,
    ProdutosLojasResponsePOSTPUT,
)
from .situacoes import SituacoesDTO, SituacoesDadosDTO, SituacoesModuloBaseDTO, SituacoesModuloDTO
from .vendedores import VendedoresDadosBaseDTO, VendedoresDadosDTO

if TYPE_CHECKING:
    from .categorias_produtos import CategoriasProdutosCategoriPaiDTO
    from .contatos import (
        ContatosDadoAdicionalDTO,
        ContatosEnderecoDTO,
        ContatosFinanceiroDTO,
        ContatosPaisDTO,
        ContatosPessoaContatoDTO,
        ContatosTipoContatoDTO,
        ContatosVendedorDTO,
    )
    from .produtos import (
        ProdutoUsuario,
        ProdutosCampoCustomizadoDTO,
        ProdutosCategoriaDTO,
        ProdutosDimensoesDTO,
        ProdutosEstoqueDTO,
        ProdutosEstruturaDTO,
        ProdutosLinhaProdutoDTO,
        ProdutosMidiaDTO,
        ProdutosTributacaoDTO,
        ProdutosVariacaoDTO,
    )
    from .produtos_fornecedores import ProdutoFornecedorDTO


class BasePostResponse(BlingModel):
    """OpenAPI schema ``BasePostResponse``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class Integracao(BlingModel):
    """OpenAPI schema ``Integracao``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        tipo: Bling ``tipo``; type ``str``; obrigatório. Tipo da integração"""

    tipo: str = Field(..., examples=["MercadoLivre"])


class Loja(BlingModel):
    """OpenAPI schema ``Loja``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID da loja"""

    id: int = Field(..., examples=[1])


class Preco(BlingModel):
    """OpenAPI schema ``Preco``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        valor: Bling ``valor``; type ``float | None``; opcional.
        promocional: Bling ``promocional``; type ``float | None``; opcional."""

    valor: float | None = Field(default=None, examples=[100.5])
    promocional: float | None = Field(default=None, examples=[90])


class AnuncioLoja(BlingModel):
    """OpenAPI schema ``AnuncioLoja``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[456])


class Categoria(BlingModel):
    """OpenAPI schema ``Categoria``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``str | None``; opcional."""

    id: str | None = Field(default=None, examples=["MLB123"])


class Atributo(BlingModel):
    """OpenAPI schema ``Atributo``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``str | None``; opcional.
        valor: Bling ``valor``; type ``str | None``; opcional."""

    id: str | None = Field(default=None, examples=["COLOR"])
    valor: str | None = Field(default=None, examples=["Azul"])


class Imagen(BlingModel):
    """OpenAPI schema ``Imagen``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        url: Bling ``url``; type ``str | None``; opcional.
        ordem: Bling ``ordem``; type ``int | None``; opcional."""

    url: str | None = Field(default=None, examples=["https://exemplo.com/imagem.jpg"])
    ordem: int | None = Field(default=None, examples=[1])


class Catalogo(BlingModel):
    """OpenAPI schema ``Catalogo``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[123])


class Grade(BlingModel):
    """OpenAPI schema ``Grade``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[987])


class Frete(BlingModel):
    """OpenAPI schema ``Frete``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        gratis: Bling ``gratis``; type ``bool | None``; opcional.
        tipo: Bling ``tipo``; type ``int | None``; opcional."""

    gratis: bool | None = Field(default=None, examples=[True])
    tipo: int | None = Field(default=None, examples=[1])


class MercadoLivre(BlingModel):
    """OpenAPI schema ``MercadoLivre``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        modalidade: Bling ``modalidade``; type ``str | None``; opcional.
        catalogo: Bling ``catalogo``; type ``Catalogo | None``; opcional.
        grade: Bling ``grade``; type ``Grade | None``; opcional.
        frete: Bling ``frete``; type ``Frete | None``; opcional.
        produto_usuario: Bling ``produtoUsuario``; type ``ProdutoUsuario | None``; opcional."""

    modalidade: str | None = Field(default=None, examples=["gold_pro"])
    catalogo: Catalogo | None = None
    grade: Grade | None = None
    frete: Frete | None = None
    produto_usuario: ProdutoUsuario | None = Field(
        default=None,
        validation_alias=AliasChoices("produto_usuario", "produtoUsuario"),
        serialization_alias="produtoUsuario",
    )


class LojaUnidadeNegocioDTO(BlingModel):
    """OpenAPI schema ``LojaUnidadeNegocioDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LotResponseDTO(BlingModel):
    """OpenAPI schema ``LotResponseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        codigo_lote: Bling ``codigoLote``; type ``str | None``; opcional.
        id_produto: Bling ``idProduto``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    codigo_lote: str | None = Field(
        default=None,
        validation_alias=AliasChoices("codigo_lote", "codigoLote"),
        examples=["Lote 1"],
        serialization_alias="codigoLote",
    )
    id_produto: int | None = Field(
        default=None,
        validation_alias=AliasChoices("id_produto", "idProduto"),
        examples=[12345678],
        serialization_alias="idProduto",
    )


class Contato1(BlingModel):
    """OpenAPI schema ``Contato1``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str | None``; opcional."""

    nome: str | None = Field(default=None, examples=["Contato do Bling"])


class CategoriasProduto(BlingModel):
    """OpenAPI schema ``CategoriasProduto``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID da categoria de produto que foi vínculada com sucesso"""

    id: int | None = Field(default=None, examples=[12345678])


class DeletedItem(BlingModel):
    """OpenAPI schema ``DeletedItem``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do produto
        variations: Bling ``variations``; type ``dict[str, Any] | None``; opcional.
        warnings: Bling ``warnings``; type ``list[str] | None``; opcional."""

    id: int | None = Field(default=None, examples=[6423817579])
    variations: dict[str, Any] | None = None
    warnings: list[str] | None = None


class UpdatedItem(BlingModel):
    """OpenAPI schema ``UpdatedItem``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do produto
        variations: Bling ``variations``; type ``dict[str, Any] | None``; opcional.
        warnings: Bling ``warnings``; type ``list[str] | None``; opcional."""

    id: int | None = Field(default=None, examples=[6423817579])
    variations: dict[str, Any] | None = None
    warnings: list[str] | None = None


class SavedItem(BlingModel):
    """OpenAPI schema ``SavedItem``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do produto
        variations: Bling ``variations``; type ``dict[str, Any] | None``; opcional.
        warnings: Bling ``warnings``; type ``list[str] | None``; opcional."""

    id: int | None = Field(default=None, examples=[6423817579])
    variations: dict[str, Any] | None = None
    warnings: list[str] | None = None


class Variations(BlingModel):
    """OpenAPI schema ``Variations``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        deleted: Bling ``deleted``; type ``list[DeletedItem] | None``; opcional.
        updated: Bling ``updated``; type ``list[UpdatedItem] | None``; opcional.
        saved: Bling ``saved``; type ``list[SavedItem] | None``; opcional."""

    deleted: list[DeletedItem] | None = None
    updated: list[UpdatedItem] | None = None
    saved: list[SavedItem] | None = None


class Data(BlingModel):
    """OpenAPI schema ``Data``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``float | None``; opcional. ID do produto
        variations: Bling ``variations``; type ``Variations | None``; opcional.
        warnings: Bling ``warnings``; type ``list[str] | None``; opcional."""

    id: float | None = Field(default=None, examples=[6423817751])
    variations: Variations | None = None
    warnings: list[str] | None = None


class ErrorFieldCollection(BlingModel):
    """OpenAPI schema ``ErrorFieldCollection``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        index: Bling ``index``; type ``int``; obrigatório.
        code: Bling ``code``; type ``int``; obrigatório.
        msg: Bling ``msg``; type ``str``; obrigatório.
        element: Bling ``element``; type ``str | None``; opcional.
        namespace: Bling ``namespace``; type ``str | None``; opcional. Referência ao objeto com erro."""

    index: int = Field(..., examples=[1])
    code: int = Field(..., examples=[12])
    msg: str = Field(..., examples=["Id da forma de pagamento inválido."])
    element: str | None = Field(default=None, examples=["formaPagamento"])
    namespace: str | None = Field(default=None, examples=["VENDAS"])


class Datum1(CamposCustomizadosTipoBaseDTO, CamposCustomizadosTipoDTO):
    """OpenAPI schema ``Datum1``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CamposCustomizadosTipoBaseDTO, CamposCustomizadosTipoDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str | None``; opcional.
        mascara: Bling ``mascara``; type ``str | None``; opcional."""

    pass


class Data2(BasePostResponse, CamposCustomizadosResponsePOSTPUT):
    """OpenAPI schema ``Data2``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: BasePostResponse, CamposCustomizadosResponsePOSTPUT.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        ids_vinculos_agrupadores: Bling ``idsVinculosAgrupadores``; type ``list[int] | None``; opcional.
        ids_opcoes: Bling ``idsOpcoes``; type ``list[int] | None``; opcional."""

    pass


class Datum2(CategoriasProdutosDadosDTO):
    """OpenAPI schema ``Datum2``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CategoriasProdutosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição da categoria
        categoria_pai: Bling ``categoriaPai``; type ``CategoriasProdutosCategoriPaiDTO | None``; opcional."""

    categoria_pai: CategoriasProdutosCategoriPaiDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("categoria_pai", "categoriaPai"),
        serialization_alias="categoriaPai",
    )


class Data4(CategoriasProdutosDadosDTO):
    """OpenAPI schema ``Data4``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CategoriasProdutosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição da categoria
        categoria_pai: Bling ``categoriaPai``; type ``CategoriasProdutosCategoriPaiDTO | None``; opcional."""

    categoria_pai: CategoriasProdutosCategoriPaiDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("categoria_pai", "categoriaPai"),
        serialization_alias="categoriaPai",
    )


class Data6(CategoriasReceitasDespesasDadosBaseDTO, CategoriasReceitasDespesasDadosDTO):
    """OpenAPI schema ``Data6``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CategoriasReceitasDespesasDadosBaseDTO, CategoriasReceitasDespesasDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        id_categoria_pai: Bling ``idCategoriaPai``; type ``int | None``; opcional. Id da categoria pai. Se for a categoria raíz será 0.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        tipo: Bling ``tipo``; type ``int``; obrigatório. `1` Despesa<br>`2` Receita<br>`3` Receita e despesa
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativa <br> `1` Ativa"""

    pass


class Bordero(BlingModel):
    """OpenAPI schema ``Bordero``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])


class Error1(BlingModel):
    """OpenAPI schema ``Error1``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        type: Bling ``type``; type ``str | None``; opcional. Tipo do erro.
        message: Bling ``message``; type ``str | None``; opcional. Mensagem de erro.
        description: Bling ``description``; type ``str | None``; opcional. Descrição do erro."""

    type: str | None = Field(default=None, examples=["RESOURCE_NOT_FOUND"])
    message: str | None = Field(default=None, examples=["Nenhum boleto foi localizado"])
    description: str | None = Field(
        default=None,
        examples=[
            "O recurso requisitado não foi encontrado. Verifique se o endpoint solicitado está correto ou se o ID informado realmente existe no sistema"
        ],
    )


class FieldModel(BlingModel):
    """OpenAPI schema ``FieldModel``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        code: Bling ``code``; type ``int | None``; opcional.
        msg: Bling ``msg``; type ``str | None``; opcional.
        element: Bling ``element``; type ``str | None``; opcional.
        namespace: Bling ``namespace``; type ``str | None``; opcional."""

    code: int | None = Field(default=None, examples=[""])
    msg: str | None = Field(
        default=None,
        examples=[
            "Conta(s) a receber não foram encontrada(s), verifique se as contas estão em aberto e com forma de pagamento boleto bancário"
        ],
    )
    element: str | None = Field(default=None, examples=["idDuplicata"])
    namespace: str | None = Field(default=None, examples=[""])


class Datum3(EstoquesSaldosBaseDTO, EstoquesSaldosDTO):
    """OpenAPI schema ``Datum3``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: EstoquesSaldosBaseDTO, EstoquesSaldosDTO.

    Fields:
        produto: Bling ``produto``; type ``EstoquesProdutoDTO | None``; opcional.
        saldo_fisico_total: Bling ``saldoFisicoTotal``; type ``float | None``; opcional. Saldo físico total do produto
        saldo_virtual_total: Bling ``saldoVirtualTotal``; type ``float | None``; opcional. Saldo total do produto desconsiderando produtos reservados
        depositos: Bling ``depositos``; type ``list[Deposito] | None``; opcional."""

    pass


class Data12(HomologacaoDadosDTO, HomologacaoDadosBaseDTO):
    """OpenAPI schema ``Data12``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: HomologacaoDadosDTO, HomologacaoDadosBaseDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``float | None``; opcional.
        codigo: Bling ``codigo``; type ``str | None``; opcional."""

    pass


class Data13(BasePostResponse, NotaFiscalResponsePOST):
    """OpenAPI schema ``Data13``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: BasePostResponse, NotaFiscalResponsePOST.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório.
        contato: Bling ``contato``; type ``Contato1``; obrigatório."""

    pass


class Data16(BlingModel):
    """OpenAPI schema ``Data16``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        xml: Bling ``xml``; type ``str | None``; opcional."""

    xml: str | None = None


class Data17(BasePostResponse, NotaFiscalResponsePOST):
    """OpenAPI schema ``Data17``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: BasePostResponse, NotaFiscalResponsePOST.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório.
        contato: Bling ``contato``; type ``Contato1``; obrigatório."""

    pass


class Data20(BlingModel):
    """OpenAPI schema ``Data20``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        xml: Bling ``xml``; type ``str | None``; opcional."""

    xml: str | None = None


class Data21(BasePostResponse, NotasServicosResponsePOSTPUT):
    """OpenAPI schema ``Data21``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: BasePostResponse, NotasServicosResponsePOSTPUT.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero_rps: Bling ``numeroRPS``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório."""

    pass


class Data25(BasePostResponse, PedidosCompraResponsePOSTPUT):
    """OpenAPI schema ``Data25``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: BasePostResponse, PedidosCompraResponsePOSTPUT.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``int``; obrigatório.
        alertas: Bling ``alertas``; type ``list[str] | None``; opcional.
        erros_anexo: Bling ``errosAnexo``; type ``list[str] | None``; opcional."""

    pass


class Data30(BasePostResponse, ProdutosLojasResponsePOSTPUT):
    """OpenAPI schema ``Data30``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: BasePostResponse, ProdutosLojasResponsePOSTPUT.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        categorias_produtos: Bling ``categoriasProdutos``; type ``list[CategoriasProduto] | None``; opcional."""

    pass


class Datum6(SituacoesModuloBaseDTO, SituacoesModuloDTO):
    """OpenAPI schema ``Datum6``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: SituacoesModuloBaseDTO, SituacoesModuloDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório. Nome do módulo.
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição do módulo.
        criar_situacoes: Bling ``criarSituacoes``; type ``bool``; obrigatório. Identifica a possibilidade de criar situações."""

    pass


class Datum7(SituacoesDTO, SituacoesDadosDTO):
    """OpenAPI schema ``Datum7``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: SituacoesDTO, SituacoesDadosDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório. Utilizado no GET.
        id_herdado: Bling ``idHerdado``; type ``int | None``; opcional. ID da situação de referência.
        cor: Bling ``cor``; type ``str | None``; opcional. Código hexadecimal."""

    pass


class Data33(SituacoesDTO, SituacoesDadosDTO):
    """OpenAPI schema ``Data33``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: SituacoesDTO, SituacoesDadosDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório. Utilizado no GET.
        id_herdado: Bling ``idHerdado``; type ``int | None``; opcional. ID da situação de referência.
        cor: Bling ``cor``; type ``str | None``; opcional. Código hexadecimal."""

    pass


class Datum8(BlingModel):
    """OpenAPI schema ``Datum8``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        message: Bling ``message``; type ``str | None``; opcional."""

    message: str | None = Field(
        default=None,
        examples=[
            "Caso o e-mail informado esteja cadastrado em nosso sistema, uma mensagem com instruções para a troca de senha será enviada."
        ],
    )


class Datum9(BlingModel):
    """OpenAPI schema ``Datum9``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        valido: Bling ``valido``; type ``bool | None``; opcional."""

    valido: bool | None = Field(default=None, examples=["true"])


class Data35(BlingModel):
    """OpenAPI schema ``Data35``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        alertas: Bling ``alertas``; type ``list[str] | None``; opcional."""

    alertas: list[str] | None = None


class Contato(NotasServicosContatoBaseDTO, NotasServicosContatoDTO):
    """OpenAPI schema ``Contato``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasServicosContatoBaseDTO, NotasServicosContatoDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str``; obrigatório. CNPJ ou CPF.
        email: Bling ``email``; type ``str``; obrigatório.
        ie: Bling ``ie``; type ``str | None``; opcional. Inscrição estadual.
        telefone: Bling ``telefone``; type ``str | None``; opcional.
        im: Bling ``im``; type ``str | None``; opcional. Inscrição municipal.
        endereco: Bling ``endereco``; type ``NotasServicosContatoEnderecoDTO | None``; opcional."""

    pass


class ErrorField(BlingModel):
    """OpenAPI schema ``ErrorField``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        code: Bling ``code``; type ``int``; obrigatório.
        msg: Bling ``msg``; type ``str``; obrigatório.
        element: Bling ``element``; type ``str | None``; opcional.
        namespace: Bling ``namespace``; type ``str | None``; opcional. Referência ao objeto com erro.
        collection: Bling ``collection``; type ``list[ErrorFieldCollection] | None``; opcional."""

    code: int = Field(..., examples=[49])
    msg: str = Field(..., examples=["Uma ou mais parcelas da venda possuem erros de validação"])
    element: str | None = Field(default=None, examples=["parcelas"])
    namespace: str | None = Field(default=None, examples=["VENDAS"])
    collection: list[ErrorFieldCollection] | None = None


class Datum(CamposCustomizadosModuloBaseDTO, CamposCustomizadosModuloDTO):
    """OpenAPI schema ``Datum``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CamposCustomizadosModuloBaseDTO, CamposCustomizadosModuloDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório.
        modulo: Bling ``modulo``; type ``str``; obrigatório.
        agrupador: Bling ``agrupador``; type ``str | None``; opcional. Atributo do cadastro utilizado como agrupador.
        permissoes: Bling ``permissoes``; type ``list[CamposCustomizadosPermissaoDTO]``; obrigatório."""

    pass


class Data1(
    CamposCustomizadosDadosBaseDTO, CamposCustomizadosDadosEdicaoDTO, CamposCustomizadosDadosDTO
):
    """OpenAPI schema ``Data1``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CamposCustomizadosDadosBaseDTO, CamposCustomizadosDadosEdicaoDTO, CamposCustomizadosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório. Ignorado no método PUT
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativo <br> `1` Ativo
        placeholder: Bling ``placeholder``; type ``str | None``; opcional.
        obrigatorio: Bling ``obrigatorio``; type ``bool | None``; opcional.
        opcoes: Bling ``opcoes``; type ``list[CamposCustomizadosOpcaoDTO] | None``; opcional.
        tamanho: Bling ``tamanho``; type ``CamposCustomizadosTamanhoDTO | None``; opcional.
        agrupadores: Bling ``agrupadores``; type ``list[CamposCustomizadosAgrupadorDTO] | None``; opcional.
        modulo: Bling ``modulo``; type ``CamposCustomizadosModuloBaseDTO``; obrigatório.
        tipo_campo: Bling ``tipoCampo``; type ``CamposCustomizadosTipoBaseDTO``; obrigatório."""

    pass


class Data7(ContasReceberDadosListDTO, ContasReceberDadosBaseDTO, ContasReceberDadosDTO):
    """OpenAPI schema ``Data7``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ContasReceberDadosListDTO, ContasReceberDadosBaseDTO, ContasReceberDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `1` Aberto <br>`2` Pago<br>`3` Parcial<br>`4` Devolvido<br>`5` Cancelado<br>`6` Devolvido parcial<br>`7` Confirmado
        vencimento: Bling ``vencimento``; type ``date``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        id_transacao: Bling ``idTransacao``; type ``str | None``; opcional.
        link_qr_code_pix: Bling ``linkQRCodePix``; type ``str | None``; opcional.
        link_boleto: Bling ``linkBoleto``; type ``str | None``; opcional.
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        contato: Bling ``contato``; type ``ContasReceberContatoDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContasReceberFormaPagamentoDTO | None``; opcional.
        conta_contabil: Bling ``contaContabil``; type ``ContasReceberContaContabilDTO | None``; opcional.
        origem: Bling ``origem``; type ``ContasReceberDadosOrigemDTO | None``; opcional.
        saldo: Bling ``saldo``; type ``float``; obrigatório. É calculado subtraindo os valores dos recebimentos do valor da conta
        vencimento_original: Bling ``vencimentoOriginal``; type ``date``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. Número para controle interno da empresa
        competencia: Bling ``competencia``; type ``date | None``; opcional.
        historico: Bling ``historico``; type ``str | None``; opcional. Descriçao da conta para controle interno da empresa
        numero_banco: Bling ``numeroBanco``; type ``str``; obrigatório. Adicionado automaticamente com o número preenchido no cadastro do banco
        portador: Bling ``portador``; type ``ContasPortadorDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``ContasCategoriaDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``ContasReceberVendedorDTO | None``; opcional.
        borderos: Bling ``borderos``; type ``list[int]``; obrigatório. IDs de borderos relacionados à conta caso ela possua pagamentos
        ocorrencia: Bling ``ocorrencia``; type ``ContasReceberOcorrenciaUnicaDTO | ContasReceberOcorrenciaParceladaDTO | ContasReceberOcorrenciaDTO | ContasReceberOcorrenciaSemanalDTO | None``; opcional."""

    pass


class Data8(BlingModel):
    """OpenAPI schema ``Data8``.

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


class Data11(FormasPagamentosDadosBaseDTO, FormasPagamentosDadosDTO):
    """OpenAPI schema ``Data11``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: FormasPagamentosDadosBaseDTO, FormasPagamentosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        tipo_pagamento: Bling ``tipoPagamento``; type ``int``; obrigatório. `1` Dinheiro<br>`2` Cheque<br>`3` Cartão de Crédito<br>`4` Cartão de Débito<br>`5` Cartão da Loja (Private Label)<br>`10` Vale Alimentação<br>`11` Vale Refeição<br>`12` Vale Prese...
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativa<br>`1` Ativa<br>
        fixa: Bling ``fixa``; type ``bool | None``; opcional.
        padrao: Bling ``padrao``; type ``int | None``; opcional. `0` Não<br>`1` Padrão<br>`2` Padrão devolução
        finalidade: Bling ``finalidade``; type ``int``; obrigatório. `1` Pagamentos<br>`2` Recebimentos<br>`3` Pagamentos e Recebimentos<br>
        juros: Bling ``juros``; type ``float | None``; opcional. Valor em porcentagem, com até 2 casas decimais.
        multa: Bling ``multa``; type ``float | None``; opcional. Valor em porcentagem, com até 2 casas decimais.
        condicao: Bling ``condicao``; type ``str | None``; opcional. Condição de pagamento padrão.
        destino: Bling ``destino``; type ``int``; obrigatório. `1` Conta a receber/pagar<br>`2` Ficha financeira<br>`3` Caixa e bancos
        utiliza_dias_uteis: Bling ``utilizaDiasUteis``; type ``bool | None``; opcional. Indica se a forma de pagamento utiliza lançamentos em dias úteis.
        taxas: Bling ``taxas``; type ``FormasPagamentosTaxaDTO | None``; opcional.
        dados_cartao: Bling ``dadosCartao``; type ``FormasPagamentosDadosCartaoDTO | None``; opcional."""

    pass


class Data19(BasePostResponse, NotaFiscalResponsePOST):
    """OpenAPI schema ``Data19``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: BasePostResponse, NotaFiscalResponsePOST.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório.
        contato: Bling ``contato``; type ``Contato1``; obrigatório.
        alertas: Bling ``alertas``; type ``list[ErrorField] | None``; opcional."""

    alertas: list[ErrorField] | None = None


class Data22(NotasServicosDadosBaseDTO, NotasServicosDadosDTO):
    """OpenAPI schema ``Data22``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasServicosDadosBaseDTO, NotasServicosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``str | None``; opcional.
        numero_rps: Bling ``numeroRPS``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Pendente <br> `1` Emitida <br> `2` Disponível para consulta <br> `3` Cancelada
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``NotasServicosContatoBaseDTO | None``; opcional.
        link: Bling ``link``; type ``str | None``; opcional. Link para acesso e impressão da NFS-e.
        codigo_verificacao: Bling ``codigoVerificacao``; type ``str | None``; opcional."""

    pass


class Datum4(NotificacoesUlidsDTO, NotificacoesDadosBaseDTO):
    """OpenAPI schema ``Datum4``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotificacoesUlidsDTO, NotificacoesDadosBaseDTO.

    Fields:
        id: Bling ``id``; type ``str | None``; opcional. ULID da notificação.
        emitente: Bling ``emitente``; type ``str``; obrigatório. Nome do usuário que criou a notificação.
        modulo: Bling ``modulo``; type ``str``; obrigatório.
        descricao: Bling ``descricao``; type ``str``; obrigatório. Mensagem do corpo da notificação.
        titulo: Bling ``titulo``; type ``str``; obrigatório. Título no cabeçalho da notificação.
        fonte: Bling ``fonte``; type ``str | None``; opcional. Nome do orgão ou entidade em que se baseia a informação.
        link_ajuda: Bling ``linkAjuda``; type ``str | None``; opcional. Link para direcionar o cliente à mais informações.
        acao: Bling ``acao``; type ``str | None``; opcional. Ação executada na notificação.
        data_criacao: Bling ``dataCriacao``; type ``date | None``; opcional. Data de criação da notificação.
        data_envio: Bling ``dataEnvio``; type ``str``; obrigatório. Data de publicação da notificação.
        data_vigencia: Bling ``dataVigencia``; type ``date | None``; opcional. Data em que uma possível alteração informada entrará em vigor.
        data_acao: Bling ``dataAcao``; type ``date | None``; opcional. Data em que a ação foi realizada pelo usuário.
        data_leitura: Bling ``dataLeitura``; type ``str | None``; opcional. Data em que o usuário leu a notificação.
        data_alerta: Bling ``dataAlerta``; type ``date | None``; opcional. Data em que a notificação ficará com a cor amarela para alertar usuário.
        data_perigo: Bling ``dataPerigo``; type ``date | None``; opcional. Data em que a notificação ficará com a cor vermelha para alertar usuário.
        enquadramentos: Bling ``enquadramentos``; type ``list[NotificacoesEnquadramentosFiscaisDTO] | None``; opcional."""

    pass


class Data29(ProdutosFornecedoresDadosBaseDTO, ProdutosFornecedoresDadosDTO):
    """OpenAPI schema ``Data29``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ProdutosFornecedoresDadosBaseDTO, ProdutosFornecedoresDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Utilizado no GET.
        descricao: Bling ``descricao``; type ``str | None``; opcional. Descrição do produto no fornecedor.
        codigo: Bling ``codigo``; type ``str | None``; opcional. Código do produto no fornecedor.
        preco_custo: Bling ``precoCusto``; type ``float | None``; opcional. Valor de compra do produto com rateio de frete, descontos e impostos.
        preco_compra: Bling ``precoCompra``; type ``float | None``; opcional. Valor de compra do produto.
        padrao: Bling ``padrao``; type ``bool | None``; opcional. Indica se é o fornecedor padrão do produto.
        produto: Bling ``produto``; type ``ProdutosFornecedoresProdutoDTO | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``ProdutosFornecedoresFornecedorDTO | None``; opcional.
        garantia: Bling ``garantia``; type ``int | None``; opcional. Quantidade de meses de garantia."""

    pass


class Data31(ProdutosLojasDadosDTO, ProdutosLojasDadosBaseDTO):
    """OpenAPI schema ``Data31``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ProdutosLojasDadosDTO, ProdutosLojasDadosBaseDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        codigo: Bling ``codigo``; type ``str``; obrigatório. Código do produto na loja virtual
        preco: Bling ``preco``; type ``float | None``; opcional.
        preco_promocional: Bling ``precoPromocional``; type ``float | None``; opcional.
        produto: Bling ``produto``; type ``ProdutosLojasProdutoDTO``; obrigatório.
        loja: Bling ``loja``; type ``ProdutosLojasLojaDTO``; obrigatório.
        fornecedor_loja: Bling ``fornecedorLoja``; type ``ProdutosLojasFornecedorLojaDTO | None``; opcional.
        marca_loja: Bling ``marcaLoja``; type ``ProdutosLojasMarcaLojaDTO | None``; opcional.
        categorias_produtos: Bling ``categoriasProdutos``; type ``list[ProdutosLojasCategoriaDTO] | CategoriasProdutos | None``; opcional."""

    pass


class Data38(VendedoresDadosBaseDTO, VendedoresDadosDTO):
    """OpenAPI schema ``Data38``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: VendedoresDadosBaseDTO, VendedoresDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        desconto_limite: Bling ``descontoLimite``; type ``float | None``; opcional. Percentagem máxima para ceder como desconto, 0 para sem limite.
        loja: Bling ``loja``; type ``VendedoresLojaDTO | None``; opcional.
        contato: Bling ``contato``; type ``VendedoresContatoDTO``; obrigatório.
        comissoes: Bling ``comissoes``; type ``list[VendedoresComissaoDTO]``; obrigatório."""

    pass


class Data39(ContasDadosBaseDTO, ContasPagarDadosDTO):
    """OpenAPI schema ``Data39``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ContasDadosBaseDTO, ContasPagarDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `1` Aberto <br>`2` Pago<br>`3` Parcial<br>`4` Devolvido<br>`5` Cancelado<br>`6` Devolvido parcial<br>`7` Confirmado
        vencimento: Bling ``vencimento``; type ``date``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        contato: Bling ``contato``; type ``ContasContatoDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContasFormaPagamentoDTO | None``; opcional.
        saldo: Bling ``saldo``; type ``float | None``; opcional. Valor total subtraído dos valores dos recebimentos
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        vencimento_original: Bling ``vencimentoOriginal``; type ``date``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. Número para controle interno da empresa
        competencia: Bling ``competencia``; type ``date | None``; opcional.
        historico: Bling ``historico``; type ``str | None``; opcional. Descriçao da conta para controle interno da empresa
        numero_banco: Bling ``numeroBanco``; type ``str``; obrigatório. Adicionado automaticamente com o número preenchido no cadastro do banco
        portador: Bling ``portador``; type ``ContasPortadorDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``ContasCategoriaDTO | None``; opcional.
        borderos: Bling ``borderos``; type ``list[int]``; obrigatório.
        ocorrencia: Bling ``ocorrencia``; type ``ContasReceberOcorrenciaUnicaDTO | ContasReceberOcorrenciaParceladaDTO | ContasReceberOcorrenciaDTO | ContasReceberOcorrenciaSemanalDTO | None``; opcional."""

    pass


class Variaco(BlingModel):
    """OpenAPI schema ``Variaco``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str``; obrigatório.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``float | None``; opcional.
        tipo: Bling ``tipo``; type ``str``; obrigatório. Tipo do produto <br> `S` Serviço <br> `P` Produto <br> `N` Serviço 06 21 22
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação do produto <br> `A` Ativo <br> `I` Inativo
        formato: Bling ``formato``; type ``str``; obrigatório. Formato do produto <br> `S` Simples <br> `E` Com composição <br>
        descricao_curta: Bling ``descricaoCurta``; type ``str | None``; opcional.
        imagem_url: Bling ``imagemURL``; type ``str | None``; opcional. Link da primeira imagem de acordo com tipo de armazenamento definido.
        data_validade: Bling ``dataValidade``; type ``date | None``; opcional.
        unidade: Bling ``unidade``; type ``str | None``; opcional.
        peso_liquido: Bling ``pesoLiquido``; type ``float | None``; opcional. Peso líquido em KG
        peso_bruto: Bling ``pesoBruto``; type ``float | None``; opcional. Peso bruto em KG
        volumes: Bling ``volumes``; type ``int | None``; opcional.
        itens_por_caixa: Bling ``itensPorCaixa``; type ``float | None``; opcional.
        gtin: Bling ``gtin``; type ``str | None``; opcional. Código GTIN (GTIN-8, GTIN-12, GTIN-13 ou GTIN-14) do produto que está sendo comercializado
        gtin_embalagem: Bling ``gtinEmbalagem``; type ``str | None``; opcional. Código GTIN (GTIN-8, GTIN-12 ou GTIN-13) da menor unidade comercializada no varejo
        tipo_producao: Bling ``tipoProducao``; type ``str | None``; opcional. Tipo da produção <br> `P` Própria <br> `T` Terceiros
        condicao: Bling ``condicao``; type ``int | None``; opcional. Condição do produto <br> `0` Não especificado <br> `1` Novo <br> `2`Usado
        frete_gratis: Bling ``freteGratis``; type ``bool | None``; opcional. Frete grátis <br> Valor default: `false`
        marca: Bling ``marca``; type ``str | None``; opcional.
        descricao_complementar: Bling ``descricaoComplementar``; type ``str | None``; opcional.
        link_externo: Bling ``linkExterno``; type ``str | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        descricao_embalagem_discreta: Bling ``descricaoEmbalagemDiscreta``; type ``str | None``; opcional. Descrição discreta do produto para utilizar na declaração de conteúdo.
        categoria: Bling ``categoria``; type ``ProdutosCategoriaDTO | None``; opcional.
        estoque: Bling ``estoque``; type ``ProdutosEstoqueDTO | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``ProdutoFornecedorDTO | None``; opcional.
        action_estoque: Bling ``actionEstoque``; type ``str | None``; opcional. Ação de estoque ao transformar produto Simples em Variação <br> `Z` Irá zerar os saldos de estoque <br> `T` Transfere o estoque do produto pai para a primeira variação informada
        dimensoes: Bling ``dimensoes``; type ``ProdutosDimensoesDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``ProdutosTributacaoDTO | None``; opcional.
        midia: Bling ``midia``; type ``ProdutosMidiaDTO | None``; opcional.
        linha_produto: Bling ``linhaProduto``; type ``ProdutosLinhaProdutoDTO | None``; opcional.
        estrutura: Bling ``estrutura``; type ``ProdutosEstruturaDTO | None``; opcional.
        campos_customizados: Bling ``camposCustomizados``; type ``list[ProdutosCampoCustomizadoDTO] | None``; opcional.
        artigo_perigoso: Bling ``artigoPerigoso``; type ``bool | None``; opcional. Indica se o produto é um artigo perigoso conforme regulamentação ANAC. Quando habilitado, adiciona automaticamente o código de serviço 095 nas etiquetas de envio.
        variacao: Bling ``variacao``; type ``ProdutosVariacaoDTO``; obrigatório."""

    id: int | None = Field(default=None, examples=[123456789])
    nome: str = Field(..., examples=["Produto 1"], max_length=120)
    codigo: str | None = Field(default=None, examples=["CODE_123"])
    preco: float | None = Field(default=None, examples=[1])
    tipo: str = Field(..., examples=["P"])
    situacao: str = Field(..., examples=["A"])
    formato: str = Field(..., examples=["S"])
    descricao_curta: str | None = Field(
        default=None,
        validation_alias=AliasChoices("descricao_curta", "descricaoCurta"),
        examples=["Descrição curta"],
        serialization_alias="descricaoCurta",
    )
    imagem_url: str | None = Field(
        default=None,
        validation_alias=AliasChoices("imagem_url", "imagemURL"),
        examples=["https://www.bling.com.br/imagens/imagens-produtos/123456789.jpg"],
        serialization_alias="imagemURL",
    )
    data_validade: date | None = Field(
        default=None,
        validation_alias=AliasChoices("data_validade", "dataValidade"),
        examples=["2020-01-01"],
        serialization_alias="dataValidade",
    )
    unidade: str | None = Field(default=None, examples=["UN"])
    peso_liquido: float | None = Field(
        default=None,
        validation_alias=AliasChoices("peso_liquido", "pesoLiquido"),
        examples=[1],
        serialization_alias="pesoLiquido",
    )
    peso_bruto: float | None = Field(
        default=None,
        validation_alias=AliasChoices("peso_bruto", "pesoBruto"),
        examples=[1],
        serialization_alias="pesoBruto",
    )
    volumes: int | None = Field(default=None, examples=[1])
    itens_por_caixa: float | None = Field(
        default=None,
        validation_alias=AliasChoices("itens_por_caixa", "itensPorCaixa"),
        examples=["1.00"],
        serialization_alias="itensPorCaixa",
    )
    gtin: str | None = Field(default="", examples=["1234567890123"])
    gtin_embalagem: str | None = Field(
        default="",
        validation_alias=AliasChoices("gtin_embalagem", "gtinEmbalagem"),
        examples=["1234567890123"],
        serialization_alias="gtinEmbalagem",
    )
    tipo_producao: str | None = Field(
        default="P",
        validation_alias=AliasChoices("tipo_producao", "tipoProducao"),
        examples=["P"],
        serialization_alias="tipoProducao",
    )
    condicao: int | None = Field(default=0, examples=[0])
    frete_gratis: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("frete_gratis", "freteGratis"),
        examples=[False],
        serialization_alias="freteGratis",
    )
    marca: str | None = Field(default=None, examples=["Marca"])
    descricao_complementar: str | None = Field(
        default=None,
        validation_alias=AliasChoices("descricao_complementar", "descricaoComplementar"),
        examples=["Descrição complementar"],
        serialization_alias="descricaoComplementar",
    )
    link_externo: str | None = Field(
        default=None,
        validation_alias=AliasChoices("link_externo", "linkExterno"),
        examples=["https://www.google.com"],
        serialization_alias="linkExterno",
    )
    observacoes: str | None = Field(default=None, examples=["Observações"])
    descricao_embalagem_discreta: str | None = Field(
        default=None,
        validation_alias=AliasChoices("descricao_embalagem_discreta", "descricaoEmbalagemDiscreta"),
        examples=["Produto teste"],
        serialization_alias="descricaoEmbalagemDiscreta",
    )
    categoria: ProdutosCategoriaDTO | None = None
    estoque: ProdutosEstoqueDTO | None = None
    fornecedor: ProdutoFornecedorDTO | None = None
    action_estoque: str | None = Field(
        default=None,
        validation_alias=AliasChoices("action_estoque", "actionEstoque"),
        examples=[""],
        serialization_alias="actionEstoque",
    )
    dimensoes: ProdutosDimensoesDTO | None = None
    tributacao: ProdutosTributacaoDTO | None = None
    midia: ProdutosMidiaDTO | None = None
    linha_produto: ProdutosLinhaProdutoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("linha_produto", "linhaProduto"),
        serialization_alias="linhaProduto",
    )
    estrutura: ProdutosEstruturaDTO | None = None
    campos_customizados: list[ProdutosCampoCustomizadoDTO] | None = Field(
        default=None,
        validation_alias=AliasChoices("campos_customizados", "camposCustomizados"),
        serialization_alias="camposCustomizados",
    )
    artigo_perigoso: bool | None = Field(
        default=False,
        validation_alias=AliasChoices("artigo_perigoso", "artigoPerigoso"),
        examples=[False],
        serialization_alias="artigoPerigoso",
    )
    variacao: ProdutosVariacaoDTO


class Variaco1(BlingModel):
    """OpenAPI schema ``Variaco1``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str | None``; opcional.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``float | None``; opcional.
        tipo: Bling ``tipo``; type ``str | None``; opcional. Tipo do produto <br> `S` Serviço <br> `P` Produto <br> `N` Serviço 06 21 22
        situacao: Bling ``situacao``; type ``str | None``; opcional. Situação do produto <br> `A` Ativo <br> `I` Inativo
        formato: Bling ``formato``; type ``str | None``; opcional. Formato do produto <br> `S` Simples <br> `E` Com composição <br>
        descricao_curta: Bling ``descricaoCurta``; type ``str | None``; opcional.
        imagem_url: Bling ``imagemURL``; type ``str | None``; opcional. Link da primeira imagem de acordo com tipo de armazenamento definido.
        data_validade: Bling ``dataValidade``; type ``date | None``; opcional.
        unidade: Bling ``unidade``; type ``str | None``; opcional.
        peso_liquido: Bling ``pesoLiquido``; type ``float | None``; opcional. Peso líquido em KG
        peso_bruto: Bling ``pesoBruto``; type ``float | None``; opcional. Peso bruto em KG
        volumes: Bling ``volumes``; type ``int | None``; opcional.
        itens_por_caixa: Bling ``itensPorCaixa``; type ``float | None``; opcional.
        gtin: Bling ``gtin``; type ``str | None``; opcional. Código GTIN (GTIN-8, GTIN-12, GTIN-13 ou GTIN-14) do produto que está sendo comercializado
        gtin_embalagem: Bling ``gtinEmbalagem``; type ``str | None``; opcional. Código GTIN (GTIN-8, GTIN-12 ou GTIN-13) da menor unidade comercializada no varejo
        tipo_producao: Bling ``tipoProducao``; type ``str | None``; opcional. Tipo da produção <br> `P` Própria <br> `T` Terceiros
        condicao: Bling ``condicao``; type ``int | None``; opcional. Condição do produto <br> `0` Não especificado <br> `1` Novo <br> `2`Usado
        frete_gratis: Bling ``freteGratis``; type ``bool | None``; opcional. Frete grátis <br> Valor default: `false`
        marca: Bling ``marca``; type ``str | None``; opcional.
        descricao_complementar: Bling ``descricaoComplementar``; type ``str | None``; opcional.
        link_externo: Bling ``linkExterno``; type ``str | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        descricao_embalagem_discreta: Bling ``descricaoEmbalagemDiscreta``; type ``str | None``; opcional. Descrição discreta do produto para utilizar na declaração de conteúdo.
        categoria: Bling ``categoria``; type ``ProdutosCategoriaDTO | None``; opcional.
        estoque: Bling ``estoque``; type ``ProdutosEstoqueDTO | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``ProdutoFornecedorDTO | None``; opcional.
        action_estoque: Bling ``actionEstoque``; type ``str | None``; opcional. Ação de estoque ao transformar produto Simples em Variação <br> `Z` Irá zerar os saldos de estoque <br> `T` Transfere o estoque do produto pai para a primeira variação informada
        dimensoes: Bling ``dimensoes``; type ``ProdutosDimensoesDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``ProdutosTributacaoDTO | None``; opcional.
        midia: Bling ``midia``; type ``ProdutosMidiaDTO | None``; opcional.
        linha_produto: Bling ``linhaProduto``; type ``ProdutosLinhaProdutoDTO | None``; opcional.
        estrutura: Bling ``estrutura``; type ``ProdutosEstruturaDTO | None``; opcional.
        campos_customizados: Bling ``camposCustomizados``; type ``list[ProdutosCampoCustomizadoDTO] | None``; opcional.
        artigo_perigoso: Bling ``artigoPerigoso``; type ``bool | None``; opcional. Indica se o produto é um artigo perigoso conforme regulamentação ANAC. Quando habilitado, adiciona automaticamente o código de serviço 095 nas etiquetas de envio.
        variacao: Bling ``variacao``; type ``ProdutosVariacaoDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[123456789])
    nome: str | None = Field(default=None, examples=["Produto 1"], max_length=120)
    codigo: str | None = Field(default=None, examples=["CODE_123"])
    preco: float | None = Field(default=None, examples=[1])
    tipo: str | None = Field(default=None, examples=["P"])
    situacao: str | None = Field(default="A", examples=["A"])
    formato: str | None = Field(default=None, examples=["S"])
    descricao_curta: str | None = Field(
        default=None,
        validation_alias=AliasChoices("descricao_curta", "descricaoCurta"),
        examples=["Descrição curta"],
        serialization_alias="descricaoCurta",
    )
    imagem_url: str | None = Field(
        default=None,
        validation_alias=AliasChoices("imagem_url", "imagemURL"),
        examples=["https://www.bling.com.br/imagens/imagens-produtos/123456789.jpg"],
        serialization_alias="imagemURL",
    )
    data_validade: date | None = Field(
        default=None,
        validation_alias=AliasChoices("data_validade", "dataValidade"),
        examples=["2020-01-01"],
        serialization_alias="dataValidade",
    )
    unidade: str | None = Field(default=None, examples=["UN"])
    peso_liquido: float | None = Field(
        default=None,
        validation_alias=AliasChoices("peso_liquido", "pesoLiquido"),
        examples=[1],
        serialization_alias="pesoLiquido",
    )
    peso_bruto: float | None = Field(
        default=None,
        validation_alias=AliasChoices("peso_bruto", "pesoBruto"),
        examples=[1],
        serialization_alias="pesoBruto",
    )
    volumes: int | None = Field(default=None, examples=[1])
    itens_por_caixa: float | None = Field(
        default=None,
        validation_alias=AliasChoices("itens_por_caixa", "itensPorCaixa"),
        examples=["1.00"],
        serialization_alias="itensPorCaixa",
    )
    gtin: str | None = Field(default="", examples=["1234567890123"])
    gtin_embalagem: str | None = Field(
        default="",
        validation_alias=AliasChoices("gtin_embalagem", "gtinEmbalagem"),
        examples=["1234567890123"],
        serialization_alias="gtinEmbalagem",
    )
    tipo_producao: str | None = Field(
        default="P",
        validation_alias=AliasChoices("tipo_producao", "tipoProducao"),
        examples=["P"],
        serialization_alias="tipoProducao",
    )
    condicao: int | None = Field(default=0, examples=[0])
    frete_gratis: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("frete_gratis", "freteGratis"),
        examples=[False],
        serialization_alias="freteGratis",
    )
    marca: str | None = Field(default=None, examples=["Marca"])
    descricao_complementar: str | None = Field(
        default=None,
        validation_alias=AliasChoices("descricao_complementar", "descricaoComplementar"),
        examples=["Descrição complementar"],
        serialization_alias="descricaoComplementar",
    )
    link_externo: str | None = Field(
        default=None,
        validation_alias=AliasChoices("link_externo", "linkExterno"),
        examples=["https://www.google.com"],
        serialization_alias="linkExterno",
    )
    observacoes: str | None = Field(default=None, examples=["Observações"])
    descricao_embalagem_discreta: str | None = Field(
        default=None,
        validation_alias=AliasChoices("descricao_embalagem_discreta", "descricaoEmbalagemDiscreta"),
        examples=["Produto teste"],
        serialization_alias="descricaoEmbalagemDiscreta",
    )
    categoria: ProdutosCategoriaDTO | None = None
    estoque: ProdutosEstoqueDTO | None = None
    fornecedor: ProdutoFornecedorDTO | None = None
    action_estoque: str | None = Field(
        default=None,
        validation_alias=AliasChoices("action_estoque", "actionEstoque"),
        examples=[""],
        serialization_alias="actionEstoque",
    )
    dimensoes: ProdutosDimensoesDTO | None = None
    tributacao: ProdutosTributacaoDTO | None = None
    midia: ProdutosMidiaDTO | None = None
    linha_produto: ProdutosLinhaProdutoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("linha_produto", "linhaProduto"),
        serialization_alias="linhaProduto",
    )
    estrutura: ProdutosEstruturaDTO | None = None
    campos_customizados: list[ProdutosCampoCustomizadoDTO] | None = Field(
        default=None,
        validation_alias=AliasChoices("campos_customizados", "camposCustomizados"),
        serialization_alias="camposCustomizados",
    )
    artigo_perigoso: bool | None = Field(
        default=False,
        validation_alias=AliasChoices("artigo_perigoso", "artigoPerigoso"),
        examples=[False],
        serialization_alias="artigoPerigoso",
    )
    variacao: ProdutosVariacaoDTO | None = None


class Error(BlingModel):
    """OpenAPI schema ``Error``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        type: Bling ``type``; type ``str``; obrigatório.
        message: Bling ``message``; type ``str``; obrigatório.
        description: Bling ``description``; type ``str``; obrigatório.
        fields: Bling ``fields``; type ``list[ErrorField] | None``; opcional."""

    type: str = Field(..., examples=["VALIDATION_ERROR"])
    message: str = Field(..., examples=["Não foi possível salvar a venda"])
    description: str = Field(
        ..., examples=["A venda não pode ser salva, pois ocorreram problemas em sua validação."]
    )
    fields: list[ErrorField] | None = None


class Data14(NotasFiscaisDadosBaseDTO, NotasFiscaisDadosGetDTO):
    """OpenAPI schema ``Data14``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasFiscaisDadosBaseDTO, NotasFiscaisDadosGetDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        tipo: Bling ``tipo``; type ``int``; obrigatório. `0` Entrada <br> `1` Saída
        situacao: Bling ``situacao``; type ``int | None``; opcional. `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10...
        numero: Bling ``numero``; type ``str``; obrigatório.
        data_emissao: Bling ``dataEmissao``; type ``str | None``; opcional. Data e hora da emissão.
        data_operacao: Bling ``dataOperacao``; type ``str``; obrigatório. Data de saída/entrada de acordo com o tipo da nota.
        chave_acesso: Bling ``chaveAcesso``; type ``str | None``; opcional.
        contato: Bling ``contato``; type ``NotasFiscaisContatoDTO``; obrigatório.
        natureza_operacao: Bling ``naturezaOperacao``; type ``NotasFiscaisNaturezaOperacaoDTO``; obrigatório.
        loja: Bling ``loja``; type ``NotasFiscaisLojaDTO | None``; opcional.
        serie: Bling ``serie``; type ``int | None``; opcional.
        valor_nota: Bling ``valorNota``; type ``float | None``; opcional.
        valor_frete: Bling ``valorFrete``; type ``float | None``; opcional.
        finalidade: Bling ``finalidade``; type ``int | None``; opcional. `1` Normal <br>`2` Complementar <br>`3` Ajuste <br>`4` Devolução <br>`5` Crédito <br>`6` Débito
        tipo_nota: Bling ``tipoNota``; type ``str | None``; opcional. Presente quando finalidade for 5 (Crédito) ou 6 (Débito). <br><br>**Crédito (finalidade 5):** <br>`01` Multa e juros <br>`02` Apropriação de crédito presumido de IBS sobre o saldo...
        xml: Bling ``xml``; type ``str | None``; opcional.
        link_danfe: Bling ``linkDanfe``; type ``str | None``; opcional.
        link_pdf: Bling ``linkPDF``; type ``str | None``; opcional.
        optante_simples_nacional: Bling ``optanteSimplesNacional``; type ``bool | None``; opcional.
        numero_pedido_loja: Bling ``numeroPedidoLoja``; type ``str | None``; opcional.
        transporte: Bling ``transporte``; type ``NotasFiscaisTransporteGetDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``NotasFiscaisVendedorDTO | None``; opcional.
        itens: Bling ``itens``; type ``list[NotasFiscaisItemDTO] | None``; opcional.
        parcelas: Bling ``parcelas``; type ``list[NotasFiscaisParcelaDTO] | None``; opcional."""

    pass


class Data26(PedidosComprasDadosBaseDTO, PedidosComprasDadosDTO):
    """OpenAPI schema ``Data26``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: PedidosComprasDadosBaseDTO, PedidosComprasDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        data: Bling ``data``; type ``date | None``; opcional.
        data_prevista: Bling ``dataPrevista``; type ``date | None``; opcional.
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``PedidosComprasFornecedorDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``PedidosComprasSituacaoDTO | None``; opcional.
        ordem_compra: Bling ``ordemCompra``; type ``str | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        observacoes_internas: Bling ``observacoesInternas``; type ``str | None``; opcional.
        desconto: Bling ``desconto``; type ``PedidosComprasDescontoDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``PedidosComprasCategoriaDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``PedidosComprasTributacaoDTO | None``; opcional.
        transporte: Bling ``transporte``; type ``PedidosComprasTransporteDTO | None``; opcional.
        itens: Bling ``itens``; type ``list[PedidosComprasItemDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[PedidosComprasParcelaDTO] | None``; opcional."""

    pass


class Data28(BlingModel):
    """OpenAPI schema ``Data28``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        alertas: Bling ``alertas``; type ``list[Error] | None``; opcional."""

    alertas: list[Error] | None = None


class Data34(BasePostResponse, VendasResponsePOSTPUT):
    """OpenAPI schema ``Data34``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: BasePostResponse, VendasResponsePOSTPUT.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        alertas: Bling ``alertas``; type ``list[ErrorField] | None``; opcional.
        rastreamento: Bling ``rastreamento``; type ``dict[str, Any] | None``; opcional. Dados de rastreamento."""

    pass


class Data36(VendasDadosBaseDTO, VendasDadosDTO):
    """OpenAPI schema ``Data36``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: VendasDadosBaseDTO, VendasDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        numero_loja: Bling ``numeroLoja``; type ``str | None``; opcional.
        data: Bling ``data``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_saida: Bling ``dataSaida``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_prevista: Bling ``dataPrevista``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``VendasContatoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``VendasSituacaoDTO | None``; opcional.
        loja: Bling ``loja``; type ``VendasLojaDTO | None``; opcional.
        numero_pedido_compra: Bling ``numeroPedidoCompra``; type ``str | None``; opcional. Número da ordem de compra do pedido.
        outras_despesas: Bling ``outrasDespesas``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        observacoes_internas: Bling ``observacoesInternas``; type ``str | None``; opcional.
        desconto: Bling ``desconto``; type ``VendasDescontoDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``VendasCategoriaDTO | None``; opcional.
        nota_fiscal: Bling ``notaFiscal``; type ``VendasNotaFiscalDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``VendasTributacaoDTO | None``; opcional.
        itens: Bling ``itens``; type ``list[VendasItemDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[VendasParcelaDTO]``; obrigatório.
        transporte: Bling ``transporte``; type ``VendasTransporteDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``VendasVendedorDTO | None``; opcional.
        intermediador: Bling ``intermediador``; type ``VendasIntermediadorDTO | None``; opcional.
        taxas: Bling ``taxas``; type ``VendasTaxaDTO | None``; opcional."""

    pass


class Data37(BasePostResponse, VendasResponsePOSTPUT):
    """OpenAPI schema ``Data37``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: BasePostResponse, VendasResponsePOSTPUT.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        alertas: Bling ``alertas``; type ``list[ErrorField] | None``; opcional.
        rastreamento: Bling ``rastreamento``; type ``dict[str, Any] | None``; opcional. Dados de rastreamento."""

    pass


class ErrorResponse(BlingModel):
    """OpenAPI schema ``ErrorResponse``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        error: Bling ``error``; type ``Error | None``; opcional."""

    error: Error | None = None


class Data5(BlingModel):
    """OpenAPI schema ``Data5``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        alertas: Bling ``alertas``; type ``list[ErrorResponse] | None``; opcional."""

    alertas: list[ErrorResponse] | None = None


class Data10(ContratosDadosBaseDTO, ContratosDadosDTO):
    """OpenAPI schema ``Data10``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ContratosDadosBaseDTO, ContratosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        data: Bling ``data``; type ``date``; obrigatório. Data de criação do contrato.
        numero: Bling ``numero``; type ``str``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `0` Inativo<br>`1` Ativo<br>`2` Baixado<br>`3` Isento<br>`4` Em avaliação
        contato: Bling ``contato``; type ``ContratosContatoDTO``; obrigatório.
        data_fim: Bling ``dataFim``; type ``str``; obrigatório. Formato: YYYY-MM
        tipo_manutencao: Bling ``tipoManutencao``; type ``int``; obrigatório. `1` Valor <br> `2` Indexação
        emitir_ordem_servico: Bling ``emitirOrdemServico``; type ``bool``; obrigatório.
        observacoes: Bling ``observacoes``; type ``str``; obrigatório.
        vendedor: Bling ``vendedor``; type ``ContratosVendedorDTO``; obrigatório.
        categoria: Bling ``categoria``; type ``ContratosCategoriaDTO``; obrigatório.
        desconto: Bling ``desconto``; type ``ContratosDescontoDTO``; obrigatório.
        conta_contabil: Bling ``contaContabil``; type ``ContratosContaContabilDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContratosFormaPagamentoDTO``; obrigatório.
        nota_fiscal: Bling ``notaFiscal``; type ``ContratosNotaFiscalDTO | None``; opcional.
        cobranca: Bling ``cobranca``; type ``ContratosCobrancaDTO``; obrigatório."""

    pass


class Data24(BlingModel):
    """OpenAPI schema ``Data24``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        alertas: Bling ``alertas``; type ``list[ErrorResponse] | None``; opcional."""

    alertas: list[ErrorResponse] | None = None


class Alerta(ErrorResponse):
    """OpenAPI schema ``Alerta``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ErrorResponse.

    Fields:
        error: Bling ``error``; type ``Error | None``; opcional.
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])


__all__ = [
    "Alerta",
    "AnuncioLoja",
    "Atributo",
    "BasePostResponse",
    "Bordero",
    "Catalogo",
    "Categoria",
    "CategoriasProduto",
    "Contato",
    "Contato1",
    "Data",
    "Data1",
    "Data10",
    "Data11",
    "Data12",
    "Data13",
    "Data14",
    "Data16",
    "Data17",
    "Data19",
    "Data2",
    "Data20",
    "Data21",
    "Data22",
    "Data24",
    "Data25",
    "Data26",
    "Data28",
    "Data29",
    "Data30",
    "Data31",
    "Data33",
    "Data34",
    "Data35",
    "Data36",
    "Data37",
    "Data38",
    "Data39",
    "Data4",
    "Data5",
    "Data6",
    "Data7",
    "Data8",
    "Datum",
    "Datum1",
    "Datum2",
    "Datum3",
    "Datum4",
    "Datum6",
    "Datum7",
    "Datum8",
    "Datum9",
    "DeletedItem",
    "Error",
    "Error1",
    "ErrorField",
    "ErrorFieldCollection",
    "ErrorResponse",
    "FieldModel",
    "Frete",
    "Grade",
    "Imagen",
    "Integracao",
    "Loja",
    "LojaUnidadeNegocioDTO",
    "LotResponseDTO",
    "MercadoLivre",
    "Preco",
    "SavedItem",
    "UpdatedItem",
    "Variaco",
    "Variaco1",
    "Variations",
]
