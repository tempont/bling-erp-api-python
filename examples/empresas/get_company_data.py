"""Exemplo que obtém dados básicos da empresa usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.empresas import EmpresasMeDadosBasicosGetResponse200


def main() -> None:
    """Obtém dados básicos da empresa (CNPJ, razão social, e-mail)."""
    with BlingClient.from_env() as client:
        response = client.empresas.obter_dados_basicos()
        parsed = EmpresasMeDadosBasicosGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
