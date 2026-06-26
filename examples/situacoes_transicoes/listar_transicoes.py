"""Example: List situation transitions (Situações Transições).

Demonstra como listar as transições disponíveis para um módulo de situação.

Endpoints:
    - GET /situacoes/modulos/{idModuloSistema}/transicoes

Docs:
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es/get_situacoes_modulos__idModuloSistema__transicoes

"""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.situacoes_modulos import (
    SituacoesModulosIdModuloSistemaTransicoesGetResponse200,
)


def main() -> None:
    """Lista as transições disponíveis para um módulo de situação."""
    with BlingClient.from_env() as client:
        response = client.situacoes_modulos.listar_transicoes(id_modulo_sistema=1)
        parsed = SituacoesModulosIdModuloSistemaTransicoesGetResponse200.model_validate(response)
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
