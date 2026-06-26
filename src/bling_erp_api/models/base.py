"""Base model configuration."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, cast

from pydantic import AliasChoices, AliasPath, BaseModel, ConfigDict, model_validator

if TYPE_CHECKING:
    from pydantic.fields import FieldInfo


class BlingModel(BaseModel):
    """Base Pydantic model for Bling API data transfer objects.

    Accepts both Python snake_case field names and Bling wire-format aliases
    (camelCase) in constructors (``populate_by_name=True``). Unknown fields
    from API responses are preserved (``extra="allow"``).

    A ``model_validator`` (``_normalize_known_aliases``) resolves known field
    aliases before extras are stored. Conflicting snake_case and alias keys
    with different values raise ``ValueError`` during validation.

    Use the standalone :func:`bling_erp_api.utils.serialization.to_json_object`
    helper to serialize models back to Bling wire format.
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    @model_validator(mode="before")
    @classmethod
    def _normalize_known_aliases(cls, data: object) -> object:
        """Normalize Bling field aliases before extras are preserved."""
        if not isinstance(data, Mapping):
            return data

        raw_data = cast("Mapping[object, object]", data)
        normalized: dict[str, object] = {str(key): value for key, value in raw_data.items()}
        for field_name, field in cls.model_fields.items():
            aliases = _field_aliases(field)
            for alias in aliases:
                if alias == field_name or alias not in normalized:
                    continue

                if field_name in normalized:
                    if normalized[field_name] != normalized[alias]:
                        msg = (
                            f"Conflicting values for field '{field_name}' and "
                            f"Bling alias '{alias}'. Use the Python field name."
                        )
                        raise ValueError(msg)
                    normalized.pop(alias)
                else:
                    normalized[field_name] = normalized.pop(alias)

        return normalized


def _field_aliases(field: FieldInfo) -> set[str]:
    aliases: set[str] = set()
    if isinstance(field.alias, str):
        aliases.add(field.alias)
    if isinstance(field.serialization_alias, str):
        aliases.add(field.serialization_alias)
    aliases.update(_validation_aliases(field.validation_alias))
    return aliases


def _validation_aliases(alias: str | AliasChoices | AliasPath | None) -> set[str]:
    if isinstance(alias, str):
        return {alias}
    if isinstance(alias, AliasChoices):
        return {choice for choice in alias.choices if isinstance(choice, str)}
    if isinstance(alias, AliasPath):
        return set()
    return set()
