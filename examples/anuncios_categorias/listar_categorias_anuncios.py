"""Example: List ad categories (Anúncios Categorias).

Endpoints:
    - GET /anuncios/categorias

Docs:
    - https://developer.bling.com.br/referencia#/An%C3%BAncios/get_anuncios_categorias

"""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista categorias de anúncios."""
    with BlingClient.from_env() as client:
        response = client.anuncios_categorias.listar(
            tipo_integracao="MLA",
            id_loja=1,
        )
        print(response)


if __name__ == "__main__":
    main()
