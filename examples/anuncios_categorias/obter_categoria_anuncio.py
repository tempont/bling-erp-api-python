"""Example: Get a single ad category (Anúncios Categorias).

Endpoint:
    - GET /anuncios/categorias/{idCategoria}

Docs:
    - https://developer.bling.com.br/referencia#/An%C3%BAncios/get_anuncios_categorias__idCategoria_

"""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém uma categoria de anúncio pelo ID com seus atributos."""
    with BlingClient.from_env() as client:
        response = client.anuncios_categorias.obter(
            id_categoria="MLA12345",
            tipo_integracao="MLA",
            id_loja=1,
        )
        print(response)


if __name__ == "__main__":
    main()
