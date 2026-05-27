"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

ORDENS_PRODUCAO_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterAcaoMultiplos",
            "description": "Obtém ordens de produção paginadas.",
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
                    "description": "IDs das situações",
                    "location": "query",
                    "name": "idsSituacoes[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_situacoes",
                },
            ],
            "path": "/ordens-producao",
            "request_schema_refs": [],
            "resource": "OrdensProducao",
            "response_schema_refs": {"200": ["OrdensProducaoDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém ordens de produção",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma ordem de produção.",
            "method": "POST",
            "parameters": [],
            "path": "/ordens-producao",
            "request_schema_refs": ["OrdensProducaoDadosBaseDTO", "OrdensProducaoDadosPostDTO"],
            "resource": "OrdensProducao",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria uma ordem de produção",
        }
    ),
    "criar_multiplos": OperationContract.model_validate(
        {
            "action": "CriarMultiplos",
            "description": "Gera ordens de produção sob demanda (abaixo do estoque mínimo).",
            "method": "POST",
            "parameters": [],
            "path": "/ordens-producao/gerar-sob-demanda",
            "request_schema_refs": [],
            "resource": "OrdensProducao",
            "response_schema_refs": {"201": ["OrdensProducaoDadosGeradosPorDemandaDTO"]},
            "sdk_method": "criar_multiplos",
            "summary": "Gera ordens de produção sob demanda",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma ordem de produção pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da ordem de produção",
                    "location": "path",
                    "name": "idOrdemProducao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_ordem_producao",
                }
            ],
            "path": "/ordens-producao/{idOrdemProducao}",
            "request_schema_refs": [],
            "resource": "OrdensProducao",
            "response_schema_refs": {"404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma ordem de produção",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma ordem de produção pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da ordem de produção",
                    "location": "path",
                    "name": "idOrdemProducao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_ordem_producao",
                }
            ],
            "path": "/ordens-producao/{idOrdemProducao}",
            "request_schema_refs": [],
            "resource": "OrdensProducao",
            "response_schema_refs": {
                "200": ["OrdensProducaoDadosBaseDTO", "OrdensProducaoDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma ordem de produção",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma ordem de produção pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da ordem de produção",
                    "location": "path",
                    "name": "idOrdemProducao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_ordem_producao",
                }
            ],
            "path": "/ordens-producao/{idOrdemProducao}",
            "request_schema_refs": ["OrdensProducaoDadosBaseDTO", "OrdensProducaoDadosPostDTO"],
            "resource": "OrdensProducao",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera uma ordem de produção",
        }
    ),
    "alterar_situacao": OperationContract.model_validate(
        {
            "action": "AlterarSituacao",
            "description": "Altera a situação de uma ordem de produção pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da ordem de produção",
                    "location": "path",
                    "name": "idOrdemProducao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_ordem_producao",
                }
            ],
            "path": "/ordens-producao/{idOrdemProducao}/situacoes",
            "request_schema_refs": ["OrdensProducaoSituacaoDadosDTO"],
            "resource": "OrdensProducao",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao",
            "summary": "Altera a situação de uma ordem de produção",
        }
    ),
}
