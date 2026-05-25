"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PRODUCT_OPERATIONS: dict[str, OperationContract] = {
    "remover_varios": OperationContract.model_validate(
        {
            "action": "RemoverMultiplos",
            "description": "Remove múltiplos produtos pelos IDs.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "IDs dos produtos",
                    "location": "query",
                    "name": "idsProdutos[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_produtos",
                }
            ],
            "path": "/produtos",
            "request_schema_refs": [],
            "resource": "Produtos",
            "response_schema_refs": {"200": ["ProdutosAlertasResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "remover_varios",
            "summary": "Remove múltiplos produtos",
        }
    ),
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém produtos paginados.",
            "method": "GET",
            "parameters": [
                {
                    "description": "N° da página da listagem",
                    "location": "query",
                    "name": "pagina",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "pagina",
                },
                {
                    "description": "Quantidade de registros que devem ser exibidos por página",
                    "location": "query",
                    "name": "limite",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "limite",
                },
                {
                    "description": "Critério de listagem <br> `1` Últimos incluídos <br> `2` Ativos "
                    "<br> `3` Inativos <br> `4` Excluídos <br> `5` Todos",
                    "location": "query",
                    "name": "criterio",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "criterio",
                },
                {
                    "description": "`T` Todos <br> `P` Produtos <br> `S` Serviços <br> `E` "
                    "Composições <br> `PS` Produtos simples <br> `C` Com variações "
                    "<br> `V` Variações",
                    "location": "query",
                    "name": "tipo",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo",
                },
                {
                    "description": "ID do componente. Utilizado quando o filtro **tipo** for `E`.",
                    "location": "query",
                    "name": "idComponente",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_componente",
                },
                {
                    "description": "Data de inclusão inicial",
                    "location": "query",
                    "name": "dataInclusaoInicial",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_inclusao_inicial",
                },
                {
                    "description": "Data de inclusão final",
                    "location": "query",
                    "name": "dataInclusaoFinal",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_inclusao_final",
                },
                {
                    "description": "Data de alteração inicial",
                    "location": "query",
                    "name": "dataAlteracaoInicial",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_alteracao_inicial",
                },
                {
                    "description": "Data de alteração final",
                    "location": "query",
                    "name": "dataAlteracaoFinal",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_alteracao_final",
                },
                {
                    "description": "ID da categoria do produto",
                    "location": "query",
                    "name": "idCategoria",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria",
                },
                {
                    "description": "ID da loja",
                    "location": "query",
                    "name": "idLoja",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_loja",
                },
                {
                    "description": "Nome do produto",
                    "location": "query",
                    "name": "nome",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "nome",
                },
                {
                    "description": "IDs dos produtos",
                    "location": "query",
                    "name": "idsProdutos[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_produtos",
                },
                {
                    "description": "Códigos (SKU) dos produtos",
                    "location": "query",
                    "name": "codigos[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "codigos",
                },
                {
                    "description": "GTINs/EANs dos produtos",
                    "location": "query",
                    "name": "gtins[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "gtins",
                },
                {
                    "description": "Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> "
                    "`2` negativo",
                    "location": "query",
                    "name": "filtroSaldoEstoque",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "filtro_saldo_estoque",
                },
                {
                    "description": "ID do depósito para considerar no filtro de saldo em estoque. Se "
                    "omitido, considera todos os depósitos.",
                    "location": "query",
                    "name": "filtroSaldoEstoqueDeposito",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "filtro_saldo_estoque_deposito",
                },
            ],
            "path": "/produtos",
            "request_schema_refs": [],
            "resource": "Produtos",
            "response_schema_refs": {"200": ["ProdutosDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém produtos",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria um produto.",
            "method": "POST",
            "parameters": [],
            "path": "/produtos",
            "request_schema_refs": ["ProdutosDadosDTO"],
            "resource": "Produtos",
            "response_schema_refs": {
                "201": ["ProdutosResponse_POST_PUT"],
                "400": ["ErrorResponse"],
                "403": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria um produto",
        }
    ),
    "alterar_situacao_varios": OperationContract.model_validate(
        {
            "action": "AlterarSituacaoMultiplos",
            "description": "Altera a situação de múltiplos produtos pelos IDs.",
            "method": "POST",
            "parameters": [],
            "path": "/produtos/situacoes",
            "request_schema_refs": [],
            "resource": "Produtos",
            "response_schema_refs": {"200": ["ProdutosAlertasResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao_varios",
            "summary": "Altera a situação de múltiplos produtos",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove um produto pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do produto",
                    "location": "path",
                    "name": "idProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto",
                }
            ],
            "path": "/produtos/{idProduto}",
            "request_schema_refs": [],
            "resource": "Produtos",
            "response_schema_refs": {"404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove um produto",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um produto pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do produto",
                    "location": "path",
                    "name": "idProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto",
                }
            ],
            "path": "/produtos/{idProduto}",
            "request_schema_refs": [],
            "resource": "Produtos",
            "response_schema_refs": {
                "200": ["ProdutosDadosDTO"],
                "403": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um produto",
        }
    ),
    "alterar_parcialmente": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera parcialmente um produto pelo ID. Somente os campos informados terão o "
            "valor alterado.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID do produto",
                    "location": "path",
                    "name": "idProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto",
                }
            ],
            "path": "/produtos/{idProduto}",
            "request_schema_refs": ["ProdutosDadosPatchDTO"],
            "resource": "Produtos",
            "response_schema_refs": {
                "200": ["ProdutosResponse_POST_PUT"],
                "400": ["ErrorResponse"],
                "403": ["ErrorResponse"],
            },
            "sdk_method": "alterar_parcialmente",
            "summary": "Altera parcialmente um produto",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera um produto pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do produto",
                    "location": "path",
                    "name": "idProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto",
                }
            ],
            "path": "/produtos/{idProduto}",
            "request_schema_refs": ["ProdutosDadosDTO"],
            "resource": "Produtos",
            "response_schema_refs": {
                "200": ["ProdutosResponse_POST_PUT"],
                "400": ["ErrorResponse"],
                "403": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Altera um produto",
        }
    ),
    "alterar_situacao": OperationContract.model_validate(
        {
            "action": "AlterarSituacao",
            "description": "Altera a situação de um produto pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID do produto",
                    "location": "path",
                    "name": "idProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto",
                }
            ],
            "path": "/produtos/{idProduto}/situacoes",
            "request_schema_refs": [],
            "resource": "Produtos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao",
            "summary": "Altera a situação de um produto",
        }
    ),
}
