"""Pydantic contracts derived from the Bling OpenAPI document."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from bling_erp_api.models.base import BlingModel

ParameterLocation = Literal["query", "path", "body"]
HttpMethod = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]


class ParameterContract(BlingModel):
    """Contract for an operation parameter exposed by the SDK."""

    name: str
    location: ParameterLocation
    sdk_name: str
    required: bool = False
    description: str | None = None
    schema_type: str | None = None
    schema_format: str | None = None


class OperationContract(BlingModel):
    """Contract for one SDK method backed by one OpenAPI operation."""

    sdk_method: str
    method: HttpMethod
    path: str
    resource: str
    action: str
    summary: str
    description: str | None = None
    parameters: list[ParameterContract] = Field(default_factory=list)
    request_schema_refs: list[str] = Field(default_factory=list)
    response_schema_refs: dict[str, list[str]] = Field(default_factory=dict)
