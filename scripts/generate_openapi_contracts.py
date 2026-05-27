"""Generate SDK operation contracts and docs from the local OpenAPI reference."""

from __future__ import annotations

import json
from pathlib import Path
from pprint import pformat
from typing import TYPE_CHECKING, NotRequired, TypedDict, cast

if TYPE_CHECKING:
    from collections.abc import Mapping

SPEC_PATH = Path("specs/bling-openapi-reference.json")
CONTRACTS_DIR = Path("src/bling_erp_api/contracts/generated")
DOCS_DIR = Path("docs/resources")


class ResourceConfig(TypedDict):
    """Resource generation settings."""

    openapi_resource: str
    module: str
    constant: str
    title: str
    example: list[str]
    extra_openapi_resources: NotRequired[list[str]]


ACTION_TO_SDK_METHOD = {
    "ObterMultiplos": "listar",
    "Obter": "obter",
    "Criar": "criar",
    "Alterar": "alterar",
    "Remover": "remover",
    "RemoverMultiplos": "remover_varios",
    "CriarMultiplos": "criar_varios",
    "AlterarSituacao": "alterar_situacao",
    "AlterarSituacaoMultiplos": "alterar_situacao_varios",
    "LancarEstoqueDeposito": "lancar_estoque",
    "LancarEstoque": "lancar_estoque",
    "EstornarEstoque": "estornar_estoque",
    "LancarContas": "lancar_contas",
    "EstornarContas": "estornar_contas",
    "GerarNotaFiscal": "gerar_nota_fiscal",
    "GerarNotaFiscalConsumidor": "gerar_nota_fiscal_consumidor",
    "VincularComponenteMultiplos": "vincular_componentes",
    "RemoverComponenteMultiplos": "remover_componentes",
    "AlterarComponente": "alterar_componente",
    "GerarCombinacoes": "gerar_combinacoes",
    "AlterarAtributo": "alterar_atributo",
    "ObterSaldosLote": "obter_saldos",
    "ObterMultiplosProdutoControlaLote": "listar_produtos_controlam_lote",
    "ObterTipoContato": "obter_tipo_contato",
    "ObterTipoContatoMultiplos": "listar_tipos",
    "Pausar": "pausar",
    "Publicar": "publicar",
    "Autorizar": "autorizar",
    "ObterDocumentoNotaFiscal": "obter_documento_nota_fiscal",
    "Cancelar": "cancelar",
    "ObterConfiguracoes": "obter_configuracoes",
    "AlterarConfiguracoes": "alterar_configuracoes",
    "BaixarConta": "baixar",
    "CancelarBoletos": "cancelar_boletos",
    "ObterBoletos": "obter_boletos",
    "ObterSaldosEstoque": "obter_saldos",
    "ObterSaldosEstoqueDeposito": "obter_saldos_por_deposito",
    "ObterServicoLogisticoMultiplos": "listar_servicos",
    "ObterServicoLogistico": "obter_servico",
    "CriarLogisticaServico": "criar_servico",
    "AlterarLogisticaServico": "alterar_servico",
    "AlterarSituacaoLogisticaServico": "alterar_situacao_servico",
    "ObterObjetoLogistico": "obter_objeto",
    "AlterarLogisticaObjeto": "alterar_objeto",
    "RemoverObjetoLogistico": "remover_objeto",
    "CriarLogisticaObjeto": "criar_objeto",
    "ObterEtiquetaMultiplos": "obter_etiquetas",
    "ObterRemessa": "obter_remessa",
    "AlterarRemessa": "alterar_remessa",
    "RemoverRemessa": "remover_remessa",
    "ObterLogisticaRemessaMultiplos": "listar_remessas_por_logistica",
    "CriarRemessa": "criar_remessa",
    "ObterTributacao": "obter_tributacao",
    "ObterAcaoMultiplos": "listar",
}

PARAMETER_TO_SDK_NAME = {
    "pagina": "pagina",
    "limite": "limite",
    "idPedidoVenda": "id_pedido_venda",
    "idSituacao": "id_situacao",
    "idDeposito": "id_deposito",
    "idContato": "id_contato",
    "idsSituacoes[]": "ids_situacoes",
    "dataInicial": "data_inicial",
    "dataFinal": "data_final",
    "dataAlteracaoInicial": "data_alteracao_inicial",
    "dataAlteracaoFinal": "data_alteracao_final",
    "dataPrevistaInicial": "data_prevista_inicial",
    "dataPrevistaFinal": "data_prevista_final",
    "numero": "numero",
    "idLoja": "id_loja",
    "idVendedor": "id_vendedor",
    "idControleCaixa": "id_controle_caixa",
    "numerosLojas[]": "numeros_lojas",
    "idUnidadeNegocio": "id_unidade_negocio",
    "idsPedidosVendas[]": "ids_pedidos_vendas",
    "idProduto": "id_produto",
    "idProdutoPai": "id_produto_pai",
    "idProdutoEstrutura": "id_produto_estrutura",
    "idProdutoFornecedor": "id_produto_fornecedor",
    "idProdutoLoja": "id_produto_loja",
    "idComponente": "id_componente",
    "idsComponentes[]": "ids_componentes",
    "idsProdutos[]": "ids_produtos",
    "codigos[]": "codigos",
    "gtins[]": "gtins",
    "criterio": "criterio",
    "tipo": "tipo",
    "tipoIntegracao": "tipo_integracao",
    "tipoProduto": "tipo_produto",
    "idCategoria": "id_categoria",
    "idCategoriaProduto": "id_categoria_produto",
    "dataInclusaoInicial": "data_inclusao_inicial",
    "dataInclusaoFinal": "data_inclusao_final",
    "filtroSaldoEstoque": "filtro_saldo_estoque",
    "filtroSaldoEstoqueDeposito": "filtro_saldo_estoque_deposito",
    "idFornecedor": "id_fornecedor",
    "idLote": "id_lote",
    "idsLotes[]": "ids_lotes",
    "idsDepositos[]": "ids_depositos",
    "codigosLotes[]": "codigos_lotes",
    "status": "status",
    "dataValidadeInicial": "data_validade_inicial",
    "dataValidadeFinal": "data_validade_final",
    "dataFabricacaoInicial": "data_fabricacao_inicial",
    "dataFabricacaoFinal": "data_fabricacao_final",
    "dataCriacaoInicial": "data_criacao_inicial",
    "dataCriacaoFinal": "data_criacao_final",
    "idLancamento": "id_lancamento",
    "idTipoContato": "id_tipo_contato",
    "idsContatos[]": "ids_contatos",
    "numeroDocumento": "numero_documento",
    "pesquisa": "pesquisa",
    "telefone": "telefone",
    "tipoPessoa": "tipo_pessoa",
    "uf": "uf",
    "chaveAcesso": "chave_acesso",
    "dataEmissaoFinal": "data_emissao_final",
    "dataEmissaoInicial": "data_emissao_inicial",
    "enviarEmail": "enviar_email",
    "formato": "formato",
    "idNotaFiscal": "id_nota_fiscal",
    "idNotaFiscalConsumidor": "id_nota_fiscal_consumidor",
    "idTransportador": "id_transportador",
    "idsNotas[]": "ids_notas",
    "numeroLoja": "numero_loja",
    "serie": "serie",
    "situacao": "situacao",
    "idNotaServico": "id_nota_servico",
    "idBordero": "id_bordero",
    "idsCategorias": "ids_categorias",
    "idContaFinanceira": "id_conta_financeira",
    "valor": "valor",
    "situacaoConciliacao": "situacao_conciliacao",
    "idCategoriaLoja": "id_categoria_loja",
    "idCategoriaProdutoPai": "id_categoria_produto_pai",
    "idsCategorias[]": "ids_categorias",
    "situacoes[]": "situacoes",
    "tipoFiltroData": "tipo_filtro_data",
    "dataVencimentoInicial": "data_vencimento_inicial",
    "dataVencimentoFinal": "data_vencimento_final",
    "dataPagamentoInicial": "data_pagamento_inicial",
    "dataPagamentoFinal": "data_pagamento_final",
    "idPortador": "id_portador",
    "idFormaPagamento": "id_forma_pagamento",
    "boletoGerado": "boleto_gerado",
    "idOrigem": "id_origem",
    "ocultarInvisiveis": "ocultar_invisiveis",
    "ocultarTipoContaBancaria": "ocultar_tipo_conta_bancaria",
    "aliasIntegracao": "alias_integracao",
    "ordenacao": "ordenacao",
    "idContaPagar": "id_conta_pagar",
    "idContaReceber": "id_conta_receber",
    "descricao": "descricao",
    "tiposPagamentos[]": "tipos_pagamentos",
    "nome": "nome",
    "nomePai": "nome_pai",
    "idGrupoProduto": "id_grupo_produto",
    "idsGruposProdutos[]": "ids_grupos_produtos",
    "idProdutoHomologacao": "id_produto_homologacao",
    "tiposIntegracoes[]": "tipos_integracoes",
    "logisticasReversas": "logisticas_reversas",
    "listarServicosInativos": "listar_servicos_inativos",
    "idLogistica": "id_logistica",
    "idLogisticaServico": "id_logistica_servico",
    "idObjeto": "id_objeto",
    "idRemessa": "id_remessa",
    "idsVendas[]": "ids_vendas",
    "idNaturezaOperacao": "id_natureza_operacao",
    "idNotificacao": "id_notificacao",
    "idOrdemProducao": "id_ordem_producao",
    "periodo": "periodo",
}

DOCSTRING_ONLY_RESOURCES: list[ResourceConfig] = []

_CLASS_NAME_MAP: dict[str, str] = {
    "sales_orders": "SalesOrdersResource",
    "products": "ProductsResource",
    "product_structures": "ProductStructuresResource",
    "product_suppliers": "ProductSuppliersResource",
    "product_stores": "ProductStoresResource",
    "product_batches": "ProductBatchesResource",
    "product_batch_entries": "ProductBatchEntriesResource",
    "product_variations": "ProductVariationsResource",
    "ad_categories": "AdCategoriesResource",
    "ads": "AdsResource",
    "contacts": "ContactsResource",
    "invoices": "NfeResource",
    "nfse": "NfseResource",
    "borderos": "BorderosResource",
    "caixas_bancos": "CaixasBancosResource",
    "store_categories": "StoreCategoriesResource",
    "product_categories": "ProductCategoriesResource",
    "income_expense_categories": "IncomeExpenseCategoriesResource",
    "contas_pagar": "ContasPagarResource",
    "contas_receber": "ContasReceberResource",
    "contas_contabeis": "ContasContabeisResource",
    "depositos": "DepositosResource",
    "empresas": "EmpresasResource",
    "estoques": "EstoquesResource",
    "payment_methods": "PaymentMethodsResource",
    "product_groups": "ProductGroupsResource",
    "homologation": "HomologationResource",
    "logisticas": "LogisticasResource",
    "naturezas_operacoes": "NaturezasOperacoesResource",
    "notificacoes": "NotificacoesResource",
    "ordens_producao": "OrdensProducaoResource",
}

RESOURCES: list[ResourceConfig] = [
    {
        "openapi_resource": "PedidosVenda",
        "module": "sales_orders",
        "constant": "SALES_ORDER_OPERATIONS",
        "title": "Pedidos de venda",
        "example": [
            "pedidos = client.pedidos_vendas.listar(",
            '    data_inicial="2024-01-01",',
            "    ids_situacoes=[123456],",
            ")",
            "pedido = client.pedidos_vendas.obter(123456)",
        ],
    },
    {
        "openapi_resource": "Produtos",
        "module": "products",
        "constant": "PRODUCT_OPERATIONS",
        "title": "Produtos",
        "example": [
            "produtos = client.produtos.listar(",
            '    nome="Camiseta",',
            "    ids_produtos=[123456],",
            ")",
            "produto = client.produtos.obter(123456)",
        ],
    },
    {
        "openapi_resource": "ProdutosEstruturas",
        "module": "product_structures",
        "constant": "PRODUCT_STRUCTURE_OPERATIONS",
        "title": "Produtos - Estruturas",
        "example": [
            "estrutura = client.produtos_estruturas.obter(123456789)",
        ],
    },
    {
        "openapi_resource": "ProdutosFornecedores",
        "module": "product_suppliers",
        "constant": "PRODUCT_SUPPLIER_OPERATIONS",
        "title": "Produtos - Fornecedores",
        "example": [
            "fornecedores = client.produtos_fornecedores.listar(",
            "    limite=10, id_produto=123456789",
            ")",
            "um = client.produtos_fornecedores.obter(123456789)",
        ],
    },
    {
        "openapi_resource": "ProdutosLojas",
        "module": "product_stores",
        "constant": "PRODUCT_STORE_OPERATIONS",
        "title": "Produtos - Lojas",
        "example": [
            "lojas = client.produtos_lojas.listar(limite=10, id_produto=123456789)",
            "vinculo = client.produtos_lojas.obter(123456789)",
        ],
    },
    {
        "openapi_resource": "Lotes",
        "module": "product_batches",
        "constant": "PRODUCT_BATCH_OPERATIONS",
        "title": "Produtos - Lotes",
        "example": [
            "lotes = client.lotes.listar(ids_produtos=[123456789], limite=10)",
            "lote = client.lotes.obter(123456789)",
            "controle = client.lotes.listar_produtos_controlam_lote(ids_produtos=[123456789])",
        ],
    },
    {
        "openapi_resource": "LotesLancamentos",
        "module": "product_batch_entries",
        "constant": "PRODUCT_BATCH_ENTRY_OPERATIONS",
        "title": "Produtos - Lotes Lancamentos",
        "example": [
            "lancs = client.lotes_lancamentos.listar(id_lote=123456789)",
            "saldo_total = client.lotes_lancamentos.obter_saldos_soma(id_produto=123456789)",
            (
                "soma_dep = client.lotes_lancamentos.obter_saldos_soma_deposito("
                "id_produto=123456789, id_deposito=987654321)"
            ),
        ],
    },
    {
        "openapi_resource": "ProdutosVariacoes",
        "module": "product_variations",
        "constant": "PRODUCT_VARIATION_OPERATIONS",
        "title": "Produtos - Variacoes",
        "example": [
            "variacoes = client.produtos_variacoes.listar(id_produto_pai=123456789)",
        ],
    },
    {
        "openapi_resource": "AnunciosCategorias",
        "module": "ad_categories",
        "constant": "AD_CATEGORY_OPERATIONS",
        "title": "Anúncios - Categorias",
        "example": [
            "categorias = client.ad_categories.listar()",
            "categoria = client.ad_categories.obter(123456)",
        ],
    },
    {
        "openapi_resource": "Anuncios",
        "module": "ads",
        "constant": "AD_OPERATIONS",
        "title": "Anúncios",
        "example": [
            "anuncios = client.ads.listar(pagina=1, limite=10)",
            "anuncio = client.ads.obter(123456)",
        ],
    },
    {
        "openapi_resource": "Contatos",
        "extra_openapi_resources": ["ContatosTipos"],
        "module": "contacts",
        "constant": "CONTACT_OPERATIONS",
        "title": "Contatos",
        "example": [
            'contatos = client.contatos.listar(pesquisa="Ana", limite=10)',
            "contato = client.contatos.obter(123456)",
        ],
    },
    {
        "openapi_resource": "NotasFiscais",
        "module": "invoices",
        "constant": "INVOICE_OPERATIONS",
        "title": "Notas Fiscais",
        "example": [
            "notas = client.invoices.listar(pagina=1, limite=10)",
        ],
    },
    {
        "openapi_resource": "NFSe",
        "module": "nfse",
        "constant": "NFSE_OPERATIONS",
        "title": "Notas Fiscais de Serviço",
        "example": [
            "notas = client.nfse.listar(pagina=1, limite=10)",
        ],
    },
    {
        "openapi_resource": "Borderos",
        "module": "borderos",
        "constant": "BORDERO_OPERATIONS",
        "title": "Borderôs",
        "example": [
            "bordero = client.borderos.obter(123456)",
        ],
    },
    {
        "openapi_resource": "Caixas",
        "module": "caixas_bancos",
        "constant": "CAIXAS_BANCOS_OPERATIONS",
        "title": "Caixas e Bancos",
        "example": [
            "lancamentos = client.caixas_bancos.listar(",
            '    data_inicial="2024-01-01",',
            '    data_final="2024-12-31",',
            ")",
        ],
    },
    {
        "openapi_resource": "CategoriasLojas",
        "module": "store_categories",
        "constant": "STORE_CATEGORY_OPERATIONS",
        "title": "Categorias - Lojas",
        "example": [
            "categorias = client.store_categories.listar()",
            "categoria = client.store_categories.obter(123456)",
        ],
    },
    {
        "openapi_resource": "CategoriasProdutos",
        "module": "product_categories",
        "constant": "PRODUCT_CATEGORY_OPERATIONS",
        "title": "Categorias - Produtos",
        "example": [
            "categorias = client.product_categories.listar()",
            "categoria = client.product_categories.obter(123456)",
        ],
    },
    {
        "openapi_resource": "CategoriasReceitasDespesas",
        "module": "income_expense_categories",
        "constant": "INCOME_EXPENSE_CATEGORY_OPERATIONS",
        "title": "Categorias - Receitas e Despesas",
        "example": [
            "categorias = client.income_expense_categories.listar(tipo=2)",
            "categoria = client.income_expense_categories.obter(123456)",
        ],
    },
    {
        "openapi_resource": "ContasPagar",
        "module": "contas_pagar",
        "constant": "CONTAS_PAGAR_OPERATIONS",
        "title": "Contas a Pagar",
        "example": [
            "contas = client.contas_pagar.listar(",
            "    situacao=1,",
            '    data_vencimento_inicial="2024-01-01",',
            ")",
            "conta = client.contas_pagar.obter(123456)",
        ],
    },
    {
        "openapi_resource": "ContasReceber",
        "module": "contas_receber",
        "constant": "CONTAS_RECEBER_OPERATIONS",
        "title": "Contas a Receber",
        "example": [
            "contas = client.contas_receber.listar(",
            "    situacoes=[1, 2],",
            '    data_inicial="2024-01-01",',
            ")",
            "conta = client.contas_receber.obter(123456)",
        ],
    },
    {
        "openapi_resource": "ContasContabeis",
        "module": "contas_contabeis",
        "constant": "CONTAS_CONTABEIS_OPERATIONS",
        "title": "Contas Financeiras",
        "example": [
            "contas = client.contas_contabeis.listar(",
            "    situacoes=[1],",
            ")",
            "conta = client.contas_contabeis.obter(123456)",
        ],
    },
    {
        "openapi_resource": "Depositos",
        "module": "depositos",
        "constant": "DEPOSITO_OPERATIONS",
        "title": "Depósitos",
        "example": [
            "depositos = client.depositos.listar()",
            "deposito = client.depositos.obter(123456)",
        ],
    },
    {
        "openapi_resource": "Empresas",
        "module": "empresas",
        "constant": "EMPRESA_OPERATIONS",
        "title": "Empresas",
        "example": [
            "dados = client.empresas.obter_dados_basicos()",
        ],
    },
    {
        "openapi_resource": "Estoques",
        "module": "estoques",
        "constant": "ESTOQUE_OPERATIONS",
        "title": "Estoques",
        "example": [
            "saldos = client.estoques.obter_saldos(ids_produtos=[123, 456])",
            "saldos_dep = client.estoques.obter_saldos_por_deposito(1, ids_produtos=[123])",
        ],
    },
    {
        "openapi_resource": "FormasPagamentos",
        "module": "payment_methods",
        "constant": "PAYMENT_METHOD_OPERATIONS",
        "title": "Formas de Pagamentos",
        "example": [
            "formas = client.payment_methods.listar()",
            "forma = client.payment_methods.obter(123456)",
        ],
    },
    {
        "openapi_resource": "GruposProdutos",
        "module": "product_groups",
        "constant": "PRODUCT_GROUP_OPERATIONS",
        "title": "Grupos de Produtos",
        "example": [
            "grupos = client.product_groups.listar()",
            "grupo = client.product_groups.obter(123456)",
        ],
    },
    {
        "openapi_resource": "Homologacao",
        "module": "homologation",
        "constant": "HOMOLOGATION_OPERATIONS",
        "title": "Homologação",
        "example": [
            "produto = client.homologation.obter()",
            "result = client.homologation.criar({'nome': 'Produto Teste', 'preco': 10.00})",
        ],
    },
    {
        "openapi_resource": "Logisticas",
        "module": "logisticas",
        "constant": "LOGISTICAS_OPERATIONS",
        "title": "Logísticas",
        "example": [
            "logisticas = client.logisticas.listar()",
            "servicos = client.logisticas_servicos.listar()",
        ],
    },
    {
        "openapi_resource": "NaturezasOperacoes",
        "module": "naturezas_operacoes",
        "constant": "NATUREZAS_OPERACOES_OPERATIONS",
        "title": "Naturezas de Operações",
        "example": [
            "naturezas = client.naturezas_operacoes.listar(",
            "    situacao=1,",
            ")",
            "tributacao = client.naturezas_operacoes.obter_tributacao(",
            "    12345678, calculo={...})",
        ],
    },
    {
        "openapi_resource": "Notificacoes",
        "module": "notificacoes",
        "constant": "NOTIFICACOES_OPERATIONS",
        "title": "Notificações",
        "example": [
            "notificacoes = client.notificacoes.listar(",
            '    periodo="2025-01",',
            ")",
            'client.notificacoes.alterar("01ARZ3NDEKTSV4RRFFQ69G5FAV")',
        ],
    },
    {
        "openapi_resource": "OrdensProducao",
        "module": "ordens_producao",
        "constant": "ORDENS_PRODUCAO_OPERATIONS",
        "title": "Ordens de Produção",
        "example": [
            "ordens = client.ordens_producao.listar(",
            "    ids_situacoes=[1, 2],",
            ")",
            "ordem = client.ordens_producao.obter(12345678)",
        ],
    },
]


def main() -> None:
    """Generate supported resource contracts and docstrings."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    all_contracts: dict[str, list[dict[str, object]]] = {}

    # Existing resources: generate contracts + docs + collect for docstrings
    for resource in RESOURCES:
        resource_names = [
            resource["openapi_resource"],
            *resource.get("extra_openapi_resources", []),
        ]
        contracts: list[dict[str, object]] = []
        for name in resource_names:
            contracts.extend(_resource_contracts(payload, resource=name))
        contracts.sort(key=lambda item: (str(item["path"]), str(item["method"])))
        _write_contract_module(
            resource["module"],
            resource["constant"],
            contracts,
        )
        _write_resource_docs(
            resource["module"],
            resource["title"],
            contracts,
            resource["example"],
        )
        class_name = _class_name_for_module(resource["module"])
        all_contracts[class_name] = contracts

    # Docstring-only resources (not yet fully implemented as SDK resources)
    for resource in DOCSTRING_ONLY_RESOURCES:
        contracts = _resource_contracts(payload, resource=resource["openapi_resource"])
        if contracts:
            class_name = _class_name_for_module(resource["module"])
            all_contracts[class_name] = contracts

    _write_docstring_module(all_contracts)


def _resource_contracts(payload: Mapping[str, object], *, resource: str) -> list[dict[str, object]]:
    paths = _mapping(payload.get("paths"))
    components = _mapping(payload.get("components"))
    parameters = _mapping(components.get("parameters"))
    contracts: list[dict[str, object]] = []

    for raw_path, methods in paths.items():
        path = str(raw_path)
        for raw_method, raw_operation in _mapping(methods).items():
            operation = _mapping(raw_operation)
            if operation.get("x-api-resource") != resource:
                continue

            action = str(operation.get("x-api-action") or raw_method)
            sdk_method = _sdk_method_for_operation(
                action=action,
                method=str(raw_method).upper(),
                path=path,
            )
            contracts.append(
                {
                    "sdk_method": sdk_method,
                    "method": str(raw_method).upper(),
                    "path": path,
                    "resource": resource,
                    "action": action,
                    "summary": str(operation.get("summary") or ""),
                    "description": _optional_str(operation.get("description")),
                    "parameters": _operation_parameters(operation, parameters),
                    "request_schema_refs": _request_schema_refs(operation),
                    "response_schema_refs": _response_schema_refs(operation),
                }
            )

    return sorted(contracts, key=lambda item: (str(item["path"]), str(item["method"])))


def _operation_parameters(
    operation: Mapping[str, object],
    component_parameters: Mapping[str, object],
) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for raw_parameter in _sequence(operation.get("parameters")):
        parameter = _resolve_parameter(raw_parameter, component_parameters)
        name = str(parameter.get("name") or "")
        schema = _mapping(parameter.get("schema"))
        result.append(
            {
                "name": name,
                "location": str(parameter.get("in") or "query"),
                "sdk_name": PARAMETER_TO_SDK_NAME.get(name, _snake_case(name)),
                "required": bool(parameter.get("required", False)),
                "description": _optional_str(parameter.get("description")),
                "schema_type": _optional_str(schema.get("type")),
                "schema_format": _optional_str(schema.get("format")),
            }
        )
    return result


def _sdk_method_for_operation(*, action: str, method: str, path: str) -> str:  # noqa: PLR0911
    if action == "Obter" and method == "GET" and path == "/contatos/consumidor-final":
        return "obter_consumidor_final"
    if action == "Obter" and method == "GET" and path == "/empresas/me/dados-basicos":
        return "obter_dados_basicos"
    if action == "Alterar" and method == "PATCH":
        return "alterar_parcialmente"
    if action == "ObterSaldosLote" and method == "GET":
        # Four distinct paths share the same Bling action; keep stable sdk_method keys.
        if path == "/produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo":
            return "obter_saldos"
        if path == "/produtos/{idProduto}/lotes/saldo/soma":
            return "obter_saldos_soma"
        if path == "/produtos/{idProduto}/lotes/{idLote}/depositos/{idDeposito}/saldo":
            return "obter_saldos_saldo"
        if path == "/produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo/soma":
            return "obter_saldos_soma_deposito"
    if action == "AlterarAtributo" and path == "/formas-pagamentos/{idFormaPagamento}/padrao":
        return "alterar_padrao"
    # Notificações: /notificacoes/quantidade uses obter_quantidade (not listar)
    if path == "/notificacoes/quantidade" and method == "GET":
        return "obter_quantidade"
    # OrdensProducao: /ordens-producao/gerar-sob-demanda uses criar_multiplos (not criar_varios)
    if path == "/ordens-producao/gerar-sob-demanda" and method == "POST":
        return "criar_multiplos"
    return ACTION_TO_SDK_METHOD[action]


def _resolve_parameter(
    raw_parameter: object,
    component_parameters: Mapping[str, object],
) -> Mapping[str, object]:
    parameter = _mapping(raw_parameter)
    ref = parameter.get("$ref")
    if isinstance(ref, str):
        name = ref.rsplit("/", maxsplit=1)[-1]
        return _mapping(component_parameters.get(name))
    return parameter


def _request_schema_refs(operation: Mapping[str, object]) -> list[str]:
    request_body = _mapping(operation.get("requestBody"))
    content = _mapping(request_body.get("content"))
    application_json = _mapping(content.get("application/json"))
    schema = _mapping(application_json.get("schema"))
    return sorted(_schema_refs(schema))


def _response_schema_refs(operation: Mapping[str, object]) -> dict[str, list[str]]:
    responses = _mapping(operation.get("responses"))
    result: dict[str, list[str]] = {}
    for status_code, raw_response in responses.items():
        response = _mapping(raw_response)
        content = _mapping(response.get("content"))
        application_json = _mapping(content.get("application/json"))
        schema = _mapping(application_json.get("schema"))
        refs = sorted(_schema_refs(schema))
        if refs:
            result[str(status_code)] = refs
    return result


def _schema_refs(schema: object) -> set[str]:
    if isinstance(schema, dict):
        mapping = cast("dict[str, object]", schema)
        found_refs: set[str] = set()
        ref = mapping.get("$ref")
        if isinstance(ref, str):
            found_refs.add(ref.rsplit("/", maxsplit=1)[-1])
        for value in mapping.values():
            found_refs.update(_schema_refs(value))
        return found_refs
    if isinstance(schema, list):
        values = cast("list[object]", schema)
        list_refs: set[str] = set()
        for item in values:
            list_refs.update(_schema_refs(item))
        return list_refs
    return set()


def _write_contract_module(
    module_name: str,
    constant_name: str,
    contracts: list[dict[str, object]],
) -> None:
    CONTRACTS_DIR.mkdir(parents=True, exist_ok=True)
    mapping = _operation_mapping(contracts)
    module = (
        '"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""\n\n'
        "from __future__ import annotations\n\n"
        "from bling_erp_api.contracts import OperationContract\n\n"
        f"{constant_name}: dict[str, OperationContract] = {{\n"
    )
    for key, value in mapping.items():
        module += f"    {key!r}: OperationContract.model_validate({pformat(value, width=100)}),\n"
    module += "}\n"
    (CONTRACTS_DIR / f"{module_name}.py").write_text(module, encoding="utf-8")


def _operation_mapping(contracts: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    mapping: dict[str, dict[str, object]] = {}
    for contract in contracts:
        sdk_method = str(contract["sdk_method"])
        key = sdk_method
        if key in mapping:
            suffix = str(contract["path"]).rsplit("/", maxsplit=1)[-1]
            key = f"{sdk_method}_{_snake_case(suffix)}"
        mapping[key] = contract
    return mapping


def _write_resource_docs(
    resource_slug: str,
    title: str,
    contracts: list[dict[str, object]],
    example: list[str],
) -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {title}",
        "",
        "Esta página é gerada a partir de `specs/bling-openapi-reference.json`.",
        "A documentação oficial é usada como contrato para paths, métodos e parâmetros.",
        "",
        "## Exemplo",
        "",
        "```python",
        *(example or ["# Veja as operacoes geradas abaixo."]),
        "```",
        "",
        "## Operações",
        "",
    ]

    for operation_name, contract in _operation_mapping(contracts).items():
        lines.extend(_operation_docs(operation_name, contract))

    (DOCS_DIR / f"{resource_slug}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _operation_docs(operation_name: str, contract: Mapping[str, object]) -> list[str]:
    parameters = cast("list[dict[str, object]]", contract.get("parameters") or [])
    lines = [
        f"### `{operation_name}`",
        "",
        f"- Bling: `{contract['method']} {contract['path']}`",
        f"- Ação oficial: `{contract['action']}`",
        f"- Resumo oficial: {contract['summary']}",
        "",
    ]
    if parameters:
        lines.extend(
            [
                "| Argumento SDK | Parâmetro Bling | Local | Obrigatório |",
                "| --- | --- | --- | --- |",
            ]
        )
        for parameter in parameters:
            required = "sim" if parameter["required"] else "não"
            lines.append(
                f"| `{parameter['sdk_name']}` | `{parameter['name']}` | "
                f"`{parameter['location']}` | {required} |"
            )
        lines.append("")
    request_refs = cast("list[str]", contract.get("request_schema_refs") or [])
    response_refs = cast("dict[str, list[str]]", contract.get("response_schema_refs") or {})
    if request_refs:
        lines.append(f"- Schemas de request: {', '.join(f'`{item}`' for item in request_refs)}")
    if response_refs:
        formatted = ", ".join(
            f"{status}: {'/'.join(refs)}" for status, refs in response_refs.items()
        )
        lines.append(f"- Schemas de response: {formatted}")
    lines.append("")
    return lines


def _mapping(value: object) -> Mapping[str, object]:
    if isinstance(value, dict):
        return cast("Mapping[str, object]", value)
    return {}


def _sequence(value: object) -> list[object]:
    return cast("list[object]", value) if isinstance(value, list) else []


def _optional_str(value: object) -> str | None:
    return value if isinstance(value, str) else None


def _snake_case(value: str) -> str:
    clean = value.replace("[]", "").replace("{", "").replace("}", "")
    chars: list[str] = []
    for index, char in enumerate(clean):
        if char.isupper() and index > 0:
            chars.append("_")
        chars.append(char.lower() if char.isalnum() else "_")
    return "".join(chars).strip("_")


def _class_name_for_module(module: str) -> str:
    """Convert a module name to the corresponding resource class name."""
    return _CLASS_NAME_MAP[module]


def _generate_docstring(contract: dict[str, object]) -> str:
    """Generate a Google-style docstring from an operation contract.

    Args:
        contract: A single operation contract dict.

    Returns:
        A formatted Google-style docstring string.
    """
    summary = str(contract.get("summary") or "")
    method = str(contract.get("method") or "")
    path = str(contract.get("path") or "")
    description = contract.get("description")
    parameters = cast("list[dict[str, object]]", contract.get("parameters") or [])
    request_schema_refs = cast("list[str]", contract.get("request_schema_refs") or [])
    response_schema_refs = cast("dict[str, list[str]]", contract.get("response_schema_refs") or {})

    # Ensure summary ends with punctuation (D415 compliance)
    if summary and summary[-1] not in ".?!":
        summary += "."

    lines = [summary, "", f"Endpoint: {method} {path}"]

    # Add description if present and different from summary
    desc = _optional_str(description)
    if desc and desc != summary:
        lines.extend(["", desc])

    # Args section
    if parameters:
        lines.append("")
        lines.append("Args:")
        for param in parameters:
            sdk_name = str(param.get("sdk_name", ""))
            param_name = str(param.get("name", ""))
            param_desc = param.get("description")
            schema_type = param.get("schema_type")
            required = bool(param.get("required", False))

            # Fallback description for None or empty
            if not param_desc:
                location = str(param.get("location", "query"))
                param_desc = "ID do recurso." if location == "path" else f"Filtrar por {sdk_name}."

            type_str = str(schema_type) if schema_type else "string"
            req_str = "obrigatório" if required else "opcional"

            lines.append(
                f"    {sdk_name}: {param_desc} (Bling: ``{param_name}``, {type_str}, {req_str})"
            )

    # Request body schema note
    if request_schema_refs:
        lines.append("")
        lines.append(f"Request body schema: {', '.join(request_schema_refs)}")

    # Returns section
    if response_schema_refs:
        lines.append("")
        lines.append("Returns:")
        schema_parts: list[str] = []
        for status, refs in sorted(response_schema_refs.items()):
            sorted_refs = sorted(refs)
            schema_parts.append(f"{status}: {', '.join(sorted_refs)}")
        lines.append(f"    Bling API response. Response schemas: {'; '.join(schema_parts)}")

    return "\n".join(lines)


def _write_docstring_module(all_contracts: dict[str, list[dict[str, object]]]) -> None:
    """Write the _docstrings.py module with all operation docstrings.

    Args:
        all_contracts: Mapping of class name to list of operation contracts.
    """
    CONTRACTS_DIR.mkdir(parents=True, exist_ok=True)

    lines = [
        '"""Generated docstrings for Bling SDK methods. Do not edit manually."""',
        "",
        "from __future__ import annotations",
        "",
        "OPERATION_DOCSTRINGS: dict[str, str] = {",
    ]

    for class_name in sorted(all_contracts):
        contracts = all_contracts[class_name]
        mapping = _operation_mapping(contracts)
        for method_name in sorted(mapping):
            contract = mapping[method_name]
            docstring = _generate_docstring(contract)
            key = f"{class_name}.{method_name}"
            escaped = docstring.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
            lines.append(f'    {key!r}: "{escaped}",')

    lines.append("}")
    lines.append("")

    (CONTRACTS_DIR / "_docstrings.py").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
