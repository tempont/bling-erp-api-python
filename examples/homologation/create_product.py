"""Exemplo que cria um produto da homologação usando o SDK."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


def main() -> None:
    """Cria um produto da homologação."""
    with BlingClient.from_env() as client:
        dados: JsonObject = {
            "nome": "Produto Homologação",
            "preco": 10.0,
            "codigo": "HOM-001",
        }
        response = client.homologacao.criar(dados)
        print(response)


if __name__ == "__main__":
    main()
