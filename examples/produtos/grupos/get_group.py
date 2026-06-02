"""Exemplo que obtém um grupo de produtos pelo ID usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém um grupo de produtos pelo ID."""
    with BlingClient.from_env() as client:
        response = client.grupos_produtos.obter(100)
        print(response.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
