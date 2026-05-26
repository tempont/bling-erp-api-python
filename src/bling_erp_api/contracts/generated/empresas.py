"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

EMPRESA_OPERATIONS: dict[str, OperationContract] = {
    "obter_dados_basicos": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém CNPJ, razão social e e-mail da empresa.",
            "method": "GET",
            "parameters": [],
            "path": "/empresas/me/dados-basicos",
            "request_schema_refs": [],
            "resource": "Empresas",
            "response_schema_refs": {"200": ["EmpresasDadosBasicosDTO"]},
            "sdk_method": "obter_dados_basicos",
            "summary": "Obtém dados básicos da empresa",
        }
    ),
}
