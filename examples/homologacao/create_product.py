"""Exemplo que cria um produto da homologação usando o SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.homologation import HomologacaoProdutosPostResponse201

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


def main() -> None:
    """Cria um produto da homologação."""
    with BlingClient.from_env() as client:
        # NOTE: No Pydantic request model available for homologation create.
        # Using raw dict with JsonObject.
        dados: JsonObject = {
            "nome": "Produto Homologação",
            "preco": 10.0,
            "codigo": "HOM-001",
        }
        response = client.homologacao.criar(dados)
        parsed = HomologacaoProdutosPostResponse201(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
