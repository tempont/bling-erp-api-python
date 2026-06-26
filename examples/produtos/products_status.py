"""Example: Product Status (Situações) Workflow Examples.

Demonstrates changing product status through the Bling products API.

Endpoints:
    - PATCH /produtos/{idProduto}/situacoes
    - POST /produtos/situacoes

Docs:
    - https://developer.bling.com.br/referencia#/Produtos/patch_produtos__idProduto__situacoes
    - https://developer.bling.com.br/referencia#/Produtos/post_produtos_situacoes

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Literal

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.products import (
        ProdutosSituacoesPostResponse200,
    )


## ---------------------------------------------------------------------------
## UPDATE SINGLE PRODUCT STATUS
## ---------------------------------------------------------------------------


def update_single_product_status(product_id: int, status: Literal["A", "I", "E"]) -> None:
    """Update a single product's status (situação)."""
    with BlingClient.from_env() as client:
        client.produtos.alterar_situacao(id_produto=product_id, situacao=status)


## ---------------------------------------------------------------------------
## UPDATE MULTIPLE PRODUCTS STATUS
## ---------------------------------------------------------------------------


def update_multiple_product_status(
    product_ids: list[int], status: Literal["A", "I", "E"]
) -> ProdutosSituacoesPostResponse200:
    """Update the status of multiple products at once."""
    with BlingClient.from_env() as client:
        return client.produtos.alterar_situacao_varios(ids_produtos=product_ids, situacao=status)


def main() -> None:
    """Demonstrate product status operations."""
    # Single product status update
    product_id = 16656139131  # Exemplo — substitua pelo ID real.
    update_single_product_status(product_id, "I")  # Inativo
    time.sleep(1)

    # Reactivate the same product
    update_single_product_status(product_id, "A")  # Ativo
    time.sleep(1)

    # Multiple products status update
    response = update_multiple_product_status([16656139131, 16656139132], "I")
    print(response.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Reactivate multiple
    response = update_multiple_product_status([16656139131, 16656139132], "A")
    print(response.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
