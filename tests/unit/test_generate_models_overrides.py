"""Tests for the field-override guard in ``scripts/generate_models.py``."""

from __future__ import annotations

import ast
import importlib.util
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
