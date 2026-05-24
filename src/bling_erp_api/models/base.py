"""Base model configuration."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class BlingModel(BaseModel):
    """Base class for hand-written and generated models."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)
