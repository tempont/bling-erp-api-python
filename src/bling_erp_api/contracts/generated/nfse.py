"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

NFSE_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém notas de serviços paginadas.",
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
                    "description": "`0` Pendente <br> `1` Emitida <br> `2` Disponível para consulta "
                    "<br> `3` Cancelada",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "situacao",
                },
                {
                    "description": "Data incial do período de emissão",
                    "location": "query",
                    "name": "dataEmissaoInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_emissao_inicial",
                },
                {
                    "description": "Data final do período de emissão",
                    "location": "query",
                    "name": "dataEmissaoFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_emissao_final",
                },
            ],
            "path": "/nfse",
            "request_schema_refs": [],
            "resource": "NFSe",
            "response_schema_refs": {
                "200": ["NotasServicosDadosBaseDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "listar",
            "summary": "Obtém notas de serviços",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma nota de serviço.",
            "method": "POST",
            "parameters": [],
            "path": "/nfse",
            "request_schema_refs": ["NotasServicosDadosBaseDTO_POST", "NotasServicosDadosDTO_POST"],
            "resource": "NFSe",
            "response_schema_refs": {
                "201": ["BasePostResponse", "NotasServicosResponse_POST_PUT"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria uma nota de serviço",
        }
    ),
    "obter_configuracoes": OperationContract.model_validate(
        {
            "action": "ObterConfiguracoes",
            "description": "Obtém todas as configurações de nota de serviço.",
            "method": "GET",
            "parameters": [],
            "path": "/nfse/configuracoes",
            "request_schema_refs": [],
            "resource": "NFSe",
            "response_schema_refs": {"200": ["ConfiguracaoNotaServicoDadosBaseDTO"]},
            "sdk_method": "obter_configuracoes",
            "summary": "Configurações de nota de serviço",
        }
    ),
    "alterar_configuracoes": OperationContract.model_validate(
        {
            "action": "AlterarConfiguracoes",
            "description": "Cria e altera configurações para emissão de notas de serviço.",
            "method": "PUT",
            "parameters": [],
            "path": "/nfse/configuracoes",
            "request_schema_refs": ["ConfiguracaoNotaServicoDadosBaseDTO"],
            "resource": "NFSe",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "alterar_configuracoes",
            "summary": "Configurações de nota de serviço",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Exclui uma nota de serviço pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da nota de serviço",
                    "location": "path",
                    "name": "idNotaServico",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_servico",
                }
            ],
            "path": "/nfse/{idNotaServico}",
            "request_schema_refs": [],
            "resource": "NFSe",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Exclui uma nota de serviço",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma nota de serviço pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da nota de serviço",
                    "location": "path",
                    "name": "idNotaServico",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_servico",
                }
            ],
            "path": "/nfse/{idNotaServico}",
            "request_schema_refs": [],
            "resource": "NFSe",
            "response_schema_refs": {
                "200": ["NotasServicosDadosBaseDTO", "NotasServicosDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma nota de serviço",
        }
    ),
    "cancelar": OperationContract.model_validate(
        {
            "action": "Cancelar",
            "description": "Cancela uma nota de serviço pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota de serviço",
                    "location": "path",
                    "name": "idNotaServico",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_servico",
                }
            ],
            "path": "/nfse/{idNotaServico}/cancelar",
            "request_schema_refs": ["NotasServicosCancelamentoDTO"],
            "resource": "NFSe",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "cancelar",
            "summary": "Cancela uma nota de serviço",
        }
    ),
    "autorizar": OperationContract.model_validate(
        {
            "action": "Autorizar",
            "description": "Envia uma nota de serviço pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota de serviço",
                    "location": "path",
                    "name": "idNotaServico",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_servico",
                }
            ],
            "path": "/nfse/{idNotaServico}/enviar",
            "request_schema_refs": [],
            "resource": "NFSe",
            "response_schema_refs": {
                "200": ["NotasServicosDadosBaseDTO", "NotasServicosDadosDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "autorizar",
            "summary": "Envia uma nota de serviço",
        }
    ),
}
