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
    from bling_erp_api.models.generated.products import ProdutosIdProdutoGetResponse200

## ----------------------------------------------------------------------------
## GET A PRODUCT BY ITS ID
## ----------------------------------------------------------------------------


def get_product(product_id: int) -> ProdutosIdProdutoGetResponse200:
    """Get a product by its ID."""
    client = BlingClient.from_env()
    with client:
        return client.products.obter(id_produto=product_id)


def main() -> None:
    """Get a product by its ID."""
    product_id = 16656139131  # Exemplo — substitua pelo ID real.
    print(get_product(product_id))


if __name__ == "__main__":
    main()
