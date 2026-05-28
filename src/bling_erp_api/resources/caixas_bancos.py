"""Caixas e Bancos resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.models.generated.caixas_bancos import (
        CaixasBancosSalvarLancamentoDTO,
    )
    from bling_erp_api.types import JsonObject, QueryParams


def _caixas_list_params(  # noqa: PLR0913
    *,
    data_inicial: str | None = None,
    data_final: str | None = None,
    ids_categorias: list[int] | None = None,
    id_conta_financeira: int | None = None,
    pesquisa: str | None = None,
    valor: float | None = None,
    situacao_conciliacao: int | None = None,
    situacao: str | None = None,
) -> QueryParams:
    """Build query params for GET /caixas from SDK param names."""
    return compact_params(
        {
            "dataInicial": data_inicial,
            "dataFinal": data_final,
            "idsCategorias": ids_categorias,
            "idContaFinanceira": id_conta_financeira,
            "pesquisa": pesquisa,
            "valor": valor,
            "situacaoConciliacao": situacao_conciliacao,
            "situacao": situacao,
        }
    )


class CaixasBancosResource(BaseResource):
    """Operações de caixas e bancos do Bling.

    Este recurso mapeia os endpoints ``/caixas``. Os métodos canônicos usam
    português para acompanhar a documentação oficial; os métodos em inglês
    continuam disponíveis como aliases de compatibilidade.
    """

    def listar(  # noqa: PLR0913
        self,
        *,
        pagina: int = 1,
        data_inicial: str | None = None,
        data_final: str | None = None,
        ids_categorias: list[int] | None = None,
        id_conta_financeira: int | None = None,
        pesquisa: str | None = None,
        valor: float | None = None,
        situacao_conciliacao: int | None = None,
        situacao: str | None = None,
    ) -> JsonObject:
        """Lista lançamentos de caixas e bancos.

        Endpoint: GET /caixas

        Obtém lista paginada de lançamentos de caixas e bancos.

        Args:
            pagina: N° da página (Bling: ``pagina``, integer, opcional)
            data_inicial: Data inicial de consulta (Bling: ``dataInicial``, string, opcional)
            data_final: Data final de consulta (Bling: ``dataFinal``, string, opcional)
            ids_categorias: IDs das categorias (Bling: ``idsCategorias``, array, opcional)
            id_conta_financeira: ID da conta financeira (Bling: ``idContaFinanceira``, integer, opcional)
            pesquisa: Pesquisa por descrição (Bling: ``pesquisa``, string, opcional)
            valor: Valor do lançamento (Bling: ``valor``, number, opcional)
            situacao_conciliacao: Situação da conciliação: 1=Conciliados, 2=Não conciliados, 3=Todos (Bling: ``situacaoConciliacao``, integer, opcional)
            situacao: Situação do lançamento: 'R'=Registros, 'E'=Excluídos (Bling: ``situacao``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: CaixasBancosItemLancamentoDTO; 400: ErrorResponse
        """
        params = _caixas_list_params(
            data_inicial=data_inicial,
            data_final=data_final,
            ids_categorias=ids_categorias,
            id_conta_financeira=id_conta_financeira,
            pesquisa=pesquisa,
            valor=valor,
            situacao_conciliacao=situacao_conciliacao,
            situacao=situacao,
        )
        return self._get(f"/caixas?pagina={pagina}", params=params)

    def list(  # noqa: PLR0913
        self,
        *,
        page: int = 1,
        start_date: str | None = None,
        end_date: str | None = None,
        category_ids: list[int] | None = None,
        financial_account_id: int | None = None,
        search: str | None = None,
        amount: float | None = None,
        reconciliation_status: int | None = None,
        status: str | None = None,
    ) -> JsonObject:
        """Compatibility alias for ``listar()``.

        Lista lançamentos de caixas e bancos.

        Endpoint: GET /caixas

        Obtém lista paginada de lançamentos de caixas e bancos.

        Args:
            page: N° da página (Bling: ``pagina``, integer, opcional)
            start_date: Data inicial (Bling: ``dataInicial``, string, opcional)
            end_date: Data final (Bling: ``dataFinal``, string, opcional)
            category_ids: IDs das categorias (Bling: ``idsCategorias``, array, opcional)
            financial_account_id: ID da conta financeira (Bling: ``idContaFinanceira``, integer, opcional)
            search: Pesquisa por descrição (Bling: ``pesquisa``, string, opcional)
            amount: Valor do lançamento (Bling: ``valor``, number, opcional)
            reconciliation_status: Situação da conciliação (Bling: ``situacaoConciliacao``, integer, opcional)
            status: Situação do lançamento (Bling: ``situacao``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: CaixasBancosItemLancamentoDTO; 400: ErrorResponse
        """
        return self.listar(
            pagina=page,
            data_inicial=start_date,
            data_final=end_date,
            ids_categorias=category_ids,
            id_conta_financeira=financial_account_id,
            pesquisa=search,
            valor=amount,
            situacao_conciliacao=reconciliation_status,
            situacao=status,
        )

    def criar(
        self,
        lancamento: CaixasBancosSalvarLancamentoDTO,
    ) -> JsonObject:
        """Cria um lançamento de caixa e banco.

        Endpoint: POST /caixas

        Cria um novo lançamento de caixa e banco.

        Args:
            lancamento: Dados do lançamento. Request body schema: CaixasBancosSalvarLancamentoDTO

        Returns:
            Bling API response. Response schemas: 201: CaixasBancosSalvarLancamentoResponseDTO; 400: ErrorResponse
        """
        return self._post("/caixas", json=to_json_object(lancamento))

    def create(
        self,
        entry: CaixasBancosSalvarLancamentoDTO,
    ) -> JsonObject:
        """Compatibility alias for ``criar()``.

        Cria um lançamento de caixa e banco.

        Endpoint: POST /caixas

        Cria um novo lançamento de caixa e banco.

        Args:
            entry: Dados do lançamento. Request body schema: CaixasBancosSalvarLancamentoDTO

        Returns:
            Bling API response. Response schemas: 201: CaixasBancosSalvarLancamentoResponseDTO; 400: ErrorResponse
        """
        return self.criar(lancamento=entry)

    def obter(self, id_caixa: int) -> JsonObject:
        """Obtém um lançamento de caixa e banco.

        Endpoint: GET /caixas/{idCaixa}

        Obtém os detalhes de um lançamento pelo ID.

        Args:
            id_caixa: ID do lançamento (Bling: ``idCaixa``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: CaixasBancosLancamentoDTO; 404: ErrorResponse
        """
        return self._get(f"/caixas/{id_caixa}")

    def get(self, entry_id: int) -> JsonObject:
        """Compatibility alias for ``obter()``.

        Obtém um lançamento de caixa e banco.

        Endpoint: GET /caixas/{idCaixa}

        Obtém os detalhes de um lançamento pelo ID.

        Args:
            entry_id: ID do lançamento (Bling: ``idCaixa``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: CaixasBancosLancamentoDTO; 404: ErrorResponse
        """
        return self.obter(id_caixa=entry_id)

    def alterar(
        self,
        id_caixa: int,
        lancamento: CaixasBancosSalvarLancamentoDTO,
    ) -> JsonObject:
        """Altera um lançamento de caixa e banco.

        Endpoint: PUT /caixas/{idCaixa}

        Altera um lançamento pelo ID.

        Args:
            id_caixa: ID do lançamento (Bling: ``idCaixa``, integer, obrigatório)
            lancamento: Dados do lançamento para atualização. Request body schema: CaixasBancosSalvarLancamentoDTO

        Returns:
            Bling API response. Response schemas: 200: CaixasBancosSalvarLancamentoResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._put(f"/caixas/{id_caixa}", json=to_json_object(lancamento))

    def update(
        self,
        entry_id: int,
        entry: CaixasBancosSalvarLancamentoDTO,
    ) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Altera um lançamento de caixa e banco.

        Endpoint: PUT /caixas/{idCaixa}

        Altera um lançamento pelo ID.

        Args:
            entry_id: ID do lançamento (Bling: ``idCaixa``, integer, obrigatório)
            entry: Dados do lançamento. Request body schema: CaixasBancosSalvarLancamentoDTO

        Returns:
            Bling API response. Response schemas: 200: CaixasBancosSalvarLancamentoResponseDTO; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.alterar(id_caixa=entry_id, lancamento=entry)

    def remover(self, id_caixa: int) -> JsonObject:
        """Remove um lançamento de caixa e banco.

        Endpoint: DELETE /caixas/{idCaixa}

        Remove um lançamento pelo ID.

        Args:
            id_caixa: ID do lançamento (Bling: ``idCaixa``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self._delete(f"/caixas/{id_caixa}")

    def delete(self, entry_id: int) -> JsonObject:
        """Compatibility alias for ``remover()``.

        Remove um lançamento de caixa e banco.

        Endpoint: DELETE /caixas/{idCaixa}

        Remove um lançamento pelo ID.

        Args:
            entry_id: ID do lançamento (Bling: ``idCaixa``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 204: NoContent; 400: ErrorResponse; 404: ErrorResponse
        """
        return self.remover(id_caixa=entry_id)
