"""NFC-e (Nota Fiscal do Consumidor Eletrônica) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams


class NfceResource(BaseResource):
    """Operações de notas fiscais do consumidor eletrônicas (NFC-e).

    Mapeia os endpoints ``/nfce``.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        id_transportador: int | None = None,
        chave_acesso: str | None = None,
        numero: str | None = None,
        serie: str | None = None,
        situacao: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> JsonObject:
        """Lista as NFC-e."""
        return self._get(
            "/nfce",
            params=_nfce_list_params(
                pagina=pagina,
                limite=limite,
                id_transportador=id_transportador,
                chave_acesso=chave_acesso,
                numero=numero,
                serie=serie,
                situacao=situacao,
                data_emissao_inicial=data_emissao_inicial,
                data_emissao_final=data_emissao_final,
            ),
        )

    def list(  # noqa: PLR0913
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        carrier_id: int | None = None,
        access_key: str | None = None,
        number: str | None = None,
        series: str | None = None,
        status: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``."""
        return self.listar(
            pagina=page,
            limite=limit,
            id_transportador=carrier_id,
            chave_acesso=access_key,
            numero=number,
            serie=series,
            situacao=status,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        id_transportador: int | None = None,
        chave_acesso: str | None = None,
        numero: str | None = None,
        serie: str | None = None,
        situacao: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> Iterator[JsonObject]:
        """Itera pelas NFC-e página a página.

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.
        """
        params = _nfce_list_params(
            pagina=pagina,
            limite=limite,
            id_transportador=id_transportador,
            chave_acesso=chave_acesso,
            numero=numero,
            serie=serie,
            situacao=situacao,
            data_emissao_inicial=data_emissao_inicial,
            data_emissao_final=data_emissao_final,
        )
        return self._iterate("/nfce", page=pagina or 1, limit=limite or 100, params=params)

    def iterate(  # noqa: PLR0913
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        carrier_id: int | None = None,
        access_key: str | None = None,
        number: str | None = None,
        series: str | None = None,
        status: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``."""
        return self.iterar(
            pagina=page,
            limite=limit,
            id_transportador=carrier_id,
            chave_acesso=access_key,
            numero=number,
            serie=series,
            situacao=status,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def obter(self, id_nota_fiscal_consumidor: int) -> JsonObject:
        """Obtém uma NFC-e pelo ID."""
        return self._get(f"/nfce/{id_nota_fiscal_consumidor}")

    def get(self, consumer_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``."""
        return self.obter(consumer_invoice_id)

    def criar(self, dados: JsonObject) -> JsonObject:
        """Cria uma NFC-e."""
        return self._post("/nfce", json=to_json_object(dados))

    def create(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``."""
        return self.criar(data)

    def alterar(self, id_nota_fiscal_consumidor: int, dados: JsonObject) -> JsonObject:
        """Altera uma NFC-e existente."""
        return self._put(f"/nfce/{id_nota_fiscal_consumidor}", json=to_json_object(dados))

    def update(self, consumer_invoice_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``."""
        return self.alterar(consumer_invoice_id, data)

    def autorizar(
        self, id_nota_fiscal_consumidor: int, *, enviar_email: bool | None = None
    ) -> JsonObject:
        """Autoriza (envia para a SEFAZ) uma NFC-e."""
        params = compact_params({"enviarEmail": enviar_email})
        return self._post(f"/nfce/{id_nota_fiscal_consumidor}/enviar", params=params)

    def authorize(self, consumer_invoice_id: int, *, send_email: bool | None = None) -> JsonObject:
        """Compatibility alias for ``autorizar()``."""
        return self.autorizar(consumer_invoice_id, enviar_email=send_email)

    def lancar_contas(self, id_nota_fiscal_consumidor: int) -> JsonObject:
        """Lança as contas de uma NFC-e."""
        return self._post(f"/nfce/{id_nota_fiscal_consumidor}/lancar-contas")

    def post_accounts(self, consumer_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``lancar_contas()``."""
        return self.lancar_contas(consumer_invoice_id)

    def estornar_contas(self, id_nota_fiscal_consumidor: int) -> JsonObject:
        """Estorna as contas de uma NFC-e."""
        return self._post(f"/nfce/{id_nota_fiscal_consumidor}/estornar-contas")

    def reverse_accounts(self, consumer_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_contas()``."""
        return self.estornar_contas(consumer_invoice_id)

    def lancar_estoque(
        self, id_nota_fiscal_consumidor: int, *, id_deposito: int | None = None
    ) -> JsonObject:
        """Lança o estoque de uma NFC-e."""
        if id_deposito is not None:
            return self._post(f"/nfce/{id_nota_fiscal_consumidor}/lancar-estoque/{id_deposito}")
        return self._post(f"/nfce/{id_nota_fiscal_consumidor}/lancar-estoque")

    def post_stock(self, consumer_invoice_id: int, *, deposit_id: int | None = None) -> JsonObject:
        """Compatibility alias for ``lancar_estoque()``."""
        return self.lancar_estoque(consumer_invoice_id, id_deposito=deposit_id)

    def estornar_estoque(self, id_nota_fiscal_consumidor: int) -> JsonObject:
        """Estorna o estoque de uma NFC-e."""
        return self._post(f"/nfce/{id_nota_fiscal_consumidor}/estornar-estoque")

    def reverse_stock(self, consumer_invoice_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_estoque()``."""
        return self.estornar_estoque(consumer_invoice_id)


def _nfce_list_params(  # noqa: PLR0913
    *,
    pagina: int | None,
    limite: int | None,
    id_transportador: int | None,
    chave_acesso: str | None,
    numero: str | None,
    serie: str | None,
    situacao: int | None,
    data_emissao_inicial: str | None,
    data_emissao_final: str | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "idTransportador": id_transportador,
            "chaveAcesso": chave_acesso,
            "numero": numero,
            "serie": serie,
            "situacao": situacao,
            "dataEmissaoInicial": data_emissao_inicial,
            "dataEmissaoFinal": data_emissao_final,
        }
    )
