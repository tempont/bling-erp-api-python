"""Exemplo que obtém o contato padrão Consumidor Final."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosConsumidorFinalGetResponse200


def main() -> None:
    """Consulta o contato de consumidor final do sistema."""
    with BlingClient.from_env() as client:
        response = client.contatos.obter_consumidor_final()
        parsed = ContatosConsumidorFinalGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
