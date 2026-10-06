"""Response-only invoice contact validation, using fictional HTTP fixtures."""

from __future__ import annotations

import json
from inspect import signature
from pathlib import Path
from typing import TYPE_CHECKING, cast

import httpx
import pytest
from pydantic import ValidationError

from bling_erp_api import BlingClient
from bling_erp_api.models.aliases import (
    NfeIdNotaFiscalGetResponse200,
    NotasFiscaisContatoResponseDTO,
)
from bling_erp_api.models.generated.invoices import (
    NfeGetResponse200,
    NfeIdNotaFiscalPutRequest,
    NfePostRequest,
)
from bling_erp_api.models.generated.nfce import (
    NfceGetResponse200,
    NfceIdNotaFiscalConsumidorGetResponse200,
    NfceIdNotaFiscalConsumidorPutRequest,
    NfcePostRequest,
)
from bling_erp_api.models.generated.schemas.notas_fiscais import NotasFiscaisContatoDTO
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from pydantic import BaseModel


FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "responses"


def _invoice_payload() -> dict[str, object]:
    return cast(
        "dict[str, object]",
        json.loads((FIXTURES / "nfe_get_read_contact.json").read_text(encoding="utf-8")),
    )


def _contact(payload: dict[str, object]) -> dict[str, object]:
    data = cast("dict[str, object]", payload["data"])
    return cast("dict[str, object]", data["contato"])


def _mock_client(payload: dict[str, object], calls: list[httpx.Request]) -> BlingClient:
    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        if int(request.url.params.get("pagina", "1")) > 1:
            return httpx.Response(200, json={"data": []})
        return httpx.Response(200, json=payload)

    return BlingClient(
        auth=httpx.BasicAuth("synthetic", "synthetic"),
        http_client=httpx.Client(
            base_url="https://api.bling.test/Api/v3",
            transport=httpx.MockTransport(handler),
        ),
    )


@pytest.mark.parametrize("with_write_fields", [False, True])
@pytest.mark.parametrize("english_alias", [False, True])
def test_public_invoice_read(*, with_write_fields: bool, english_alias: bool) -> None:
    """Public reads parse missing or present writeOnly fields through real transport."""
    payload = _invoice_payload()
    if with_write_fields:
        _contact(payload).update({"tipoPessoa": "J", "contribuinte": 1})
    calls: list[httpx.Request] = []
    with _mock_client(payload, calls) as client:
        response = (
            client.invoices.get(invoice_id=12345)
            if english_alias
            else client.notas_fiscais.obter(id_nota_fiscal=12345)
        )

    assert isinstance(response, NfeIdNotaFiscalGetResponse200)
    invoice = response.data
    assert invoice is not None
    assert invoice.id == 12345
    assert invoice.contato.tipo_pessoa == ("J" if with_write_fields else None)
    assert invoice.contato.contribuinte == (1 if with_write_fields else None)
    assert invoice.contato.numero_documento == "00000000000000"
    assert invoice.itens is not None
    assert invoice.itens[0].codigo == "PROD-001"
    assert invoice.transporte is not None
    assert invoice.transporte.volumes is not None
    assert invoice.transporte.volumes[0].id == 501
    assert invoice.transporte.volumes[0].model_extra == {"codigoRastreamento": "TESTE000001BR"}
    serialized = to_json_object(invoice.contato)
    if with_write_fields:
        assert serialized["tipoPessoa"] == "J"
        assert serialized["contribuinte"] == 1
    else:
        assert "tipoPessoa" not in serialized
        assert "contribuinte" not in serialized
        assert "tipo_pessoa" not in invoice.contato.model_fields_set
        assert "contribuinte" not in invoice.contato.model_fields_set
    assert len(calls) == 1
    assert calls[0].method == "GET"
    assert calls[0].url.path == "/Api/v3/nfe/12345"
    assert not calls[0].url.query
    assert calls[0].content == b""


@pytest.mark.parametrize(
    ("field", "value", "error_type"),
    [
        ("nome", None, "missing"),
        ("numeroDocumento", None, "missing"),
        ("nome", [], "string_type"),
        ("tipoPessoa", [], "string_type"),
        ("contribuinte", "invalid", "int_parsing"),
        ("id", "invalid", "int_parsing"),
    ],
)
def test_public_invoice_read_rejects_invalid_contact(
    field: str, value: object, error_type: str
) -> None:
    """Invalid response data still fails, inspecting sanitized error metadata only."""
    payload = _invoice_payload()
    contact = _contact(payload)
    if value is None:
        contact.pop(field)
    else:
        contact[field] = value
    with _mock_client(payload, []) as client, pytest.raises(ValidationError) as caught:
        client.notas_fiscais.obter(id_nota_fiscal=12345)
    errors = caught.value.errors(include_input=False, include_context=False, include_url=False)
    assert [(error["loc"], error["type"]) for error in errors] == [
        (
            (
                "data",
                "contato",
                {"tipoPessoa": "tipo_pessoa", "numeroDocumento": "numero_documento"}.get(
                    field, field
                ),
            ),
            error_type,
        )
    ]


@pytest.mark.parametrize("resource", ["nfe", "nfce"])
def test_other_invoice_read_paths(resource: str) -> None:
    """Lists, pagination, and NFC-e detail share the same response-only contract."""
    payload = _invoice_payload()
    with _mock_client(payload, []) as client:
        if resource == "nfce":
            response = client.notas_fiscais_consumidor.obter(id_nota_fiscal_consumidor=12345)
            assert isinstance(response, NfceIdNotaFiscalConsumidorGetResponse200)
            assert response.data is not None
            assert response.data.contato.tipo_pessoa is None
    listing: dict[str, object] = {"data": [payload["data"]]}
    calls: list[httpx.Request] = []
    with _mock_client(listing, calls) as client:
        invoices = client.notas_fiscais if resource == "nfe" else client.notas_fiscais_consumidor
        response = invoices.listar()
        assert isinstance(response, (NfceGetResponse200, NfeGetResponse200))
        assert response.data is not None
        assert response.data[0].contato.contribuinte is None
        records = list(invoices.iterar(limite=100))
        assert len(records) == 1
        assert cast("dict[str, object]", records[0]["contato"])["tipo_pessoa"] is None
    assert all(request.url.path == f"/Api/v3/{resource}" for request in calls)


@pytest.mark.parametrize(
    "model",
    [
        NfePostRequest,
        NfeIdNotaFiscalPutRequest,
        NfcePostRequest,
        NfceIdNotaFiscalConsumidorPutRequest,
    ],
)
@pytest.mark.parametrize("missing", ["tipoPessoa", "contribuinte"])
def test_invoice_writes_still_require_contact_fields(model: type[BaseModel], missing: str) -> None:
    """All NF-e and NFC-e POST/PUT models retain their required contact fields."""
    data = cast("dict[str, object]", _invoice_payload()["data"])
    contact = cast("dict[str, object]", data["contato"])
    contact.update({"tipoPessoa": "J", "contribuinte": 1})
    # The response transport shape differs from the request transport shape.
    data.pop("transporte")
    model.model_validate(data)
    contact.pop(missing)
    with pytest.raises(ValidationError) as caught:
        model.model_validate(data)
    errors = caught.value.errors(include_input=False, include_context=False, include_url=False)
    expected = "tipo_pessoa" if missing == "tipoPessoa" else "contribuinte"
    assert [(error["loc"], error["type"]) for error in errors] == [
        (("contato", expected), "missing")
    ]
    assert NotasFiscaisContatoDTO.model_fields[expected].is_required()


def test_response_contact_alias_contract() -> None:
    """Response variants retain snake_case signatures, aliases, extras and conflicts."""
    contact = NotasFiscaisContatoResponseDTO(
        nome="CLIENTE SINTETICO", numero_documento="00000000000000", tipo_pessoa="J", contribuinte=1
    )
    serialized = to_json_object(contact)
    assert serialized["numeroDocumento"] == "00000000000000"
    assert serialized["tipoPessoa"] == "J"
    parsed = NotasFiscaisContatoResponseDTO.model_validate(
        {**serialized, "novoCampo": "preservado"}
    )
    assert parsed.tipo_pessoa == "J"
    assert parsed.model_extra == {"novoCampo": "preservado"}
    parameters = signature(NotasFiscaisContatoResponseDTO).parameters
    assert "tipo_pessoa" in parameters
    assert "numero_documento" in parameters
    assert "tipoPessoa" not in parameters
    assert "numeroDocumento" not in parameters
    with pytest.raises(ValidationError):
        NotasFiscaisContatoResponseDTO.model_validate({**serialized, "tipo_pessoa": "F"})
