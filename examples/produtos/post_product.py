"""Exemplo de código para criar um produto.."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.products import ProdutosDadosDTO

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


def create_product(data: ProdutosDadosDTO) -> JsonObject:
    """Cria um produto no Bling."""
    with BlingClient.from_env() as client:
        return client.products.create(data)


def main() -> None:
    """Exemplo de código para criar um produto."""
    product_data = ProdutosDadosDTO(
        codigo="123456",
        nome="Produto teste",
        descricao_curta="Um produto para testes.",
        tipo="P",
        formato="S",
        situacao="A",
        preco=10.0,
    )

    product = create_product(product_data)
    print(product)


if __name__ == "__main__":
    main()
