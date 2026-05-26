"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

HOMOLOGATION_OPERATIONS: dict[str, OperationContract] = {
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém o produto que será utilizado durante os demais passos da homologação, e, "
            "inicia o processo de validação, o qual deve ser acompanhando via interface do "
            "cadastro de aplicativos.",
            "method": "GET",
            "parameters": [],
            "path": "/homologacao/produtos",
            "request_schema_refs": [],
            "resource": "Homologacao",
            "response_schema_refs": {"200": ["HomologacaoDadosBaseDTO"]},
            "sdk_method": "obter",
            "summary": "Obtém o produto da homologação",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria o produto da homologação.",
            "method": "POST",
            "parameters": [],
            "path": "/homologacao/produtos",
            "request_schema_refs": ["HomologacaoDadosBaseDTO"],
            "resource": "Homologacao",
            "response_schema_refs": {
                "201": ["HomologacaoDadosBaseDTO", "HomologacaoDadosDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria o produto da homologação",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove o produto da homologação pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do produto da homologação.",
                    "location": "path",
                    "name": "idProdutoHomologacao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_homologacao",
                }
            ],
            "path": "/homologacao/produtos/{idProdutoHomologacao}",
            "request_schema_refs": [],
            "resource": "Homologacao",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove o produto da homologação",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera o produto da homologação pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do produto da homologação.",
                    "location": "path",
                    "name": "idProdutoHomologacao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_homologacao",
                }
            ],
            "path": "/homologacao/produtos/{idProdutoHomologacao}",
            "request_schema_refs": ["HomologacaoDadosBaseDTO"],
            "resource": "Homologacao",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera o produto da homologação",
        }
    ),
    "alterar_situacao": OperationContract.model_validate(
        {
            "action": "AlterarSituacao",
            "description": "Altera a situação do produto da homologação pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID do produto da homologação.",
                    "location": "path",
                    "name": "idProdutoHomologacao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_homologacao",
                }
            ],
            "path": "/homologacao/produtos/{idProdutoHomologacao}/situacoes",
            "request_schema_refs": ["HomologacaoSituacaoDTO"],
            "resource": "Homologacao",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao",
            "summary": "Altera a situação do produto da homologação",
        }
    ),
}
