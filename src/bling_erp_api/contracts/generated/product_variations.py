"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PRODUCT_VARIATION_OPERATIONS: dict[str, OperationContract] = {
    "gerar_combinacoes": OperationContract.model_validate(
        {
            "action": "GerarCombinacoes",
            "description": "Ação responsável por retornar o produto pai com combinação de novas variações a "
            "partir dos atributos. Esta ação não persistirá os dados.",
            "method": "POST",
            "parameters": [],
            "path": "/produtos/variacoes/atributos/gerar-combinacoes",
            "request_schema_refs": ["ProdutosVariacoesCombinacaoDadosDTO"],
            "resource": "ProdutosVariacoes",
            "response_schema_refs": {"200": ["ProdutosDadosDTO"], "400": ["ErrorResponse"]},
            "sdk_method": "gerar_combinacoes",
            "summary": "Retorna o produto pai com combinações de novas variações",
        }
    ),
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém o produto e variações pelo ID do produto pai.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do produto pai",
                    "location": "path",
                    "name": "idProdutoPai",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_pai",
                }
            ],
            "path": "/produtos/variacoes/{idProdutoPai}",
            "request_schema_refs": [],
            "resource": "ProdutosVariacoes",
            "response_schema_refs": {"200": ["ProdutosDadosDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "listar",
            "summary": "Obtém o produto e variações",
        }
    ),
    "alterar_atributo": OperationContract.model_validate(
        {
            "action": "AlterarAtributo",
            "description": "Altera o nome do atributo nas variações de um produto pai.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID do produto pai",
                    "location": "path",
                    "name": "idProdutoPai",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_pai",
                }
            ],
            "path": "/produtos/variacoes/{idProdutoPai}/atributos",
            "request_schema_refs": ["ProdutosVariacoesDadosAtributoDTO"],
            "resource": "ProdutosVariacoes",
            "response_schema_refs": {"200": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "alterar_atributo",
            "summary": "Altera o nome do atributo nas variações",
        }
    ),
}
