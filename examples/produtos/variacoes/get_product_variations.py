"""Example: Product Variations (Variações) Operations.

Demonstrates operations on product variations (variações de produtos) through
the Bling API.

Endpoints:
    - GET /produtos/variacoes/{idProdutoPai}
    - POST /produtos/variacoes/atributos/gerar-combinacoes
    - PATCH /produtos/variacoes/{idProdutoPai}/atributos

Docs:
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Varia%C3%A7%C3%B5es/get_produtos_variacoes__idProdutoPai_
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Varia%C3%A7%C3%B5es/post_produtos_variacoes_atributos_gerar-combinacoes
    - https://developer.bling.com.br/referencia#/Produtos%20-%20Varia%C3%A7%C3%B5es/patch_produtos_variacoes__idProdutoPai__atributos

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_variations import (
    ProdutosVariacoesCombinacaoDadosDTO,  # noqa: TC001 — runtime import for write ops
    ProdutosVariacoesDadosAtributoDTO,  # noqa: TC001 — runtime import for write ops
)

if TYPE_CHECKING:
    from bling_erp_api.models.generated.product_variations import (
        ProdutosVariacoesAtributosGerarCombinacoesPostResponse200,
        ProdutosVariacoesIdProdutoPaiAtributosPatchResponse200,
        ProdutosVariacoesIdProdutoPaiGetResponse200,
    )

## ---------------------------------------------------------------------------
## LIST VARIATIONS
## ---------------------------------------------------------------------------


def listar_variacoes(
    id_produto_pai: int,
) -> ProdutosVariacoesIdProdutoPaiGetResponse200:
    """Lista variações de um produto pai."""
    with BlingClient.from_env() as client:
        return client.produtos_variacoes.listar(
            id_produto_pai=id_produto_pai,
        )


## ---------------------------------------------------------------------------
## GENERATE COMBINATIONS
## ---------------------------------------------------------------------------


def gerar_combinacoes(
    dados: ProdutosVariacoesCombinacaoDadosDTO,
) -> ProdutosVariacoesAtributosGerarCombinacoesPostResponse200:
    """Gera combinações de variações a partir de atributos."""
    with BlingClient.from_env() as client:
        return client.produtos_variacoes.gerar_combinacoes(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE VARIATION ATTRIBUTES
## ---------------------------------------------------------------------------


def alterar_atributo_variacao(
    id_produto_pai: int,
    dados: ProdutosVariacoesDadosAtributoDTO,
) -> ProdutosVariacoesIdProdutoPaiAtributosPatchResponse200:
    """Altera atributos de variação de um produto pai."""
    with BlingClient.from_env() as client:
        return client.produtos_variacoes.alterar_atributo(
            id_produto_pai=id_produto_pai,
            dados=dados,
        )


def main() -> None:
    """Demonstrate product variation operations."""
    id_produto_pai = 123456789  # Exemplo — substitua pelo ID real.

    # Read operations
    print(listar_variacoes(id_produto_pai).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Write operations (commented out)
    # combinacao = ProdutosVariacoesCombinacaoDadosDTO(
    #     id_produto_pai=id_produto_pai,
    #     atributos=[{"nome": "Cor", "valor": "Azul"}],
    # )
    # print(
    #     gerar_combinacoes(combinacao).model_dump_json(indent=2, by_alias=True)
    # )
    # time.sleep(1)
    # atributo = ProdutosVariacoesDadosAtributoDTO(
    #     atributos=[{"nome": "Tamanho", "valor": "G"}],
    # )
    # print(
    #     alterar_atributo_variacao(id_produto_pai, atributo).model_dump_json(
    #         indent=2, by_alias=True
    #     )
    # )
    # time.sleep(1)


if __name__ == "__main__":
    main()
