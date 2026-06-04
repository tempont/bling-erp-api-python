"""Example: Product Basic Operation Examples.

Demonstrates how to use the product endpoint trough the SDK.

Endpoints:
    - GET /produtos/{idProduto}
    - PATCH /produtos/{idProduto}
    - DELETE /produtos/{idProduto}

Docs:
    - https://developer.bling.com.br/referencia#/Produtos/get_produtos__idProduto_
    - https://developer.bling.com.br/referencia#/Produtos/patch_produtos__idProduto_
    - https://developer.bling.com.br/referencia#/Produtos/delete_produtos__idProduto_

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.products import (
        ProdutosDadosDTO,
        ProdutosDadosPatchDTO,
        ProdutosIdProdutoGetResponse200,
    )

## ----------------------------------------------------------------------------
## GET A PRODUCT BY ITS ID
## ----------------------------------------------------------------------------


def get_product(product_id: int) -> ProdutosIdProdutoGetResponse200:
    """Get a product by its ID."""
    client = BlingClient.from_env()
    with client:
        return client.products.obter(id_produto=product_id)


def update_product(product_id: int, payload: ProdutosDadosDTO) -> None:
    """Update a product by ID (PUT)."""
    with BlingClient.from_env() as client:
        client.products.alterar(id_produto=product_id, dados=payload)


def update_patch_product(product_id: int, payload: ProdutosDadosPatchDTO) -> None:
    """Update a product by ID (PATCH)."""
    with BlingClient.from_env() as client:
        client.products.alterar_parcialmente(id_produto=product_id, dados=payload)


def delete_product(product_id: int) -> None:
    """Delete a product by ID."""
    with BlingClient.from_env() as client:
        client.products.remover(id_produto=product_id)


def main() -> None:
    """Get a product by its ID."""
    product_id = 16656139131  # Exemplo — substitua pelo ID real.
    print(get_product(product_id))


if __name__ == "__main__":
    main()
