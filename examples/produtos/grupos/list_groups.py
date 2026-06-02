"""Exemplo que lista grupos de produtos usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista grupos de produtos."""
    with BlingClient.from_env() as client:
        response = client.grupos_produtos.listar()
        print(response.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
