"""Tests for resource request mapping."""

from __future__ import annotations

from datetime import UTC, date, datetime

from bling_erp_api.models.generated.products import ProductCreateRequest, ProductPatchRequest
from bling_erp_api.models.generated.sales_orders import SalesOrderCreateRequest
from bling_erp_api.resources.ad_categories import AdCategoriesResource
from bling_erp_api.resources.ads import AdsResource
from bling_erp_api.resources.borderos import BorderosResource
from bling_erp_api.resources.caixas_bancos import CaixasBancosResource
from bling_erp_api.resources.contacts import ContactsResource
from bling_erp_api.resources.contas_contabeis import ContasContabeisResource
from bling_erp_api.resources.contas_pagar import ContasPagarResource
from bling_erp_api.resources.contas_receber import ContasReceberResource
from bling_erp_api.resources.depositos import DepositosResource
from bling_erp_api.resources.empresas import EmpresasResource
from bling_erp_api.resources.estoques import EstoquesResource
from bling_erp_api.resources.income_expense_categories import (
    IncomeExpenseCategoriesResource,
)
from bling_erp_api.resources.nfce import NfceResource
from bling_erp_api.resources.nfe import NfeResource
from bling_erp_api.resources.nfse import NfseResource
from bling_erp_api.resources.product_batch_entries import ProductBatchEntriesResource
from bling_erp_api.resources.product_batches import ProductBatchesResource
from bling_erp_api.resources.product_categories import ProductCategoriesResource
from bling_erp_api.resources.product_stores import ProductStoresResource
from bling_erp_api.resources.product_structures import ProductStructuresResource
from bling_erp_api.resources.product_suppliers import ProductSuppliersResource
from bling_erp_api.resources.product_variations import ProductVariationsResource
from bling_erp_api.resources.products import ProductsResource
from bling_erp_api.resources.sales_orders import SalesOrdersResource
from bling_erp_api.resources.store_categories import StoreCategoriesResource
from bling_erp_api.types import JsonObject, JsonPayload, QueryParams


class RecordingTransport:
    """Transport test double that records the latest request."""

    def __init__(self) -> None:
        """Create an empty recorder."""
        self.calls: list[tuple[str, str, QueryParams | None, JsonPayload | None]] = []

    def request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonPayload | None = None,
    ) -> JsonObject:
        """Record a request and return a simple response."""
        self.calls.append((method, path, params, json))

        return {"data": []}


def test_contacts_list_maps_to_bling_endpoint() -> None:
    """Contacts listing should map SDK params to Bling query keys."""
    transport = RecordingTransport()
    resource = ContactsResource(transport)

    response = resource.listar(pagina=2, limite=50, pesquisa="Ana")

    assert response == {"data": []}
    assert transport.calls == [
        ("GET", "/contatos", {"pagina": 2, "limite": 50, "pesquisa": "Ana"}, None),
    ]


def test_contacts_operations_map_to_bling_endpoints() -> None:
    """All contact resource methods should target the documented Bling paths."""
    transport = RecordingTransport()
    resource = ContactsResource(transport)

    resource.obter(101)
    resource.obter_consumidor_final()
    resource.criar({"nome": "Novo"})
    resource.alterar(102, {"nome": "Atualizado"})
    resource.remover(103)
    resource.remover_varios([201, 202])
    resource.obter_tipo_contato(104)
    resource.listar_tipos()
    resource.alterar_situacao(105, "A")
    resource.alterar_situacao_varios([301, 302], "I")
    resource.listar(pagina=1, ids_contatos=[10, 20])

    assert transport.calls == [
        ("GET", "/contatos/101", None, None),
        ("GET", "/contatos/consumidor-final", None, None),
        ("POST", "/contatos", None, {"nome": "Novo"}),
        ("PUT", "/contatos/102", None, {"nome": "Atualizado"}),
        ("DELETE", "/contatos/103", None, None),
        ("DELETE", "/contatos", {"idsContatos[]": [201, 202]}, None),
        ("GET", "/contatos/104/tipos", None, None),
        ("GET", "/contatos/tipos", None, None),
        ("PATCH", "/contatos/105/situacoes", None, {"situacao": "A"}),
        ("POST", "/contatos/situacoes", None, {"idsContatos": [301, 302], "situacao": "I"}),
        ("GET", "/contatos", {"pagina": 1, "limite": 100, "idsContatos[]": [10, 20]}, None),
    ]


def test_products_list_maps_to_bling_endpoint() -> None:
    """Product listing should use Portuguese SDK names and Bling query names."""
    transport = RecordingTransport()
    resource = ProductsResource(transport)

    response = resource.listar(
        pagina=2,
        limite=50,
        criterio=2,
        tipo="P",
        ids_produtos=[123, 456],
        codigos=["SKU-1"],
        data_alteracao_inicial=datetime(2024, 1, 2, 10, 30, 45, tzinfo=UTC),
    )

    assert response == {"data": []}
    assert transport.calls == [
        (
            "GET",
            "/produtos",
            {
                "pagina": 2,
                "limite": 50,
                "criterio": 2,
                "tipo": "P",
                "dataAlteracaoInicial": "2024-01-02 10:30:45",
                "idsProdutos[]": [123, 456],
                "codigos[]": ["SKU-1"],
            },
            None,
        )
    ]


def test_products_create_and_patch_serialize_model_with_api_aliases() -> None:
    """Product write operations should serialize Pydantic payloads using Bling aliases."""
    transport = RecordingTransport()
    resource = ProductsResource(transport)
    product = ProductCreateRequest.model_validate(
        {
            "nome": "Produto Teste",
            "codigo": "SKU-1",
            "preco": 19.9,
            "tipo": "P",
            "situacao": "A",
            "formato": "S",
        }
    )
    patch = ProductPatchRequest.model_validate({"preco": 21.9, "situacao": "A"})

    resource.criar(product)
    resource.alterar_parcialmente(123, patch)

    assert transport.calls == [
        (
            "POST",
            "/produtos",
            None,
            {
                "nome": "Produto Teste",
                "codigo": "SKU-1",
                "preco": 19.9,
                "tipo": "P",
                "situacao": "A",
                "formato": "S",
            },
        ),
        ("PATCH", "/produtos/123", None, {"preco": 21.9, "situacao": "A"}),
    ]


def test_products_write_operations_map_to_bling_endpoints() -> None:
    """Product write operations should map to expected Bling paths."""
    transport = RecordingTransport()
    resource = ProductsResource(transport)

    resource.obter(123)
    resource.alterar(123, {"nome": "Produto"})
    resource.remover(123)
    resource.remover_varios([123, 456])
    resource.alterar_situacao(123, "I")
    resource.alterar_situacao_varios([123, 456], "A")

    assert transport.calls == [
        ("GET", "/produtos/123", None, None),
        ("PUT", "/produtos/123", None, {"nome": "Produto"}),
        ("DELETE", "/produtos/123", None, None),
        ("DELETE", "/produtos", {"idsProdutos[]": [123, 456]}, None),
        ("PATCH", "/produtos/123/situacoes", None, {"situacao": "I"}),
        ("POST", "/produtos/situacoes", None, {"idsProdutos": [123, 456], "situacao": "A"}),
    ]


def test_sales_orders_list_maps_to_bling_endpoint() -> None:
    """Sales order listing should use Portuguese SDK names and Bling query names."""
    transport = RecordingTransport()
    resource = SalesOrdersResource(transport)

    response = resource.listar(
        pagina=2,
        limite=50,
        id_contato=123,
        ids_situacoes=[1, 2],
        data_inicial=date(2024, 1, 1),
        data_alteracao_inicial=datetime(2024, 1, 2, 10, 30, 45, tzinfo=UTC),
        numeros_lojas=["WEB-1", "WEB-2"],
    )

    assert response == {"data": []}
    assert transport.calls == [
        (
            "GET",
            "/pedidos/vendas",
            {
                "pagina": 2,
                "limite": 50,
                "idContato": 123,
                "idsSituacoes[]": [1, 2],
                "dataInicial": "2024-01-01",
                "dataAlteracaoInicial": "2024-01-02 10:30:45",
                "numerosLojas[]": ["WEB-1", "WEB-2"],
            },
            None,
        )
    ]


def test_sales_orders_english_list_alias_still_maps_to_bling_endpoint() -> None:
    """English alias should keep compatibility while Portuguese is canonical."""
    transport = RecordingTransport()
    resource = SalesOrdersResource(transport)

    resource.list(page=2, limit=50, contact_id=123)

    assert transport.calls == [
        ("GET", "/pedidos/vendas", {"pagina": 2, "limite": 50, "idContato": 123}, None)
    ]


def test_sales_orders_create_serializes_model_with_api_aliases() -> None:
    """Sales order creation should serialize Pydantic payloads using Bling aliases."""
    transport = RecordingTransport()
    resource = SalesOrdersResource(transport)
    order = SalesOrderCreateRequest.model_validate(
        {
            "data": "2024-01-10",
            "dataSaida": "2024-01-10",
            "dataPrevista": "2024-01-12",
            "contato": {"id": 123, "nome": "Ana"},
            "itens": [
                {
                    "codigo": "SKU-1",
                    "quantidade": 2,
                    "valor": 10.5,
                    "descricao": "Produto",
                    "produto": {"id": 456},
                }
            ],
            "parcelas": [
                {
                    "dataVencimento": "2024-01-20",
                    "valor": 21,
                    "formaPagamento": {"id": 789},
                }
            ],
        }
    )

    response = resource.create(order)

    assert response == {"data": []}
    assert transport.calls == [
        (
            "POST",
            "/pedidos/vendas",
            None,
            {
                "data": "2024-01-10",
                "dataSaida": "2024-01-10",
                "dataPrevista": "2024-01-12",
                "contato": {"id": 123, "nome": "Ana"},
                "itens": [
                    {
                        "codigo": "SKU-1",
                        "quantidade": 2.0,
                        "valor": 10.5,
                        "descricao": "Produto",
                        "produto": {"id": 456},
                    }
                ],
                "parcelas": [
                    {
                        "dataVencimento": "2024-01-20",
                        "valor": 21.0,
                        "formaPagamento": {"id": 789},
                    }
                ],
            },
        )
    ]


def test_sales_orders_write_operations_map_to_bling_endpoints() -> None:
    """Sales order write operations should map to the expected Bling paths."""
    transport = RecordingTransport()
    resource = SalesOrdersResource(transport)

    resource.alterar(123, {"numeroLoja": "WEB-123"})
    resource.remover(123)
    resource.remover_varios([123, 456])
    resource.alterar_situacao(123, 9)

    assert transport.calls == [
        ("PUT", "/pedidos/vendas/123", None, {"numeroLoja": "WEB-123"}),
        ("DELETE", "/pedidos/vendas/123", None, None),
        ("DELETE", "/pedidos/vendas", {"idsPedidosVendas[]": [123, 456]}, None),
        ("PATCH", "/pedidos/vendas/123/situacoes/9", None, None),
    ]


def test_sales_orders_posting_operations_map_to_bling_endpoints() -> None:
    """Sales order post actions should map to their action endpoints."""
    transport = RecordingTransport()
    resource = SalesOrdersResource(transport)

    resource.lancar_estoque(123)
    resource.lancar_estoque(123, id_deposito=456)
    resource.estornar_estoque(123)
    resource.lancar_contas(123)
    resource.estornar_contas(123)
    resource.gerar_nota_fiscal(123)
    resource.gerar_nota_fiscal_consumidor(123)

    assert transport.calls == [
        ("POST", "/pedidos/vendas/123/lancar-estoque", None, None),
        ("POST", "/pedidos/vendas/123/lancar-estoque/456", None, None),
        ("POST", "/pedidos/vendas/123/estornar-estoque", None, None),
        ("POST", "/pedidos/vendas/123/lancar-contas", None, None),
        ("POST", "/pedidos/vendas/123/estornar-contas", None, None),
        ("POST", "/pedidos/vendas/123/gerar-nfe", None, None),
        ("POST", "/pedidos/vendas/123/gerar-nfce", None, None),
    ]


def test_product_structures_map_requests_to_bling() -> None:
    """Structures resource should serialize paths, params, and payloads."""
    transport = RecordingTransport()
    resource = ProductStructuresResource(transport)

    resource.remover_varios([1, 2])
    resource.obter(3)
    resource.alterar(4, {"tipoEstoque": "F", "lancamentoEstoque": "A", "componentes": []})
    resource.remover_componentes(5, ids_componentes=[9])
    resource.vincular_componentes(
        6,
        [{"produto": {"id": 42}, "quantidade": 1.5}],
    )
    resource.alterar_componente(
        7,
        id_componente=8,
        dados={"produto": {"id": 99}, "quantidade": 2.0},
    )

    assert transport.calls == [
        ("DELETE", "/produtos/estruturas", {"idsProdutos[]": [1, 2]}, None),
        ("GET", "/produtos/estruturas/3", None, None),
        (
            "PUT",
            "/produtos/estruturas/4",
            None,
            {"tipoEstoque": "F", "lancamentoEstoque": "A", "componentes": []},
        ),
        (
            "DELETE",
            "/produtos/estruturas/5/componentes",
            {"idsComponentes[]": [9]},
            None,
        ),
        (
            "POST",
            "/produtos/estruturas/6/componentes",
            None,
            [{"produto": {"id": 42}, "quantidade": 1.5}],
        ),
        (
            "PATCH",
            "/produtos/estruturas/7/componentes/8",
            None,
            {"produto": {"id": 99}, "quantidade": 2.0},
        ),
    ]


def test_product_suppliers_map_requests_to_bling() -> None:
    """Supplier links should mirror Bling query and path conventions."""
    transport = RecordingTransport()
    resource = ProductSuppliersResource(transport)

    resource.listar(pagina=2, limite=40, id_produto=111, id_fornecedor=222)
    resource.criar(
        {"produto": {"id": 1}, "fornecedor": {"id": 2}, "codigo": "SKU-F", "garantia": 3}
    )
    resource.obter(77)
    resource.alterar(77, {"produto": {"id": 1}, "garantia": 12})
    resource.remover(88)

    assert transport.calls == [
        (
            "GET",
            "/produtos/fornecedores",
            {"pagina": 2, "limite": 40, "idProduto": 111, "idFornecedor": 222},
            None,
        ),
        (
            "POST",
            "/produtos/fornecedores",
            None,
            {
                "produto": {"id": 1},
                "fornecedor": {"id": 2},
                "codigo": "SKU-F",
                "garantia": 3,
            },
        ),
        ("GET", "/produtos/fornecedores/77", None, None),
        (
            "PUT",
            "/produtos/fornecedores/77",
            None,
            {"produto": {"id": 1}, "garantia": 12},
        ),
        ("DELETE", "/produtos/fornecedores/88", None, None),
    ]


def test_product_stores_map_requests_to_bling() -> None:
    """Filtros de loja devem espelhar parâmetros Bling camelCase."""
    transport = RecordingTransport()
    resource = ProductStoresResource(transport)

    resource.listar(
        pagina=1,
        limite=50,
        id_produto=1,
        id_loja=9,
        data_alteracao_inicial=datetime(2024, 2, 1, 14, 0, tzinfo=UTC),
        data_alteracao_final="2024-03-02 09:01:03",
    )
    resource.obter(55)

    assert transport.calls == [
        (
            "GET",
            "/produtos/lojas",
            {
                "pagina": 1,
                "limite": 50,
                "idProduto": 1,
                "idLoja": 9,
                "dataAlteracaoInicial": "2024-02-01 14:00:00",
                "dataAlteracaoFinal": "2024-03-02 09:01:03",
            },
            None,
        ),
        ("GET", "/produtos/lojas/55", None, None),
    ]


def test_product_batches_map_requests_to_bling() -> None:
    """Lotes enviam arrays obrigatórios, corpo em lista e endpoints de status."""
    transport = RecordingTransport()
    resource = ProductBatchesResource(transport)

    resource.remover_varios([1, 9])
    resource.listar(
        pagina=2,
        limite=33,
        ids_produtos=[5, 6],
        ids_lotes=[7],
        data_validade_inicial=date(2024, 1, 1),
        data_criacao_final=datetime(2024, 4, 1, 14, tzinfo=UTC),
        status="1",
        codigos_lotes=["ABC"],
    )
    resource.criar_varios(
        [
            {
                "idLote": 1,
                "produto": {"id": 11},
                "deposito": {"id": 22},
                "dataFabricacao": "2024-01-01",
                "dataValidade": "2024-06-01",
            }
        ]
    )
    resource.listar_produtos_controlam_lote([111])
    resource.obter(999)
    resource.alterar(999, {"codigoLote": "L"})
    resource.alterar_situacao(999, {"status": 2})
    resource.alterar_situacao_desativar(4321)

    assert transport.calls[:2] == [
        ("DELETE", "/produtos/lotes", {"idsLotes[]": [1, 9]}, None),
        (
            "GET",
            "/produtos/lotes",
            {
                "pagina": 2,
                "limite": 33,
                "idsProdutos[]": [5, 6],
                "idsLotes[]": [7],
                "codigosLotes[]": ["ABC"],
                "status": "1",
                "dataValidadeInicial": "2024-01-01",
                "dataCriacaoFinal": "2024-04-01 14:00:00",
            },
            None,
        ),
    ]
    batch_put = transport.calls[2]
    assert batch_put[:2] == ("PUT", "/produtos/lotes")
    assert batch_put[3] == [
        {
            "idLote": 1,
            "produto": {"id": 11},
            "deposito": {"id": 22},
            "dataFabricacao": "2024-01-01",
            "dataValidade": "2024-06-01",
        }
    ]

    assert transport.calls[3:] == [
        ("GET", "/produtos/lotes/controla-lote", {"idsProdutos[]": [111]}, None),
        ("GET", "/produtos/lotes/999", None, None),
        ("PUT", "/produtos/lotes/999", None, {"codigoLote": "L"}),
        ("PATCH", "/produtos/lotes/999/status", None, {"status": 2}),
        ("POST", "/produtos/4321/lotes/controla-lote/desativar", None, None),
    ]


def test_product_batch_entries_map_requests_to_bling() -> None:
    """Lancamentos usam paths aninhados e query idsLotes[]."""
    transport = RecordingTransport()
    resource = ProductBatchEntriesResource(transport)

    resource.obter(1001)
    resource.alterar_atributo(1001, {"observacao": "ajuste"})
    resource.listar(2002)
    resource.criar(2002, {"idLote": 2002, "observacao": "novo"})
    resource.obter_saldos(id_produto=303, id_deposito=404, ids_lotes=[505, 506])
    resource.obter_saldos_soma(id_produto=303)
    resource.obter_saldos_soma_deposito(id_produto=303, id_deposito=404)
    resource.obter_saldos_saldo(id_produto=303, id_lote=505, id_deposito=404)

    assert transport.calls == [
        ("GET", "/produtos/lotes/lancamentos/1001", None, None),
        ("PATCH", "/produtos/lotes/lancamentos/1001", None, {"observacao": "ajuste"}),
        ("GET", "/produtos/lotes/2002/lancamentos", None, None),
        (
            "POST",
            "/produtos/lotes/2002/lancamentos",
            None,
            {"idLote": 2002, "observacao": "novo"},
        ),
        (
            "GET",
            "/produtos/303/lotes/depositos/404/saldo",
            {"idsLotes[]": [505, 506]},
            None,
        ),
        ("GET", "/produtos/303/lotes/saldo/soma", None, None),
        ("GET", "/produtos/303/lotes/depositos/404/saldo/soma", None, None),
        (
            "GET",
            "/produtos/303/lotes/505/depositos/404/saldo",
            None,
            None,
        ),
    ]


def test_product_variations_map_requests_to_bling() -> None:
    """Gerar combinacoes e atributos usam payloads aliasados."""
    transport = RecordingTransport()
    resource = ProductVariationsResource(transport)

    resource.gerar_combinacoes(
        {"produtoPai": {"id": 9}, "atributos": [{"nome": "Cor", "opcoes": ["Azul"]}]}
    )
    resource.listar(10)
    resource.alterar_atributo(10, {"atributoAntigo": "Cor", "atributoNovo": "Coloração"})

    assert transport.calls == [
        (
            "POST",
            "/produtos/variacoes/atributos/gerar-combinacoes",
            None,
            {
                "produtoPai": {"id": 9},
                "atributos": [{"nome": "Cor", "opcoes": ["Azul"]}],
            },
        ),
        ("GET", "/produtos/variacoes/10", None, None),
        (
            "PATCH",
            "/produtos/variacoes/10/atributos",
            None,
            {"atributoAntigo": "Cor", "atributoNovo": "Coloração"},
        ),
    ]


# --- NF-e mapping tests ---


class TestNfeResourceMapping:
    """Mapping tests for NfeResource (NF-e endpoints)."""

    def test_nfe_list_maps_to_bling_endpoint(self) -> None:
        """NF-e listar maps pagination params to /nfe."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.listar(pagina=1, limite=10)
        assert transport.calls == [
            ("GET", "/nfe", {"pagina": 1, "limite": 10}, None),
        ]

    def test_nfe_list_with_filters(self) -> None:
        """NF-e listar maps situacao/tipo/date filters to Bling camelCase."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.listar(
            situacao=3,
            tipo=1,
            data_emissao_inicial="2024-01-01",
            data_emissao_final="2024-01-31",
        )
        assert transport.calls == [
            (
                "GET",
                "/nfe",
                {
                    "situacao": 3,
                    "tipo": 1,
                    "dataEmissaoInicial": "2024-01-01",
                    "dataEmissaoFinal": "2024-01-31",
                },
                None,
            ),
        ]

    def test_nfe_obter_maps_to_bling_endpoint(self) -> None:
        """NF-e obter maps ID to /nfe/{id}."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.obter(12345)
        assert transport.calls == [
            ("GET", "/nfe/12345", None, None),
        ]

    def test_nfe_criar_maps_to_bling_endpoint(self) -> None:
        """NF-e criar posts JSON body to /nfe."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        dados: JsonObject = {"tipo": 1, "numero": "123"}
        resource.criar(dados)
        assert len(transport.calls) == 1
        assert transport.calls[0][:2] == ("POST", "/nfe")
        assert transport.calls[0][3] is not None  # body was serialized

    def test_nfe_alterar_maps_to_bling_endpoint(self) -> None:
        """NF-e alterar puts JSON body to /nfe/{id}."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        dados: JsonObject = {"tipo": 1}
        resource.alterar(12345, dados)
        assert transport.calls[0][:2] == ("PUT", "/nfe/12345")
        assert transport.calls[0][3] is not None

    def test_nfe_remover_varios_maps_to_bling_endpoint(self) -> None:
        """NF-e remover_varios sends ids as query params to DELETE /nfe."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.remover_varios([1, 2, 3])
        assert transport.calls == [
            ("DELETE", "/nfe", {"idsNotas[]": [1, 2, 3]}, None),
        ]

    def test_nfe_autorizar_maps_to_bling_endpoint(self) -> None:
        """NF-e autorizar sends email flag to /nfe/{id}/enviar."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.autorizar(12345, enviar_email=True)
        assert transport.calls == [
            ("POST", "/nfe/12345/enviar", {"enviarEmail": True}, None),
        ]

    def test_nfe_autorizar_without_email(self) -> None:
        """NF-e autorizar works without email param."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.autorizar(12345)
        assert transport.calls[0][:2] == ("POST", "/nfe/12345/enviar")

    def test_nfe_lancar_contas_maps_to_bling_endpoint(self) -> None:
        """NF-e lancar_contas posts to /nfe/{id}/lancar-contas."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.lancar_contas(12345)
        assert transport.calls == [
            ("POST", "/nfe/12345/lancar-contas", None, None),
        ]

    def test_nfe_estornar_contas_maps_to_bling_endpoint(self) -> None:
        """NF-e estornar_contas posts to /nfe/{id}/estornar-contas."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.estornar_contas(12345)
        assert transport.calls == [
            ("POST", "/nfe/12345/estornar-contas", None, None),
        ]

    def test_nfe_lancar_estoque_maps_to_bling_endpoint(self) -> None:
        """NF-e lancar_estoque posts to /nfe/{id}/lancar-estoque."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.lancar_estoque(12345)
        assert transport.calls == [
            ("POST", "/nfe/12345/lancar-estoque", None, None),
        ]

    def test_nfe_lancar_estoque_with_deposito(self) -> None:
        """NF-e lancar_estoque with deposito appends /{deposito}."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.lancar_estoque(12345, id_deposito=5)
        assert transport.calls == [
            ("POST", "/nfe/12345/lancar-estoque/5", None, None),
        ]

    def test_nfe_estornar_estoque_maps_to_bling_endpoint(self) -> None:
        """NF-e estornar_estoque posts to /nfe/{id}/estornar-estoque."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.estornar_estoque(12345)
        assert transport.calls == [
            ("POST", "/nfe/12345/estornar-estoque", None, None),
        ]

    def test_nfe_obter_documento_nota_fiscal_maps_to_bling_endpoint(
        self,
    ) -> None:
        """NF-e get document maps chave de acesso to /nfe/documento/{chave}."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.obter_documento_nota_fiscal("35240112345678901234567890123456789012345678")
        call = transport.calls[0]
        assert call[:2] == (
            "GET",
            "/nfe/documento/35240112345678901234567890123456789012345678",
        )
        # compact_params returns {} when all values are None
        assert call[2] == {}
        assert call[3] is None

    def test_nfe_obter_documento_nota_fiscal_with_formato(self) -> None:
        """NF-e get document passes formato as query param."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.obter_documento_nota_fiscal(
            "35240112345678901234567890123456789012345678", formato="pdf"
        )
        assert transport.calls == [
            (
                "GET",
                "/nfe/documento/35240112345678901234567890123456789012345678",
                {"formato": "pdf"},
                None,
            ),
        ]

    def test_nfe_english_alias_get(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.get(12345)
        assert transport.calls == [
            ("GET", "/nfe/12345", None, None),
        ]

    def test_nfe_english_alias_list(self) -> None:
        """English alias 'list' should map to 'listar'."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.list(page=1)
        assert transport.calls[0][:2] == ("GET", "/nfe")

    def test_nfe_english_alias_authorize(self) -> None:
        """English alias 'authorize' should map to 'autorizar'."""
        transport = RecordingTransport()
        resource = NfeResource(transport)
        resource.authorize(12345)
        assert transport.calls[0][:2] == ("POST", "/nfe/12345/enviar")


# --- NFC-e mapping tests ---


class TestNfceResourceMapping:
    """Mapping tests for NfceResource (NFC-e endpoints)."""

    def test_nfce_list_maps_to_bling_endpoint(self) -> None:
        """NFC-e listar maps pagination params to /nfce."""
        transport = RecordingTransport()
        resource = NfceResource(transport)
        resource.listar(pagina=1, limite=20)
        assert transport.calls == [
            ("GET", "/nfce", {"pagina": 1, "limite": 20}, None),
        ]

    def test_nfce_list_with_filters(self) -> None:
        """NFC-e listar maps situacao/date filters to Bling camelCase."""
        transport = RecordingTransport()
        resource = NfceResource(transport)
        resource.listar(situacao=3, data_emissao_inicial="2024-01-01")
        assert transport.calls == [
            ("GET", "/nfce", {"situacao": 3, "dataEmissaoInicial": "2024-01-01"}, None),
        ]

    def test_nfce_obter_maps_to_bling_endpoint(self) -> None:
        """NFC-e obter maps ID to /nfce/{id}."""
        transport = RecordingTransport()
        resource = NfceResource(transport)
        resource.obter(54321)
        assert transport.calls == [
            ("GET", "/nfce/54321", None, None),
        ]

    def test_nfce_criar_maps_to_bling_endpoint(self) -> None:
        """NFC-e criar posts JSON body to /nfce."""
        transport = RecordingTransport()
        resource = NfceResource(transport)
        dados: JsonObject = {"tipo": 1}
        resource.criar(dados)
        assert transport.calls[0][:2] == ("POST", "/nfce")
        assert transport.calls[0][3] is not None

    def test_nfce_alterar_maps_to_bling_endpoint(self) -> None:
        """NFC-e alterar puts to /nfce/{id}."""
        transport = RecordingTransport()
        resource = NfceResource(transport)
        resource.alterar(54321, {"tipo": 1})
        assert transport.calls[0][:2] == ("PUT", "/nfce/54321")

    def test_nfce_autorizar_maps_to_bling_endpoint(self) -> None:
        """NFC-e autorizar sends email flag to /nfce/{id}/enviar."""
        transport = RecordingTransport()
        resource = NfceResource(transport)
        resource.autorizar(54321, enviar_email=True)
        assert transport.calls == [
            ("POST", "/nfce/54321/enviar", {"enviarEmail": True}, None),
        ]

    def test_nfce_lancar_contas_maps_to_bling_endpoint(self) -> None:
        """NFC-e lancar_contas posts to /nfce/{id}/lancar-contas."""
        transport = RecordingTransport()
        resource = NfceResource(transport)
        resource.lancar_contas(54321)
        assert transport.calls == [
            ("POST", "/nfce/54321/lancar-contas", None, None),
        ]

    def test_nfce_estornar_estoque_maps_to_bling_endpoint(self) -> None:
        """NFC-e estornar_estoque posts to /nfce/{id}/estornar-estoque."""
        transport = RecordingTransport()
        resource = NfceResource(transport)
        resource.estornar_estoque(54321)
        assert transport.calls == [
            ("POST", "/nfce/54321/estornar-estoque", None, None),
        ]

    def test_nfce_lancar_estoque_with_deposito(self) -> None:
        """NFC-e lancar_estoque with deposito appends /{deposito}."""
        transport = RecordingTransport()
        resource = NfceResource(transport)
        resource.lancar_estoque(54321, id_deposito=3)
        assert transport.calls == [
            ("POST", "/nfce/54321/lancar-estoque/3", None, None),
        ]

    def test_nfce_english_alias_get(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = NfceResource(transport)
        resource.get(54321)
        assert transport.calls == [
            ("GET", "/nfce/54321", None, None),
        ]


# --- NFS-e mapping tests ---


class TestNfseResourceMapping:
    """Mapping tests for NfseResource (NFS-e endpoints)."""

    def test_nfse_list_maps_to_bling_endpoint(self) -> None:
        """NFS-e listar maps pagination params to /nfse."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        resource.listar(pagina=1, limite=10)
        assert transport.calls == [
            ("GET", "/nfse", {"pagina": 1, "limite": 10}, None),
        ]

    def test_nfse_list_with_situacao(self) -> None:
        """NFS-e listar maps situacao filter to /nfse."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        resource.listar(situacao=3)
        assert transport.calls == [
            ("GET", "/nfse", {"situacao": 3}, None),
        ]

    def test_nfse_obter_maps_to_bling_endpoint(self) -> None:
        """NFS-e obter maps ID to /nfse/{id}."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        resource.obter(111)
        assert transport.calls == [
            ("GET", "/nfse/111", None, None),
        ]

    def test_nfse_criar_maps_to_bling_endpoint(self) -> None:
        """NFS-e criar posts JSON body to /nfse."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        dados: JsonObject = {"numero": "111"}
        resource.criar(dados)
        assert transport.calls[0][:2] == ("POST", "/nfse")
        assert transport.calls[0][3] is not None

    def test_nfse_remover_maps_to_bling_endpoint(self) -> None:
        """NFS-e remover sends DELETE to /nfse/{id}."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        resource.remover(111)
        assert transport.calls == [
            ("DELETE", "/nfse/111", None, None),
        ]

    def test_nfse_autorizar_maps_to_bling_endpoint(self) -> None:
        """NFS-e autorizar posts to /nfse/{id}/enviar."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        resource.autorizar(111)
        assert transport.calls == [
            ("POST", "/nfse/111/enviar", None, None),
        ]

    def test_nfse_cancelar_maps_to_bling_endpoint(self) -> None:
        """NFS-e cancelar posts cancellation body to /nfse/{id}/cancelar."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        dados: JsonObject = {"codigoMotivo": 1, "justificativa": "Erro na emissão"}
        resource.cancelar(111, dados)
        assert transport.calls[0][:2] == ("POST", "/nfse/111/cancelar")
        assert transport.calls[0][3] is not None

    def test_nfse_obter_configuracoes_maps_to_bling_endpoint(self) -> None:
        """NFS-e obter_configuracoes gets /nfse/configuracoes."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        resource.obter_configuracoes()
        assert transport.calls == [
            ("GET", "/nfse/configuracoes", None, None),
        ]

    def test_nfse_alterar_configuracoes_maps_to_bling_endpoint(self) -> None:
        """NFS-e alterar_configuracoes puts to /nfse/configuracoes."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        dados: JsonObject = {"basicas": {"emissorPadrao": 1}}
        resource.alterar_configuracoes(dados)
        assert transport.calls[0][:2] == ("PUT", "/nfse/configuracoes")
        assert transport.calls[0][3] is not None

    def test_nfse_english_alias_get(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        resource.get(111)
        assert transport.calls == [
            ("GET", "/nfse/111", None, None),
        ]

    def test_nfse_english_alias_delete(self) -> None:
        """English alias 'delete' should map to 'remover'."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        resource.delete(111)
        assert transport.calls == [
            ("DELETE", "/nfse/111", None, None),
        ]

    def test_nfse_english_alias_get_settings(self) -> None:
        """English alias 'get_settings' should map to 'obter_configuracoes'."""
        transport = RecordingTransport()
        resource = NfseResource(transport)
        resource.get_settings()
        assert transport.calls == [
            ("GET", "/nfse/configuracoes", None, None),
        ]


# --- Ads (Anúncios) mapping tests ---


class TestAdsResourceMapping:
    """Mapping tests for AdsResource (Anúncios endpoints)."""

    def test_ads_listar_maps_to_bling_endpoint(self) -> None:
        """Ads listar maps required params to GET /anuncios."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.listar(tipo_integracao="MercadoLivre", id_loja=1)
        assert len(transport.calls) == 1
        assert transport.calls[0][0] == "GET"
        assert transport.calls[0][1] == "/anuncios?pagina=1&limite=100"
        assert transport.calls[0][2] == {"tipoIntegracao": "MercadoLivre", "idLoja": 1}

    def test_ads_listar_with_filters(self) -> None:
        """Ads listar maps optional filters to Bling camelCase."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.listar(
            tipo_integracao="MercadoLivre",
            id_loja=1,
            situacao=1,
            id_produto=99,
        )
        assert transport.calls[0][2] == {
            "tipoIntegracao": "MercadoLivre",
            "idLoja": 1,
            "situacao": 1,
            "idProduto": 99,
        }

    def test_ads_obter_maps_to_bling_endpoint(self) -> None:
        """Ads obter maps ID to GET /anuncios/{id}."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.obter(123, tipo_integracao="MercadoLivre", id_loja=1)
        assert transport.calls == [
            (
                "GET",
                "/anuncios/123",
                {"tipoIntegracao": "MercadoLivre", "idLoja": 1},
                None,
            ),
        ]

    def test_ads_criar_maps_to_bling_endpoint(self) -> None:
        """Ads criar posts JSON body to POST /anuncios."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        dados: JsonObject = {
            "produto": {"id": 1},
            "integracao": {"tipo": "ML"},
            "loja": {"id": 1},
        }
        resource.criar(dados)
        assert len(transport.calls) == 1
        assert transport.calls[0][0] == "POST"
        assert transport.calls[0][1] == "/anuncios"
        assert transport.calls[0][3] is not None

    def test_ads_alterar_maps_to_bling_endpoint(self) -> None:
        """Ads alterar puts JSON body to PUT /anuncios/{id}."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        dados: JsonObject = {"nome": "Atualizado"}
        resource.alterar(123, dados)
        assert transport.calls[0][0] == "PUT"
        assert transport.calls[0][1] == "/anuncios/123"
        assert transport.calls[0][3] is not None

    def test_ads_remover_maps_to_bling_endpoint(self) -> None:
        """Ads remover sends DELETE to /anuncios/{id} with params."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.remover(123, tipo_integracao="MercadoLivre", id_loja=1)
        assert transport.calls == [
            (
                "DELETE",
                "/anuncios/123",
                {"tipoIntegracao": "MercadoLivre", "idLoja": 1},
                None,
            ),
        ]

    def test_ads_publicar_maps_to_bling_endpoint(self) -> None:
        """Ads publicar posts to POST /anuncios/{id}/publicar."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.publicar(123, tipo_integracao="MercadoLivre", id_loja=1)
        assert transport.calls == [
            (
                "POST",
                "/anuncios/123/publicar",
                {"tipoIntegracao": "MercadoLivre", "idLoja": 1},
                None,
            ),
        ]

    def test_ads_pausar_maps_to_bling_endpoint(self) -> None:
        """Ads pausar posts to POST /anuncios/{id}/pausar."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.pausar(123, tipo_integracao="MercadoLivre", id_loja=1)
        assert transport.calls == [
            (
                "POST",
                "/anuncios/123/pausar",
                {"tipoIntegracao": "MercadoLivre", "idLoja": 1},
                None,
            ),
        ]

    def test_ads_english_alias_list(self) -> None:
        """English alias 'list' should map to 'listar'."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.list(integration_type="MercadoLivre", store_id=1)
        assert transport.calls[0][0] == "GET"
        assert "anuncios" in transport.calls[0][1]

    def test_ads_english_alias_get(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.get(123, integration_type="MercadoLivre", store_id=1)
        assert transport.calls[0][0] == "GET"
        assert "/anuncios/123" in transport.calls[0][1]

    def test_ads_english_alias_create(self) -> None:
        """English alias 'create' should map to 'criar'."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.create({"produto": {"id": 1}, "integracao": {"tipo": "ML"}, "loja": {"id": 1}})
        assert transport.calls[0][0] == "POST"
        assert transport.calls[0][1] == "/anuncios"

    def test_ads_english_alias_publish(self) -> None:
        """English alias 'publish' should map to 'publicar'."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.publish(123, integration_type="MercadoLivre", store_id=1)
        assert transport.calls[0][0] == "POST"
        assert "/anuncios/123/publicar" in transport.calls[0][1]

    def test_ads_english_alias_pause(self) -> None:
        """English alias 'pause' should map to 'pausar'."""
        transport = RecordingTransport()
        resource = AdsResource(transport)
        resource.pause(123, integration_type="MercadoLivre", store_id=1)
        assert transport.calls[0][0] == "POST"
        assert "/anuncios/123/pausar" in transport.calls[0][1]


# --- Ad Categories (Anúncios - Categorias) mapping tests ---


class TestAdCategoriesResourceMapping:
    """Mapping tests for AdCategoriesResource (Anúncios - Categorias endpoints)."""

    def test_ad_categories_listar_maps_to_bling_endpoint(self) -> None:
        """Ad categories listar maps required params to GET /anuncios/categorias."""
        transport = RecordingTransport()
        resource = AdCategoriesResource(transport)
        resource.listar(tipo_integracao="MercadoLivre", id_loja=1)
        assert transport.calls == [
            (
                "GET",
                "/anuncios/categorias",
                {"tipoIntegracao": "MercadoLivre", "idLoja": 1},
                None,
            ),
        ]

    def test_ad_categories_listar_with_filters(self) -> None:
        """Ad categories listar maps optional filters."""
        transport = RecordingTransport()
        resource = AdCategoriesResource(transport)
        resource.listar(
            tipo_integracao="MercadoLivre",
            id_loja=1,
            id_categoria=42,
            tipo_produto="new",
        )
        assert transport.calls[0][2] == {
            "tipoIntegracao": "MercadoLivre",
            "idLoja": 1,
            "idCategoria": 42,
            "tipoProduto": "new",
        }

    def test_ad_categories_obter_maps_to_bling_endpoint(self) -> None:
        """Ad categories obter maps category ID to GET /anuncios/categorias/{id}."""
        transport = RecordingTransport()
        resource = AdCategoriesResource(transport)
        resource.obter("MLB1430", tipo_integracao="MercadoLivre", id_loja=1)
        assert transport.calls == [
            (
                "GET",
                "/anuncios/categorias/MLB1430",
                {"tipoIntegracao": "MercadoLivre", "idLoja": 1},
                None,
            ),
        ]

    def test_ad_categories_english_alias_list(self) -> None:
        """English alias 'list' should map to 'listar'."""
        transport = RecordingTransport()
        resource = AdCategoriesResource(transport)
        resource.list(integration_type="MercadoLivre", store_id=1)
        assert transport.calls[0][0] == "GET"
        assert "/anuncios/categorias" in transport.calls[0][1]

    def test_ad_categories_english_alias_get(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = AdCategoriesResource(transport)
        resource.get("MLB1430", integration_type="MercadoLivre", store_id=1)
        assert transport.calls[0][0] == "GET"
        assert "/anuncios/categorias/MLB1430" in transport.calls[0][1]


# --- Borderos (Borderôs) mapping tests ---


class TestBorderosResourceMapping:
    """Mapping tests for BorderosResource."""

    def test_borderos_obter_maps_to_bling_endpoint(self) -> None:
        """Borderos obter maps ID to GET /borderos/{idBordero}."""
        transport = RecordingTransport()
        resource = BorderosResource(transport)
        resource.obter(123456)
        assert transport.calls == [("GET", "/borderos/123456", None, None)]

    def test_borderos_remover_maps_to_bling_endpoint(self) -> None:
        """Borderos remover sends DELETE to /borderos/{idBordero}."""
        transport = RecordingTransport()
        resource = BorderosResource(transport)
        resource.remover(123456)
        assert transport.calls == [("DELETE", "/borderos/123456", None, None)]

    def test_borderos_english_alias_get(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = BorderosResource(transport)
        resource.get(123456)
        assert transport.calls[0][0] == "GET"
        assert transport.calls[0][1] == "/borderos/123456"

    def test_borderos_english_alias_delete(self) -> None:
        """English alias 'delete' should map to 'remover'."""
        transport = RecordingTransport()
        resource = BorderosResource(transport)
        resource.delete(123456)
        assert transport.calls[0][0] == "DELETE"
        assert transport.calls[0][1] == "/borderos/123456"


# --- Caixas e Bancos mapping tests ---


class TestCaixasBancosResourceMapping:
    """Mapping tests for CaixasBancosResource."""

    def test_caixas_bancos_listar_maps_to_bling_endpoint(self) -> None:
        """Caixas listar maps to GET /caixas with pagina in URL."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        resource.listar()
        assert transport.calls == [("GET", "/caixas?pagina=1", {}, None)]

    def test_caixas_bancos_listar_with_filters(self) -> None:
        """Caixas listar maps optional filters to Bling camelCase."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        resource.listar(
            data_inicial="2025-01-01",
            data_final="2025-01-31",
            ids_categorias=[10, 20],
            id_conta_financeira=5,
            situacao_conciliacao=1,
            situacao="R",
        )
        assert transport.calls[0][0] == "GET"
        assert transport.calls[0][1] == "/caixas?pagina=1"
        assert transport.calls[0][2] == {
            "dataInicial": "2025-01-01",
            "dataFinal": "2025-01-31",
            "idsCategorias": [10, 20],
            "idContaFinanceira": 5,
            "situacaoConciliacao": 1,
            "situacao": "R",
        }
        assert transport.calls[0][3] is None

    def test_caixas_bancos_obter_maps_to_bling_endpoint(self) -> None:
        """Caixas obter maps ID to GET /caixas/{idCaixa}."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        resource.obter(123456)
        assert transport.calls == [("GET", "/caixas/123456", None, None)]

    def test_caixas_bancos_criar_maps_to_bling_endpoint(self) -> None:
        """Caixas criar posts JSON body to POST /caixas."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        dados: JsonObject = {
            "data": "2025-02-01",
            "valor": 350.00,
            "debCred": "C",
            "competencia": "2025-02-01",
            "observacoes": "Teste",
        }
        resource.criar(dados)
        assert len(transport.calls) == 1
        assert transport.calls[0][0] == "POST"
        assert transport.calls[0][1] == "/caixas"
        assert transport.calls[0][3] is not None

    def test_caixas_bancos_alterar_maps_to_bling_endpoint(self) -> None:
        """Caixas alterar puts JSON body to PUT /caixas/{idCaixa}."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        dados: JsonObject = {
            "data": "2025-02-01",
            "valor": 500.00,
            "debCred": "D",
            "competencia": "2025-02-01",
            "observacoes": "Atualizado",
        }
        resource.alterar(123456, dados)
        assert transport.calls[0][0] == "PUT"
        assert transport.calls[0][1] == "/caixas/123456"
        assert transport.calls[0][3] is not None

    def test_caixas_bancos_remover_maps_to_bling_endpoint(self) -> None:
        """Caixas remover sends DELETE to /caixas/{idCaixa}."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        resource.remover(123456)
        assert transport.calls == [("DELETE", "/caixas/123456", None, None)]

    def test_caixas_bancos_list_english_alias(self) -> None:
        """English alias 'list' should map to 'listar'."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        resource.list(page=2, start_date="2025-01-01", reconciliation_status=1)
        assert transport.calls[0][0] == "GET"
        assert "caixas" in transport.calls[0][1]
        assert "pagina=2" in transport.calls[0][1]
        params = transport.calls[0][2]
        assert params is not None
        assert params["dataInicial"] == "2025-01-01"
        assert params["situacaoConciliacao"] == 1

    def test_caixas_bancos_create_english_alias(self) -> None:
        """English alias 'create' should map to 'criar'."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        resource.create(
            {
                "data": "2025-02-01",
                "valor": 100.00,
                "debCred": "C",
                "competencia": "2025-02-01",
                "observacoes": "Test",
            }
        )
        assert transport.calls[0][0] == "POST"
        assert transport.calls[0][1] == "/caixas"

    def test_caixas_bancos_get_english_alias(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        resource.get(123456)
        assert transport.calls[0][0] == "GET"
        assert transport.calls[0][1] == "/caixas/123456"

    def test_caixas_bancos_update_english_alias(self) -> None:
        """English alias 'update' should map to 'alterar'."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        resource.update(
            123456,
            {
                "data": "2025-02-01",
                "valor": 500.00,
                "debCred": "D",
                "competencia": "2025-02-01",
                "observacoes": "Upd",
            },
        )
        assert transport.calls[0][0] == "PUT"
        assert transport.calls[0][1] == "/caixas/123456"

    def test_caixas_bancos_delete_english_alias(self) -> None:
        """English alias 'delete' should map to 'remover'."""
        transport = RecordingTransport()
        resource = CaixasBancosResource(transport)
        resource.delete(123456)
        assert transport.calls[0][0] == "DELETE"
        assert transport.calls[0][1] == "/caixas/123456"


# --- Store Categories (Categorias - Lojas) mapping tests ---


class TestStoreCategoriesResourceMapping:
    """Mapping tests for StoreCategoriesResource."""

    def test_store_categories_listar_maps_to_bling_endpoint(self) -> None:
        """Store categories listar maps to GET /categorias/lojas."""
        transport = RecordingTransport()
        resource = StoreCategoriesResource(transport)
        resource.listar()
        assert transport.calls == [("GET", "/categorias/lojas?pagina=1&limite=100", {}, None)]

    def test_store_categories_listar_with_filters(self) -> None:
        """Store categories listar maps optional filters."""
        transport = RecordingTransport()
        resource = StoreCategoriesResource(transport)
        resource.listar(id_loja=1, id_categoria_produto=50)
        assert transport.calls[0][0] == "GET"
        assert transport.calls[0][2] == {"idLoja": 1, "idCategoriaProduto": 50}

    def test_store_categories_obter_maps_to_bling_endpoint(self) -> None:
        """Store categories obter maps ID to GET /categorias/lojas/{id}."""
        transport = RecordingTransport()
        resource = StoreCategoriesResource(transport)
        resource.obter(100)
        assert transport.calls == [("GET", "/categorias/lojas/100", None, None)]

    def test_store_categories_criar_maps_to_bling_endpoint(self) -> None:
        """Store categories criar posts to POST /categorias/lojas."""
        transport = RecordingTransport()
        resource = StoreCategoriesResource(transport)
        resource.criar({"loja": {"id": 1}, "descricao": "Test", "codigo": "ABC"})
        assert transport.calls[0][0] == "POST"
        assert transport.calls[0][1] == "/categorias/lojas"
        assert transport.calls[0][3] is not None

    def test_store_categories_alterar_maps_to_bling_endpoint(self) -> None:
        """Store categories alterar puts to PUT /categorias/lojas/{id}."""
        transport = RecordingTransport()
        resource = StoreCategoriesResource(transport)
        resource.alterar(100, {"loja": {"id": 1}, "descricao": "Upd", "codigo": "XYZ"})
        assert transport.calls[0][0] == "PUT"
        assert transport.calls[0][1] == "/categorias/lojas/100"

    def test_store_categories_remover_maps_to_bling_endpoint(self) -> None:
        """Store categories remover sends DELETE to /categorias/lojas/{id}."""
        transport = RecordingTransport()
        resource = StoreCategoriesResource(transport)
        resource.remover(100)
        assert transport.calls == [("DELETE", "/categorias/lojas/100", None, None)]

    def test_store_categories_english_alias_list(self) -> None:
        """English alias 'list' should map to 'listar'."""
        transport = RecordingTransport()
        resource = StoreCategoriesResource(transport)
        resource.list(store_id=5)
        assert transport.calls[0][0] == "GET"
        params = transport.calls[0][2]
        assert params is not None
        assert params["idLoja"] == 5

    def test_store_categories_english_alias_get(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = StoreCategoriesResource(transport)
        resource.get(100)
        assert transport.calls[0] == ("GET", "/categorias/lojas/100", None, None)

    def test_store_categories_english_alias_create(self) -> None:
        """English alias 'create' should map to 'criar'."""
        transport = RecordingTransport()
        resource = StoreCategoriesResource(transport)
        resource.create({"loja": {"id": 1}, "descricao": "Test", "codigo": "X"})
        assert transport.calls[0][0] == "POST"

    def test_store_categories_english_alias_delete(self) -> None:
        """English alias 'delete' should map to 'remover'."""
        transport = RecordingTransport()
        resource = StoreCategoriesResource(transport)
        resource.delete(100)
        assert transport.calls[0] == ("DELETE", "/categorias/lojas/100", None, None)


# --- Product Categories (Categorias - Produtos) mapping tests ---


class TestProductCategoriesResourceMapping:
    """Mapping tests for ProductCategoriesResource."""

    def test_product_categories_listar_maps_to_bling_endpoint(self) -> None:
        """Product categories listar maps to GET /categorias/produtos."""
        transport = RecordingTransport()
        resource = ProductCategoriesResource(transport)
        resource.listar()
        assert transport.calls == [("GET", "/categorias/produtos?pagina=1&limite=100", None, None)]

    def test_product_categories_obter_maps_to_bling_endpoint(self) -> None:
        """Product categories obter maps ID to GET .../{id}."""
        transport = RecordingTransport()
        resource = ProductCategoriesResource(transport)
        resource.obter(200)
        assert transport.calls == [("GET", "/categorias/produtos/200", None, None)]

    def test_product_categories_criar_maps_to_bling_endpoint(self) -> None:
        """Product categories criar posts to POST."""
        transport = RecordingTransport()
        resource = ProductCategoriesResource(transport)
        resource.criar({"id": 1, "descricao": "Nova"})
        assert transport.calls[0][0] == "POST"
        assert transport.calls[0][1] == "/categorias/produtos"

    def test_product_categories_alterar_maps_to_bling_endpoint(self) -> None:
        """Product categories alterar puts to PUT."""
        transport = RecordingTransport()
        resource = ProductCategoriesResource(transport)
        resource.alterar(200, {"descricao": "Atualizada"})
        assert transport.calls[0][0] == "PUT"
        assert transport.calls[0][1] == "/categorias/produtos/200"

    def test_product_categories_remover_maps_to_bling_endpoint(self) -> None:
        """Product categories remover sends DELETE."""
        transport = RecordingTransport()
        resource = ProductCategoriesResource(transport)
        resource.remover(200)
        assert transport.calls == [("DELETE", "/categorias/produtos/200", None, None)]

    def test_product_categories_english_alias_list(self) -> None:
        """EN alias 'list' maps to listar."""
        transport = RecordingTransport()
        resource = ProductCategoriesResource(transport)
        resource.list(page=3, limit=50)
        assert "pagina=3" in transport.calls[0][1]
        assert "limite=50" in transport.calls[0][1]

    def test_product_categories_english_alias_get(self) -> None:
        """EN alias 'get' maps to obter."""
        transport = RecordingTransport()
        resource = ProductCategoriesResource(transport)
        resource.get(200)
        assert transport.calls[0] == ("GET", "/categorias/produtos/200", None, None)

    def test_product_categories_english_alias_create(self) -> None:
        """EN alias 'create' maps to criar."""
        transport = RecordingTransport()
        resource = ProductCategoriesResource(transport)
        resource.create({"descricao": "Nova"})
        assert transport.calls[0][0] == "POST"

    def test_product_categories_english_alias_update(self) -> None:
        """EN alias 'update' maps to alterar."""
        transport = RecordingTransport()
        resource = ProductCategoriesResource(transport)
        resource.update(200, {"descricao": "Upd"})
        assert transport.calls[0][0] == "PUT"

    def test_product_categories_english_alias_delete(self) -> None:
        """EN alias 'delete' maps to remover."""
        transport = RecordingTransport()
        resource = ProductCategoriesResource(transport)
        resource.delete(200)
        assert transport.calls[0] == ("DELETE", "/categorias/produtos/200", None, None)


# --- Income/Expense Categories (Categorias - Receitas e Despesas) mapping tests ---


class TestIncomeExpenseCategoriesResourceMapping:
    """Mapping tests for IncomeExpenseCategoriesResource."""

    def test_income_expense_listar_maps_to_bling_endpoint(self) -> None:
        """Income/expense listar maps to GET."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.listar()
        assert transport.calls == [
            ("GET", "/categorias/receitas-despesas?pagina=1&limite=100", {}, None)
        ]

    def test_income_expense_listar_with_filters(self) -> None:
        """Income/expense listar maps tipo and situacao."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.listar(tipo=2, situacao=1)
        assert transport.calls[0][2] == {"tipo": 2, "situacao": 1}

    def test_income_expense_obter_maps_to_bling_endpoint(self) -> None:
        """Income/expense obter maps ID."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.obter(300)
        assert transport.calls == [("GET", "/categorias/receitas-despesas/300", None, None)]

    def test_income_expense_criar_maps_to_bling_endpoint(self) -> None:
        """Income/expense criar posts to POST."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.criar({"descricao": "Nova", "tipo": 2})
        assert transport.calls[0][0] == "POST"
        assert transport.calls[0][1] == "/categorias/receitas-despesas"

    def test_income_expense_alterar_maps_to_bling_endpoint(self) -> None:
        """Income/expense alterar puts."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.alterar(300, {"descricao": "Upd", "tipo": 1})
        assert transport.calls[0][0] == "PUT"
        assert transport.calls[0][1] == "/categorias/receitas-despesas/300"

    def test_income_expense_remover_maps_to_bling_endpoint(self) -> None:
        """Income/expense remover sends DELETE."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.remover(300)
        assert transport.calls == [("DELETE", "/categorias/receitas-despesas/300", None, None)]

    def test_income_expense_remover_varios_maps_to_bling_endpoint(self) -> None:
        """Income/expense remover_varios sends DELETE with idsCategorias."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.remover_varios([10, 20, 30])
        assert transport.calls[0][0] == "DELETE"
        assert transport.calls[0][1] == "/categorias/receitas-despesas"
        assert transport.calls[0][2] == {"idsCategorias[]": [10, 20, 30]}

    def test_income_expense_english_alias_list(self) -> None:
        """EN alias 'list' maps to listar."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.list(type_=2, status=1)
        assert transport.calls[0][2] == {"tipo": 2, "situacao": 1}

    def test_income_expense_english_alias_get(self) -> None:
        """EN alias 'get' maps to obter."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.get(300)
        assert transport.calls[0] == ("GET", "/categorias/receitas-despesas/300", None, None)

    def test_income_expense_english_alias_create(self) -> None:
        """EN alias 'create' maps to criar."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.create({"descricao": "Test", "tipo": 2})
        assert transport.calls[0][0] == "POST"

    def test_income_expense_english_alias_update(self) -> None:
        """EN alias 'update' maps to alterar."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.update(300, {"descricao": "Upd", "tipo": 1})
        assert transport.calls[0][0] == "PUT"

    def test_income_expense_english_alias_delete(self) -> None:
        """EN alias 'delete' maps to remover."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.delete(300)
        assert transport.calls[0] == ("DELETE", "/categorias/receitas-despesas/300", None, None)

    def test_income_expense_english_alias_delete_multiple(self) -> None:
        """EN alias 'delete_multiple' maps to remover_varios."""
        transport = RecordingTransport()
        resource = IncomeExpenseCategoriesResource(transport)
        resource.delete_multiple([10, 20])
        assert transport.calls[0][0] == "DELETE"
        assert transport.calls[0][2] == {"idsCategorias[]": [10, 20]}


# --- Contas a Pagar mapping tests ---


class TestContasPagarResourceMapping:
    """Mapping tests for ContasPagarResource."""

    def test_contas_pagar_listar_maps_to_bling_endpoint(self) -> None:
        """Contas pagar listar maps pagination params to GET /contas/pagar."""
        transport = RecordingTransport()
        resource = ContasPagarResource(transport)
        resource.listar(pagina=1, limite=100)
        assert transport.calls == [
            ("GET", "/contas/pagar?pagina=1&limite=100", {}, None),
        ]

    def test_contas_pagar_listar_with_filters(self) -> None:
        """Contas pagar listar maps situacao filter to Bling camelCase."""
        transport = RecordingTransport()
        resource = ContasPagarResource(transport)
        resource.listar(pagina=1, limite=100, situacao=1)
        assert transport.calls[0] == (
            "GET",
            "/contas/pagar?pagina=1&limite=100",
            {"situacao": 1},
            None,
        )

    def test_contas_pagar_obter_maps_to_bling_endpoint(self) -> None:
        """Contas pagar obter maps ID to GET /contas/pagar/{id}."""
        transport = RecordingTransport()
        resource = ContasPagarResource(transport)
        resource.obter(123)
        assert transport.calls == [
            ("GET", "/contas/pagar/123", None, None),
        ]

    def test_contas_pagar_criar_maps_to_bling_endpoint(self) -> None:
        """Contas pagar criar posts JSON body to POST /contas/pagar."""
        transport = RecordingTransport()
        resource = ContasPagarResource(transport)
        dados: JsonObject = {"vencimento": "2025-03-15", "valor": 1500.00}
        resource.criar(dados)
        assert transport.calls[0][:2] == ("POST", "/contas/pagar")
        body = transport.calls[0][3]
        assert body is not None

    def test_contas_pagar_remover_maps_to_bling_endpoint(self) -> None:
        """Contas pagar remover sends DELETE to /contas/pagar/{id}."""
        transport = RecordingTransport()
        resource = ContasPagarResource(transport)
        resource.remover(123)
        assert transport.calls == [
            ("DELETE", "/contas/pagar/123", None, None),
        ]

    def test_contas_pagar_baixar_maps_to_bling_endpoint(self) -> None:
        """Contas pagar baixar posts to POST /contas/pagar/{id}/baixar."""
        transport = RecordingTransport()
        resource = ContasPagarResource(transport)
        dados: JsonObject = {"data": "2025-03-16", "usarDataVencimento": False}
        resource.baixar(123, dados)
        assert transport.calls[0][:2] == ("POST", "/contas/pagar/123/baixar")
        body = transport.calls[0][3]
        assert body is not None

    def test_contas_pagar_english_alias_list(self) -> None:
        """English alias 'list' should map to 'listar'."""
        transport = RecordingTransport()
        resource = ContasPagarResource(transport)
        resource.list(page=1, limit=100)
        assert transport.calls[0][:2] == ("GET", "/contas/pagar?pagina=1&limite=100")

    def test_contas_pagar_english_alias_get(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = ContasPagarResource(transport)
        resource.get(123)
        assert transport.calls == [
            ("GET", "/contas/pagar/123", None, None),
        ]

    def test_contas_pagar_english_alias_settle(self) -> None:
        """English alias 'settle' should map to 'baixar'."""
        transport = RecordingTransport()
        resource = ContasPagarResource(transport)
        dados: JsonObject = {"data": "2025-03-16", "usarDataVencimento": False}
        resource.settle(123, data=dados)
        assert transport.calls[0][:2] == ("POST", "/contas/pagar/123/baixar")
        body = transport.calls[0][3]
        assert body is not None


# --- Contas a Receber mapping tests ---


class TestContasReceberResourceMapping:
    """Mapping tests for ContasReceberResource."""

    def test_contas_receber_listar_maps_to_bling_endpoint(self) -> None:
        """Contas receber listar maps pagination params to GET /contas/receber."""
        transport = RecordingTransport()
        resource = ContasReceberResource(transport)
        resource.listar(pagina=1, limite=100)
        assert transport.calls == [
            ("GET", "/contas/receber?pagina=1&limite=100", {}, None),
        ]

    def test_contas_receber_listar_with_filters(self) -> None:
        """Contas receber listar maps situacoes filter to Bling camelCase."""
        transport = RecordingTransport()
        resource = ContasReceberResource(transport)
        resource.listar(pagina=1, limite=100, situacoes=[1, 2])
        assert transport.calls[0] == (
            "GET",
            "/contas/receber?pagina=1&limite=100",
            {"situacoes[]": [1, 2]},
            None,
        )

    def test_contas_receber_obter_maps_to_bling_endpoint(self) -> None:
        """Contas receber obter maps ID to GET /contas/receber/{id}."""
        transport = RecordingTransport()
        resource = ContasReceberResource(transport)
        resource.obter(123)
        assert transport.calls == [
            ("GET", "/contas/receber/123", None, None),
        ]

    def test_contas_receber_criar_maps_to_bling_endpoint(self) -> None:
        """Contas receber criar posts JSON body to POST /contas/receber."""
        transport = RecordingTransport()
        resource = ContasReceberResource(transport)
        dados: JsonObject = {"vencimento": "2025-04-10", "valor": 2500.00}
        resource.criar(dados)
        assert transport.calls[0][:2] == ("POST", "/contas/receber")
        body = transport.calls[0][3]
        assert body is not None

    def test_contas_receber_remover_maps_to_bling_endpoint(self) -> None:
        """Contas receber remover sends DELETE to /contas/receber/{id}."""
        transport = RecordingTransport()
        resource = ContasReceberResource(transport)
        resource.remover(123)
        assert transport.calls == [
            ("DELETE", "/contas/receber/123", None, None),
        ]

    def test_contas_receber_baixar_maps_to_bling_endpoint(self) -> None:
        """Contas receber baixar posts to POST /contas/receber/{id}/baixar."""
        transport = RecordingTransport()
        resource = ContasReceberResource(transport)
        dados: JsonObject = {"data": "2025-04-10", "usarDataVencimento": False}
        resource.baixar(123, dados)
        assert transport.calls[0][:2] == ("POST", "/contas/receber/123/baixar")
        body = transport.calls[0][3]
        assert body is not None

    def test_contas_receber_obter_boletos_maps_to_bling_endpoint(self) -> None:
        """Contas receber obter_boletos maps to GET /contas/receber/boletos."""
        transport = RecordingTransport()
        resource = ContasReceberResource(transport)
        resource.obter_boletos(id_origem=500)
        assert transport.calls[0] == (
            "GET",
            "/contas/receber/boletos?idOrigem=500",
            {},
            None,
        )

    def test_contas_receber_cancelar_boletos_maps_to_bling_endpoint(self) -> None:
        """Contas receber cancelar_boletos posts to POST /contas/receber/boletos/cancelar."""
        transport = RecordingTransport()
        resource = ContasReceberResource(transport)
        dados: JsonObject = {"motivo": "Cancelamento por atraso"}
        resource.cancelar_boletos(dados)
        assert transport.calls[0][:2] == ("POST", "/contas/receber/boletos/cancelar")
        body = transport.calls[0][3]
        assert body is not None

    def test_contas_receber_english_alias_list(self) -> None:
        """English alias 'list' should map to 'listar'."""
        transport = RecordingTransport()
        resource = ContasReceberResource(transport)
        resource.list(page=1, limit=100)
        assert transport.calls[0][:2] == (
            "GET",
            "/contas/receber?pagina=1&limite=100",
        )

    def test_contas_receber_english_alias_get_boletos(self) -> None:
        """English alias 'get_boletos' should map to 'obter_boletos'."""
        transport = RecordingTransport()
        resource = ContasReceberResource(transport)
        resource.get_boletos(source_id=500)
        assert transport.calls[0] == (
            "GET",
            "/contas/receber/boletos?idOrigem=500",
            {},
            None,
        )


# --- Contas Contábeis mapping tests ---


class TestContasContabeisResourceMapping:
    """Mapping tests for ContasContabeisResource."""

    def test_contas_contabeis_listar_maps_to_bling_endpoint(self) -> None:
        """Contas contabeis listar maps pagination to GET /contas-contabeis."""
        transport = RecordingTransport()
        resource = ContasContabeisResource(transport)
        resource.listar(pagina=1, limite=100)
        assert transport.calls == [
            ("GET", "/contas-contabeis?pagina=1&limite=100", {}, None),
        ]

    def test_contas_contabeis_listar_with_filters(self) -> None:
        """Contas contabeis listar maps situacoes filter to Bling camelCase."""
        transport = RecordingTransport()
        resource = ContasContabeisResource(transport)
        resource.listar(pagina=1, limite=100, situacoes=[1, 2])
        assert transport.calls[0] == (
            "GET",
            "/contas-contabeis?pagina=1&limite=100",
            {"situacoes": [1, 2]},
            None,
        )

    def test_contas_contabeis_obter_maps_to_bling_endpoint(self) -> None:
        """Contas contabeis obter maps ID to GET /contas-contabeis/{id}."""
        transport = RecordingTransport()
        resource = ContasContabeisResource(transport)
        resource.obter(10)
        assert transport.calls == [
            ("GET", "/contas-contabeis/10", None, None),
        ]

    def test_contas_contabeis_english_alias_list(self) -> None:
        """English alias 'list' should map to 'listar'."""
        transport = RecordingTransport()
        resource = ContasContabeisResource(transport)
        resource.list(page=1, limit=100)
        assert transport.calls[0][:2] == (
            "GET",
            "/contas-contabeis?pagina=1&limite=100",
        )

    def test_contas_contabeis_english_alias_get(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = ContasContabeisResource(transport)
        resource.get(10)
        assert transport.calls == [
            ("GET", "/contas-contabeis/10", None, None),
        ]


# --- Depósitos mapping tests ---


class TestDepositosResourceMapping:
    """Mapping tests for DepositosResource."""

    def test_depositos_listar_maps_to_bling_endpoint(self) -> None:
        """Depositos listar maps pagination to GET /depositos."""
        transport = RecordingTransport()
        resource = DepositosResource(transport)
        resource.listar(pagina=1, limite=100)
        assert transport.calls == [
            ("GET", "/depositos?pagina=1&limite=100", {}, None),
        ]

    def test_depositos_listar_with_filters(self) -> None:
        """Depositos listar maps situacao filter to Bling camelCase."""
        transport = RecordingTransport()
        resource = DepositosResource(transport)
        resource.listar(pagina=1, limite=100, situacao=1)
        assert transport.calls[0] == (
            "GET",
            "/depositos?pagina=1&limite=100",
            {"situacao": 1},
            None,
        )

    def test_depositos_obter_maps_to_bling_endpoint(self) -> None:
        """Depositos obter maps ID to GET /depositos/{id}."""
        transport = RecordingTransport()
        resource = DepositosResource(transport)
        resource.obter(1)
        assert transport.calls == [
            ("GET", "/depositos/1", None, None),
        ]

    def test_depositos_criar_maps_to_bling_endpoint(self) -> None:
        """Depositos criar posts JSON body to POST /depositos."""
        transport = RecordingTransport()
        resource = DepositosResource(transport)
        dados: JsonObject = {"descricao": "Novo Depósito", "situacao": 1}
        resource.criar(dados=dados)
        assert len(transport.calls) == 1
        assert transport.calls[0][0] == "POST"
        assert transport.calls[0][1] == "/depositos"
        assert transport.calls[0][3] is not None

    def test_depositos_alterar_maps_to_bling_endpoint(self) -> None:
        """Depositos alterar puts JSON body to PUT /depositos/{id}."""
        transport = RecordingTransport()
        resource = DepositosResource(transport)
        dados: JsonObject = {"descricao": "Depósito Alterado", "situacao": 1}
        resource.alterar(1, dados=dados)
        assert transport.calls[0][0] == "PUT"
        assert transport.calls[0][1] == "/depositos/1"
        assert transport.calls[0][3] is not None

    def test_depositos_english_alias_list(self) -> None:
        """English alias 'list' should map to 'listar'."""
        transport = RecordingTransport()
        resource = DepositosResource(transport)
        resource.list(page=1, limit=100)
        assert transport.calls[0][:2] == (
            "GET",
            "/depositos?pagina=1&limite=100",
        )

    def test_depositos_english_alias_get(self) -> None:
        """English alias 'get' should map to 'obter'."""
        transport = RecordingTransport()
        resource = DepositosResource(transport)
        resource.get(1)
        assert transport.calls == [
            ("GET", "/depositos/1", None, None),
        ]


# --- Empresas mapping tests ---


class TestEmpresasResourceMapping:
    """Mapping tests for EmpresasResource."""

    def test_empresas_obter_dados_basicos_maps_to_bling_endpoint(self) -> None:
        """Empresas obter_dados_basicos maps to GET /empresas/me/dados-basicos."""
        transport = RecordingTransport()
        resource = EmpresasResource(transport)
        resource.obter_dados_basicos()
        assert transport.calls == [
            ("GET", "/empresas/me/dados-basicos", None, None),
        ]

    def test_empresas_english_alias_get_basic_data(self) -> None:
        """English alias 'get_basic_data' should map to 'obter_dados_basicos'."""
        transport = RecordingTransport()
        resource = EmpresasResource(transport)
        resource.get_basic_data()
        assert transport.calls == [
            ("GET", "/empresas/me/dados-basicos", None, None),
        ]


# --- Estoques mapping tests ---


class TestEstoquesResourceMapping:
    """Mapping tests for EstoquesResource."""

    def test_estoques_obter_saldos_maps_to_bling_endpoint(self) -> None:
        """Estoques obter_saldos maps to GET /estoques/saldos with idsProdutos[]."""
        transport = RecordingTransport()
        resource = EstoquesResource(transport)
        resource.obter_saldos(ids_produtos=[1, 2])
        assert transport.calls[0] == (
            "GET",
            "/estoques/saldos",
            {"idsProdutos[]": [1, 2]},
            None,
        )

    def test_estoques_obter_saldos_por_deposito_maps_to_bling_endpoint(self) -> None:
        """Estoques obter_saldos_por_deposito maps to GET /estoques/saldos/{id}."""
        transport = RecordingTransport()
        resource = EstoquesResource(transport)
        resource.obter_saldos_por_deposito(5, ids_produtos=[1])
        assert transport.calls[0] == (
            "GET",
            "/estoques/saldos/5",
            {"idsProdutos[]": [1]},
            None,
        )

    def test_estoques_criar_maps_to_bling_endpoint(self) -> None:
        """Estoques criar posts JSON body to POST /estoques."""
        transport = RecordingTransport()
        resource = EstoquesResource(transport)
        dados: JsonObject = {"operacao": "E", "quantidade": 10}
        resource.criar(dados=dados)
        assert len(transport.calls) == 1
        assert transport.calls[0][0] == "POST"
        assert transport.calls[0][1] == "/estoques"
        assert transport.calls[0][3] is not None

    def test_estoques_english_alias_get_balances(self) -> None:
        """English alias 'get_balances' should map to 'obter_saldos'."""
        transport = RecordingTransport()
        resource = EstoquesResource(transport)
        resource.get_balances(product_ids=[1, 2])
        assert transport.calls[0][:2] == (
            "GET",
            "/estoques/saldos",
        )

    def test_estoques_english_alias_get_balances_by_deposit(self) -> None:
        """English alias 'get_balances_by_deposit' should map to 'obter_saldos_por_deposito'."""
        transport = RecordingTransport()
        resource = EstoquesResource(transport)
        resource.get_balances_by_deposit(5, product_ids=[1])
        assert transport.calls[0][:2] == (
            "GET",
            "/estoques/saldos/5",
        )
