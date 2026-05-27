"""Example: Get notification count for a period."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.notificacoes import NotificacoesQuantidadeGetResponse200


def main() -> None:
    """Retrieve the number of notifications for the current year."""
    with BlingClient.from_env() as client:
        response = client.notificacoes.obter_quantidade()
        parsed = NotificacoesQuantidadeGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
