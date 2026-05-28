"""Exemplo que altera a situação de um contato."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosIdContatoSituacoesPatchRequest

CONTATO_ID = 12345678


def main() -> None:
    """Define situação ``A`` (ativo) para o contato informado."""
    # Model: ContatosIdContatoSituacoesPatchRequest  # noqa: ERA001
    #   Optional: situacao (str|None)  # noqa: ERA001
    payload = ContatosIdContatoSituacoesPatchRequest(situacao="A")
    with BlingClient.from_env() as client:
        response = client.contatos.alterar_situacao(CONTATO_ID, payload.situacao)  # type: ignore[arg-type]
        # NOTE: No success response model for PATCH situacoes (only error responses in OpenAPI spec).
        print(response)


if __name__ == "__main__":
    main()
