"""Generate Pydantic models from the local Bling OpenAPI reference."""

# pyright: reportPrivateUsage=false

from __future__ import annotations

import ast
import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, cast

from generate_openapi_contracts import (
    RESOURCES,
    _class_name_for_module,
    _operation_mapping,
    _resource_contracts,
)

if TYPE_CHECKING:
    from collections.abc import Iterable, Mapping, Sequence

SPEC_PATH = Path("specs/bling-openapi-reference.json")
GENERATED_DIR = Path("src/bling_erp_api/models/generated")
RESOURCE_REEXPORT_DIR = GENERATED_DIR / "resources"
SCHEMAS_PACKAGE_DIR = GENERATED_DIR / "schemas"
RAW_SCHEMAS_MODULE = GENERATED_DIR / "_schemas_raw.py"
LEGACY_SCHEMAS_MODULE = GENERATED_DIR / "schemas.py"
OPERATION_MODELS_MODULE = Path("src/bling_erp_api/contracts/generated/_operation_models.py")

SUCCESS_STATUS_PRIORITY = ("200", "201", "202", "204")
COMMON_SCHEMA_MODULE = "common"
COMMON_SCHEMA_NAMES = {
    "BasePostResponse",
    "DeletedItem",
    "Error",
    "ErrorField",
    "ErrorFieldCollection",
    "ErrorResponse",
    "FieldModel",
    "SavedItem",
    "UpdatedItem",
}
GENERIC_SCHEMA_NAME_RE = re.compile(r"(?:Data|Datum)\d*$")
SCHEMA_FAMILY_PREFIXES = (
    ("AnunciosCategorias", "anuncios_categorias"),
    ("Anuncios", "anuncios"),
    ("Borderos", "borderos"),
    ("CaixasBancos", "caixas_bancos"),
    ("Caixas", "caixas_bancos"),
    ("CalculosImpostos", "calculos_impostos"),
    ("CamposCustomizados", "campos_customizados"),
    ("CanaisVenda", "canais_venda"),
    ("CanalVenda", "canais_venda"),
    ("CategoriasReceitasDespesas", "categorias_receitas_despesas"),
    ("CategoriasProdutos", "categorias_produtos"),
    ("CategoriasLojas", "categorias_lojas"),
    ("Configuracao", "configuracoes"),
    ("ContasContabeis", "contas_contabeis"),
    ("ContasPagar", "contas_pagar"),
    ("ContasReceber", "contas_receber"),
    ("ContasFinanceiras", "contas_financeiras"),
    ("Contas", "contas"),
    ("Contatos", "contatos"),
    ("Contratos", "contratos"),
    ("Depositos", "depositos"),
    ("Deposito", "depositos"),
    ("Empresas", "empresas"),
    ("Estoques", "estoques"),
    ("Estoque", "estoques"),
    ("FormasPagamentos", "formas_pagamentos"),
    ("Fornecedor", "produtos_fornecedores"),
    ("GruposProdutos", "grupos_produtos"),
    ("Homologacao", "homologacao"),
    ("LogisticasEtiquetas", "logisticas_etiquetas"),
    ("LogisticasObjetos", "logisticas_objetos"),
    ("LogisticasRemessas", "logisticas_remessas"),
    ("LogisticasServicos", "logisticas_servicos"),
    ("Logisticas", "logisticas"),
    ("Logistica", "logisticas"),
    ("NaturezasOperacoes", "naturezas_operacoes"),
    ("NotasFiscais", "notas_fiscais"),
    ("NotaFiscal", "notas_fiscais"),
    ("Nfce", "notas_fiscais_consumidor"),
    ("Nfe", "notas_fiscais"),
    ("NotasServicos", "notas_servicos"),
    ("Nfse", "notas_servicos"),
    ("Notificacoes", "notificacoes"),
    ("Orcamentos", "orcamentos"),
    ("OrdensProducao", "ordens_producao"),
    ("PedidosCompras", "pedidos_compras"),
    ("PedidosVendas", "pedidos_vendas"),
    ("PedidosCompra", "pedidos_compras"),
    ("PedidoCompra", "pedidos_compras"),
    ("ProdutoControlaLotes", "lotes"),
    ("ProdutosFornecedores", "produtos_fornecedores"),
    ("ProdutosLojas", "produtos_lojas"),
    ("ProdutosVariacoes", "produtos_variacoes"),
    ("ProdutosEstruturas", "produtos_estruturas"),
    ("ProdutosLotes", "lotes"),
    ("Produtos", "produtos"),
    ("ProdutoFornecedor", "produtos_fornecedores"),
    ("ProdutoUsuario", "produtos"),
    ("Produto", "produtos"),
    ("LoteLancamento", "lotes_lancamentos"),
    ("Lotes", "lotes"),
    ("Lote", "lotes"),
    ("PropostasComerciais", "propostas_comerciais"),
    ("Situacoes", "situacoes"),
    ("Usuarios", "usuarios"),
    ("Vendedores", "vendedores"),
    ("Vendas", "pedidos_vendas"),
)
BUILTIN_TYPE_NAMES = {
    "Any",
    "AwareDatetime",
    "BlingDate",
    "BlingModel",
    "Field",
    "None",
    "RootModel",
    "bool",
    "date",
    "dict",
    "float",
    "int",
    "list",
    "str",
}
FIELD_ANNOTATION_OVERRIDES = {
    ("SituacoesAcaoDTO", "descricao"): "str | None",
    ("SituacoesModuloDTO", "descricao"): "str | None",
    ("VendedoresGetResponse200", "data"): "list[VendedoresDadosBaseDTO] | None",
    # Bug 4: OrdensProducaoPostRequest.id should be optional on POST
    ("OrdensProducaoPostRequest", "id"): "int | None",
    # Bug 5: ContatosPostRequest.id should be optional on POST
    ("ContatosPostRequest", "id"): "int | None",
}
FIELD_NONE_DEFAULT_OVERRIDES = {
    ("SituacoesAcaoDTO", "descricao"),
    ("SituacoesModuloDTO", "descricao"),
    # Bug 4: OrdensProducaoPostRequest.situacao should be optional on POST
    ("OrdensProducaoPostRequest", "situacao"),
    # Bug 5: ContatosPostRequest.id should be optional on POST
    ("ContatosPostRequest", "id"),
}

# Type that replaces bare ``date`` in all generated annotations.
DATE_TYPE_REWRITE = "BlingDate"
DATE_IMPORT = "from bling_erp_api.models.fields import BlingDate"

# Map of model name → inner data type for wrapper generation.
# Models listed here will have their body replaced with:
#   data: <InnerType> | None = None
# If the model name does not exist in the generated schemas, a new class is
# injected (so the wrappers survive regeneration).
RESPONSE_MODEL_DATA_WRAPPERS: dict[str, str] = {
    "ContasPagarPostResponse201": "BasePostResponse",
    "ContasPagarIdContaPagarPutResponse200": "BasePostResponse",
    "DepositosIdDepositoPutResponse200": "BasePostResponse",
    "CaixasBancosSalvarLancamentoResponseDTO": "BasePostResponse",
    "CaixasBancosIdCaixaGetResponse200": "CaixasBancosLancamentoDTO",
}


@dataclass(frozen=True)
class FieldDoc:
    """Human-readable metadata for a generated Pydantic field."""

    name: str
    alias: str
    annotation: str
    required: bool
    description: str | None


def main() -> None:
    """Generate canonical schemas, resource reexports, and operation model metadata."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    _prepare_generated_dirs()

    _run_datamodel_codegen()
    class_order, class_nodes = _schema_class_nodes()

    # Inject response data wrapper models (new classes or body overwrites).
    # Must happen BEFORE _schema_class_modules so module assignment is correct.
    _inject_response_model_data_wrappers(class_order, class_nodes)

    class_names = set(class_order)
    all_contracts = _contracts_by_module(payload)
    class_modules = _schema_class_modules(class_order, all_contracts)

    _write_schema_package(class_order, class_nodes, class_modules)
    _write_resource_reexports(all_contracts, class_names, class_modules)
    _write_generated_init(class_order)
    _write_operation_models(all_contracts, class_names, class_modules)
    RAW_SCHEMAS_MODULE.unlink(missing_ok=True)
    _run_ruff_fix()


def _prepare_generated_dirs() -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    RESOURCE_REEXPORT_DIR.mkdir(parents=True, exist_ok=True)
    OPERATION_MODELS_MODULE.parent.mkdir(parents=True, exist_ok=True)
    LEGACY_SCHEMAS_MODULE.unlink(missing_ok=True)

    if SCHEMAS_PACKAGE_DIR.exists():
        shutil.rmtree(SCHEMAS_PACKAGE_DIR)
    SCHEMAS_PACKAGE_DIR.mkdir(parents=True)


def _run_datamodel_codegen() -> None:
    command = [
        _datamodel_codegen_bin(),
        "--input",
        str(SPEC_PATH),
        "--input-file-type",
        "openapi",
        "--openapi-scopes",
        "schemas",
        "paths",
        "--output",
        str(RAW_SCHEMAS_MODULE),
        "--output-model-type",
        "pydantic_v2.BaseModel",
        "--base-class",
        "bling_erp_api.models.base.BlingModel",
        "--snake-case-field",
        "--field-constraints",
        "--ignore-enum-constraints",
        "--use-standard-collections",
        "--use-union-operator",
        "--target-python-version",
        "3.14",
        "--disable-timestamp",
        "--formatters",
        "ruff-format",
        "ruff-check",
        "--no-use-type-checking-imports",
        "--use-status-code-in-response-name",
        "--use-schema-description",
        "--use-field-description",
        "--use-default-kwarg",
    ]
    subprocess.run(command, check=True)  # noqa: S603


def _datamodel_codegen_bin() -> str:
    executable = shutil.which("datamodel-codegen")
    if executable is None:
        msg = "datamodel-codegen was not found. Run `uv sync --all-groups` first."
        raise RuntimeError(msg)
    return executable


def _run_ruff_fix() -> None:
    executable = shutil.which("ruff")
    if executable is None:
        msg = "ruff was not found. Run `uv sync --all-groups` first."
        raise RuntimeError(msg)
    subprocess.run(  # noqa: S603
        [
            executable,
            "check",
            "--fix",
            "--select",
            "I001,RUF022",
            str(GENERATED_DIR),
            str(OPERATION_MODELS_MODULE),
        ],
        check=True,
    )
    subprocess.run(  # noqa: S603
        [executable, "format", str(GENERATED_DIR), str(OPERATION_MODELS_MODULE)],
        check=True,
    )


def _schema_class_nodes() -> tuple[list[str], dict[str, ast.ClassDef]]:
    tree = ast.parse(RAW_SCHEMAS_MODULE.read_text(encoding="utf-8"))
    class_order: list[str] = []
    class_nodes: dict[str, ast.ClassDef] = {}
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_order.append(node.name)
            class_nodes[node.name] = node
    return class_order, class_nodes


def _contracts_by_module(
    payload: Mapping[str, object],
) -> dict[str, list[dict[str, object]]]:
    all_contracts: dict[str, list[dict[str, object]]] = {}
    for resource in RESOURCES:
        contracts: list[dict[str, object]] = []
        resource_names = [
            resource["openapi_resource"],
            *resource.get("extra_openapi_resources", []),
        ]
        for name in resource_names:
            contracts.extend(_resource_contracts(payload, resource=name))
        contracts.sort(key=lambda item: (str(item["path"]), str(item["method"])))
        all_contracts[resource["module"]] = contracts
    return all_contracts


def _schema_class_modules(
    class_order: Sequence[str],
    all_contracts: Mapping[str, list[dict[str, object]]],
) -> dict[str, str]:
    class_names = set(class_order)
    usage = {
        module: _resource_model_names(module, contracts, class_names)
        for module, contracts in all_contracts.items()
    }
    resource_schema_modules = {
        str(resource["module"]): _camel_to_snake(str(resource["openapi_resource"]))
        for resource in RESOURCES
    }

    modules: dict[str, str] = {}
    for name in class_order:
        owners = [module for module, names in usage.items() if name in names]
        modules[name] = _schema_module_for_class(name, owners, resource_schema_modules)
    return modules


def _schema_module_for_class(
    name: str,
    owners: Sequence[str],
    resource_schema_modules: Mapping[str, str],
) -> str:
    if GENERIC_SCHEMA_NAME_RE.fullmatch(name) and owners:
        return resource_schema_modules.get(owners[0], COMMON_SCHEMA_MODULE)
    if name in COMMON_SCHEMA_NAMES or name.startswith("Error"):
        return COMMON_SCHEMA_MODULE

    for prefix, module in SCHEMA_FAMILY_PREFIXES:
        if name.startswith(prefix):
            return module

    if len(owners) == 1:
        return resource_schema_modules.get(owners[0], COMMON_SCHEMA_MODULE)
    return COMMON_SCHEMA_MODULE


def _write_schema_package(
    class_order: Sequence[str],
    class_nodes: Mapping[str, ast.ClassDef],
    class_modules: Mapping[str, str],
) -> None:
    modules = sorted(set(class_modules.values()))
    for module in modules:
        names = [name for name in class_order if class_modules[name] == module]
        (SCHEMAS_PACKAGE_DIR / f"{module}.py").write_text(
            _schema_module_content(module, names, class_nodes, class_modules),
            encoding="utf-8",
        )

    (SCHEMAS_PACKAGE_DIR / "__init__.py").write_text(
        _schema_init_content(class_order, class_modules),
        encoding="utf-8",
    )


def _schema_module_content(
    module: str,
    names: Sequence[str],
    class_nodes: Mapping[str, ast.ClassDef],
    class_modules: Mapping[str, str],
) -> str:
    class_names = set(class_nodes)
    base_deps: set[str] = set()
    annotation_deps: set[str] = set()
    rendered_classes: list[str] = []

    for name in names:
        node = _class_with_docstring(name, class_nodes)
        deps = _class_dependencies(node, class_names)
        base_deps.update(_class_base_dependencies(node, class_names))
        annotation_deps.update(deps - base_deps - set(names))
        rendered_classes.append(ast.unparse(node))

    top_imports = _schema_import_lines(base_deps, module, class_modules)
    type_checking_imports = _schema_import_lines(annotation_deps, module, class_modules)
    exports = "".join(f'    "{name}",\n' for name in sorted(names))

    lines = [
        "# ruff: noqa",
        "# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false",
        f'"""Generated OpenAPI schemas for ``{module}``. Do not edit manually."""',
        "",
        "from __future__ import annotations",
        "",
        "from bling_erp_api.models.fields import BlingDate",
        "from typing import TYPE_CHECKING, Any",
        "",
        "from pydantic import AliasChoices, AwareDatetime, Field, RootModel",
        "",
        "from bling_erp_api.models.base import BlingModel",
    ]
    if top_imports:
        lines.extend(["", *top_imports])
    if type_checking_imports:
        lines.extend(["", "if TYPE_CHECKING:", *[f"    {line}" for line in type_checking_imports]])
    lines.extend(["", "", "\n\n".join(rendered_classes), "", "__all__ = [", exports + "]", ""])
    return "\n".join(lines)


def _schema_import_lines(
    names: Iterable[str],
    current_module: str,
    class_modules: Mapping[str, str],
) -> list[str]:
    by_module: dict[str, list[str]] = {}
    for name in sorted(names):
        module = class_modules.get(name)
        if module is None or module == current_module:
            continue
        by_module.setdefault(module, []).append(name)

    lines: list[str] = []
    for module, module_names in sorted(by_module.items()):
        imports = ", ".join(sorted(module_names))
        lines.append(f"from .{module} import {imports}")
    return lines


def _schema_init_content(
    class_order: Sequence[str],
    class_modules: Mapping[str, str],
) -> str:
    by_module: dict[str, list[str]] = {}
    for name in sorted(class_order):
        by_module.setdefault(class_modules[name], []).append(name)

    lines = [
        "# ruff: noqa",
        "# pyright: reportUnsupportedDunderAll=false, reportUnknownMemberType=false",
        '"""Generated OpenAPI schema package. Do not edit manually."""',
        "",
        "from __future__ import annotations",
        "",
        "from bling_erp_api.models.fields import BlingDate",
        "from typing import Any",
        "",
        "from pydantic import AwareDatetime",
        "",
    ]
    for module, names in sorted(by_module.items()):
        imports = ", ".join(names)
        lines.append(f"from .{module} import {imports}")

    exports = "".join(f'    "{name}",\n' for name in sorted(class_order))
    lines.extend(
        [
            "",
            "__all__ = [",
            exports + "]",
            "",
            "_MODEL_NAMESPACE = {name: globals()[name] for name in __all__}",
            "_MODEL_NAMESPACE.update({'Any': Any, 'AwareDatetime': AwareDatetime, 'BlingDate': BlingDate})",
            "for _model in _MODEL_NAMESPACE.values():",
            "    if isinstance(_model, type) and hasattr(_model, 'model_rebuild'):",
            "        _model.model_rebuild(_types_namespace=_MODEL_NAMESPACE)",
            "",
        ]
    )
    return "\n".join(lines)


def _class_with_docstring(
    name: str,
    class_nodes: Mapping[str, ast.ClassDef],
) -> ast.ClassDef:
    node = cast(
        "ast.ClassDef", ast.fix_missing_locations(ast.parse(ast.unparse(class_nodes[name])).body[0])
    )

    wrapper_info = RESPONSE_MODEL_DATA_WRAPPERS.get(name)
    if wrapper_info is not None:
        # Data wrapper models replace the entire body with a single ``data``
        # field. No field alias / date / override transforms are needed.
        _rewrite_as_data_wrapper(node, wrapper_info)
    else:
        _rewrite_field_aliases(node)
        _apply_field_overrides(name, node, class_nodes=class_nodes)
        _rewrite_date_types(node)

    docstring_nodes = dict(class_nodes)
    docstring_nodes[name] = node
    docstring = _model_docstring(name, docstring_nodes)
    doc_node = ast.Expr(value=ast.Constant(value=docstring))
    existing_doc = ast.get_docstring(node, clean=False)
    if existing_doc is not None and node.body:
        node.body[0] = doc_node
    else:
        node.body.insert(0, doc_node)
    node.body = [
        stmt
        for index, stmt in enumerate(node.body)
        if index == 0 or _string_value_from_expr_stmt(stmt) is None
    ]
    return ast.fix_missing_locations(node)


def _apply_field_overrides(
    name: str,
    node: ast.ClassDef,
    class_nodes: Mapping[str, ast.ClassDef] | None = None,
) -> None:
    """Apply known runtime-contract fixes for inaccurate OpenAPI schemas."""
    # Track which overrides were actually applied (field existed in class body).
    applied_annotation_fields: set[str] = set()
    applied_default_fields: set[str] = set()

    for stmt in node.body:
        if not isinstance(stmt, ast.AnnAssign) or not isinstance(stmt.target, ast.Name):
            continue

        annotation = FIELD_ANNOTATION_OVERRIDES.get((name, stmt.target.id))
        if annotation is not None:
            stmt.annotation = ast.parse(annotation, mode="eval").body
            applied_annotation_fields.add(stmt.target.id)

        if (name, stmt.target.id) in FIELD_NONE_DEFAULT_OVERRIDES:
            _set_field_default_none(stmt)
            applied_default_fields.add(stmt.target.id)

    # Handle overrides for fields inherited from parent classes — the field
    # does not exist in this class's body, so we must insert a new declaration.
    for (override_name, field_name), annotation in FIELD_ANNOTATION_OVERRIDES.items():
        if override_name == name and field_name not in applied_annotation_fields:
            _insert_field_override_with_annotation(node, field_name, annotation)

    for override_name, field_name in FIELD_NONE_DEFAULT_OVERRIDES:
        if override_name == name and field_name not in applied_default_fields:
            _insert_field_none_default(node, field_name, class_nodes)


def _insert_field_override_with_annotation(
    node: ast.ClassDef,
    field_name: str,
    annotation: str,
) -> None:
    """Insert a new field declaration into the class body.

    Used when the override targets a field inherited from a parent class
    that is not declared in this class's body.
    """
    _remove_pass_if_empty(node)

    new_field = ast.AnnAssign(
        target=ast.Name(id=field_name, ctx=ast.Store()),
        annotation=ast.parse(annotation, mode="eval").body,
        value=ast.Constant(value=None),
        simple=1,
    )
    node.body.append(new_field)


def _insert_field_none_default(
    node: ast.ClassDef,
    field_name: str,
    class_nodes: Mapping[str, ast.ClassDef] | None = None,
) -> None:
    """Insert a field with ``= None`` default for a parent-inherited field.

    Looks up the original type from the parent class hierarchy so the
    generated type is correct (e.g. ``OrdensProducaoSituacaoDTO | None``).
    Falls back to ``Any`` if the type cannot be resolved.
    """
    _remove_pass_if_empty(node)

    # Try to find the original annotation from parent classes
    orig_annotation: ast.expr | None = None
    if class_nodes is not None:
        for base in node.bases:
            base_name = _name_from_expr(base)
            if base_name and base_name in class_nodes:
                orig_annotation = _find_field_annotation(field_name, base_name, class_nodes)
                if orig_annotation is not None:
                    break

    if orig_annotation is not None:
        # Build ``OriginalType | None``
        annotation = ast.BinOp(
            left=orig_annotation,
            op=ast.BitOr(),
            right=ast.Constant(value=None),
        )
    else:
        annotation = ast.Name(id="Any", ctx=ast.Load())

    new_field = ast.AnnAssign(
        target=ast.Name(id=field_name, ctx=ast.Store()),
        annotation=annotation,
        value=ast.Constant(value=None),
        simple=1,
    )
    node.body.append(new_field)


def _find_field_annotation(
    field_name: str,
    class_name: str,
    class_nodes: Mapping[str, ast.ClassDef],
) -> ast.expr | None:
    """Walk the class hierarchy to find the annotation expression for a field."""
    node = class_nodes.get(class_name)
    if node is None:
        return None
    for stmt in node.body:
        if (
            isinstance(stmt, ast.AnnAssign)
            and isinstance(stmt.target, ast.Name)
            and stmt.target.id == field_name
        ):
            return stmt.annotation
    for base in node.bases:
        base_name = _name_from_expr(base)
        if base_name:
            result = _find_field_annotation(field_name, base_name, class_nodes)
            if result is not None:
                return result
    return None


def _remove_pass_if_empty(node: ast.ClassDef) -> None:
    """Remove the ``pass`` statement if it's the only (non-docstring) body element."""
    node.body = [stmt for stmt in node.body if not (isinstance(stmt, ast.Pass))]


def _rewrite_date_types(node: ast.ClassDef) -> None:
    """Replace ``date`` with ``BlingDate`` in all field annotations."""
    for stmt in ast.walk(node):
        if isinstance(stmt, ast.Name) and stmt.id == "date":
            stmt.id = "BlingDate"


def _set_field_default_none(stmt: ast.AnnAssign) -> None:
    default = ast.Constant(value=None)
    if isinstance(stmt.value, ast.Call) and _name_from_expr(stmt.value.func) == "Field":
        stmt.value.args = [
            arg
            for arg in stmt.value.args
            if not (isinstance(arg, ast.Constant) and arg.value is Ellipsis)
        ]
        for keyword in stmt.value.keywords:
            if keyword.arg == "default":
                keyword.value = default
                break
        else:
            stmt.value.keywords.insert(0, ast.keyword(arg="default", value=default))
        return

    stmt.value = default


def _rewrite_field_aliases(node: ast.ClassDef) -> None:
    """Keep Python field names public while preserving Bling wire aliases."""
    for stmt in node.body:
        if not isinstance(stmt, ast.AnnAssign) or not isinstance(stmt.target, ast.Name):
            continue
        if not isinstance(stmt.value, ast.Call) or _name_from_expr(stmt.value.func) != "Field":
            continue

        field_name = stmt.target.id
        alias_keyword = next(
            (
                keyword
                for keyword in stmt.value.keywords
                if keyword.arg == "alias" and _string_value(keyword.value)
            ),
            None,
        )
        if alias_keyword is None:
            continue

        alias = _string_value(alias_keyword.value)
        if alias is None or alias == field_name:
            continue

        alias_keyword.arg = "validation_alias"
        alias_keyword.value = ast.Call(
            func=ast.Name(id="AliasChoices", ctx=ast.Load()),
            args=[
                ast.Constant(value=field_name),
                ast.Constant(value=alias),
            ],
            keywords=[],
        )
        stmt.value.keywords.append(
            ast.keyword(arg="serialization_alias", value=ast.Constant(value=alias))
        )


def _model_docstring(name: str, class_nodes: Mapping[str, ast.ClassDef]) -> str:
    fields = _model_fields(name, class_nodes)
    bases = [
        base
        for base in (_name_from_expr(base) for base in class_nodes[name].bases)
        if base and base in class_nodes
    ]
    lines = [
        f"OpenAPI schema ``{name}``.",
        "",
        "Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema",
        "quando ele aparecer como request body ou response schema nos métodos do SDK.",
    ]
    if bases:
        lines.extend(["", f"Herda campos de: {', '.join(bases)}."])

    if not fields:
        lines.extend(["", "Fields:", "    Nenhum campo documentado neste schema."])
        return "\n".join(lines)

    lines.extend(["", "Fields:"])
    for field in fields:
        required = "obrigatório" if field.required else "opcional"
        description = f" {_shorten(field.description)}" if field.description else ""
        lines.append(
            f"    {field.name}: Bling ``{field.alias}``; type ``{field.annotation}``; "
            f"{required}.{description}"
        )
    return "\n".join(lines)


def _model_fields(
    name: str,
    class_nodes: Mapping[str, ast.ClassDef],
    seen: frozenset[str] = frozenset(),
) -> list[FieldDoc]:
    if name in seen:
        return []
    node = class_nodes[name]
    fields: dict[str, FieldDoc] = {}
    next_seen = seen | {name}

    for base in node.bases:
        base_name = _name_from_expr(base)
        if base_name is not None and base_name in class_nodes:
            for field in _model_fields(base_name, class_nodes, next_seen):
                fields.setdefault(field.name, field)

    for index, stmt in enumerate(node.body):
        following_doc = None
        if index + 1 < len(node.body):
            following_doc = _string_value_from_expr_stmt(node.body[index + 1])
        field = _field_doc_from_stmt(stmt, following_doc=following_doc)
        if field is not None:
            fields[field.name] = field
    return list(fields.values())


def _field_doc_from_stmt(stmt: ast.stmt, *, following_doc: str | None = None) -> FieldDoc | None:
    if not isinstance(stmt, ast.AnnAssign) or not isinstance(stmt.target, ast.Name):
        return None
    name = stmt.target.id
    alias = name
    description: str | None = None
    required = stmt.value is None

    if isinstance(stmt.value, ast.Call) and _name_from_expr(stmt.value.func) == "Field":
        required = _field_call_is_required(stmt.value)
        for keyword in stmt.value.keywords:
            if keyword.arg in {"alias", "serialization_alias"}:
                alias = _string_value(keyword.value) or alias
            elif keyword.arg == "description":
                description = _string_value(keyword.value)
    elif stmt.value is not None:
        required = False

    return FieldDoc(
        name=name,
        alias=alias,
        annotation=ast.unparse(stmt.annotation),
        required=required,
        description=description or following_doc,
    )


def _field_call_is_required(call: ast.Call) -> bool:
    for keyword in call.keywords:
        if keyword.arg == "default":
            return isinstance(keyword.value, ast.Constant) and keyword.value.value is Ellipsis
    if call.args:
        first = call.args[0]
        return isinstance(first, ast.Constant) and first.value is Ellipsis
    return False


def _string_value(value: ast.expr) -> str | None:
    if isinstance(value, ast.Constant) and isinstance(value.value, str):
        return value.value.strip()
    return None


def _string_value_from_expr_stmt(stmt: ast.stmt) -> str | None:
    if isinstance(stmt, ast.Expr):
        return _string_value(stmt.value)
    return None


def _shorten(value: str, max_length: int = 180) -> str:
    text = re.sub(r"\s+", " ", value).strip()
    if len(text) <= max_length:
        return text
    return f"{text[: max_length - 1].rstrip()}..."


def _class_dependencies(node: ast.ClassDef, class_names: set[str]) -> set[str]:
    names: set[str] = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Name) and child.id in class_names and child.id != node.name:
            names.add(child.id)
    return names


def _class_base_dependencies(node: ast.ClassDef, class_names: set[str]) -> set[str]:
    names: set[str] = set()
    for base in node.bases:
        for child in ast.walk(base):
            if isinstance(child, ast.Name) and child.id in class_names:
                names.add(child.id)
    return names


def _write_resource_reexports(
    all_contracts: Mapping[str, list[dict[str, object]]],
    class_names: set[str],
    class_modules: Mapping[str, str],
) -> None:
    generated_modules = {path.stem for path in GENERATED_DIR.glob("*.py")}
    generated_modules.discard("__init__")
    generated_modules.discard("_schemas_raw")

    for module in sorted(generated_modules):
        path = GENERATED_DIR / f"{module}.py"
        path.unlink()

    for path in RESOURCE_REEXPORT_DIR.glob("*.py"):
        path.unlink()

    (RESOURCE_REEXPORT_DIR / "__init__.py").write_text(
        '"""Resource-scoped generated model reexports."""\n',
        encoding="utf-8",
    )

    for module, contracts in sorted(all_contracts.items()):
        names = sorted(_resource_model_names(module, contracts, class_names))
        # Include response data wrapper models that belong to this module
        # but are not automatically picked up by _resource_model_names.
        for model_name in RESPONSE_MODEL_DATA_WRAPPERS:
            if class_modules.get(model_name) == module and model_name not in names:
                names.append(model_name)
        names.sort()
        content = _reexport_module_content(module, names, class_modules)
        (GENERATED_DIR / f"{module}.py").write_text(content, encoding="utf-8")
        (RESOURCE_REEXPORT_DIR / f"{module}.py").write_text(content, encoding="utf-8")


def _resource_model_names(
    module: str,
    contracts: Sequence[Mapping[str, object]],
    class_names: set[str],
) -> set[str]:
    names: set[str] = set()
    for contract in contracts:
        for ref in _schema_refs_for_contract(contract):
            schema_name = _schema_class_name(ref, class_names)
            if schema_name is not None:
                names.add(schema_name)

        response_model = _response_model_name(contract, class_names)
        if response_model is not None:
            names.add(response_model)

        request_model = _operation_request_class_name(contract)
        if request_model in class_names:
            names.add(request_model)

        item_model = _schema_class_name(_response_item_model_name(contract), class_names)
        if item_model is not None:
            names.add(item_model)

    class_name = _class_name_for_module(module)
    if class_name in class_names:
        names.add(class_name)
    return names


def _schema_refs_for_contract(contract: Mapping[str, object]) -> set[str]:
    refs: set[str] = set()
    refs.update(cast("list[str]", contract.get("request_schema_refs") or []))
    response_refs = cast("dict[str, list[str]]", contract.get("response_schema_refs") or {})
    for values in response_refs.values():
        refs.update(values)
    return refs


def _reexport_module_content(
    module: str,
    names: Sequence[str],
    class_modules: Mapping[str, str],
) -> str:
    if not names:
        return (
            f'"""Generated model reexports for {module}. Do not edit manually."""\n\n__all__ = []\n'
        )

    by_module: dict[str, list[str]] = {}
    for name in names:
        by_module.setdefault(class_modules[name], []).append(name)

    import_lines: list[str] = []
    for schema_module, module_names in sorted(by_module.items()):
        imports = ", ".join(sorted(module_names))
        import_lines.append(
            f"from bling_erp_api.models.generated.schemas.{schema_module} import {imports}"
        )
    exports = "".join(f'    "{name}",\n' for name in names)
    return (
        f'"""Generated model reexports for {module}. Do not edit manually."""\n\n'
        "from __future__ import annotations\n\n"
        f"{'\n'.join(import_lines)}\n\n"
        "__all__ = [\n"
        f"{exports}"
        "]\n"
    )


def _write_generated_init(class_order: Sequence[str]) -> None:
    exports = "".join(f'    "{name}",\n' for name in sorted(class_order))
    (GENERATED_DIR / "__init__.py").write_text(
        '"""OpenAPI-generated Pydantic models."""\n\n'
        "# ruff: noqa\n"
        "# pyright: reportUnsupportedDunderAll=false\n\n"
        "from __future__ import annotations\n\n"
        "from bling_erp_api.models.generated.schemas import *\n"
        "\n"
        "__all__ = [\n"
        f"{exports}"
        "]\n",
        encoding="utf-8",
    )


def _write_operation_models(
    all_contracts: Mapping[str, list[dict[str, object]]],
    class_names: set[str],
    class_modules: Mapping[str, str],
) -> None:
    lines = [
        '"""Generated operation-to-model metadata. Do not edit manually."""',
        "",
        "from __future__ import annotations",
        "",
        "OPERATION_MODELS: list[dict[str, object]] = [",
    ]

    for module, contracts in sorted(all_contracts.items()):
        class_name = _class_name_for_module(module)
        for operation_name, contract in _operation_mapping(contracts).items():
            response_model = _response_model_name(contract, class_names)
            item_model = _schema_class_name(_response_item_model_name(contract), class_names)
            lines.extend(
                [
                    "    {",
                    f'        "resource_class": "{class_name}",',
                    f'        "sdk_method": "{operation_name}",',
                    f'        "method": "{contract["method"]}",',
                    f'        "path": "{contract["path"]}",',
                    f'        "pattern": r"{_path_pattern(str(contract["path"]))}",',
                    f'        "response_model": {_model_path(response_model, class_modules)},',
                    f'        "response_item_model": {_model_path(item_model, class_modules)},',
                    "    },",
                ]
            )

    lines.extend(["]", ""])
    OPERATION_MODELS_MODULE.write_text("\n".join(lines), encoding="utf-8")


def _response_model_name(
    contract: Mapping[str, object],
    class_names: set[str],
) -> str | None:
    response_refs = cast("dict[str, list[str]]", contract.get("response_schema_refs") or {})
    for status in SUCCESS_STATUS_PRIORITY:
        if status == "204" and status in response_refs:
            return None
        candidate = _operation_response_class_name(contract, status)
        if candidate in class_names:
            return candidate
        refs = response_refs.get(status)
        if refs and len(refs) == 1:
            return _schema_class_name(refs[0], class_names)
    return None


def _response_item_model_name(contract: Mapping[str, object]) -> str | None:
    response_refs = cast("dict[str, list[str]]", contract.get("response_schema_refs") or {})
    refs = response_refs.get("200")
    if not refs or len(refs) != 1:
        return None
    if str(contract.get("method")) != "GET":
        return None
    if (
        "ObterMultiplos" not in str(contract.get("action"))
        and str(contract.get("sdk_method")) != "listar"
    ):
        return None
    return refs[0]


def _operation_response_class_name(contract: Mapping[str, object], status: str) -> str:
    path_name = _classify_path(str(contract["path"]))
    method_name = str(contract["method"]).lower().capitalize()
    return f"{path_name}{method_name}Response{status}"


def _operation_request_class_name(contract: Mapping[str, object]) -> str:
    path_name = _classify_path(str(contract["path"]))
    method_name = str(contract["method"]).lower().capitalize()
    return f"{path_name}{method_name}Request"


def _classify_path(path: str) -> str:
    parts = re.split(r"[^0-9A-Za-z]+", path.strip("/"))
    return "".join(_classify_part(part) for part in parts if part)


def _classify_part(part: str) -> str:
    clean = part.strip("{}")
    if not clean:
        return ""
    return clean[0].upper() + clean[1:]


def _path_pattern(path: str) -> str:
    pattern = re.sub(r"\{[^/{}]+\}", r"[^/]+", path.rstrip("/"))
    return f"^{pattern}/?$"


def _model_path(name: str | None, class_modules: Mapping[str, str]) -> str:
    if name is None:
        return "None"
    module = class_modules[name]
    return f'"bling_erp_api.models.generated.schemas.{module}.{name}"'


def _schema_class_name(ref: str | None, class_names: set[str]) -> str | None:
    if ref is None:
        return None
    if ref in class_names:
        return ref
    sanitized = re.sub(r"[^0-9A-Za-z]", "", ref)
    if sanitized in class_names:
        return sanitized
    return None


def _name_from_expr(expr: ast.expr) -> str | None:
    if isinstance(expr, ast.Name):
        return expr.id
    if isinstance(expr, ast.Attribute):
        return expr.attr
    if isinstance(expr, ast.Subscript):
        return _name_from_expr(expr.value)
    return None


def _camel_to_snake(value: str) -> str:
    value = re.sub(r"[^0-9A-Za-z]+", "_", value)
    value = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    return value.strip("_").lower() or COMMON_SCHEMA_MODULE


def _rewrite_as_data_wrapper(node: ast.ClassDef, inner_type: str) -> None:
    """Replace class body with ``data: <inner_type> | None = None``.

    Clears all existing fields, sets the base to ``BlingModel``, and
    creates a single annotation: ``data: <inner_type> | None = None``.
    """
    node.body.clear()

    # Build: data: <inner_type> | None
    annotation: ast.expr = ast.BinOp(
        left=ast.Name(id=inner_type, ctx=ast.Load()),
        op=ast.BitOr(),
        right=ast.Constant(value=None),
    )

    node.body.append(
        ast.AnnAssign(
            target=ast.Name(id="data", ctx=ast.Store()),
            annotation=annotation,
            value=ast.Constant(value=None),
            simple=1,
        )
    )

    node.bases = [ast.Name(id="BlingModel", ctx=ast.Load())]


def _inject_response_model_data_wrappers(
    class_order: list[str],
    class_nodes: dict[str, ast.ClassDef],
) -> None:
    """Inject ``ast.ClassDef`` stubs for wrapper models not yet in ``class_nodes``.

    Existing models (already generated by datamodel-codegen) are left as-is;
    their body will be replaced later in ``_class_with_docstring`` via
    ``_rewrite_as_data_wrapper``.
    """
    for model_name in RESPONSE_MODEL_DATA_WRAPPERS:
        if model_name not in class_nodes:
            # Needs a body statement so ast.unparse → ast.parse round-trip works.
            node = ast.ClassDef(
                name=model_name,
                bases=[ast.Name(id="BlingModel", ctx=ast.Load())],
                keywords=[],
                body=[ast.Pass()],
                decorator_list=[],
                type_params=[],
            )
            class_order.append(model_name)
            class_nodes[model_name] = node


if __name__ == "__main__":
    main()
