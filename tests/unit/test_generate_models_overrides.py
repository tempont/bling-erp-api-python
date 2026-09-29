"""Tests for the field-override guard in ``scripts/generate_models.py``."""

from __future__ import annotations

import ast
import importlib.util
import re
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Iterator
    from types import ModuleType

# Use importlib to load the generator scripts since scripts/ has no __init__.py
# and uv run pytest does not make it importable as a package. The contracts
# script is registered in sys.modules so generate_models' bare import resolves.
_scripts_dir = Path(__file__).resolve().parents[2] / "scripts"
_contracts_path = _scripts_dir / "generate_openapi_contracts.py"
_contracts_spec = importlib.util.spec_from_file_location(
    "generate_openapi_contracts", _contracts_path
)
assert _contracts_spec is not None, f"Could not load spec from {_contracts_path}"
assert _contracts_spec.loader is not None, f"Loader is None for spec from {_contracts_path}"
_contracts_module = importlib.util.module_from_spec(_contracts_spec)
sys.modules[_contracts_spec.name] = _contracts_module
_contracts_spec.loader.exec_module(_contracts_module)

_gen_path = _scripts_dir / "generate_models.py"
_gen_spec = importlib.util.spec_from_file_location("generate_models", _gen_path)
assert _gen_spec is not None, f"Could not load spec from {_gen_path}"
assert _gen_spec.loader is not None, f"Loader is None for spec from {_gen_path}"
_gen_module = importlib.util.module_from_spec(_gen_spec)
sys.modules[_gen_spec.name] = _gen_module
_gen_spec.loader.exec_module(_gen_module)


@pytest.fixture
def override_guard() -> Iterator[ModuleType]:
    """Snapshot the guard's module state and restore it after each test."""
    module = _gen_module
    saved_applied = set(module._APPLIED_FIELD_OVERRIDES)  # noqa: SLF001
    saved_annotations = dict(module.FIELD_ANNOTATION_OVERRIDES)
    saved_defaults = set(module.FIELD_NONE_DEFAULT_OVERRIDES)
    module._APPLIED_FIELD_OVERRIDES.clear()  # noqa: SLF001
    try:
        yield module
    finally:
        module._APPLIED_FIELD_OVERRIDES.clear()  # noqa: SLF001
        module._APPLIED_FIELD_OVERRIDES.update(saved_applied)  # noqa: SLF001
        module.FIELD_ANNOTATION_OVERRIDES.clear()
        module.FIELD_ANNOTATION_OVERRIDES.update(saved_annotations)
        module.FIELD_NONE_DEFAULT_OVERRIDES.clear()
        module.FIELD_NONE_DEFAULT_OVERRIDES.update(saved_defaults)


def _applied_for_current_overrides(module: ModuleType) -> set[tuple[str, str]]:
    annotations = module.FIELD_ANNOTATION_OVERRIDES
    defaults = module.FIELD_NONE_DEFAULT_OVERRIDES
    return set(annotations) | set(defaults)


def _call_name(func: ast.expr) -> str:
    """Return the bare name of a ``Name`` function expression."""
    assert isinstance(func, ast.Name)
    return func.id


_PARENT_WITH_FIELD_SOURCE = """\
class ParentDTO(BlingModel):
    x: str = Field(
        default="...",
        validation_alias=AliasChoices("x", "xStr"),
        serialization_alias="xStr",
    )


class ChildDTO(ParentDTO):
    pass
"""


_PARENT_RAW_ALIAS_FIELD_SOURCE = """\
class ParentDTO(BlingModel):
    x: str = Field(default="...", alias="xStr")


class ChildDTO(ParentDTO):
    pass
"""


def _parent_child_classes() -> tuple[ast.ClassDef, ast.ClassDef]:
    """Build a parent class carrying ``Field`` metadata and a child body without ``x``."""
    classes = {
        stmt.name: stmt
        for stmt in ast.parse(_PARENT_WITH_FIELD_SOURCE).body
        if isinstance(stmt, ast.ClassDef)
    }
    return classes["ParentDTO"], classes["ChildDTO"]


def _child_x_fields(node: ast.ClassDef) -> list[ast.AnnAssign]:
    """Return the ``AnnAssign`` statements for field ``x`` in the class body."""
    return [
        stmt
        for stmt in node.body
        if isinstance(stmt, ast.AnnAssign)
        and isinstance(stmt.target, ast.Name)
        and stmt.target.id == "x"
    ]


def _assert_x_field_metadata(inserted: ast.AnnAssign) -> None:
    """Assert the inserted field redeclares ``x`` keeping the parent metadata."""
    value = inserted.value
    assert isinstance(value, ast.Call)
    assert _call_name(value.func) == "Field"
    keywords = {keyword.arg: keyword.value for keyword in value.keywords}
    default = keywords["default"]
    assert isinstance(default, ast.Constant)
    assert default.value is None
    alias_call = keywords["validation_alias"]
    assert isinstance(alias_call, ast.Call)
    assert _call_name(alias_call.func) == "AliasChoices"
    assert [arg.value for arg in alias_call.args if isinstance(arg, ast.Constant)] == ["x", "xStr"]
    serialization_alias = keywords["serialization_alias"]
    assert isinstance(serialization_alias, ast.Constant)
    assert serialization_alias.value == "xStr"


def test_check_passes_when_all_override_keys_applied(override_guard: ModuleType) -> None:
    """Every key applied means the guard returns without exiting."""
    module = override_guard
    module._APPLIED_FIELD_OVERRIDES.update(  # noqa: SLF001
        _applied_for_current_overrides(module)
    )

    module._check_field_overrides_applied()  # noqa: SLF001


def test_check_fails_on_dead_class_key(override_guard: ModuleType) -> None:
    """A bogus class key exits listing dead keys sorted, naming both tables."""
    module = override_guard
    module.FIELD_ANNOTATION_OVERRIDES[("ClasseBInexistenteDTO", "campo")] = "str | None"
    module.FIELD_ANNOTATION_OVERRIDES[("ClasseAInexistenteDTO", "campo")] = "str | None"
    applied = _applied_for_current_overrides(module)
    applied -= {("ClasseAInexistenteDTO", "campo"), ("ClasseBInexistenteDTO", "campo")}
    module._APPLIED_FIELD_OVERRIDES.update(applied)  # noqa: SLF001

    with pytest.raises(SystemExit) as excinfo:
        module._check_field_overrides_applied()  # noqa: SLF001

    message = str(excinfo.value)
    assert "ClasseAInexistenteDTO.campo" in message
    assert "ClasseBInexistenteDTO.campo" in message
    assert message.index("ClasseAInexistenteDTO.campo") < message.index(
        "ClasseBInexistenteDTO.campo"
    )
    assert "FIELD_ANNOTATION_OVERRIDES" in message
    assert "FIELD_NONE_DEFAULT_OVERRIDES" in message


def test_check_fails_on_dead_field_key(override_guard: ModuleType) -> None:
    """A field key absent from the applied set exits listing ``Class.field``."""
    module = override_guard
    dead_key = ("ProdutosImagemInternaDTO", "link_miniatura")
    applied = _applied_for_current_overrides(module)
    applied.discard(dead_key)
    module._APPLIED_FIELD_OVERRIDES.update(applied)  # noqa: SLF001

    with pytest.raises(SystemExit) as excinfo:
        module._check_field_overrides_applied()  # noqa: SLF001

    assert "ProdutosImagemInternaDTO.link_miniatura" in str(excinfo.value)


def test_apply_records_body_match_and_skips_field_absent_from_parents(
    override_guard: ModuleType,
) -> None:
    """Body-matched fields are recorded; body/parent-absent fields are not inserted."""
    module = override_guard
    module.FIELD_ANNOTATION_OVERRIDES.clear()
    module.FIELD_ANNOTATION_OVERRIDES.update(
        {
            ("ExemploDTO", "campo_morto"): "str | None",
            ("ExemploDTO", "campo_vivo"): "str | None",
        }
    )
    node = ast.parse("class ExemploDTO(BlingModel):\n    campo_vivo: str\n").body[0]
    assert isinstance(node, ast.ClassDef)

    module._apply_field_overrides("ExemploDTO", node, class_nodes={})  # noqa: SLF001

    applied = module._APPLIED_FIELD_OVERRIDES  # noqa: SLF001
    assert ("ExemploDTO", "campo_vivo") in applied
    assert ("ExemploDTO", "campo_morto") not in applied
    field_names = [
        stmt.target.id
        for stmt in node.body
        if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name)
    ]
    assert field_names == ["campo_vivo"]


def test_apply_inserts_once_with_parent_metadata_for_both_tables_key(
    override_guard: ModuleType,
) -> None:
    """A both-tables key inserts one field keeping the parent Field metadata."""
    module = override_guard
    module.FIELD_ANNOTATION_OVERRIDES[("ChildDTO", "x")] = "str | None"
    module.FIELD_NONE_DEFAULT_OVERRIDES.add(("ChildDTO", "x"))
    parent, child = _parent_child_classes()

    module._apply_field_overrides(  # noqa: SLF001
        "ChildDTO",
        child,
        class_nodes={"ParentDTO": parent},
    )

    fields = _child_x_fields(child)
    assert len(fields) == 1
    assert ast.unparse(fields[0].annotation) == "str | None"
    _assert_x_field_metadata(fields[0])
    assert ("ChildDTO", "x") in module._APPLIED_FIELD_OVERRIDES  # noqa: SLF001


def test_apply_inserts_annotation_only_key_with_parent_metadata(
    override_guard: ModuleType,
) -> None:
    """An annotation-only key inserts the field with the override annotation."""
    module = override_guard
    module.FIELD_ANNOTATION_OVERRIDES[("ChildDTO", "x")] = "int | None"
    parent, child = _parent_child_classes()

    module._apply_field_overrides(  # noqa: SLF001
        "ChildDTO",
        child,
        class_nodes={"ParentDTO": parent},
    )

    fields = _child_x_fields(child)
    assert len(fields) == 1
    assert ast.unparse(fields[0].annotation) == "int | None"
    _assert_x_field_metadata(fields[0])
    assert ("ChildDTO", "x") in module._APPLIED_FIELD_OVERRIDES  # noqa: SLF001


def test_apply_inserts_default_only_key_with_parent_metadata(
    override_guard: ModuleType,
) -> None:
    """A default-only key inserts the field annotated as the parent type ``| None``."""
    module = override_guard
    module.FIELD_NONE_DEFAULT_OVERRIDES.add(("ChildDTO", "x"))
    parent, child = _parent_child_classes()

    module._apply_field_overrides(  # noqa: SLF001
        "ChildDTO",
        child,
        class_nodes={"ParentDTO": parent},
    )

    fields = _child_x_fields(child)
    assert len(fields) == 1
    assert ast.unparse(fields[0].annotation) == "str | None"
    _assert_x_field_metadata(fields[0])
    assert ("ChildDTO", "x") in module._APPLIED_FIELD_OVERRIDES  # noqa: SLF001


def test_apply_inserts_field_exactly_once_for_both_tables_key(
    override_guard: ModuleType,
) -> None:
    """A both-tables key inserts the field exactly once (dedup regression pin)."""
    module = override_guard
    module.FIELD_ANNOTATION_OVERRIDES[("ChildDTO", "x")] = "str | None"
    module.FIELD_NONE_DEFAULT_OVERRIDES.add(("ChildDTO", "x"))
    parent = ast.parse("class ParentDTO(BlingModel):\n    x: str\n").body[0]
    child = ast.parse("class ChildDTO(ParentDTO):\n    pass\n").body[0]
    assert isinstance(parent, ast.ClassDef)
    assert isinstance(child, ast.ClassDef)

    module._apply_field_overrides(  # noqa: SLF001
        "ChildDTO",
        child,
        class_nodes={"ParentDTO": parent},
    )

    field_names = [
        stmt.target.id
        for stmt in child.body
        if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name)
    ]
    assert field_names == ["x"]
    inserted = _child_x_fields(child)[0]
    assert ast.unparse(inserted.annotation) == "str | None"
    assert isinstance(inserted.value, ast.Constant)
    assert inserted.value.value is None
    assert ("ChildDTO", "x") in module._APPLIED_FIELD_OVERRIDES  # noqa: SLF001


def _classes_from_source(source: str) -> dict[str, ast.ClassDef]:
    """Parse class definitions from ``source`` keyed by class name."""
    return {stmt.name: stmt for stmt in ast.parse(source).body if isinstance(stmt, ast.ClassDef)}


def test_apply_normalizes_raw_parent_alias_in_inserted_field(
    override_guard: ModuleType,
) -> None:
    """A raw ``alias=`` parent (the real datamodel-codegen shape) emits the normalized pair.

    Raw output carries plain ``alias="xStr"``; the inserted redeclaration must
    spell ``validation_alias=AliasChoices(...)`` + ``serialization_alias`` so
    ``to_json_object()`` (``by_alias=True``) serializes the Bling key.
    """
    module = override_guard
    module.FIELD_ANNOTATION_OVERRIDES[("ChildDTO", "x")] = "str | None"
    classes = _classes_from_source(_PARENT_RAW_ALIAS_FIELD_SOURCE)

    module._apply_field_overrides(  # noqa: SLF001
        "ChildDTO",
        classes["ChildDTO"],
        class_nodes={"ParentDTO": classes["ParentDTO"]},
    )

    fields = _child_x_fields(classes["ChildDTO"])
    assert len(fields) == 1
    _assert_x_field_metadata(fields[0])
    value = fields[0].value
    assert isinstance(value, ast.Call)
    assert {keyword.arg for keyword in value.keywords} == {
        "default",
        "validation_alias",
        "serialization_alias",
    }
    emitted = ast.unparse(fields[0])
    assert "validation_alias=AliasChoices('x', 'xStr')" in emitted
    assert "serialization_alias='xStr'" in emitted


def test_apply_falls_back_to_bare_none_for_alias_less_parent_field(
    override_guard: ModuleType,
) -> None:
    """A parent Field call without alias keywords still inserts a bare ``None``.

    Schema-documentation-only kwargs (``examples``, ``description``, …) do not
    justify cloning the parent call; this pins the byte-identical fallback.
    """
    module = override_guard
    module.FIELD_ANNOTATION_OVERRIDES[("ChildDTO", "x")] = "str | None"
    classes = _classes_from_source(
        """\
class ParentDTO(BlingModel):
    x: str = Field(default="...", examples=["demo"])


class ChildDTO(ParentDTO):
    pass
"""
    )

    module._apply_field_overrides(  # noqa: SLF001
        "ChildDTO",
        classes["ChildDTO"],
        class_nodes={"ParentDTO": classes["ParentDTO"]},
    )

    fields = _child_x_fields(classes["ChildDTO"])
    assert len(fields) == 1
    assert isinstance(fields[0].value, ast.Constant)
    assert fields[0].value.value is None


def test_schema_module_content_imports_alias_choices_for_inserted_field(
    override_guard: ModuleType,
) -> None:
    """End-to-end: the rendered module carries the ``AliasChoices`` import.

    Renders parent + child through ``_schema_module_content`` so the inserted
    field flows through the full pipeline; the normalized form must survive
    into the emitted module next to the hardcoded pydantic import line.
    """
    module = override_guard
    module.FIELD_ANNOTATION_OVERRIDES[("ChildDTO", "x")] = "str | None"
    class_nodes = _classes_from_source(_PARENT_RAW_ALIAS_FIELD_SOURCE)

    content = module._schema_module_content(  # noqa: SLF001
        "exemplo",
        ["ParentDTO", "ChildDTO"],
        class_nodes,
        {"ParentDTO": "exemplo", "ChildDTO": "exemplo"},
    )

    assert "from pydantic import AliasChoices, AwareDatetime, Field, RootModel" in content
    assert "validation_alias=AliasChoices('x', 'xStr')" in content
    assert "serialization_alias='xStr'" in content
    # ``alias='xStr'`` is a substring of ``serialization_alias='xStr'``; the
    # lookbehind only matches a bare raw ``alias`` keyword surviving the run.
    assert re.search(r"(?<![\w])alias='xStr'", content) is None
