"""Exemplo que altera a situação de vários contatos."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import (
    ContatosSituacoesPostRequest,
    ContatosSituacoesPostResponse200,
)


def main() -> None:
    """Atualiza situação em massa (ex.: ``I`` inativo)."""
    ids_contatos = [11111111, 22222222]
    # Model: ContatosSituacoesPostRequest
    #   Optional: ids_contatos (list[int]|None), situacao (str|None)
    payload = ContatosSituacoesPostRequest(ids_contatos=ids_contatos, situacao="I")
    with BlingClient.from_env() as client:
        response = client.contatos.alterar_situacao_varios(payload.ids_contatos, payload.situacao)  # type: ignore[arg-type]
        parsed = ContatosSituacoesPostResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
