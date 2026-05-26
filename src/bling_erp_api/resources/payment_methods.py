"""Formas de Pagamentos resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, QueryParams


def _payment_methods_list_params(
    *,
    descricao: str | None = None,
    tipos_pagamentos: list[int] | None = None,
    situacao: int | None = None,
) -> QueryParams:
    return compact_params(
        {
            "descricao": descricao,
            "tiposPagamentos[]": tipos_pagamentos,
            "situacao": situacao,
        }
    )


class PaymentMethodsResource(BaseResource):
    """Operações de formas de pagamentos do Bling.

    Este recurso mapeia os endpoints ``/formas-pagamentos``. Os métodos canônicos usam
    português para acompanhar a documentação oficial. Aliases em inglês estão disponíveis
    para compatibilidade.
    """

    def listar(
        self,
        *,
        pagina: int = 1,
        limite: int = 100,
        descricao: str | None = None,
        tipos_pagamentos: list[int] | None = None,
        situacao: int | None = None,
    ) -> JsonObject:
        """Obtém formas de pagamentos paginadas.

        Endpoint: GET /formas-pagamentos

        Obtém formas de pagamentos paginadas.

        Args:
            pagina: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limite: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            descricao: Descrição da forma de pagamento (Bling: ``descricao``, string, opcional)
            tipos_pagamentos: Tipos de pagamento (Bling: ``tiposPagamentos[]``, array, opcional)
            situacao: Situação (Bling: ``situacao``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: FormasPagamentosDadosBaseDTO
        """
        params = _payment_methods_list_params(
            descricao=descricao,
            tipos_pagamentos=tipos_pagamentos,
            situacao=situacao,
        )
        return self._get(f"/formas-pagamentos?pagina={pagina}&limite={limite}", params=params)

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        description: str | None = None,
        payment_types: list[int] | None = None,
        status: int | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Obtém formas de pagamentos paginadas.

        Endpoint: GET /formas-pagamentos

        Obtém formas de pagamentos paginadas.

        Args:
            page: N° da página da listagem (Bling: ``pagina``, integer, opcional)
            limit: Quantidade de registros que devem ser exibidos por página (Bling: ``limite``, integer, opcional)
            description: Descrição da forma de pagamento (Bling: ``descricao``, string, opcional)
            payment_types: Tipos de pagamento (Bling: ``tiposPagamentos[]``, array, opcional)
            status: Situação (Bling: ``situacao``, integer, opcional)

        Returns:
            Bling API response. Response schemas: 200: FormasPagamentosDadosBaseDTO
        """
        return self.listar(
            pagina=page,
            limite=limit,
            descricao=description,
            tipos_pagamentos=payment_types,
            situacao=status,
        )

    def obter(self, id_forma_pagamento: int) -> JsonObject:
        """Obtém uma forma de pagamento.

        Endpoint: GET /formas-pagamentos/{idFormaPagamento}

        Obtém uma forma de pagamento pelo ID.

        Args:
            id_forma_pagamento: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: FormasPagamentosDadosBaseDTO, FormasPagamentosDadosDTO; 404: ErrorResponse
        """
        return self._get(f"/formas-pagamentos/{id_forma_pagamento}")

    def get(self, payment_method_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém uma forma de pagamento.

        Endpoint: GET /formas-pagamentos/{idFormaPagamento}

        Obtém uma forma de pagamento pelo ID.

        Args:
            payment_method_id: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: FormasPagamentosDadosBaseDTO, FormasPagamentosDadosDTO; 404: ErrorResponse
        """
        return self.obter(id_forma_pagamento=payment_method_id)

    def criar(self, dados: JsonObject) -> JsonObject:
        """Cria uma forma de pagamento.

        Endpoint: POST /formas-pagamentos

        Cria uma forma de pagamento.

        Args:
            dados: Dados da forma de pagamento (Bling: request body)

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self._post("/formas-pagamentos", json=to_json_object(dados))

    def create(self, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria uma forma de pagamento.

        Endpoint: POST /formas-pagamentos

        Cria uma forma de pagamento.

        Args:
            data: Dados da forma de pagamento (Bling: request body)

        Returns:
            Bling API response. Response schemas: 201: BasePostResponse; 400: ErrorResponse
        """
        return self.criar(dados=data)

    def alterar(self, id_forma_pagamento: int, dados: JsonObject) -> JsonObject:
        """Altera uma forma de pagamento.

        Endpoint: PUT /formas-pagamentos/{idFormaPagamento}

        Altera uma forma de pagamento pelo ID.

        Args:
            id_forma_pagamento: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)
            dados: Dados da forma de pagamento (Bling: request body)

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(
            f"/formas-pagamentos/{id_forma_pagamento}",
            json=to_json_object(dados),
        )

    def update(self, payment_method_id: int, data: JsonObject) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera uma forma de pagamento.

        Endpoint: PUT /formas-pagamentos/{idFormaPagamento}

        Altera uma forma de pagamento pelo ID.

        Args:
            payment_method_id: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)
            data: Dados da forma de pagamento (Bling: request body)

        Returns:
            Bling API response. Response schemas: 200: BasePostResponse; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_forma_pagamento=payment_method_id, dados=data)

    def remover(self, id_forma_pagamento: int) -> JsonObject:
        """Remove uma forma de pagamento.

        Endpoint: DELETE /formas-pagamentos/{idFormaPagamento}

        Remove uma forma de pagamento pelo ID.

        Args:
            id_forma_pagamento: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/formas-pagamentos/{id_forma_pagamento}")

    def delete(self, payment_method_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove uma forma de pagamento.

        Endpoint: DELETE /formas-pagamentos/{idFormaPagamento}

        Remove uma forma de pagamento pelo ID.

        Args:
            payment_method_id: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(id_forma_pagamento=payment_method_id)

    def alterar_situacao(self, id_forma_pagamento: int, situacao: int) -> JsonObject:
        """Altera a situação de uma forma de pagamento.

        Endpoint: PATCH /formas-pagamentos/{idFormaPagamento}/situacao

        Altera a situação de uma forma de pagamento pelo ID.

        Args:
            id_forma_pagamento: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)
            situacao: 1=Ativa, 0=Inativa (Bling: situacao, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(
            f"/formas-pagamentos/{id_forma_pagamento}/situacao",
            json=to_json_object({"situacao": situacao}),
        )

    def set_status(self, payment_method_id: int, status: int) -> JsonObject:
        """Compatibility alias for ``alterar_situacao()``.

        Altera a situação de uma forma de pagamento.

        Endpoint: PATCH /formas-pagamentos/{idFormaPagamento}/situacao

        Altera a situação de uma forma de pagamento pelo ID.

        Args:
            payment_method_id: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)
            status: 1=Ativa, 0=Inativa (Bling: situacao, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar_situacao(id_forma_pagamento=payment_method_id, situacao=status)

    def alterar_padrao(self, id_forma_pagamento: int, padrao: int) -> JsonObject:
        """Altera o padrão de uma forma de pagamento.

        Endpoint: PATCH /formas-pagamentos/{idFormaPagamento}/padrao

        Altera o padrão de uma forma de pagamento pelo ID.

        Args:
            id_forma_pagamento: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)
            padrao: 1=Pagamento, 2=Devolução, 3=Fiado (Bling: padrao, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self._patch(
            f"/formas-pagamentos/{id_forma_pagamento}/padrao",
            json=to_json_object({"padrao": padrao}),
        )

    def set_default(self, payment_method_id: int, default_type: int) -> JsonObject:
        """Compatibility alias for ``alterar_padrao()``.

        Altera o padrão de uma forma de pagamento.

        Endpoint: PATCH /formas-pagamentos/{idFormaPagamento}/padrao

        Altera o padrão de uma forma de pagamento pelo ID.

        Args:
            payment_method_id: ID da forma de pagamento (Bling: ``idFormaPagamento``, integer, obrigatório)
            default_type: 1=Pagamento, 2=Devolução, 3=Fiado (Bling: padrao, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar_padrao(id_forma_pagamento=payment_method_id, padrao=default_type)
