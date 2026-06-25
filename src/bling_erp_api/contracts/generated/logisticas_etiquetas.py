"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

LOGISTICAS_ETIQUETAS_OPERATIONS: dict[str, OperationContract] = {
    "obter_etiquetas": OperationContract.model_validate(
        {
            "action": "ObterEtiquetaMultiplos",
            "description": "Obtém as etiquetas dos pedidos de venda a partir dos ID's dos pedidos. No "
            "momento, o filtro está limitado para apenas um ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "Parâmetro para definir o formato do arquivo de impressão.<br> "
                    "`PDF` - Formato PDF<br> `ZPL` - Formato ZPL",
                    "location": "query",
                    "name": "formato",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "formato",
                },
                {
                    "description": "IDs dos pedidos de venda para impressão",
                    "location": "query",
                    "name": "idsVendas[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_vendas",
                },
            ],
            "path": "/logisticas/etiquetas",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasEtiquetasDadosResponseDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_etiquetas",
            "summary": "Obtém etiquetas das vendas",
        }
    ),
}
