"""Example: Get a single bordero by ID."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.borderos import BorderosIdBorderoGetResponse200


def main() -> None:
    """Retrieve bordero details by ID."""
    with BlingClient.from_env() as client:
        response = client.borderos.obter(123456)
        parsed = BorderosIdBorderoGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
