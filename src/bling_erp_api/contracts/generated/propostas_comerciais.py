"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

COMMERCIAL_PROPOSAL_OPERATIONS: dict[str, OperationContract] = {
    "remover_varios": OperationContract.model_validate(
        {
            "action": "RemoverMultiplos",
            "description": "Remove múltiplas propostas comerciais pelos IDs.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "IDs das propostas comerciais",
                    "location": "query",
                    "name": "idsPropostasComerciais[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_propostas_comerciais",
                }
            ],
            "path": "/propostas-comerciais",
            "request_schema_refs": [],
            "resource": "PropostasComerciais",
            "response_schema_refs": {"200": ["ErrorResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "remover_varios",
            "summary": "Remove múltiplas propostas comerciais",
        }
    ),
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém propostas comerciais paginadas.",
            "method": "GET",
            "parameters": [
                {
                    "description": "O valor referente a situação da proposta: Pendente, Aguardando, "
                    "Não aprovado, Aprovado, Concluido, Rascunho. Para mais situações, "
                    "pesquisar pelo número separado por vírgula.",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "situacao",
                },
                {
                    "description": "ID do contato",
                    "location": "query",
                    "name": "idContato",
                    "required": False,
                    "schema_format": "int64",
                    "schema_type": "integer",
                    "sdk_name": "id_contato",
                },
                {
                    "description": "Data inicial",
                    "location": "query",
                    "name": "dataInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_inicial",
                },
                {
                    "description": "Data final",
                    "location": "query",
                    "name": "dataFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_final",
                },
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
            ],
            "path": "/propostas-comerciais",
            "request_schema_refs": [],
            "resource": "PropostasComerciais",
            "response_schema_refs": {"200": ["OrcamentosDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém propostas comerciais",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma proposta comercial.",
            "method": "POST",
            "parameters": [],
            "path": "/propostas-comerciais",
            "request_schema_refs": ["OrcamentosDadosBaseDTO", "OrcamentosDadosDTO"],
            "resource": "PropostasComerciais",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria uma proposta comercial",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma proposta comercial pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da proposta comercial",
                    "location": "path",
                    "name": "idPropostaComercial",
                    "required": True,
                    "schema_format": "int64",
                    "schema_type": "integer",
                    "sdk_name": "id_proposta_comercial",
                }
            ],
            "path": "/propostas-comerciais/{idPropostaComercial}",
            "request_schema_refs": [],
            "resource": "PropostasComerciais",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma proposta comercial",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma proposta comercial pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da proposta comercial",
                    "location": "path",
                    "name": "idPropostaComercial",
                    "required": True,
                    "schema_format": "int64",
                    "schema_type": "integer",
                    "sdk_name": "id_proposta_comercial",
                }
            ],
            "path": "/propostas-comerciais/{idPropostaComercial}",
            "request_schema_refs": [],
            "resource": "PropostasComerciais",
            "response_schema_refs": {
                "200": ["OrcamentosDadosBaseDTO", "OrcamentosDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma proposta comercial",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma proposta comercial pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da proposta comercial",
                    "location": "path",
                    "name": "idPropostaComercial",
                    "required": True,
                    "schema_format": "int64",
                    "schema_type": "integer",
                    "sdk_name": "id_proposta_comercial",
                }
            ],
            "path": "/propostas-comerciais/{idPropostaComercial}",
            "request_schema_refs": ["OrcamentosDadosBaseDTO", "OrcamentosDadosDTO"],
            "resource": "PropostasComerciais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera uma proposta comercial",
        }
    ),
    "alterar_situacao": OperationContract.model_validate(
        {
            "action": "AlterarSituacao",
            "description": "Altera a situação de uma proposta comercial pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID da proposta comercial",
                    "location": "path",
                    "name": "idPropostaComercial",
                    "required": True,
                    "schema_format": "int64",
                    "schema_type": "integer",
                    "sdk_name": "id_proposta_comercial",
                }
            ],
            "path": "/propostas-comerciais/{idPropostaComercial}/situacoes",
            "request_schema_refs": ["OrcamentosSituacaoDTO"],
            "resource": "PropostasComerciais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao",
            "summary": "Altera a situação de uma proposta comercial",
        }
    ),
}
