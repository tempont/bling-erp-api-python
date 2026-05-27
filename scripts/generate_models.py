"""Generate Pydantic models from the local Bling OpenAPI reference."""

# pyright: reportPrivateUsage=false

from __future__ import annotations

import ast
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING, cast

from generate_openapi_contracts import (
    RESOURCES,
    _class_name_for_module,
    _operation_mapping,
    _resource_contracts,
)

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

SPEC_PATH = Path("specs/bling-openapi-reference.json")
GENERATED_DIR = Path("src/bling_erp_api/models/generated")
RESOURCE_REEXPORT_DIR = GENERATED_DIR / "resources"
SCHEMAS_MODULE = GENERATED_DIR / "schemas.py"
OPERATION_MODELS_MODULE = Path("src/bling_erp_api/contracts/generated/_operation_models.py")

SUCCESS_STATUS_PRIORITY = ("200", "201", "202", "204")


def main() -> None:
    """Generate canonical schemas, resource reexports, and operation model metadata."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    RESOURCE_REEXPORT_DIR.mkdir(parents=True, exist_ok=True)
    OPERATION_MODELS_MODULE.parent.mkdir(parents=True, exist_ok=True)

    _run_datamodel_codegen()
    class_names = _append_schema_exports()
    all_contracts = _contracts_by_module(payload)
    _write_resource_reexports(all_contracts, class_names)
    _write_generated_init()
    _write_operation_models(all_contracts, class_names)
    _run_ruff_fix()


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
        str(SCHEMAS_MODULE),
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


def _append_schema_exports() -> list[str]:
    source = SCHEMAS_MODULE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    class_names = sorted(node.name for node in tree.body if isinstance(node, ast.ClassDef))
    exports = "\n\n__all__ = [\n" + "".join(f'    "{name}",\n' for name in class_names) + "]\n"
    SCHEMAS_MODULE.write_text(
        "# ruff: noqa: D100, ERA001, FBT003, RUF001, RUF022, TC003\n"
        "# pyright: reportIncompatibleVariableOverride=false\n"
        f"{source}{exports}",
        encoding="utf-8",
    )
    return class_names


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


def _write_resource_reexports(
    all_contracts: Mapping[str, list[dict[str, object]]],
    class_names: Sequence[str],
) -> None:
    class_set = set(class_names)
    generated_modules = {path.stem for path in GENERATED_DIR.glob("*.py")}
    generated_modules.discard("__init__")
    generated_modules.discard("schemas")

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
        names = sorted(_resource_model_names(module, contracts, class_set))
        content = _reexport_module_content(module, names)
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


def _reexport_module_content(module: str, names: Sequence[str]) -> str:
    if not names:
        return (
            f'"""Generated model reexports for {module}. Do not edit manually."""\n\n__all__ = []\n'
        )
    imports = ",\n    ".join(names)
    exports = "".join(f'    "{name}",\n' for name in names)
    return (
        f'"""Generated model reexports for {module}. Do not edit manually."""\n\n'
        "from __future__ import annotations\n\n"
        "from bling_erp_api.models.generated.schemas import (\n"
        f"    {imports},\n"
        ")\n\n"
        "__all__ = [\n"
        f"{exports}"
        "]\n"
    )


def _write_generated_init() -> None:
    (GENERATED_DIR / "__init__.py").write_text(
        '"""OpenAPI-generated Pydantic models."""\n\n'
        "# pyright: reportUnsupportedDunderAll=false\n\n"
        "from __future__ import annotations\n\n"
        "from importlib import import_module\n\n"
        '_schemas = import_module("bling_erp_api.models.generated.schemas")\n\n'
        "__all__ = list(_schemas.__all__)\n\n\n"
        "def __getattr__(name: str) -> object:\n"
        "    if name in __all__:\n"
        "        return getattr(_schemas, name)\n"
        "    raise AttributeError(name)\n",
        encoding="utf-8",
    )


def _write_operation_models(
    all_contracts: Mapping[str, list[dict[str, object]]],
    class_names: Sequence[str],
) -> None:
    class_set = set(class_names)
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
            response_model = _response_model_name(contract, class_set)
            item_model = _schema_class_name(_response_item_model_name(contract), class_set)
            lines.extend(
                [
                    "    {",
                    f'        "resource_class": "{class_name}",',
                    f'        "sdk_method": "{operation_name}",',
                    f'        "method": "{contract["method"]}",',
                    f'        "path": "{contract["path"]}",',
                    f'        "pattern": r"{_path_pattern(str(contract["path"]))}",',
                    f'        "response_model": {_model_path(response_model)},',
                    f'        "response_item_model": {_model_path(item_model)},',
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


def _model_path(name: str | None) -> str:
    if name is None:
        return "None"
    return f'"bling_erp_api.models.generated.schemas.{name}"'


def _schema_class_name(ref: str | None, class_names: set[str]) -> str | None:
    if ref is None:
        return None
    if ref in class_names:
        return ref
    sanitized = re.sub(r"[^0-9A-Za-z]", "", ref)
    if sanitized in class_names:
        return sanitized
    return None


if __name__ == "__main__":
    main()
