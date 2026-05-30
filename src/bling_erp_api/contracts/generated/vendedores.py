"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

VENDEDOR_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém vendedores paginados.",
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
                    "description": "Nome do contato do vendedor",
                    "location": "query",
                    "name": "nomeContato",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "nome_contato",
                },
                {
                    "description": "Situação do contato do vendedor<br>`A` Ativo<br>`I` "
                    "Inativo<br>`S` Sem movimento<br>`E` Excluído<br>`T` Todos",
                    "location": "query",
                    "name": "situacaoContato",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "situacao_contato",
                },
                {
                    "description": "ID do contato do vendedor",
                    "location": "query",
                    "name": "idContato",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_contato",
                },
                {
                    "description": "ID da loja vinculada ao vendedor",
                    "location": "query",
                    "name": "idLoja",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_loja",
                },
                {
                    "description": "Data de alteração inicial",
                    "location": "query",
                    "name": "dataAlteracaoInicial",
                    "required": False,
                    "schema_format": "date-time",
                    "schema_type": "string",
                    "sdk_name": "data_alteracao_inicial",
                },
                {
                    "description": "Data de alteração final",
                    "location": "query",
                    "name": "dataAlteracaoFinal",
                    "required": False,
                    "schema_format": "date-time",
                    "schema_type": "string",
                    "sdk_name": "data_alteracao_final",
                },
            ],
            "path": "/vendedores",
            "request_schema_refs": [],
            "resource": "Vendedores",
            "response_schema_refs": {"200": ["VendedoresDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém vendedores",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um vendedor pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do vendedor",
                    "location": "path",
                    "name": "idVendedor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_vendedor",
                }
            ],
            "path": "/vendedores/{idVendedor}",
            "request_schema_refs": [],
            "resource": "Vendedores",
            "response_schema_refs": {
                "200": ["VendedoresDadosBaseDTO", "VendedoresDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um vendedor",
        }
    ),
}
