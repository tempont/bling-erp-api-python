"""Produtos — Lojas resource."""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.models.generated.product_stores import ProductStoreLinkCreate
    from bling_erp_api.types import JsonObject, QueryParams

type DateFilter = date | datetime | str


class ProductStoresResource(BaseResource):
    """Operações em ``/produtos/lojas``."""

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        id_produto: int | None = None,
        id_loja: int | None = None,
        id_categoria_produto: int | None = None,
        data_alteracao_inicial: DateFilter | None = None,
        data_alteracao_final: DateFilter | None = None,
    ) -> JsonObject:
        """Lista vínculos entre produto e loja."""
        return self._get(
            "/produtos/lojas",
            params=_store_list_params(
                pagina=pagina,
                limite=limite,
                id_produto=id_produto,
                id_loja=id_loja,
                id_categoria_produto=id_categoria_produto,
                data_alteracao_inicial=data_alteracao_inicial,
                data_alteracao_final=data_alteracao_final,
            ),
        )

    def iterar(self, *, pagina: int = 1, limite: int = 100) -> Iterator[JsonObject]:
        """Iterador paginado (sem filtros adicionais)."""
        return self._iterate("/produtos/lojas", page=pagina, limit=limite)

    def criar(self, dados: ProductStoreLinkCreate | JsonObject) -> JsonObject:
        """Cria vínculo produto-loja."""
        return self._post("/produtos/lojas", json=to_json_object(dados))

    def obter(self, id_produto_loja: int) -> JsonObject:
        """Obtém vínculo por ID."""
        return self._get(f"/produtos/lojas/{id_produto_loja}")

    def alterar(
        self, id_produto_loja: int, dados: ProductStoreLinkCreate | JsonObject
    ) -> JsonObject:
        """Atualização completa (``PUT``)."""
        return self._put(f"/produtos/lojas/{id_produto_loja}", json=to_json_object(dados))

    def remover(self, id_produto_loja: int) -> JsonObject:
        """Remove vínculo."""
        return self._delete(f"/produtos/lojas/{id_produto_loja}")


def _store_list_params(  # noqa: PLR0913
    *,
    pagina: int,
    limite: int,
    id_produto: int | None,
    id_loja: int | None,
    id_categoria_produto: int | None,
    data_alteracao_inicial: DateFilter | None,
    data_alteracao_final: DateFilter | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "idProduto": id_produto,
            "idLoja": id_loja,
            "idCategoriaProduto": id_categoria_produto,
            "dataAlteracaoInicial": _format_datetime_filter(data_alteracao_inicial),
            "dataAlteracaoFinal": _format_datetime_filter(data_alteracao_final),
        }
    )


def _format_datetime_filter(value: DateFilter | None) -> str | None:
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return value.isoformat()
