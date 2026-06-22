"""Example: Get a single store category binding."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.store_categories import (
        CategoriasLojasIdCategoriaLojaGetResponse200,
    )


def obter_categoria_loja(
    id_categoria_loja: int,
) -> CategoriasLojasIdCategoriaLojaGetResponse200:
    """Obtém uma categoria de loja pelo ID."""
    with BlingClient.from_env() as client:
        return client.categorias_lojas.obter(id_categoria_loja=id_categoria_loja)


def main() -> None:
    """Demonstrate getting a store category binding."""
    result = obter_categoria_loja(123456)
    print(result.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
