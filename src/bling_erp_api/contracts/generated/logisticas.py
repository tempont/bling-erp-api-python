"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

LOGISTICAS_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém logísticas paginados.",
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
                {
                    "description": "Parâmetro para filtrar os registros através de uma lista de tipos "
                    "de logística.",
                    "location": "query",
                    "name": "tiposIntegracoes[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "tipos_integracoes",
                },
                {
                    "description": "Parâmetro para filtrar os registros através da situação<br> `H` "
                    "Habilitado<br> `D` Desabilitado",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "situacao",
                },
                {
                    "description": "Parâmetro para filtrar apenas as logísticas que possuem serviço "
                    "de reversão. É sobrescrito pelo parâmetro tipoIntegracao, caso "
                    "enviado junto.",
                    "location": "query",
                    "name": "logisticasReversas",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "boolean",
                    "sdk_name": "logisticas_reversas",
                },
            ],
            "path": "/logisticas",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {"200": ["LogisticasDadosBaseDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "listar",
            "summary": "Obtém logísticas",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma logística.",
            "method": "POST",
            "parameters": [],
            "path": "/logisticas",
            "request_schema_refs": ["LogisticasDadosPostDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {"201": ["LogisticasLogisticaDTO"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria logística",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma logística pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da logística",
                    "location": "path",
                    "name": "idLogistica",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica",
                }
            ],
            "path": "/logisticas/{idLogistica}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma logística",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma logística pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da logística",
                    "location": "path",
                    "name": "idLogistica",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica",
                },
                {
                    "description": "Parâmetro para incluir serviços inativos na resposta.<br> `true` "
                    "Inclui serviços ativos e inativos<br> `false` Inclui apenas "
                    "serviços ativos (padrão)",
                    "location": "query",
                    "name": "listarServicosInativos",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "boolean",
                    "sdk_name": "listar_servicos_inativos",
                },
            ],
            "path": "/logisticas/{idLogistica}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {"200": ["LogisticasDadosDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter",
            "summary": "Obtém uma logística",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma logística pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da logística",
                    "location": "path",
                    "name": "idLogistica",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica",
                }
            ],
            "path": "/logisticas/{idLogistica}",
            "request_schema_refs": ["LogisticasDadosPutDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera uma logística",
        }
    ),
}
