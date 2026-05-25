"""Produtos — Lotes resource."""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from bling_erp_api.models.generated.product_batches import (
        ProductBatch,
        ProductBatchStatusRequest,
        ProductBatchUpdateRequest,
    )
    from bling_erp_api.types import JsonObject, QueryParams

type DateFilter = date | datetime | str


class ProductBatchesResource(BaseResource):
    """Operações em ``/produtos/lotes`` e rotas relacionadas."""

    def remover_varios(self, ids_lotes: Sequence[int]) -> JsonObject:
        """Remove múltiplos lotes."""
        return self._delete(
            "/produtos/lotes",
            params=compact_params({"idsLotes[]": list(ids_lotes)}),
        )

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        ids_produtos: Sequence[int],
        ids_lotes: Sequence[int] | None = None,
        ids_depositos: Sequence[int] | None = None,
        codigos_lotes: Sequence[str] | None = None,
        status: str | None = None,
        data_validade_inicial: DateFilter | None = None,
        data_validade_final: DateFilter | None = None,
        data_fabricacao_inicial: DateFilter | None = None,
        data_fabricacao_final: DateFilter | None = None,
        data_criacao_inicial: DateFilter | None = None,
        data_criacao_final: DateFilter | None = None,
    ) -> JsonObject:
        """Lista lotes (``idsProdutos[]`` obrigatório na API)."""
        return self._get(
            "/produtos/lotes",
            params=_batch_list_params(
                pagina=pagina,
                limite=limite,
                ids_produtos=ids_produtos,
                ids_lotes=ids_lotes,
                ids_depositos=ids_depositos,
                codigos_lotes=codigos_lotes,
                status=status,
                data_validade_inicial=data_validade_inicial,
                data_validade_final=data_validade_final,
                data_fabricacao_inicial=data_fabricacao_inicial,
                data_fabricacao_final=data_fabricacao_final,
                data_criacao_inicial=data_criacao_inicial,
                data_criacao_final=data_criacao_final,
            ),
        )

    def iterar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        ids_produtos: Sequence[int],
        ids_lotes: Sequence[int] | None = None,
        ids_depositos: Sequence[int] | None = None,
        codigos_lotes: Sequence[str] | None = None,
        status: str | None = None,
        data_validade_inicial: DateFilter | None = None,
        data_validade_final: DateFilter | None = None,
        data_fabricacao_inicial: DateFilter | None = None,
        data_fabricacao_final: DateFilter | None = None,
        data_criacao_inicial: DateFilter | None = None,
        data_criacao_final: DateFilter | None = None,
    ) -> Iterator[JsonObject]:
        """Itera páginas de lotes mantendo filtros fixos."""
        merged = compact_params(
            {
                "idsProdutos[]": list(ids_produtos),
                "idsLotes[]": list(ids_lotes) if ids_lotes is not None else None,
                "idsDepositos[]": list(ids_depositos) if ids_depositos is not None else None,
                "codigosLotes[]": list(codigos_lotes) if codigos_lotes is not None else None,
                "status": status,
                "dataValidadeInicial": _format_date_filter(data_validade_inicial),
                "dataValidadeFinal": _format_date_filter(data_validade_final),
                "dataFabricacaoInicial": _format_date_filter(data_fabricacao_inicial),
                "dataFabricacaoFinal": _format_date_filter(data_fabricacao_final),
                "dataCriacaoInicial": _format_datetime_filter(data_criacao_inicial),
                "dataCriacaoFinal": _format_datetime_filter(data_criacao_final),
            },
        )

        return self._iterate("/produtos/lotes", page=pagina, limit=limite, params=merged or {})

    def criar_varios(self, lotes: Sequence[ProductBatch | JsonObject]) -> JsonObject:
        """Cria/atualiza múltiplos lotes (corpo como array JSON)."""
        payload = [to_json_object(lote) for lote in lotes]
        return self._put("/produtos/lotes", json=payload)

    def listar_produtos_controlam_lote(self, ids_produtos: Sequence[int]) -> JsonObject:
        """Indica quais produtos controlam lote."""
        return self._get(
            "/produtos/lotes/controla-lote",
            params=compact_params({"idsProdutos[]": list(ids_produtos)}),
        )

    def obter(self, id_lote: int) -> JsonObject:
        """Obtém um lote por ID."""
        return self._get(f"/produtos/lotes/{id_lote}")

    def alterar(self, id_lote: int, dados: ProductBatchUpdateRequest | JsonObject) -> JsonObject:
        """Altera dados do lote (``PUT``)."""
        return self._put(f"/produtos/lotes/{id_lote}", json=to_json_object(dados))

    def alterar_situacao(
        self, id_lote: int, dados: ProductBatchStatusRequest | JsonObject
    ) -> JsonObject:
        """Altera status do lote (``PATCH``)."""
        return self._patch(f"/produtos/lotes/{id_lote}/status", json=to_json_object(dados))

    def alterar_situacao_desativar(self, id_produto: int) -> JsonObject:
        """Desativa controle de lote para o produto pai."""
        return self._post(f"/produtos/{id_produto}/lotes/controla-lote/desativar")


def _batch_list_params(  # noqa: PLR0913
    *,
    pagina: int,
    limite: int,
    ids_produtos: Sequence[int],
    ids_lotes: Sequence[int] | None,
    ids_depositos: Sequence[int] | None,
    codigos_lotes: Sequence[str] | None,
    status: str | None,
    data_validade_inicial: DateFilter | None,
    data_validade_final: DateFilter | None,
    data_fabricacao_inicial: DateFilter | None,
    data_fabricacao_final: DateFilter | None,
    data_criacao_inicial: DateFilter | None,
    data_criacao_final: DateFilter | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "idsProdutos[]": list(ids_produtos),
            "idsLotes[]": list(ids_lotes) if ids_lotes is not None else None,
            "idsDepositos[]": list(ids_depositos) if ids_depositos is not None else None,
            "codigosLotes[]": list(codigos_lotes) if codigos_lotes is not None else None,
            "status": status,
            "dataValidadeInicial": _format_date_filter(data_validade_inicial),
            "dataValidadeFinal": _format_date_filter(data_validade_final),
            "dataFabricacaoInicial": _format_date_filter(data_fabricacao_inicial),
            "dataFabricacaoFinal": _format_date_filter(data_fabricacao_final),
            "dataCriacaoInicial": _format_datetime_filter(data_criacao_inicial),
            "dataCriacaoFinal": _format_datetime_filter(data_criacao_final),
        }
    )


def _format_date_filter(value: DateFilter | None) -> str | None:
    if value is None or isinstance(value, str):
        return value
    return value.date().isoformat() if isinstance(value, datetime) else value.isoformat()


def _format_datetime_filter(value: DateFilter | None) -> str | None:
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return value.isoformat()
