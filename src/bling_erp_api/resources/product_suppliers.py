"""Produtos — Fornecedores resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.models.generated.product_suppliers import (
        ProductSupplierCreateRequest,
        ProductSupplierUpdateRequest,
    )
    from bling_erp_api.types import JsonObject, QueryParams


class ProductSuppliersResource(BaseResource):
    """Operações em ``/produtos/fornecedores``."""

    def listar(
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        id_produto: int | None = None,
        id_fornecedor: int | None = None,
    ) -> JsonObject:
        """Lista vínculos entre produto e fornecedor."""
        return self._get(
            "/produtos/fornecedores",
            params=_supplier_list_params(
                pagina=pagina,
                limite=limite,
                id_produto=id_produto,
                id_fornecedor=id_fornecedor,
            ),
        )

    def iterar(self, *, pagina: int = 1, limite: int = 100) -> Iterator[JsonObject]:
        """Iterador paginado (sem filtros adicionais)."""
        return self._iterate("/produtos/fornecedores", page=pagina, limit=limite)

    def criar(self, dados: ProductSupplierCreateRequest | JsonObject) -> JsonObject:
        """Cria vínculo (``POST``)."""
        return self._post("/produtos/fornecedores", json=to_json_object(dados))

    def obter(self, id_produto_fornecedor: int) -> JsonObject:
        """Obtém por ID."""
        return self._get(f"/produtos/fornecedores/{id_produto_fornecedor}")

    def alterar(
        self,
        id_produto_fornecedor: int,
        dados: ProductSupplierUpdateRequest | JsonObject,
    ) -> JsonObject:
        """Atualização completa (``PUT``)."""
        return self._put(
            f"/produtos/fornecedores/{id_produto_fornecedor}",
            json=to_json_object(dados),
        )

    def remover(self, id_produto_fornecedor: int) -> JsonObject:
        """Remove vínculo."""
        return self._delete(f"/produtos/fornecedores/{id_produto_fornecedor}")


def _supplier_list_params(
    *,
    pagina: int,
    limite: int,
    id_produto: int | None,
    id_fornecedor: int | None,
) -> QueryParams:
    return compact_params(
        {
            "pagina": pagina,
            "limite": limite,
            "idProduto": id_produto,
            "idFornecedor": id_fornecedor,
        }
    )
