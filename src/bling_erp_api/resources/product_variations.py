"""Produtos — Variações resource."""

from __future__ import annotations

from bling_erp_api.models.generated.product_variations import (
    ProdutosVariacoesAtributosGerarCombinacoesPostResponse200,
    ProdutosVariacoesCombinacaoDadosDTO,
    ProdutosVariacoesDadosAtributoDTO,
    ProdutosVariacoesIdProdutoPaiAtributosPatchResponse200,
    ProdutosVariacoesIdProdutoPaiGetResponse200,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.serialization import to_json_object


class ProductVariationsResource(BaseResource):
    """Resource para variações de produtos do Bling.

    Mapeia os endpoints ``/produtos/variacoes`` para listagem de variações,
    geração de combinações e alteração de atributos. Métodos canônicos em
    pt-BR; aliases em inglês disponíveis para compatibilidade.
    """

    def gerar_combinacoes(
        self, dados: ProdutosVariacoesCombinacaoDadosDTO
    ) -> ProdutosVariacoesAtributosGerarCombinacoesPostResponse200:
        """Retorna o produto pai com combinações de novas variações.

        Endpoint: POST /produtos/variacoes/atributos/gerar-combinacoes

        Ação responsável por retornar o produto pai com combinação de novas variações a partir dos atributos. Esta ação não persistirá os dados.

        Args:
            dados: Dados da combinação de variações (Bling: ``ProdutosVariacoesCombinacaoDadosDTO``, obrigatório)

        Request body schema: ProdutosVariacoesCombinacaoDadosDTO

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosDTO; 400: ErrorResponse
        """
        raw = self._post(
            "/produtos/variacoes/atributos/gerar-combinacoes",
            json=to_json_object(dados),
        )
        return self._validate_response(
            ProdutosVariacoesAtributosGerarCombinacoesPostResponse200, raw
        )

    def listar(self, id_produto_pai: int) -> ProdutosVariacoesIdProdutoPaiGetResponse200:
        """Obtém o produto e variações.

        Endpoint: GET /produtos/variacoes/{idProdutoPai}

        Obtém o produto e variações pelo ID do produto pai.

        Args:
            id_produto_pai: ID do produto pai (Bling: ``idProdutoPai``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosDTO; 404: ErrorResponse
        """
        raw = self._get(f"/produtos/variacoes/{id_produto_pai}")
        return self._validate_response(ProdutosVariacoesIdProdutoPaiGetResponse200, raw)

    def alterar_atributo(
        self,
        id_produto_pai: int,
        dados: ProdutosVariacoesDadosAtributoDTO,
    ) -> ProdutosVariacoesIdProdutoPaiAtributosPatchResponse200:
        """Altera o nome do atributo nas variações.

        Endpoint: PATCH /produtos/variacoes/{idProdutoPai}/atributos

        Altera o nome do atributo nas variações de um produto pai.

        Args:
            id_produto_pai: ID do produto pai (Bling: ``idProdutoPai``, integer, obrigatório)
            dados: Dados do atributo a ser alterado (Bling: ``ProdutosVariacoesDadosAtributoDTO``, object, obrigatório)

        Request body schema: ProdutosVariacoesDadosAtributoDTO

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse; 400: ErrorResponse
        """
        raw = self._patch(
            f"/produtos/variacoes/{id_produto_pai}/atributos",
            json=to_json_object(dados),
        )
        return self._validate_response(ProdutosVariacoesIdProdutoPaiAtributosPatchResponse200, raw)
