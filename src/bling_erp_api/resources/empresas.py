"""Empresas resource."""

from __future__ import annotations

from bling_erp_api.models.generated.empresas import EmpresasMeDadosBasicosGetResponse200
from bling_erp_api.resources.base import BaseResource


class EmpresasResource(BaseResource):
    """Operações de empresas do Bling.

    Este recurso mapeia os endpoints ``/empresas``.
    Os métodos canônicos usam português para acompanhar a documentação oficial;
    os métodos em inglês continuam disponíveis como aliases de compatibilidade.
    """

    def obter_dados_basicos(self) -> EmpresasMeDadosBasicosGetResponse200:
        """Obtém dados básicos da empresa.

        Endpoint: GET /empresas/me/dados-basicos

        Obtém CNPJ, razão social e e-mail da empresa.

        Returns:
            Bling API response. Response schemas: 200: EmpresasDadosBasicosDTO
        """
        raw = self._get("/empresas/me/dados-basicos")
        return self._validate_response(EmpresasMeDadosBasicosGetResponse200, raw)

    def get_basic_data(self) -> EmpresasMeDadosBasicosGetResponse200:
        """Compatibility alias for ``obter_dados_basicos()``.

        Gets basic company data.

        Endpoint: GET /empresas/me/dados-basicos

        Returns:
            Bling API response. Response schemas: 200: EmpresasDadosBasicosDTO
        """
        return self.obter_dados_basicos()
