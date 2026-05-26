"""Model mapping tests for contatos."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.contacts import (
    ContactListResponse,
    ContactResponse,
    ContactTypeListResponse,
)

FIXTURE_LIST = Path("tests/fixtures/responses/contact_list.json")
FIXTURE_OBTER = Path("tests/fixtures/responses/contact_obter.json")
FIXTURE_TYPES = Path("tests/fixtures/responses/contact_types_list.json")


def test_contact_list_fixture() -> None:
    """Deserializa uma resposta típica de ``GET /contatos``."""
    payload = json.loads(FIXTURE_LIST.read_text(encoding="utf-8"))
    response = ContactListResponse.model_validate(payload)
    assert len(response.data) == 1
    row = response.data[0]
    assert row.id == 123456789
    assert row.name == "Cliente Modelo Ltda."
    assert row.status == "A"
    assert row.person_type == "J"


def test_contact_obter_fixture() -> None:
    """Deserializa ``GET /contatos/{id}``."""
    payload = json.loads(FIXTURE_OBTER.read_text(encoding="utf-8"))
    response = ContactResponse.model_validate(payload)
    assert response.data.id == 123456789
    assert response.data.contact_types is not None
    assert len(response.data.contact_types) == 1
    assert response.data.contact_types[0].id == 10
    assert response.data.contact_types[0].description == "Cliente"


def test_contact_types_list_fixture() -> None:
    """Deserializa ``GET /contatos/tipos``."""
    payload = json.loads(FIXTURE_TYPES.read_text(encoding="utf-8"))
    response = ContactTypeListResponse.model_validate(payload)
    assert len(response.data) == 2
    assert response.data[0].description == "Cliente"
