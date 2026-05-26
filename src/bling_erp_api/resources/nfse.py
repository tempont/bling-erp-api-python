"""NFS-e (Nota Fiscal de Serviço Eletrônica) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams


class NfseResource(BaseResource):
    """Operações de notas fiscais de serviço eletrônicas (NFS-e).

    Mapeia os endpoints ``/nfse``.
    """

    def listar(
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        situacao: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> JsonObject:
        """Lista as NFS-e."""
        return self._get(
            "/nfse",
            params=_nfse_list_params(
                pagina=pagina,
                limite=limite,
                situacao=situacao,
                data_emissao_inicial=data_emissao_inicial,
                data_emissao_final=data_emissao_final,
            ),
        )

    def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        status: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``."""
        return self.listar(
            pagina=page,
            limite=limit,
            situacao=status,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def iterar(
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        situacao: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> Iterator[JsonObject]:
        """Itera pelas NFS-e página a página.

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.
        """
        params = _nfse_list_params(
            pagina=pagina,
            limite=limite,
            situacao=situacao,
            data_emissao_inicial=data_emissao_inicial,
            data_emissao_final=data_emissao_final,
        )
        return self._iterate("/nfse", page=pagina or 1, limit=limite or 100, params=params)

    def iterate(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        status: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``."""
        return self.iterar(
            pagina=page,
            limite=limit,
            situacao=status,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def obter(self, id_nota_servico: int) -> JsonObject:
        """Obtém uma NFS-e pelo ID."""
        return self._get(f"/nfse/{id_nota_servico}")

    def get(self, service_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``."""
        return self.obter(service_invoice_id)

    def criar(self, dados: JsonObject) -> JsonObject:
        """Cria uma NFS-e."""
        return self._post("/nfse", json=to_json_object(dados))

    def create(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``."""
        return self.criar(data)

    def remover(self, id_nota_servico: int) -> JsonObject:
        """Remove uma NFS-e."""
        return self._delete(f"/nfse/{id_nota_servico}")

    def delete(self, service_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``."""
        return self.remover(service_invoice_id)

    def autorizar(self, id_nota_servico: int) -> JsonObject:
        """Autoriza (envia) uma NFS-e."""
        return self._post(f"/nfse/{id_nota_servico}/enviar")

    def authorize(self, service_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``autorizar()``."""
        return self.autorizar(service_invoice_id)

    def cancelar(self, id_nota_servico: int, dados: JsonObject) -> JsonObject:
        """Cancela uma NFS-e."""
        return self._post(
            f"/nfse/{id_nota_servico}/cancelar",
            json=to_json_object(dados),
        )

    def cancel(self, service_invoice_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``cancelar()``."""
        return self.cancelar(service_invoice_id, data)

    def obter_configuracoes(self) -> JsonObject:
        """Obtém as configurações de NFS-e."""
        return self._get("/nfse/configuracoes")

    def get_settings(self) -> JsonObject:
        """Compatibility alias for ``obter_configuracoes()``."""
        return self.obter_configuracoes()

    def alterar_configuracoes(self, dados: JsonObject) -> JsonObject:
        """Altera as configurações de NFS-e."""
        return self._put("/nfse/configuracoes", json=to_json_object(dados))

    def update_settings(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar_configuracoes()``."""
        return self.alterar_configuracoes(data)


def _nfse_list_params(
    *,
    pagina: int | None,
    limite: int | None,
    situacao: int | None,
    data_emissao_inicial: str | None,
    data_emissao_final: str | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "situacao": situacao,
            "dataEmissaoInicial": data_emissao_inicial,
            "dataEmissaoFinal": data_emissao_final,
        }
    )
