"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

LOGISTICAS_SERVICOS_OPERATIONS: dict[str, OperationContract] = {
    "listar_servicos": OperationContract.model_validate(
        {
            "action": "ObterServicoLogisticoMultiplos",
            "description": "Obtém serviços de logísticas paginados.",
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
                    "description": "Parâmetro para filtrar os registros através do tipo da logística.",
                    "location": "query",
                    "name": "tipoIntegracao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo_integracao",
                },
            ],
            "path": "/logisticas/servicos",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasServicosDadosDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "listar_servicos",
            "summary": "Obtém serviços de logísticas",
        }
    ),
    "criar_servico": OperationContract.model_validate(
        {
            "action": "CriarLogisticaServico",
            "description": "Cria um serviço de logística personalizada.",
            "method": "POST",
            "parameters": [],
            "path": "/logisticas/servicos",
            "request_schema_refs": ["LogisticasServicosDadosCreateRequestDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "201": ["LogisticasServicosDadosSaveDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar_servico",
            "summary": "Cria um serviço de logística",
        }
    ),
    "obter_servico": OperationContract.model_validate(
        {
            "action": "ObterServicoLogistico",
            "description": "Obtém um servico de logística pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do serviço",
                    "location": "path",
                    "name": "idLogisticaServico",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica_servico",
                }
            ],
            "path": "/logisticas/servicos/{idLogisticaServico}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasServicosDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_servico",
            "summary": "Obtém um servico de logística",
        }
    ),
    "alterar_servico": OperationContract.model_validate(
        {
            "action": "AlterarLogisticaServico",
            "description": "Altera dados de um serviço de logística personalizada pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do serviço",
                    "location": "path",
                    "name": "idLogisticaServico",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica_servico",
                }
            ],
            "path": "/logisticas/servicos/{idLogisticaServico}",
            "request_schema_refs": ["LogisticasServicosDadosSaveRequestDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasServicosDadosSaveDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar_servico",
            "summary": "Altera um serviço de logística pelo ID",
        }
    ),
    "alterar_situacao_servico": OperationContract.model_validate(
        {
            "action": "AlterarSituacaoLogisticaServico",
            "description": "Desativa ou ativa um serviço de uma logística personalizada pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID do serviço",
                    "location": "path",
                    "name": "idLogisticaServico",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica_servico",
                }
            ],
            "path": "/logisticas/{idLogisticaServico}/situacoes",
            "request_schema_refs": ["LogisticasServicosDadosSituationDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao_servico",
            "summary": "Desativa ou ativa um serviço de uma logística",
        }
    ),
}
