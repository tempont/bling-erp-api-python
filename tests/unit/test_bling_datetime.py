"""Regression tests for Bling timestamps without UTC offsets."""

from __future__ import annotations

import inspect
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING, cast

import httpx
import pytest
from pydantic import TypeAdapter, ValidationError

from bling_erp_api import BlingClient
from bling_erp_api.models.fields import BlingDatetime
from bling_erp_api.models.generated.schemas.logisticas_objetos import (
    LogisticasObjetosIdObjetoGetResponse200,
    LogisticasObjetosRastreamentoDTO,
)
from bling_erp_api.models.generated.schemas.logisticas_remessas import (
    LogisticasRemessasIdRemessaGetResponse200,
    LogisticasRemessasRastreamentoDTO,
)
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from pytest_httpx import HTTPXMock

    from bling_erp_api.types import JsonObject

FIXTURE = Path(__file__).parents[1] / "fixtures/responses/logisticas_objetos_get.json"
TRACKING_MODELS = (LogisticasObjetosRastreamentoDTO, LogisticasRemessasRastreamentoDTO)


def _object_payload() -> JsonObject:
    return cast("JsonObject", json.loads(FIXTURE.read_text(encoding="utf-8")))


@pytest.mark.parametrize(
    ("value", "offset"),
    [
        ("2026-10-07 11:24:02", -3),
        ("2026-10-07T11:24:02.123456", -3),
        (datetime(2026, 10, 7, 11, 24, 2), -3),  # noqa: DTZ001
        ("2018-12-01 12:00:00", -2),
        ("2026-10-07T14:24:02Z", 0),
        ("2026-10-07T11:24:02-04:00", -4),
        (datetime(2026, 10, 7, 14, 24, 2, tzinfo=UTC), 0),
    ],
)
def test_bling_datetime_assigns_local_timezone_and_preserves_offsets(
    value: str | datetime, offset: int
) -> None:
    """Offset-free dates use Sao Paulo rules; explicit offsets are preserved."""
    parsed = TypeAdapter[datetime](BlingDatetime).validate_python(value)
    assert parsed.utcoffset() == timedelta(hours=offset)
    if isinstance(value, datetime) and value.tzinfo is not None:
        assert parsed is value


@pytest.mark.parametrize("value", ["not-a-date", "2026-02-30 12:00:00", "", None])
def test_bling_datetime_rejects_invalid_timestamps(value: object) -> None:
    """Do not turn malformed timestamps into silently accepted data."""
    with pytest.raises(ValidationError):
        TypeAdapter[datetime](BlingDatetime).validate_python(value)


@pytest.mark.parametrize("model_type", TRACKING_MODELS)
def test_tracking_models_accept_wire_and_python_field_names(
    model_type: type[LogisticasObjetosRastreamentoDTO | LogisticasRemessasRastreamentoDTO],
) -> None:
    """Both affected DTOs parse aliases and serialize aware ISO timestamps."""
    payload = cast("JsonObject", cast("JsonObject", _object_payload()["data"])["rastreamento"])
    wire = model_type.model_validate(payload)
    python_payload = {**payload}
    python_payload["ultima_alteracao"] = python_payload.pop("ultimaAlteracao")
    python_model = model_type.model_validate(python_payload)
    assert python_model == wire
    assert wire.ultima_alteracao.utcoffset() == timedelta(hours=-3)
    assert "ultima_alteracao" in inspect.signature(model_type).parameters
    assert "ultimaAlteracao" not in inspect.signature(model_type).parameters
    serialized = to_json_object(wire)
    assert serialized["ultimaAlteracao"] == "2026-10-07T11:24:02-03:00"
    assert "ultima_alteracao" not in serialized
    assert model_type.model_validate(serialized) == wire
    with pytest.raises(ValidationError, match="Conflicting values"):
        model_type.model_validate({**payload, "ultima_alteracao": "2026-10-08 11:24:02"})


@pytest.mark.parametrize("english_alias", [False, True])
def test_logistics_object_resource_parses_naive_datetime(
    httpx_mock: HTTPXMock, *, english_alias: bool
) -> None:
    """Exercise the public resource's two validation passes without live API calls."""
    httpx_mock.add_response(json=_object_payload())
    with BlingClient(auth=httpx.Auth()) as client:
        response = (
            client.logisticas_objetos.get(object_id=701)
            if english_alias
            else client.logisticas_objetos.obter(id_objeto=701)
        )
    assert isinstance(response, LogisticasObjetosIdObjetoGetResponse200)
    assert response.data is not None
    assert response.data.rastreamento is not None
    assert response.data.rastreamento.ultima_alteracao.isoformat() == "2026-10-07T11:24:02-03:00"
    request = httpx_mock.get_request()
    assert request is not None
    assert request.method == "GET"
    assert request.url.path == "/Api/v3/logisticas/objetos/701"
    assert not request.url.query
    assert request.content == b""


def test_logistics_shipment_resource_parses_nested_naive_datetime(httpx_mock: HTTPXMock) -> None:
    """Remessas share the same timestamp issue inside objetos[].rastreamento."""
    obj = cast("JsonObject", _object_payload()["data"])
    obj["servico"] = {"id": 301, "nome": "Synthetic service", "codigo": "TEST"}
    payload = {
        "data": {
            "id": 501,
            "numeroPlp": "PLP-TEST",
            "situacao": 1,
            "descricao": "Synthetic shipment",
            "dataCriacao": "2026-10-07",
            "logistica": {"id": 301},
            "objetos": [{"id": 701, **obj}],
        },
    }
    httpx_mock.add_response(json=payload)
    with BlingClient(auth=httpx.Auth()) as client:
        response = client.logisticas_remessas.obter(id_remessa=501)
    assert isinstance(response, LogisticasRemessasIdRemessaGetResponse200)
    assert response.data is not None
    assert response.data.objetos[0].rastreamento.ultima_alteracao.utcoffset() == timedelta(hours=-3)
