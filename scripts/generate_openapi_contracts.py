"""Generate SDK operation contracts and docs from the local OpenAPI reference."""

from __future__ import annotations

import json
from pathlib import Path
from pprint import pformat
from typing import TYPE_CHECKING, TypedDict, cast

if TYPE_CHECKING:
    from collections.abc import Mapping

SPEC_PATH = Path("specs/bling-openapi-reference.json")
CONTRACTS_DIR = Path("src/bling_erp_api/contracts/generated")
DOCS_DIR = Path("docs/resources")


class ResourceConfig(TypedDict):
    """Resource generation settings."""

    openapi_resource: str
    module: str
    constant: str
    title: str
    example: list[str]


ACTION_TO_SDK_METHOD = {
    "ObterMultiplos": "listar",
    "Obter": "obter",
    "Criar": "criar",
    "Alterar": "alterar",
    "Remover": "remover",
    "RemoverMultiplos": "remover_varios",
    "CriarMultiplos": "criar_varios",
    "AlterarSituacao": "alterar_situacao",
    "AlterarSituacaoMultiplos": "alterar_situacao_varios",
    "LancarEstoqueDeposito": "lancar_estoque",
    "LancarEstoque": "lancar_estoque",
    "EstornarEstoque": "estornar_estoque",
    "LancarContas": "lancar_contas",
    "EstornarContas": "estornar_contas",
    "GerarNotaFiscal": "gerar_nota_fiscal",
    "GerarNotaFiscalConsumidor": "gerar_nota_fiscal_consumidor",
    "VincularComponenteMultiplos": "vincular_componentes",
    "RemoverComponenteMultiplos": "remover_componentes",
    "AlterarComponente": "alterar_componente",
    "GerarCombinacoes": "gerar_combinacoes",
    "AlterarAtributo": "alterar_atributo",
    "ObterSaldosLote": "obter_saldos",
    "ObterMultiplosProdutoControlaLote": "listar_produtos_controlam_lote",
}

PARAMETER_TO_SDK_NAME = {
    "pagina": "pagina",
    "limite": "limite",
    "idPedidoVenda": "id_pedido_venda",
    "idSituacao": "id_situacao",
    "idDeposito": "id_deposito",
    "idContato": "id_contato",
    "idsSituacoes[]": "ids_situacoes",
    "dataInicial": "data_inicial",
    "dataFinal": "data_final",
    "dataAlteracaoInicial": "data_alteracao_inicial",
    "dataAlteracaoFinal": "data_alteracao_final",
    "dataPrevistaInicial": "data_prevista_inicial",
    "dataPrevistaFinal": "data_prevista_final",
    "numero": "numero",
    "idLoja": "id_loja",
    "idVendedor": "id_vendedor",
    "idControleCaixa": "id_controle_caixa",
    "numerosLojas[]": "numeros_lojas",
    "idUnidadeNegocio": "id_unidade_negocio",
    "idsPedidosVendas[]": "ids_pedidos_vendas",
    "idProduto": "id_produto",
    "idProdutoPai": "id_produto_pai",
    "idProdutoEstrutura": "id_produto_estrutura",
    "idProdutoFornecedor": "id_produto_fornecedor",
    "idProdutoLoja": "id_produto_loja",
    "idComponente": "id_componente",
    "idsComponentes[]": "ids_componentes",
    "idsProdutos[]": "ids_produtos",
    "codigos[]": "codigos",
    "gtins[]": "gtins",
    "criterio": "criterio",
    "tipo": "tipo",
    "idCategoria": "id_categoria",
    "idCategoriaProduto": "id_categoria_produto",
    "dataInclusaoInicial": "data_inclusao_inicial",
    "dataInclusaoFinal": "data_inclusao_final",
    "filtroSaldoEstoque": "filtro_saldo_estoque",
    "filtroSaldoEstoqueDeposito": "filtro_saldo_estoque_deposito",
    "idFornecedor": "id_fornecedor",
    "idLote": "id_lote",
    "idsLotes[]": "ids_lotes",
    "idsDepositos[]": "ids_depositos",
    "codigosLotes[]": "codigos_lotes",
    "status": "status",
    "dataValidadeInicial": "data_validade_inicial",
    "dataValidadeFinal": "data_validade_final",
    "dataFabricacaoInicial": "data_fabricacao_inicial",
    "dataFabricacaoFinal": "data_fabricacao_final",
    "dataCriacaoInicial": "data_criacao_inicial",
    "dataCriacaoFinal": "data_criacao_final",
    "idLancamento": "id_lancamento",
}

RESOURCES: list[ResourceConfig] = [
    {
        "openapi_resource": "PedidosVenda",
        "module": "sales_orders",
        "constant": "SALES_ORDER_OPERATIONS",
        "title": "Pedidos de venda",
        "example": [
            "pedidos = client.pedidos_vendas.listar(",
            '    data_inicial="2024-01-01",',
            "    ids_situacoes=[123456],",
            ")",
            "pedido = client.pedidos_vendas.obter(123456)",
        ],
    },
    {
        "openapi_resource": "Produtos",
        "module": "products",
        "constant": "PRODUCT_OPERATIONS",
        "title": "Produtos",
        "example": [
            "produtos = client.produtos.listar(",
            '    nome="Camiseta",',
            "    ids_produtos=[123456],",
            ")",
            "produto = client.produtos.obter(123456)",
        ],
    },
    {
        "openapi_resource": "ProdutosEstruturas",
        "module": "product_structures",
        "constant": "PRODUCT_STRUCTURE_OPERATIONS",
        "title": "Produtos - Estruturas",
        "example": [],
    },
    {
        "openapi_resource": "ProdutosFornecedores",
        "module": "product_suppliers",
        "constant": "PRODUCT_SUPPLIER_OPERATIONS",
        "title": "Produtos - Fornecedores",
        "example": [],
    },
    {
        "openapi_resource": "ProdutosLojas",
        "module": "product_stores",
        "constant": "PRODUCT_STORE_OPERATIONS",
        "title": "Produtos - Lojas",
        "example": [],
    },
    {
        "openapi_resource": "Lotes",
        "module": "product_batches",
        "constant": "PRODUCT_BATCH_OPERATIONS",
        "title": "Produtos - Lotes",
        "example": [],
    },
    {
        "openapi_resource": "LotesLancamentos",
        "module": "product_batch_entries",
        "constant": "PRODUCT_BATCH_ENTRY_OPERATIONS",
        "title": "Produtos - Lotes Lancamentos",
        "example": [],
    },
    {
        "openapi_resource": "ProdutosVariacoes",
        "module": "product_variations",
        "constant": "PRODUCT_VARIATION_OPERATIONS",
        "title": "Produtos - Variacoes",
        "example": [],
    },
]


def main() -> None:
    """Generate supported resource contracts."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    for resource in RESOURCES:
        contracts = _resource_contracts(payload, resource=resource["openapi_resource"])
        _write_contract_module(
            resource["module"],
            resource["constant"],
            contracts,
        )
        _write_resource_docs(
            resource["module"],
            resource["title"],
            contracts,
            resource["example"],
        )


def _resource_contracts(payload: Mapping[str, object], *, resource: str) -> list[dict[str, object]]:
    paths = _mapping(payload.get("paths"))
    components = _mapping(payload.get("components"))
    parameters = _mapping(components.get("parameters"))
    contracts: list[dict[str, object]] = []

    for raw_path, methods in paths.items():
        path = str(raw_path)
        for raw_method, raw_operation in _mapping(methods).items():
            operation = _mapping(raw_operation)
            if operation.get("x-api-resource") != resource:
                continue

            action = str(operation.get("x-api-action") or raw_method)
            sdk_method = _sdk_method_for_operation(action=action, method=str(raw_method).upper())
            contracts.append(
                {
                    "sdk_method": sdk_method,
                    "method": str(raw_method).upper(),
                    "path": path,
                    "resource": resource,
                    "action": action,
                    "summary": str(operation.get("summary") or ""),
                    "description": _optional_str(operation.get("description")),
                    "parameters": _operation_parameters(operation, parameters),
                    "request_schema_refs": _request_schema_refs(operation),
                    "response_schema_refs": _response_schema_refs(operation),
                }
            )

    return sorted(contracts, key=lambda item: (str(item["path"]), str(item["method"])))


def _operation_parameters(
    operation: Mapping[str, object],
    component_parameters: Mapping[str, object],
) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for raw_parameter in _sequence(operation.get("parameters")):
        parameter = _resolve_parameter(raw_parameter, component_parameters)
        name = str(parameter.get("name") or "")
        schema = _mapping(parameter.get("schema"))
        result.append(
            {
                "name": name,
                "location": str(parameter.get("in") or "query"),
                "sdk_name": PARAMETER_TO_SDK_NAME.get(name, _snake_case(name)),
                "required": bool(parameter.get("required", False)),
                "description": _optional_str(parameter.get("description")),
                "schema_type": _optional_str(schema.get("type")),
                "schema_format": _optional_str(schema.get("format")),
            }
        )
    return result


def _sdk_method_for_operation(*, action: str, method: str) -> str:
    if action == "Alterar" and method == "PATCH":
        return "alterar_parcialmente"
    return ACTION_TO_SDK_METHOD[action]


def _resolve_parameter(
    raw_parameter: object,
    component_parameters: Mapping[str, object],
) -> Mapping[str, object]:
    parameter = _mapping(raw_parameter)
    ref = parameter.get("$ref")
    if isinstance(ref, str):
        name = ref.rsplit("/", maxsplit=1)[-1]
        return _mapping(component_parameters.get(name))
    return parameter


def _request_schema_refs(operation: Mapping[str, object]) -> list[str]:
    request_body = _mapping(operation.get("requestBody"))
    content = _mapping(request_body.get("content"))
    application_json = _mapping(content.get("application/json"))
    schema = _mapping(application_json.get("schema"))
    return sorted(_schema_refs(schema))


def _response_schema_refs(operation: Mapping[str, object]) -> dict[str, list[str]]:
    responses = _mapping(operation.get("responses"))
    result: dict[str, list[str]] = {}
    for status_code, raw_response in responses.items():
        response = _mapping(raw_response)
        content = _mapping(response.get("content"))
        application_json = _mapping(content.get("application/json"))
        schema = _mapping(application_json.get("schema"))
        refs = sorted(_schema_refs(schema))
        if refs:
            result[str(status_code)] = refs
    return result


def _schema_refs(schema: object) -> set[str]:
    if isinstance(schema, dict):
        mapping = cast("dict[str, object]", schema)
        found_refs: set[str] = set()
        ref = mapping.get("$ref")
        if isinstance(ref, str):
            found_refs.add(ref.rsplit("/", maxsplit=1)[-1])
        for value in mapping.values():
            found_refs.update(_schema_refs(value))
        return found_refs
    if isinstance(schema, list):
        values = cast("list[object]", schema)
        list_refs: set[str] = set()
        for item in values:
            list_refs.update(_schema_refs(item))
        return list_refs
    return set()


def _write_contract_module(
    module_name: str,
    constant_name: str,
    contracts: list[dict[str, object]],
) -> None:
    CONTRACTS_DIR.mkdir(parents=True, exist_ok=True)
    mapping = _operation_mapping(contracts)
    module = (
        '"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""\n\n'
        "from __future__ import annotations\n\n"
        "from bling_erp_api.contracts import OperationContract\n\n"
        f"{constant_name}: dict[str, OperationContract] = {{\n"
    )
    for key, value in mapping.items():
        module += f"    {key!r}: OperationContract.model_validate({pformat(value, width=100)}),\n"
    module += "}\n"
    (CONTRACTS_DIR / f"{module_name}.py").write_text(module, encoding="utf-8")


def _operation_mapping(contracts: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    mapping: dict[str, dict[str, object]] = {}
    for contract in contracts:
        sdk_method = str(contract["sdk_method"])
        key = sdk_method
        if key in mapping:
            suffix = str(contract["path"]).rsplit("/", maxsplit=1)[-1]
            key = f"{sdk_method}_{_snake_case(suffix)}"
        mapping[key] = contract
    return mapping


def _write_resource_docs(
    resource_slug: str,
    title: str,
    contracts: list[dict[str, object]],
    example: list[str],
) -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {title}",
        "",
        "Esta página é gerada a partir de `specs/bling-openapi-reference.json`.",
        "A documentação oficial é usada como contrato para paths, métodos e parâmetros.",
        "",
        "## Exemplo",
        "",
        "```python",
        *(example or ["# Veja as operacoes geradas abaixo."]),
        "```",
        "",
        "## Operações",
        "",
    ]

    for operation_name, contract in _operation_mapping(contracts).items():
        lines.extend(_operation_docs(operation_name, contract))

    (DOCS_DIR / f"{resource_slug}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _operation_docs(operation_name: str, contract: Mapping[str, object]) -> list[str]:
    parameters = cast("list[dict[str, object]]", contract.get("parameters") or [])
    lines = [
        f"### `{operation_name}`",
        "",
        f"- Bling: `{contract['method']} {contract['path']}`",
        f"- Ação oficial: `{contract['action']}`",
        f"- Resumo oficial: {contract['summary']}",
        "",
    ]
    if parameters:
        lines.extend(
            [
                "| Argumento SDK | Parâmetro Bling | Local | Obrigatório |",
                "| --- | --- | --- | --- |",
            ]
        )
        for parameter in parameters:
            required = "sim" if parameter["required"] else "não"
            lines.append(
                f"| `{parameter['sdk_name']}` | `{parameter['name']}` | "
                f"`{parameter['location']}` | {required} |"
            )
        lines.append("")
    request_refs = cast("list[str]", contract.get("request_schema_refs") or [])
    response_refs = cast("dict[str, list[str]]", contract.get("response_schema_refs") or {})
    if request_refs:
        lines.append(f"- Schemas de request: {', '.join(f'`{item}`' for item in request_refs)}")
    if response_refs:
        formatted = ", ".join(
            f"{status}: {'/'.join(refs)}" for status, refs in response_refs.items()
        )
        lines.append(f"- Schemas de response: {formatted}")
    lines.append("")
    return lines


def _mapping(value: object) -> Mapping[str, object]:
    if isinstance(value, dict):
        return cast("Mapping[str, object]", value)
    return {}


def _sequence(value: object) -> list[object]:
    return cast("list[object]", value) if isinstance(value, list) else []


def _optional_str(value: object) -> str | None:
    return value if isinstance(value, str) else None


def _snake_case(value: str) -> str:
    clean = value.replace("[]", "").replace("{", "").replace("}", "")
    chars: list[str] = []
    for index, char in enumerate(clean):
        if char.isupper() and index > 0:
            chars.append("_")
        chars.append(char.lower() if char.isalnum() else "_")
    return "".join(chars).strip("_")


if __name__ == "__main__":
    main()
