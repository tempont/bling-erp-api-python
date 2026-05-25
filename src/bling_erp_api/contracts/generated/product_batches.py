"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PRODUCT_BATCH_OPERATIONS: dict[str, OperationContract] = {
    "remover_varios": OperationContract.model_validate(
        {
            "action": "RemoverMultiplos",
            "description": "Remove lotes de produtos pelos IDs.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "IDs dos lotes",
                    "location": "query",
                    "name": "idsLotes[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_lotes",
                }
            ],
            "path": "/produtos/lotes",
            "request_schema_refs": [],
            "resource": "Lotes",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover_varios",
            "summary": "Remove lotes de produtos",
        }
    ),
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém lotes de produtos paginados.",
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
                    "description": "IDs dos produtos",
                    "location": "query",
                    "name": "idsProdutos[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_produtos",
                },
                {
                    "description": "IDs dos lotes",
                    "location": "query",
                    "name": "idsLotes[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_lotes",
                },
                {
                    "description": "IDs dos depósitos",
                    "location": "query",
                    "name": "idsDepositos[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_depositos",
                },
                {
                    "description": "Códigos dos lotes",
                    "location": "query",
                    "name": "codigosLotes[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "codigos_lotes",
                },
                {
                    "description": "Status do lote",
                    "location": "query",
                    "name": "status",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "status",
                },
                {
                    "description": "Data de validade inicial",
                    "location": "query",
                    "name": "dataValidadeInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_validade_inicial",
                },
                {
                    "description": "Data de validade final",
                    "location": "query",
                    "name": "dataValidadeFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_validade_final",
                },
                {
                    "description": "Data de fabricação inicial",
                    "location": "query",
                    "name": "dataFabricacaoInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_fabricacao_inicial",
                },
                {
                    "description": "Data de fabricação final",
                    "location": "query",
                    "name": "dataFabricacaoFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_fabricacao_final",
                },
                {
                    "description": "Data de inclusão inicial",
                    "location": "query",
                    "name": "dataCriacaoInicial",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_criacao_inicial",
                },
                {
                    "description": "Data de inclusão final",
                    "location": "query",
                    "name": "dataCriacaoFinal",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_criacao_final",
                },
            ],
            "path": "/produtos/lotes",
            "request_schema_refs": [],
            "resource": "Lotes",
            "response_schema_refs": {"200": ["LotesDTO"], "400": ["ErrorResponse"]},
            "sdk_method": "listar",
            "summary": "Obtém lotes de produtos",
        }
    ),
    "criar_varios": OperationContract.model_validate(
        {
            "action": "CriarMultiplos",
            "description": "Cria/altera lotes de produtos.",
            "method": "PUT",
            "parameters": [],
            "path": "/produtos/lotes",
            "request_schema_refs": ["LotesDTO"],
            "resource": "Lotes",
            "response_schema_refs": {"200": ["SaveResponseLotsDTO"], "400": ["ErrorResponse"]},
            "sdk_method": "criar_varios",
            "summary": "Salva lotes de produtos",
        }
    ),
    "listar_produtos_controlam_lote": OperationContract.model_validate(
        {
            "action": "ObterMultiplosProdutoControlaLote",
            "description": "Obtém a informação se determinados produtos possuem controle de lote.",
            "method": "GET",
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
            "path": "/produtos/lotes/controla-lote",
            "request_schema_refs": [],
            "resource": "Lotes",
            "response_schema_refs": {"200": ["ProdutoControlaLotesDTO"], "400": ["ErrorResponse"]},
            "sdk_method": "listar_produtos_controlam_lote",
            "summary": "Obtém a informação se determinados produtos possuem controle de lote",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um lote de um produto pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do lote",
                    "location": "path",
                    "name": "idLote",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_lote",
                }
            ],
            "path": "/produtos/lotes/{idLote}",
            "request_schema_refs": [],
            "resource": "Lotes",
            "response_schema_refs": {"200": ["LotesDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter",
            "summary": "Obtém um lote de um produto",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera um lote de um produto pelo ID.",
            "method": "PUT",
            "parameters": [],
            "path": "/produtos/lotes/{idLote}",
            "request_schema_refs": ["LotePutRequestDTO"],
            "resource": "Lotes",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera um lote de um produto",
        }
    ),
    "alterar_situacao": OperationContract.model_validate(
        {
            "action": "AlterarSituacao",
            "description": "Altera o status de um lote do produto pelo ID.",
            "method": "PATCH",
            "parameters": [],
            "path": "/produtos/lotes/{idLote}/status",
            "request_schema_refs": ["LoteStatusDTO"],
            "resource": "Lotes",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao",
            "summary": "Altera o status de um lote do produto",
        }
    ),
    "alterar_situacao_desativar": OperationContract.model_validate(
        {
            "action": "AlterarSituacao",
            "description": "Desativa controle de lotes para o produto pelo ID do produto.",
            "method": "POST",
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
            "path": "/produtos/{idProduto}/lotes/controla-lote/desativar",
            "request_schema_refs": [],
            "resource": "Lotes",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao",
            "summary": "Desativa controle de lotes para o produto",
        }
    ),
}
