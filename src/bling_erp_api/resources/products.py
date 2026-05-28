"""Produtos resource."""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING, Literal

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from bling_erp_api.models.generated.products import (
        ProdutosDadosDTO,
        ProdutosDadosPatchDTO,
    )
    from bling_erp_api.types import JsonObject, QueryParams

type DateFilter = date | datetime | str
type ProductListCriterion = Literal[1, 2, 3, 4, 5]
type ProductListType = Literal["T", "P", "S", "E", "PS", "C", "V"]
type ProductStockBalanceFilter = Literal[0, 1, 2]
type ProductStatus = Literal["A", "I", "E"]


class ProductsResource(BaseResource):
    """Operações de produtos do Bling.

    Este recurso mapeia os endpoints ``/produtos``. Os métodos canônicos usam
    português para acompanhar a documentação oficial; os métodos em inglês
    continuam disponíveis como aliases de compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        criterio: ProductListCriterion | None = None,
        tipo: ProductListType | None = None,
        id_componente: int | None = None,
        data_inclusao_inicial: DateFilter | None = None,
        data_inclusao_final: DateFilter | None = None,
        data_alteracao_inicial: DateFilter | None = None,
        data_alteracao_final: DateFilter | None = None,
        id_categoria: int | None = None,
        id_loja: int | None = None,
        nome: str | None = None,
        ids_produtos: Sequence[int] | None = None,
        codigos: Sequence[str] | None = None,
        gtins: Sequence[str] | None = None,
        filtro_saldo_estoque: ProductStockBalanceFilter | None = None,
        filtro_saldo_estoque_deposito: int | None = None,
    ) -> JsonObject:
        """Lista produtos.

        Args:
            pagina: Parâmetro ``pagina`` do Bling.
            limite: Parâmetro ``limite`` do Bling.
            criterio: Critério de listagem, enviado como ``criterio``.
            tipo: Tipo de produto, enviado como ``tipo``.
            id_componente: Componente para composições, enviado como ``idComponente``.
            data_inclusao_inicial: Data/hora inicial de inclusão.
            data_inclusao_final: Data/hora final de inclusão.
            data_alteracao_inicial: Data/hora inicial de alteração.
            data_alteracao_final: Data/hora final de alteração.
            id_categoria: Categoria, enviada como ``idCategoria``.
            id_loja: Loja, enviada como ``idLoja``.
            nome: Nome do produto, enviado como ``nome``.
            ids_produtos: IDs, enviados como ``idsProdutos[]``.
            codigos: SKUs, enviados como ``codigos[]``.
            gtins: GTINs/EANs, enviados como ``gtins[]``.
            filtro_saldo_estoque: Filtro de saldo, enviado como ``filtroSaldoEstoque``.
            filtro_saldo_estoque_deposito: Depósito para filtro de saldo.
        """
        return self._get(
            "/produtos",
            params=_product_list_params(
                pagina=pagina,
                limite=limite,
                criterio=criterio,
                tipo=tipo,
                id_componente=id_componente,
                data_inclusao_inicial=data_inclusao_inicial,
                data_inclusao_final=data_inclusao_final,
                data_alteracao_inicial=data_alteracao_inicial,
                data_alteracao_final=data_alteracao_final,
                id_categoria=id_categoria,
                id_loja=id_loja,
                nome=nome,
                ids_produtos=ids_produtos,
                codigos=codigos,
                gtins=gtins,
                filtro_saldo_estoque=filtro_saldo_estoque,
                filtro_saldo_estoque_deposito=filtro_saldo_estoque_deposito,
            ),
        )

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        limit: int = 100,
        criterion: ProductListCriterion | None = None,
        product_type: ProductListType | None = None,
        component_id: int | None = None,
        created_start: DateFilter | None = None,
        created_end: DateFilter | None = None,
        updated_start: DateFilter | None = None,
        updated_end: DateFilter | None = None,
        category_id: int | None = None,
        store_id: int | None = None,
        name: str | None = None,
        product_ids: Sequence[int] | None = None,
        codes: Sequence[str] | None = None,
        gtins: Sequence[str] | None = None,
        stock_balance_filter: ProductStockBalanceFilter | None = None,
        stock_balance_deposit_id: int | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Obtém produtos

        Endpoint: GET /produtos

        Obtém produtos paginados.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            criterion: Critério de listagem <br> `1` Últimos incluídos <br> `2` Ativos <br> `3` Inativos <br> `4` Excluídos <br> `5` Todos (Bling: ``criterio``, integer, opcional)
            product_type: `T` Todos <br> `P` Produtos <br> `S` Serviços <br> `E` Composições <br> `PS` Produtos simples <br> `C` Com variações <br> `V` Variações (Bling: ``tipo``, string, opcional)
            component_id: ID do componente. Utilizado quando o filtro **tipo** for `E`. (Bling: ``idComponente``, integer, opcional)
            created_start: Data de inclusão inicial (Bling: ``dataInclusaoInicial``, string, opcional)
            created_end: Data de inclusão final (Bling: ``dataInclusaoFinal``, string, opcional)
            updated_start: Data de alteração inicial (Bling: ``dataAlteracaoInicial``, string, opcional)
            updated_end: Data de alteração final (Bling: ``dataAlteracaoFinal``, string, opcional)
            category_id: ID da categoria do produto (Bling: ``idCategoria``, integer, opcional)
            store_id: ID da loja (Bling: ``idLoja``, integer, opcional)
            name: Nome do produto (Bling: ``nome``, string, opcional)
            product_ids: IDs dos produtos (Bling: ``idsProdutos[]``, array, opcional)
            codes: Códigos (SKU) dos produtos (Bling: ``codigos[]``, array, opcional)
            gtins: GTINs/EANs dos produtos (Bling: ``gtins[]``, array, opcional)
            stock_balance_filter: Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> `2` negativo (Bling: ``filtroSaldoEstoque``, integer, opcional)
            stock_balance_deposit_id: ID do depósito para considerar no filtro de saldo em estoque. Se omitido, considera todos os depósitos. (Bling: ``filtroSaldoEstoqueDeposito``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosBaseDTO
        """
        return self.listar(
            pagina=page,
            limite=limit,
            criterio=criterion,
            tipo=product_type,
            id_componente=component_id,
            data_inclusao_inicial=created_start,
            data_inclusao_final=created_end,
            data_alteracao_inicial=updated_start,
            data_alteracao_final=updated_end,
            id_categoria=category_id,
            id_loja=store_id,
            nome=name,
            ids_produtos=product_ids,
            codigos=codes,
            gtins=gtins,
            filtro_saldo_estoque=stock_balance_filter,
            filtro_saldo_estoque_deposito=stock_balance_deposit_id,
        )

    def iterar(self, *, pagina: int = 1, limite: int = 100) -> Iterator[JsonObject]:
        """Itera pelos produtos página a página."""
        return self._iterate("/produtos", page=pagina, limit=limite)

    def iterate(self, *, page: int = 1, limit: int = 100) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``."""
        return self.iterar(pagina=page, limite=limit)

    def obter(self, id_produto: int) -> JsonObject:
        """Obtém um produto.

        Endpoint: GET /produtos/{idProduto}

        Obtém um produto pelo ID.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosDTO; 403: ErrorResponse; 404: ErrorResponse
        """
        return self._get(f"/produtos/{id_produto}")

    def get(self, product_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém um produto

        Endpoint: GET /produtos/{idProduto}

        Obtém um produto pelo ID.

        Args:
            product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosDadosDTO; 403: ErrorResponse; 404: ErrorResponse
        """
        return self.obter(product_id)

    def criar(self, dados: ProdutosDadosDTO) -> JsonObject:
        """Cria um produto.

        Endpoint: POST /produtos

        Cria um produto.

        Request body schema: ProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 201: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        return self._post("/produtos", json=to_json_object(dados))

    def create(self, data: ProdutosDadosDTO) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria um produto

        Endpoint: POST /produtos

        Cria um produto.

        Request body schema: ProdutosDadosDTO
        {
            "id": 123456789,
            "nome": "Produto 1",
            "codigo": "CODE_123",
            "preco": 1,
            "tipo": "P",
            "situacao": "A",
            "formato": "S",
            "descricaoCurta": "Descrição curta",
            "dataValidade": "2020-01-01",
            "unidade": "UN",
            "pesoLiquido": 1,
            "pesoBruto": 1,
            "volumes": 1,
            "itensPorCaixa": 1,
            "gtin": "1234567890123",
            "gtinEmbalagem": "1234567890123",
            "tipoProducao": "P",
            "condicao": 0,
            "freteGratis": false,
            "marca": "Marca",
            "descricaoComplementar": "Descrição complementar",
            "linkExterno": "https://www.google.com",
            "observacoes": "Observações",
            "descricaoEmbalagemDiscreta": "Produto teste",
            "categoria": {
                "id": 123456789
            },
            "estoque": {
                "minimo": 1,
                "maximo": 100,
                "crossdocking": 1,
                "localizacao": "14A"
            },
            "actionEstoque": "",
            "dimensoes": {
                "largura": 1,
                "altura": 1,
                "profundidade": 1,
                "unidadeMedida": 1
            },
            "tributacao": {
                "origem": 0,
                "nFCI": "",
                "ncm": "",
                "cest": "",
                "codigoListaServicos": "",
                "spedTipoItem": "",
                "codigoItem": "",
                "percentualTributos": 0,
                "valorBaseStRetencao": 0,
                "valorStRetencao": 0,
                "valorICMSSubstituto": 0,
                "codigoExcecaoTipi": "",
                "classeEnquadramentoIpi": "",
                "valorIpiFixo": 0,
                "codigoSeloIpi": "",
                "valorPisFixo": 0,
                "valorCofinsFixo": 0,
                "codigoANP": "",
                "descricaoANP": "",
                "percentualGLP": 0,
                "percentualGasNacional": 0,
                "percentualGasImportado": 0,
                "valorPartida": 0,
                "tipoArmamento": 0,
                "descricaoCompletaArmamento": "",
                "dadosAdicionais": "",
                "grupoProduto": {
                "id": 123456789
                }
            },
            "midia": {
                "video": {
                "url": "https://www.youtube.com/watch?v=1"
                },
                "imagens": {
                "imagensURL": [
                    {
                    "link": "https://shutterstock.com/lalala123"
                    }
                ]
                }
            },
            "linhaProduto": {
                "id": 1
            },
            "estrutura": {
                "tipoEstoque": "F",
                "lancamentoEstoque": "A",
                "componentes": [
                {
                    "produto": {
                    "id": 1
                    },
                    "quantidade": 2.1
                }
                ]
            },
            "camposCustomizados": [
                {
                "idCampoCustomizado": 123456789,
                "idVinculo": "Utilize para atualizar o valor existente. Ex: 123456789",
                "valor": "256GB",
                "item": "Opção A"
                }
            ],
            "artigoPerigoso": false,
            "variacoes": [
                {
                "id": 123456789,
                "nome": "Produto 1",
                "codigo": "CODE_123",
                "preco": 1,
                "tipo": "P",
                "situacao": "A",
                "formato": "S",
                "descricaoCurta": "Descrição curta",
                "dataValidade": "2020-01-01",
                "unidade": "UN",
                "pesoLiquido": 1,
                "pesoBruto": 1,
                "volumes": 1,
                "itensPorCaixa": 1,
                "gtin": "1234567890123",
                "gtinEmbalagem": "1234567890123",
                "tipoProducao": "P",
                "condicao": 0,
                "freteGratis": false,
                "marca": "Marca",
                "descricaoComplementar": "Descrição complementar",
                "linkExterno": "https://www.google.com",
                "observacoes": "Observações",
                "descricaoEmbalagemDiscreta": "Produto teste",
                "categoria": {
                    "id": 123456789
                },
                "estoque": {
                    "minimo": 1,
                    "maximo": 100,
                    "crossdocking": 1,
                    "localizacao": "14A"
                },
                "actionEstoque": "",
                "dimensoes": {
                    "largura": 1,
                    "altura": 1,
                    "profundidade": 1,
                    "unidadeMedida": 1
                },
                "tributacao": {
                    "origem": 0,
                    "nFCI": "",
                    "ncm": "",
                    "cest": "",
                    "codigoListaServicos": "",
                    "spedTipoItem": "",
                    "codigoItem": "",
                    "percentualTributos": 0,
                    "valorBaseStRetencao": 0,
                    "valorStRetencao": 0,
                    "valorICMSSubstituto": 0,
                    "codigoExcecaoTipi": "",
                    "classeEnquadramentoIpi": "",
                    "valorIpiFixo": 0,
                    "codigoSeloIpi": "",
                    "valorPisFixo": 0,
                    "valorCofinsFixo": 0,
                    "codigoANP": "",
                    "descricaoANP": "",
                    "percentualGLP": 0,
                    "percentualGasNacional": 0,
                    "percentualGasImportado": 0,
                    "valorPartida": 0,
                    "tipoArmamento": 0,
                    "descricaoCompletaArmamento": "",
                    "dadosAdicionais": "",
                    "grupoProduto": {
                    "id": 123456789
                    }
                },
                "midia": {
                    "video": {
                    "url": "https://www.youtube.com/watch?v=1"
                    },
                    "imagens": {
                    "imagensURL": [
                        {
                        "link": "https://shutterstock.com/lalala123"
                        }
                    ]
                    }
                },
                "linhaProduto": {
                    "id": 1
                },
                "estrutura": {
                    "tipoEstoque": "F",
                    "lancamentoEstoque": "A",
                    "componentes": [
                    {
                        "produto": {
                        "id": 1
                        },
                        "quantidade": 2.1
                    }
                    ]
                },
                "camposCustomizados": [
                    {
                    "idCampoCustomizado": 123456789,
                    "idVinculo": "Utilize para atualizar o valor existente. Ex: 123456789",
                    "valor": "256GB",
                    "item": "Opção A"
                    }
                ],
                "artigoPerigoso": false,
                "variacao": {
                    "nome": "Tamanho:G;Cor:Verde",
                    "ordem": 1,
                    "produtoPai": {
                    "cloneInfo": true
                    }
                }
                }
            ]
            }

        Returns:
            Bling API response. Response schemas: 201: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        return self.criar(data)

    def alterar(self, id_produto: int, dados: ProdutosDadosDTO) -> JsonObject:
        """Altera um produto.

        Endpoint: PUT /produtos/{idProduto}

        Altera um produto pelo ID.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            dados: Dados do produto para atualização.

        Request body schema: ProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 200: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        return self._put(f"/produtos/{id_produto}", json=to_json_object(dados))

    def update(self, product_id: int, data: ProdutosDadosDTO) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera um produto

        Endpoint: PUT /produtos/{idProduto}

        Altera um produto pelo ID.

        Args:
            product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            data: Dados do produto para atualização.

        Request body schema: ProdutosDadosDTO

        Returns:
            Bling API response. Response schemas: 200: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        return self.alterar(product_id, data)

    def alterar_parcialmente(self, id_produto: int, dados: ProdutosDadosPatchDTO) -> JsonObject:
        """Altera parcialmente um produto.

        Endpoint: PATCH /produtos/{idProduto}

        Altera parcialmente um produto pelo ID. Somente os campos informados terão o valor alterado.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            dados: Dados parciais do produto para atualização.

        Request body schema: ProdutosDadosPatchDTO

        Returns:
            Bling API response. Response schemas: 200: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        return self._patch(f"/produtos/{id_produto}", json=to_json_object(dados))

    def patch(self, product_id: int, data: ProdutosDadosPatchDTO) -> JsonObject:
        """Compatibility alias for ``alterar_parcialmente()``.

        Altera parcialmente um produto

        Endpoint: PATCH /produtos/{idProduto}

        Altera parcialmente um produto pelo ID. Somente os campos informados terão o valor alterado.

        Args:
            product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            data: Dados parciais do produto para atualização.

        Request body schema: ProdutosDadosPatchDTO

        Returns:
            Bling API response. Response schemas: 200: ProdutosResponse_POST_PUT; 400: ErrorResponse; 403: ErrorResponse
        """
        return self.alterar_parcialmente(product_id, data)

    def remover(self, id_produto: int) -> JsonObject:
        """Remove um produto.

        Endpoint: DELETE /produtos/{idProduto}

        Remove um produto pelo ID.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 404: ErrorResponse
        """
        return self._delete(f"/produtos/{id_produto}")

    def delete(self, product_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove um produto

        Endpoint: DELETE /produtos/{idProduto}

        Remove um produto pelo ID.

        Args:
            product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 404: ErrorResponse
        """
        return self.remover(product_id)

    def remover_varios(self, ids_produtos: Sequence[int]) -> JsonObject:
        """Remove múltiplos produtos.

        Endpoint: DELETE /produtos

        Remove múltiplos produtos pelos IDs.

        Args:
            ids_produtos: IDs dos produtos (Bling: ``idsProdutos[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosAlertasResponse; 400: ErrorResponse
        """
        return self._delete("/produtos", params={"idsProdutos[]": list(ids_produtos)})

    def delete_many(self, product_ids: Sequence[int]) -> JsonObject:
        """Compatibility alias for ``remover_varios()``.

        Remove múltiplos produtos

        Endpoint: DELETE /produtos

        Remove múltiplos produtos pelos IDs.

        Args:
            product_ids: IDs dos produtos (Bling: ``idsProdutos[]``, array, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: ProdutosAlertasResponse; 400: ErrorResponse
        """
        return self.remover_varios(product_ids)

    def alterar_situacao(self, id_produto: int, situacao: ProductStatus) -> JsonObject:
        """Altera a situação de um produto.

        Endpoint: PATCH /produtos/{idProduto}/situacoes

        Altera a situação de um produto pelo ID.

        Args:
            id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            situacao: Situação do produto.

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(f"/produtos/{id_produto}/situacoes", json={"situacao": situacao})

    def update_status(self, product_id: int, status: ProductStatus) -> JsonObject:
        """Compatibility alias for ``alterar_situacao()``.

        Altera a situação de um produto

        Endpoint: PATCH /produtos/{idProduto}/situacoes

        Altera a situação de um produto pelo ID.

        Args:
            product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)
            status: Situação do produto.

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar_situacao(product_id, status)

    def alterar_situacao_varios(
        self, ids_produtos: Sequence[int], situacao: ProductStatus
    ) -> JsonObject:
        """Altera a situação de múltiplos produtos.

        Endpoint: POST /produtos/situacoes

        Altera a situação de múltiplos produtos pelos IDs.

        Returns:
            Bling API response. Response schemas: 200: ProdutosAlertasResponse; 400: ErrorResponse
        """
        return self._post(
            "/produtos/situacoes",
            json={"idsProdutos": list(ids_produtos), "situacao": situacao},
        )

    def update_many_status(self, product_ids: Sequence[int], status: ProductStatus) -> JsonObject:
        """Compatibility alias for ``alterar_situacao_varios()``.

        Altera a situação de múltiplos produtos

        Endpoint: POST /produtos/situacoes

        Altera a situação de múltiplos produtos pelos IDs.

        Returns:
            Bling API response. Response schemas: 200: ProdutosAlertasResponse; 400: ErrorResponse
        """
        return self.alterar_situacao_varios(product_ids, status)


def _product_list_params(  # noqa: PLR0913
    *,
    pagina: int,
    limite: int,
    criterio: ProductListCriterion | None,
    tipo: ProductListType | None,
    id_componente: int | None,
    data_inclusao_inicial: DateFilter | None,
    data_inclusao_final: DateFilter | None,
    data_alteracao_inicial: DateFilter | None,
    data_alteracao_final: DateFilter | None,
    id_categoria: int | None,
    id_loja: int | None,
    nome: str | None,
    ids_produtos: Sequence[int] | None,
    codigos: Sequence[str] | None,
    gtins: Sequence[str] | None,
    filtro_saldo_estoque: ProductStockBalanceFilter | None,
    filtro_saldo_estoque_deposito: int | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "criterio": criterio,
            "tipo": tipo,
            "idComponente": id_componente,
            "dataInclusaoInicial": _format_datetime_filter(data_inclusao_inicial),
            "dataInclusaoFinal": _format_datetime_filter(data_inclusao_final),
            "dataAlteracaoInicial": _format_datetime_filter(data_alteracao_inicial),
            "dataAlteracaoFinal": _format_datetime_filter(data_alteracao_final),
            "idCategoria": id_categoria,
            "idLoja": id_loja,
            "nome": nome,
            "idsProdutos[]": list(ids_produtos) if ids_produtos is not None else None,
            "codigos[]": list(codigos) if codigos is not None else None,
            "gtins[]": list(gtins) if gtins is not None else None,
            "filtroSaldoEstoque": filtro_saldo_estoque,
            "filtroSaldoEstoqueDeposito": filtro_saldo_estoque_deposito,
        }
    )


def _format_datetime_filter(value: DateFilter | None) -> str | None:
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return value.isoformat()
