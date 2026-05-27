"""Example: Generate production orders on demand."""

from bling_erp_api import BlingClient


def main() -> None:
    """Generate production orders automatically based on minimum stock."""
    with BlingClient.from_env() as client:
        response = client.ordens_producao.criar_multiplos()
        print(response)


if __name__ == "__main__":
    main()
