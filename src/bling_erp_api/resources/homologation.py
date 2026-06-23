"""Homologação resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.models.generated.homologation import (
    HomologacaoProdutosGetResponse200,
    HomologacaoProdutosPostResponse201,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.serialization import to_json_object

_HOMOLOGACAO_HEADER: dict[str, str] = {"x-bling-homologacao": "true"}

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class HomologationResource(BaseResource):
    """Operações de homologação do Bling.

    Este recurso mapeia os endpoints ``/homologacao/produtos``. Os métodos canônicos usam
    português para acompanhar a documentação oficial. Aliases em inglês estão disponíveis
    para compatibilidade.
    """

    def obter(self) -> HomologacaoProdutosGetResponse200:
        """Obtém o produto da homologação.

        Endpoint: GET /homologacao/produtos

        Obtém o produto que será utilizado durante os demais passos da homologação, e
        inicia o processo de validação.

        Returns:
            Bling API response. Response schemas: 200: HomologacaoDadosBaseDTO
        """
        raw = self._get("/homologacao/produtos")
        return self._validate_response(HomologacaoProdutosGetResponse200, raw)

    def get(self) -> HomologacaoProdutosGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém o produto da homologação.

        Endpoint: GET /homologacao/produtos

        Obtém o produto que será utilizado durante os demais passos da homologação, e
        inicia o processo de validação.

        Returns:
            Bling API response. Response schemas: 200: HomologacaoDadosBaseDTO
        """
        return self.obter()

    def criar(self, dados: JsonObject) -> HomologacaoProdutosPostResponse201:
        """Cria o produto da homologação.

        Endpoint: POST /homologacao/produtos

        Cria o produto da homologação.

        Args:
            dados: Dados do produto da homologação (Bling: request body)

        Returns:
            Bling API response. Response schemas: 201: HomologacaoDadosBaseDTO, HomologacaoDadosDTO; 400: ErrorResponse
        """
        raw = self._post(
            "/homologacao/produtos",
            json=to_json_object(dados),
            headers=_HOMOLOGACAO_HEADER,
        )
        return self._validate_response(HomologacaoProdutosPostResponse201, raw)

    def create(self, data: JsonObject) -> HomologacaoProdutosPostResponse201:
        """Compatibility alias for ``criar()``.

        Cria o produto da homologação.

        Endpoint: POST /homologacao/produtos

        Cria o produto da homologação.

        Args:
            data: Dados do produto da homologação (Bling: request body)

        Returns:
            Bling API response. Response schemas: 201: HomologacaoDadosBaseDTO, HomologacaoDadosDTO; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(self, id_produto_homologacao: int, dados: JsonObject) -> JsonObject:
        """Altera o produto da homologação.

        Endpoint: PUT /homologacao/produtos/{idProdutoHomologacao}

        Altera o produto da homologação pelo ID.

        Args:
            id_produto_homologacao: ID do produto da homologação (Bling: ``idProdutoHomologacao``, integer, obrigatório)
            dados: Dados do produto da homologação (Bling: request body)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse
        """
        return self._put(
            f"/homologacao/produtos/{id_produto_homologacao}",
            json=to_json_object(dados),
            headers=_HOMOLOGACAO_HEADER,
        )

    def update(self, homologation_product_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera o produto da homologação.

        Endpoint: PUT /homologacao/produtos/{idProdutoHomologacao}

        Altera o produto da homologação pelo ID.

        Args:
            homologation_product_id: ID do produto da homologação (Bling: ``idProdutoHomologacao``, integer, obrigatório)
            data: Dados do produto da homologação (Bling: request body)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse
        """
        return self.alterar(id_produto_homologacao=homologation_product_id, dados=data)

    def remover(self, id_produto_homologacao: int) -> JsonObject:
        """Remove o produto da homologação.

        Endpoint: DELETE /homologacao/produtos/{idProdutoHomologacao}

        Remove o produto da homologação pelo ID.

        Args:
            id_produto_homologacao: ID do produto da homologação (Bling: ``idProdutoHomologacao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse
        """
        return self._delete(
            f"/homologacao/produtos/{id_produto_homologacao}",
            headers=_HOMOLOGACAO_HEADER,
        )

    def delete(self, homologation_product_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove o produto da homologação.

        Endpoint: DELETE /homologacao/produtos/{idProdutoHomologacao}

        Remove o produto da homologação pelo ID.

        Args:
            homologation_product_id: ID do produto da homologação (Bling: ``idProdutoHomologacao``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse
        """
        return self.remover(id_produto_homologacao=homologation_product_id)

    def alterar_situacao(self, id_produto_homologacao: int, situacao: str) -> JsonObject:
        """Altera a situação do produto da homologação.

        Endpoint: PATCH /homologacao/produtos/{idProdutoHomologacao}/situacoes

        Altera a situação do produto da homologação pelo ID.

        Args:
            id_produto_homologacao: ID do produto da homologação (Bling: ``idProdutoHomologacao``, integer, obrigatório)
            situacao: Nova situação (Bling: situacao, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse
        """
        return self._patch(
            f"/homologacao/produtos/{id_produto_homologacao}/situacoes",
            json=to_json_object({"situacao": situacao}),
            headers=_HOMOLOGACAO_HEADER,
        )

    def set_status(self, homologation_product_id: int, status: str) -> JsonObject:
        """Compatibility alias for ``alterar_situacao()``.

        Altera a situação do produto da homologação.

        Endpoint: PATCH /homologacao/produtos/{idProdutoHomologacao}/situacoes

        Altera a situação do produto da homologação pelo ID.

        Args:
            homologation_product_id: ID do produto da homologação (Bling: ``idProdutoHomologacao``, integer, obrigatório)
            status: Nova situação (Bling: situacao, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse
        """
        return self.alterar_situacao(
            id_produto_homologacao=homologation_product_id,
            situacao=status,
        )
