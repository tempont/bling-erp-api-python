"""NF-e (Nota Fiscal Eletrônica) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from bling_erp_api.types import JsonObject, QueryParams


class NfeResource(BaseResource):
    """Operações de notas fiscais eletrônicas (NF-e).

    Mapeia os endpoints ``/nfe``. Para NFC-e use ``NfceResource``.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        numero_loja: int | None = None,
        id_transportador: int | None = None,
        chave_acesso: str | None = None,
        numero: str | None = None,
        serie: str | None = None,
        situacao: int | None = None,
        tipo: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> JsonObject:
        """Lista as notas fiscais eletrônicas (NF-e)."""
        return self._get(
            "/nfe",
            params=_nfe_list_params(
                pagina=pagina,
                limite=limite,
                numero_loja=numero_loja,
                id_transportador=id_transportador,
                chave_acesso=chave_acesso,
                numero=numero,
                serie=serie,
                situacao=situacao,
                tipo=tipo,
                data_emissao_inicial=data_emissao_inicial,
                data_emissao_final=data_emissao_final,
            ),
        )

    def list(  # noqa: PLR0913
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        store_number: int | None = None,
        carrier_id: int | None = None,
        access_key: str | None = None,
        number: str | None = None,
        series: str | None = None,
        status: int | None = None,
        kind: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``."""
        return self.listar(
            pagina=page,
            limite=limit,
            numero_loja=store_number,
            id_transportador=carrier_id,
            chave_acesso=access_key,
            numero=number,
            serie=series,
            situacao=status,
            tipo=kind,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int | None = None,
        limite: int | None = None,
        numero_loja: int | None = None,
        id_transportador: int | None = None,
        chave_acesso: str | None = None,
        numero: str | None = None,
        serie: str | None = None,
        situacao: int | None = None,
        tipo: int | None = None,
        data_emissao_inicial: str | None = None,
        data_emissao_final: str | None = None,
    ) -> Iterator[JsonObject]:
        """Itera pelas NF-e página a página.

        Aceita os mesmos filtros de ``listar()`` e busca novas páginas enquanto
        o Bling retornar registros no envelope ``data``.
        """
        params = _nfe_list_params(
            pagina=pagina,
            limite=limite,
            numero_loja=numero_loja,
            id_transportador=id_transportador,
            chave_acesso=chave_acesso,
            numero=numero,
            serie=serie,
            situacao=situacao,
            tipo=tipo,
            data_emissao_inicial=data_emissao_inicial,
            data_emissao_final=data_emissao_final,
        )
        return self._iterate("/nfe", page=pagina or 1, limit=limite or 100, params=params)

    def iterate(  # noqa: PLR0913
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        store_number: int | None = None,
        carrier_id: int | None = None,
        access_key: str | None = None,
        number: str | None = None,
        series: str | None = None,
        status: int | None = None,
        kind: int | None = None,
        issued_start: str | None = None,
        issued_end: str | None = None,
    ) -> Iterator[JsonObject]:
        """Compatibility alias for ``iterar()``."""
        return self.iterar(
            pagina=page,
            limite=limit,
            numero_loja=store_number,
            id_transportador=carrier_id,
            chave_acesso=access_key,
            numero=number,
            serie=series,
            situacao=status,
            tipo=kind,
            data_emissao_inicial=issued_start,
            data_emissao_final=issued_end,
        )

    def obter(self, id_nota_fiscal: int) -> JsonObject:
        """Obtém uma NF-e pelo ID."""
        return self._get(f"/nfe/{id_nota_fiscal}")

    def get(self, invoice_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``."""
        return self.obter(invoice_id)

    def criar(self, dados: JsonObject) -> JsonObject:
        """Cria uma NF-e."""
        return self._post("/nfe", json=to_json_object(dados))

    def create(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``."""
        return self.criar(data)

    def alterar(self, id_nota_fiscal: int, dados: JsonObject) -> JsonObject:
        """Altera uma NF-e existente."""
        return self._put(f"/nfe/{id_nota_fiscal}", json=to_json_object(dados))

    def update(self, invoice_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``."""
        return self.alterar(invoice_id, data)

    def remover_varios(self, ids_notas: Sequence[int]) -> JsonObject:
        """Remove várias NF-e."""
        return self._delete("/nfe", params={"idsNotas[]": list(ids_notas)})

    def delete_many(self, invoice_ids: Sequence[int]) -> JsonObject:
        """Compatibility alias for ``remover_varios()``."""
        return self.remover_varios(invoice_ids)

    def autorizar(self, id_nota_fiscal: int, *, enviar_email: bool | None = None) -> JsonObject:
        """Autoriza (envia para a SEFAZ) uma NF-e."""
        params = compact_params({"enviarEmail": enviar_email})
        return self._post(f"/nfe/{id_nota_fiscal}/enviar", params=params)

    def authorize(self, invoice_id: int, *, send_email: bool | None = None) -> JsonObject:
        """Compatibility alias for ``autorizar()``."""
        return self.autorizar(invoice_id, enviar_email=send_email)

    def lancar_contas(self, id_nota_fiscal: int) -> JsonObject:
        """Lança as contas de uma NF-e."""
        return self._post(f"/nfe/{id_nota_fiscal}/lancar-contas")

    def post_accounts(self, invoice_id: int) -> JsonObject:
        """Compatibility alias for ``lancar_contas()``."""
        return self.lancar_contas(invoice_id)

    def estornar_contas(self, id_nota_fiscal: int) -> JsonObject:
        """Estorna as contas de uma NF-e."""
        return self._post(f"/nfe/{id_nota_fiscal}/estornar-contas")

    def reverse_accounts(self, invoice_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_contas()``."""
        return self.estornar_contas(invoice_id)

    def lancar_estoque(self, id_nota_fiscal: int, *, id_deposito: int | None = None) -> JsonObject:
        """Lança o estoque de uma NF-e."""
        if id_deposito is not None:
            return self._post(f"/nfe/{id_nota_fiscal}/lancar-estoque/{id_deposito}")
        return self._post(f"/nfe/{id_nota_fiscal}/lancar-estoque")

    def post_stock(self, invoice_id: int, *, deposit_id: int | None = None) -> JsonObject:
        """Compatibility alias for ``lancar_estoque()``."""
        return self.lancar_estoque(invoice_id, id_deposito=deposit_id)

    def estornar_estoque(self, id_nota_fiscal: int) -> JsonObject:
        """Estorna o estoque de uma NF-e."""
        return self._post(f"/nfe/{id_nota_fiscal}/estornar-estoque")

    def reverse_stock(self, invoice_id: int) -> JsonObject:
        """Compatibility alias for ``estornar_estoque()``."""
        return self.estornar_estoque(invoice_id)

    def obter_documento_nota_fiscal(
        self, chave_acesso: str, *, formato: str | None = None
    ) -> JsonObject:
        """Obtém o documento (XML/DANFE) de uma NF-e pela chave de acesso."""
        params = compact_params({"formato": formato})
        return self._get(f"/nfe/documento/{chave_acesso}", params=params)

    def get_document(self, access_key: str, *, output_format: str | None = None) -> JsonObject:
        """Compatibility alias for ``obter_documento_nota_fiscal()``."""
        return self.obter_documento_nota_fiscal(access_key, formato=output_format)


def _nfe_list_params(  # noqa: PLR0913
    *,
    pagina: int | None,
    limite: int | None,
    numero_loja: int | None,
    id_transportador: int | None,
    chave_acesso: str | None,
    numero: str | None,
    serie: str | None,
    situacao: int | None,
    tipo: int | None,
    data_emissao_inicial: str | None,
    data_emissao_final: str | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "numeroLoja": numero_loja,
            "idTransportador": id_transportador,
            "chaveAcesso": chave_acesso,
            "numero": numero,
            "serie": serie,
            "situacao": situacao,
            "tipo": tipo,
            "dataEmissaoInicial": data_emissao_inicial,
            "dataEmissaoFinal": data_emissao_final,
        }
    )
