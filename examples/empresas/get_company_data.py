"""Exemplo que obtém dados básicos da empresa usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém dados básicos da empresa (CNPJ, razão social, e-mail)."""
    with BlingClient.from_env() as client:
        response = client.empresas.obter_dados_basicos()
        print(response)


if __name__ == "__main__":
    main()
