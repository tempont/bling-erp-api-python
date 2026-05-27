"""Example: List all notifications for a period."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.notificacoes import NotificacoesGetResponse200


def main() -> None:
    """List notifications for January 2025."""
    with BlingClient.from_env() as client:
        response = client.notificacoes.listar(periodo="2025-01")
        parsed = NotificacoesGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
