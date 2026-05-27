"""Example: Generate production orders on demand."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.ordens_producao import (
    OrdensProducaoGerarSobDemandaPostResponse201,
)


def main() -> None:
    """Generate production orders automatically based on minimum stock."""
    with BlingClient.from_env() as client:
        response = client.ordens_producao.criar_multiplos()
        parsed = OrdensProducaoGerarSobDemandaPostResponse201(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
