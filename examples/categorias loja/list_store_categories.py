"""Example: List store categories."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.store_categories import (
        CategoriasLojasGetResponse200,
    )


def listar_categorias_loja(
    *,
    pagina: int = 1,
    limite: int = 10,
    id_loja: int | None = None,
) -> CategoriasLojasGetResponse200:
    """Lista categorias de lojas."""
    with BlingClient.from_env() as client:
        return client.categorias_lojas.listar(
            pagina=pagina,
            limite=limite,
            id_loja=id_loja,
        )


def main() -> None:
    """List store categories with store filter."""
    result = listar_categorias_loja(id_loja=1)
    print(result.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
