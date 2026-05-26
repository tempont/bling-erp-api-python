"""Tests for resource request mapping."""

from __future__ import annotations

from datetime import UTC, date, datetime

from bling_erp_api.models.generated.products import ProductCreateRequest, ProductPatchRequest
from bling_erp_api.models.generated.sales_orders import SalesOrderCreateRequest
from bling_erp_api.resources.contacts import ContactsResource
from bling_erp_api.resources.product_batch_entries import ProductBatchEntriesResource
from bling_erp_api.resources.product_batches import ProductBatchesResource
from bling_erp_api.resources.product_stores import ProductStoresResource
from bling_erp_api.resources.product_structures import ProductStructuresResource
from bling_erp_api.resources.product_suppliers import ProductSuppliersResource
from bling_erp_api.resources.product_variations import ProductVariationsResource
from bling_erp_api.resources.products import ProductsResource
from bling_erp_api.resources.sales_orders import SalesOrdersResource
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
