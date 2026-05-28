# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``produtos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Alerta, Data, Variaco, Variaco1
    from .estoques import EstoqueGetAllResponseDTO
    from .lotes_lancamentos import SaldoLoteDTO, SaldoSomaLotesDTO, SaldoSomaLotesTodosDepositosDTO
    from .produtos_fornecedores import ProdutoFornecedorDTO


class Produto(BlingModel):
    """OpenAPI schema ``Produto``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do produto."""

    id: int | None = Field(default=None, examples=[12345])


class Produto1(BlingModel):
    """OpenAPI schema ``Produto1``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID do produto pai"""

    id: int = Field(..., examples=[123])


class ProdutoUsuario(BlingModel):
    """OpenAPI schema ``ProdutoUsuario``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        ativo: Bling ``ativo``; type ``bool | None``; opcional."""

    id: int | None = Field(default=None, examples=[321])
    ativo: bool | None = Field(default=None, examples=[True])


class ProdutosAnexoDTO(BlingModel):
    """OpenAPI schema ``ProdutosAnexoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ProdutosAnexoVinculoDTO(BlingModel):
    """OpenAPI schema ``ProdutosAnexoVinculoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ProdutosCampoCustomizadoDTO(BlingModel):
    """OpenAPI schema ``ProdutosCampoCustomizadoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id_campo_customizado: Bling ``idCampoCustomizado``; type ``int``; obrigatório.
        id_vinculo: Bling ``idVinculo``; type ``int | None``; opcional.
        valor: Bling ``valor``; type ``str | None``; opcional.
        item: Bling ``item``; type ``str | None``; opcional."""

    id_campo_customizado: int = Field(
        ...,
        validation_alias=AliasChoices("id_campo_customizado", "idCampoCustomizado"),
        examples=[123456789],
        serialization_alias="idCampoCustomizado",
    )
    id_vinculo: int | None = Field(
        default=None,
        validation_alias=AliasChoices("id_vinculo", "idVinculo"),
        examples=["Utilize para atualizar o valor existente. Ex: 123456789"],
        serialization_alias="idVinculo",
    )
    valor: str | None = Field(default=None, examples=["256GB"])
    item: str | None = Field(default=None, examples=["Opção A"])


class ProdutosCategoriaDTO(BlingModel):
    """OpenAPI schema ``ProdutosCategoriaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[123456789])


class ProdutosComponenteProdutoDTO(BlingModel):
    """OpenAPI schema ``ProdutosComponenteProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[1])


class ProdutosDadosBaseDTOGetByID(BlingModel):
    """OpenAPI schema ``ProdutosDadosBaseDTOGetByID``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str``; obrigatório.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``float | None``; opcional.
        tipo: Bling ``tipo``; type ``str``; obrigatório. Tipo do produto <br> `S` Serviço <br> `P` Produto <br> `N` Serviço 06 21 22
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação do produto <br> `A` Ativo <br> `I` Inativo
        formato: Bling ``formato``; type ``str``; obrigatório. Formato do produto <br> `S` Simples <br> `V` Com variações <br> `E` Com composição <br>
        descricao_curta: Bling ``descricaoCurta``; type ``str | None``; opcional.
        imagem_url: Bling ``imagemURL``; type ``str | None``; opcional. Link da primeira imagem de acordo com tipo de armazenamento definido."""

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


class ProdutosDadosBaseDTOPatch(BlingModel):
    """OpenAPI schema ``ProdutosDadosBaseDTOPatch``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str | None``; opcional.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``float | None``; opcional.
        tipo: Bling ``tipo``; type ``str | None``; opcional. Tipo do produto <br> `S` Serviço <br> `P` Produto <br> `N` Serviço 06 21 22
        situacao: Bling ``situacao``; type ``str | None``; opcional. Situação do produto <br> `A` Ativo <br> `I` Inativo
        formato: Bling ``formato``; type ``str | None``; opcional. Formato do produto <br> `S` Simples <br> `V` Com variações <br> `E` Com composição <br>
        descricao_curta: Bling ``descricaoCurta``; type ``str | None``; opcional.
        imagem_url: Bling ``imagemURL``; type ``str | None``; opcional. Link da primeira imagem de acordo com tipo de armazenamento definido."""

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


class ProdutosDimensoesDTO(BlingModel):
    """OpenAPI schema ``ProdutosDimensoesDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        largura: Bling ``largura``; type ``float | None``; opcional.
        altura: Bling ``altura``; type ``float | None``; opcional.
        profundidade: Bling ``profundidade``; type ``float | None``; opcional.
        unidade_medida: Bling ``unidadeMedida``; type ``int | None``; opcional. `0` Metros <br> `1` Centímetros <br> `2` Milímetros"""

    largura: float | None = Field(default=None, examples=[1])
    altura: float | None = Field(default=None, examples=[1])
    profundidade: float | None = Field(default=None, examples=[1])
    unidade_medida: int | None = Field(
        default=None,
        validation_alias=AliasChoices("unidade_medida", "unidadeMedida"),
        examples=[1],
        serialization_alias="unidadeMedida",
    )


class ProdutosEstoqueDTO(BlingModel):
    """OpenAPI schema ``ProdutosEstoqueDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        minimo: Bling ``minimo``; type ``float | None``; opcional.
        maximo: Bling ``maximo``; type ``float | None``; opcional.
        crossdocking: Bling ``crossdocking``; type ``int | None``; opcional.
        localizacao: Bling ``localizacao``; type ``str | None``; opcional.
        saldo_virtual_total: Bling ``saldoVirtualTotal``; type ``float | None``; opcional. Saldo em estoque atual, considerando a reserva de estoque."""

    minimo: float | None = Field(default=None, examples=[1])
    maximo: float | None = Field(default=None, examples=[100])
    crossdocking: int | None = Field(default=None, examples=[1])
    localizacao: str | None = Field(default=None, examples=["14A"])
    saldo_virtual_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("saldo_virtual_total", "saldoVirtualTotal"),
        examples=["1.0"],
        serialization_alias="saldoVirtualTotal",
    )


class ProdutosGrupoProdutoDTO(BlingModel):
    """OpenAPI schema ``ProdutosGrupoProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[123456789])


class ProdutosImagemDTO(BlingModel):
    """OpenAPI schema ``ProdutosImagemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        link: Bling ``link``; type ``str``; obrigatório."""

    link: str = Field(..., examples=["https://shutterstock.com/lalala123"])


class ProdutosImagemInternaDTO(BlingModel):
    """OpenAPI schema ``ProdutosImagemInternaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        link: Bling ``link``; type ``str``; obrigatório.
        link_miniatura: Bling ``linkMiniatura``; type ``str``; obrigatório.
        validade: Bling ``validade``; type ``str``; obrigatório.
        ordem: Bling ``ordem``; type ``int``; obrigatório.
        anexo: Bling ``anexo``; type ``ProdutosAnexoDTO``; obrigatório.
        anexo_vinculo: Bling ``anexoVinculo``; type ``ProdutosAnexoVinculoDTO``; obrigatório."""

    link: str = Field(..., examples=["https://www.bling.com.br/imagens/miniatura.jpg"])
    link_miniatura: str = Field(
        ...,
        validation_alias=AliasChoices("link_miniatura", "linkMiniatura"),
        examples=["https://www.bling.com.br/imagens/miniatura.jpg"],
        serialization_alias="linkMiniatura",
    )
    validade: str = Field(..., examples=["2020-01-01 00:00:00"])
    ordem: int = Field(..., examples=[1])
    anexo: ProdutosAnexoDTO
    anexo_vinculo: ProdutosAnexoVinculoDTO = Field(
        ...,
        validation_alias=AliasChoices("anexo_vinculo", "anexoVinculo"),
        serialization_alias="anexoVinculo",
    )


class ProdutosImagensDTO(BlingModel):
    """OpenAPI schema ``ProdutosImagensDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        imagens_url: Bling ``imagensURL``; type ``list[ProdutosImagemDTO] | None``; opcional.
        externas: Bling ``externas``; type ``list[ProdutosImagemDTO] | None``; opcional.
        internas: Bling ``internas``; type ``list[ProdutosImagemInternaDTO] | None``; opcional."""

    imagens_url: list[ProdutosImagemDTO] | None = Field(
        default=None,
        validation_alias=AliasChoices("imagens_url", "imagensURL"),
        serialization_alias="imagensURL",
    )
    externas: list[ProdutosImagemDTO] | None = None
    internas: list[ProdutosImagemInternaDTO] | None = None


class ProdutosLinhaProdutoDTO(BlingModel):
    """OpenAPI schema ``ProdutosLinhaProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[1])


class ProdutosProdutoPaiDTO(BlingModel):
    """OpenAPI schema ``ProdutosProdutoPaiDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        clone_info: Bling ``cloneInfo``; type ``bool``; obrigatório."""

    id: int | None = Field(default=None, examples=[12345678])
    clone_info: bool = Field(
        ...,
        validation_alias=AliasChoices("clone_info", "cloneInfo"),
        examples=[True],
        serialization_alias="cloneInfo",
    )


class ProdutosTributacaoDTO(BlingModel):
    """OpenAPI schema ``ProdutosTributacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        origem: Bling ``origem``; type ``int | None``; opcional.
        n_fci: Bling ``nFCI``; type ``str | None``; opcional.
        ncm: Bling ``ncm``; type ``str | None``; opcional.
        cest: Bling ``cest``; type ``str | None``; opcional.
        codigo_lista_servicos: Bling ``codigoListaServicos``; type ``str | None``; opcional.
        sped_tipo_item: Bling ``spedTipoItem``; type ``str | None``; opcional.
        codigo_item: Bling ``codigoItem``; type ``str | None``; opcional.
        percentual_tributos: Bling ``percentualTributos``; type ``float | None``; opcional.
        valor_base_st_retencao: Bling ``valorBaseStRetencao``; type ``float | None``; opcional.
        valor_st_retencao: Bling ``valorStRetencao``; type ``float | None``; opcional.
        valor_icms_substituto: Bling ``valorICMSSubstituto``; type ``float | None``; opcional.
        codigo_excecao_tipi: Bling ``codigoExcecaoTipi``; type ``str | None``; opcional.
        classe_enquadramento_ipi: Bling ``classeEnquadramentoIpi``; type ``str | None``; opcional.
        valor_ipi_fixo: Bling ``valorIpiFixo``; type ``float | None``; opcional.
        codigo_selo_ipi: Bling ``codigoSeloIpi``; type ``str | None``; opcional.
        valor_pis_fixo: Bling ``valorPisFixo``; type ``float | None``; opcional.
        valor_cofins_fixo: Bling ``valorCofinsFixo``; type ``float | None``; opcional.
        codigo_anp: Bling ``codigoANP``; type ``str | None``; opcional.
        descricao_anp: Bling ``descricaoANP``; type ``str | None``; opcional.
        percentual_glp: Bling ``percentualGLP``; type ``float | None``; opcional.
        percentual_gas_nacional: Bling ``percentualGasNacional``; type ``float | None``; opcional.
        percentual_gas_importado: Bling ``percentualGasImportado``; type ``float | None``; opcional.
        valor_partida: Bling ``valorPartida``; type ``float | None``; opcional.
        tipo_armamento: Bling ``tipoArmamento``; type ``int | None``; opcional. Preencher quando a classificação do produto for armamento <br> `0` Uso permitido <br> `1` Uso restrito
        descricao_completa_armamento: Bling ``descricaoCompletaArmamento``; type ``str | None``; opcional.
        dados_adicionais: Bling ``dadosAdicionais``; type ``str | None``; opcional. Campo referente a tag infAdProd da nota fiscal
        grupo_produto: Bling ``grupoProduto``; type ``ProdutosGrupoProdutoDTO | None``; opcional."""

    origem: int | None = Field(default=None, examples=[0])
    n_fci: str | None = Field(
        default=None,
        validation_alias=AliasChoices("n_fci", "nFCI"),
        examples=[""],
        serialization_alias="nFCI",
    )
    ncm: str | None = Field(default=None, examples=[""])
    cest: str | None = Field(default=None, examples=[""])
    codigo_lista_servicos: str | None = Field(
        default=None,
        validation_alias=AliasChoices("codigo_lista_servicos", "codigoListaServicos"),
        examples=[""],
        serialization_alias="codigoListaServicos",
    )
    sped_tipo_item: str | None = Field(
        default=None,
        validation_alias=AliasChoices("sped_tipo_item", "spedTipoItem"),
        examples=[""],
        serialization_alias="spedTipoItem",
    )
    codigo_item: str | None = Field(
        default=None,
        validation_alias=AliasChoices("codigo_item", "codigoItem"),
        examples=[""],
        serialization_alias="codigoItem",
    )
    percentual_tributos: float | None = Field(
        default=None,
        validation_alias=AliasChoices("percentual_tributos", "percentualTributos"),
        examples=[0],
        serialization_alias="percentualTributos",
    )
    valor_base_st_retencao: float | None = Field(
        default=None,
        validation_alias=AliasChoices("valor_base_st_retencao", "valorBaseStRetencao"),
        examples=[0],
        serialization_alias="valorBaseStRetencao",
    )
    valor_st_retencao: float | None = Field(
        default=None,
        validation_alias=AliasChoices("valor_st_retencao", "valorStRetencao"),
        examples=[0],
        serialization_alias="valorStRetencao",
    )
    valor_icms_substituto: float | None = Field(
        default=None,
        validation_alias=AliasChoices("valor_icms_substituto", "valorICMSSubstituto"),
        examples=[0],
        serialization_alias="valorICMSSubstituto",
    )
    codigo_excecao_tipi: str | None = Field(
        default=None,
        validation_alias=AliasChoices("codigo_excecao_tipi", "codigoExcecaoTipi"),
        examples=[""],
        serialization_alias="codigoExcecaoTipi",
    )
    classe_enquadramento_ipi: str | None = Field(
        default=None,
        validation_alias=AliasChoices("classe_enquadramento_ipi", "classeEnquadramentoIpi"),
        examples=[""],
        serialization_alias="classeEnquadramentoIpi",
    )
    valor_ipi_fixo: float | None = Field(
        default=None,
        validation_alias=AliasChoices("valor_ipi_fixo", "valorIpiFixo"),
        examples=[0],
        serialization_alias="valorIpiFixo",
    )
    codigo_selo_ipi: str | None = Field(
        default=None,
        validation_alias=AliasChoices("codigo_selo_ipi", "codigoSeloIpi"),
        examples=[""],
        serialization_alias="codigoSeloIpi",
    )
    valor_pis_fixo: float | None = Field(
        default=None,
        validation_alias=AliasChoices("valor_pis_fixo", "valorPisFixo"),
        examples=[0],
        serialization_alias="valorPisFixo",
    )
    valor_cofins_fixo: float | None = Field(
        default=None,
        validation_alias=AliasChoices("valor_cofins_fixo", "valorCofinsFixo"),
        examples=[0],
        serialization_alias="valorCofinsFixo",
    )
    codigo_anp: str | None = Field(
        default=None,
        validation_alias=AliasChoices("codigo_anp", "codigoANP"),
        examples=[""],
        serialization_alias="codigoANP",
    )
    descricao_anp: str | None = Field(
        default=None,
        validation_alias=AliasChoices("descricao_anp", "descricaoANP"),
        examples=[""],
        serialization_alias="descricaoANP",
    )
    percentual_glp: float | None = Field(
        default=None,
        validation_alias=AliasChoices("percentual_glp", "percentualGLP"),
        examples=[0],
        serialization_alias="percentualGLP",
    )
    percentual_gas_nacional: float | None = Field(
        default=None,
        validation_alias=AliasChoices("percentual_gas_nacional", "percentualGasNacional"),
        examples=[0],
        serialization_alias="percentualGasNacional",
    )
    percentual_gas_importado: float | None = Field(
        default=None,
        validation_alias=AliasChoices("percentual_gas_importado", "percentualGasImportado"),
        examples=[0],
        serialization_alias="percentualGasImportado",
    )
    valor_partida: float | None = Field(
        default=None,
        validation_alias=AliasChoices("valor_partida", "valorPartida"),
        examples=[0],
        serialization_alias="valorPartida",
    )
    tipo_armamento: int | None = Field(
        default=0,
        validation_alias=AliasChoices("tipo_armamento", "tipoArmamento"),
        examples=[0],
        serialization_alias="tipoArmamento",
    )
    descricao_completa_armamento: str | None = Field(
        default=None,
        validation_alias=AliasChoices("descricao_completa_armamento", "descricaoCompletaArmamento"),
        examples=[""],
        serialization_alias="descricaoCompletaArmamento",
    )
    dados_adicionais: str | None = Field(
        default=None,
        validation_alias=AliasChoices("dados_adicionais", "dadosAdicionais"),
        examples=[""],
        serialization_alias="dadosAdicionais",
    )
    grupo_produto: ProdutosGrupoProdutoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("grupo_produto", "grupoProduto"),
        serialization_alias="grupoProduto",
    )


class ProdutosVariacaoDTO(BlingModel):
    """OpenAPI schema ``ProdutosVariacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str``; obrigatório.
        ordem: Bling ``ordem``; type ``int``; obrigatório.
        produto_pai: Bling ``produtoPai``; type ``ProdutosProdutoPaiDTO``; obrigatório."""

    nome: str = Field(..., examples=["Tamanho:G;Cor:Verde"])
    ordem: int = Field(..., examples=[1])
    produto_pai: ProdutosProdutoPaiDTO = Field(
        ...,
        validation_alias=AliasChoices("produto_pai", "produtoPai"),
        serialization_alias="produtoPai",
    )


class ProdutosVideoDTO(BlingModel):
    """OpenAPI schema ``ProdutosVideoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        url: Bling ``url``; type ``str``; obrigatório."""

    url: str = Field(..., examples=["https://www.youtube.com/watch?v=1"])


class ProdutosResponsePOSTPUT(BlingModel):
    """OpenAPI schema ``ProdutosResponsePOSTPUT``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data | None``; opcional."""

    data: Data | None = None


class ProdutosIdProdutoLotesIdLoteDepositosIdDepositoSaldoGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosIdProdutoLotesIdLoteDepositosIdDepositoSaldoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``SaldoLoteDTO | None``; opcional."""

    data: SaldoLoteDTO | None = None


class ProdutosIdProdutoLotesDepositosIdDepositoSaldoGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosIdProdutoLotesDepositosIdDepositoSaldoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[SaldoLoteDTO] | None``; opcional."""

    data: list[SaldoLoteDTO] | None = None


class ProdutosIdProdutoLotesDepositosIdDepositoSaldoSomaGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosIdProdutoLotesDepositosIdDepositoSaldoSomaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[SaldoSomaLotesDTO] | None``; opcional."""

    data: list[SaldoSomaLotesDTO] | None = None


class ProdutosIdProdutoLotesSaldoSomaGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosIdProdutoLotesSaldoSomaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``SaldoSomaLotesTodosDepositosDTO | None``; opcional."""

    data: SaldoSomaLotesTodosDepositosDTO | None = None


class ProdutosIdProdutoSituacoesPatchRequest(BlingModel):
    """OpenAPI schema ``ProdutosIdProdutoSituacoesPatchRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        situacao: Bling ``situacao``; type ``str | None``; opcional. Situação do produto <br> `A` Ativo <br> `I` Inativo <br> 'E' Excluído"""

    situacao: str | None = Field(default=None, examples=["A"])


class ProdutosSituacoesPostRequest(BlingModel):
    """OpenAPI schema ``ProdutosSituacoesPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        ids_produtos: Bling ``idsProdutos``; type ``list[int] | None``; opcional.
        situacao: Bling ``situacao``; type ``str | None``; opcional. Situação do produto <br> `A` Ativo <br> `I` Inativo <br> 'E' Excluído"""

    ids_produtos: list[int] | None = Field(
        default=None,
        validation_alias=AliasChoices("ids_produtos", "idsProdutos"),
        serialization_alias="idsProdutos",
    )
    situacao: str | None = Field(default=None, examples=["A"])


class ProdutosComponenteDTO(BlingModel):
    """OpenAPI schema ``ProdutosComponenteDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        produto: Bling ``produto``; type ``ProdutosComponenteProdutoDTO``; obrigatório.
        quantidade: Bling ``quantidade``; type ``float``; obrigatório."""

    produto: ProdutosComponenteProdutoDTO
    quantidade: float = Field(..., examples=[2.1])


class ProdutosDadosBaseDTO(BlingModel):
    """OpenAPI schema ``ProdutosDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        id_produto_pai: Bling ``idProdutoPai``; type ``int | None``; opcional. ID do produto pai, caso seja uma variação.
        nome: Bling ``nome``; type ``str``; obrigatório.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``float | None``; opcional.
        preco_custo: Bling ``precoCusto``; type ``float | None``; opcional. Preço de custo do fornecedor padrão do produto.
        estoque: Bling ``estoque``; type ``EstoqueGetAllResponseDTO | None``; opcional.
        tipo: Bling ``tipo``; type ``str``; obrigatório. Tipo do produto <br> `S` Serviço <br> `P` Produto <br> `N` Serviço 06 21 22
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação do produto <br> `A` Ativo <br> `I` Inativo
        formato: Bling ``formato``; type ``str``; obrigatório. Formato do produto <br> `S` Simples <br> `V` Com variações <br> `E` Com composição <br>
        descricao_curta: Bling ``descricaoCurta``; type ``str | None``; opcional.
        imagem_url: Bling ``imagemURL``; type ``str | None``; opcional. Link da primeira imagem de acordo com tipo de armazenamento definido."""

    id: int | None = Field(default=None, examples=[123456789])
    id_produto_pai: int | None = Field(
        default=None,
        validation_alias=AliasChoices("id_produto_pai", "idProdutoPai"),
        examples=[123456789],
        serialization_alias="idProdutoPai",
    )
    nome: str = Field(..., examples=["Produto 1"], max_length=120)
    codigo: str | None = Field(default=None, examples=["CODE_123"])
    preco: float | None = Field(default=None, examples=[1])
    preco_custo: float | None = Field(
        default=None,
        validation_alias=AliasChoices("preco_custo", "precoCusto"),
        examples=[1],
        serialization_alias="precoCusto",
    )
    estoque: EstoqueGetAllResponseDTO | None = None
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


class ProdutosDadosVariacaoDTO(BlingModel):
    """OpenAPI schema ``ProdutosDadosVariacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        variacao: Bling ``variacao``; type ``ProdutosVariacaoDTO``; obrigatório."""

    variacao: ProdutosVariacaoDTO


class ProdutosDadosVariacaoDTOPatch(BlingModel):
    """OpenAPI schema ``ProdutosDadosVariacaoDTOPatch``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        variacao: Bling ``variacao``; type ``ProdutosVariacaoDTO | None``; opcional."""

    variacao: ProdutosVariacaoDTO | None = None


class ProdutosEstruturaDTO(BlingModel):
    """OpenAPI schema ``ProdutosEstruturaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        tipo_estoque: Bling ``tipoEstoque``; type ``str``; obrigatório. `F` Físico<br> `V` Virtual
        lancamento_estoque: Bling ``lancamentoEstoque``; type ``str``; obrigatório. `A` Produto e Componente<br> `M` Componente<br> `P` Produto
        componentes: Bling ``componentes``; type ``list[ProdutosComponenteDTO]``; obrigatório."""

    tipo_estoque: str = Field(
        ...,
        validation_alias=AliasChoices("tipo_estoque", "tipoEstoque"),
        examples=["F"],
        serialization_alias="tipoEstoque",
    )
    lancamento_estoque: str = Field(
        ...,
        validation_alias=AliasChoices("lancamento_estoque", "lancamentoEstoque"),
        examples=["A"],
        serialization_alias="lancamentoEstoque",
    )
    componentes: list[ProdutosComponenteDTO]


class ProdutosMidiaDTO(BlingModel):
    """OpenAPI schema ``ProdutosMidiaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        video: Bling ``video``; type ``ProdutosVideoDTO``; obrigatório.
        imagens: Bling ``imagens``; type ``ProdutosImagensDTO``; obrigatório."""

    video: ProdutosVideoDTO
    imagens: ProdutosImagensDTO


class ProdutosGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ProdutosDadosBaseDTO] | None``; opcional."""

    data: list[ProdutosDadosBaseDTO] | None = None


class ProdutosDados(BlingModel):
    """OpenAPI schema ``ProdutosDados``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
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
        artigo_perigoso: Bling ``artigoPerigoso``; type ``bool | None``; opcional. Indica se o produto é um artigo perigoso conforme regulamentação ANAC. Quando habilitado, adiciona automaticamente o código de serviço 095 nas etiquetas de envio."""

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


class ProdutosDadosPatch(BlingModel):
    """OpenAPI schema ``ProdutosDadosPatch``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
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
        artigo_perigoso: Bling ``artigoPerigoso``; type ``bool | None``; opcional. Indica se o produto é um artigo perigoso conforme regulamentação ANAC. Quando habilitado, adiciona automaticamente o código de serviço 095 nas etiquetas de envio."""

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


class ProdutosDadosPatchDTO(ProdutosDadosBaseDTOPatch, ProdutosDadosPatch):
    """OpenAPI schema ``ProdutosDadosPatchDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ProdutosDadosBaseDTOPatch, ProdutosDadosPatch.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str | None``; opcional.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``float | None``; opcional.
        tipo: Bling ``tipo``; type ``str | None``; opcional. Tipo do produto <br> `S` Serviço <br> `P` Produto <br> `N` Serviço 06 21 22
        situacao: Bling ``situacao``; type ``str | None``; opcional. Situação do produto <br> `A` Ativo <br> `I` Inativo
        formato: Bling ``formato``; type ``str | None``; opcional. Formato do produto <br> `S` Simples <br> `V` Com variações <br> `E` Com composição <br>
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
        variacoes: Bling ``variacoes``; type ``list[Variaco1] | None``; opcional."""

    variacoes: list[Variaco1] | None = None


class ProdutosDadosDTO(ProdutosDadosBaseDTOGetByID, ProdutosDados):
    """OpenAPI schema ``ProdutosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ProdutosDadosBaseDTOGetByID, ProdutosDados.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str``; obrigatório.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``float | None``; opcional.
        tipo: Bling ``tipo``; type ``str``; obrigatório. Tipo do produto <br> `S` Serviço <br> `P` Produto <br> `N` Serviço 06 21 22
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação do produto <br> `A` Ativo <br> `I` Inativo
        formato: Bling ``formato``; type ``str``; obrigatório. Formato do produto <br> `S` Simples <br> `V` Com variações <br> `E` Com composição <br>
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
        variacoes: Bling ``variacoes``; type ``list[Variaco] | None``; opcional."""

    variacoes: list[Variaco] | None = None


class ProdutosIdProdutoGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosIdProdutoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``ProdutosDadosDTO | None``; opcional."""

    data: ProdutosDadosDTO | None = None


class ProdutosAlertasResponse(BlingModel):
    """OpenAPI schema ``ProdutosAlertasResponse``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        alertas: Bling ``alertas``; type ``list[Alerta] | None``; opcional."""

    alertas: list[Alerta] | None = None


class ProdutosDeleteResponse200(BlingModel):
    """OpenAPI schema ``ProdutosDeleteResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``ProdutosAlertasResponse | None``; opcional."""

    data: ProdutosAlertasResponse | None = None


class ProdutosSituacoesPostResponse200(BlingModel):
    """OpenAPI schema ``ProdutosSituacoesPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``ProdutosAlertasResponse | None``; opcional."""

    data: ProdutosAlertasResponse | None = None


__all__ = [
    "Produto",
    "Produto1",
    "ProdutoUsuario",
    "ProdutosAlertasResponse",
    "ProdutosAnexoDTO",
    "ProdutosAnexoVinculoDTO",
    "ProdutosCampoCustomizadoDTO",
    "ProdutosCategoriaDTO",
    "ProdutosComponenteDTO",
    "ProdutosComponenteProdutoDTO",
    "ProdutosDados",
    "ProdutosDadosBaseDTO",
    "ProdutosDadosBaseDTOGetByID",
    "ProdutosDadosBaseDTOPatch",
    "ProdutosDadosDTO",
    "ProdutosDadosPatch",
    "ProdutosDadosPatchDTO",
    "ProdutosDadosVariacaoDTO",
    "ProdutosDadosVariacaoDTOPatch",
    "ProdutosDeleteResponse200",
    "ProdutosDimensoesDTO",
    "ProdutosEstoqueDTO",
    "ProdutosEstruturaDTO",
    "ProdutosGetResponse200",
    "ProdutosGrupoProdutoDTO",
    "ProdutosIdProdutoGetResponse200",
    "ProdutosIdProdutoLotesDepositosIdDepositoSaldoGetResponse200",
    "ProdutosIdProdutoLotesDepositosIdDepositoSaldoSomaGetResponse200",
    "ProdutosIdProdutoLotesIdLoteDepositosIdDepositoSaldoGetResponse200",
    "ProdutosIdProdutoLotesSaldoSomaGetResponse200",
    "ProdutosIdProdutoSituacoesPatchRequest",
    "ProdutosImagemDTO",
    "ProdutosImagemInternaDTO",
    "ProdutosImagensDTO",
    "ProdutosLinhaProdutoDTO",
    "ProdutosMidiaDTO",
    "ProdutosProdutoPaiDTO",
    "ProdutosResponsePOSTPUT",
    "ProdutosSituacoesPostRequest",
    "ProdutosSituacoesPostResponse200",
    "ProdutosTributacaoDTO",
    "ProdutosVariacaoDTO",
    "ProdutosVideoDTO",
]
