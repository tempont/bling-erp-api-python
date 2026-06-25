# Bling ERP API SDK

## Rules

- Project uses ruff for linting and formatting and basedpyright for type checking.
- Don't run real requests to the Bling API in the tests, unless explicitly stated.
- Use `uv` to run the commands.
- Only flexbilize ruff and basedpyright rules if absolutely necessary.
- After any change, run the tests to ensure the code is working as expected:

```bash
make check
```

## Project design decisions

- Each endpoint is considered "done" when it has:
  - a canonical public method in Portuguese in the resource;
  - an English compatibility alias when the resource already exposes one;
  - path/method/params/body matching the OpenAPI specification;
  - a request model, if there is a body;
  - a response model, if the response is important;
  - a unit test for mapping;
  - a fixture or model test;
  - typed error handling covered when applicable;
  - an example/docs if it is a commonly used endpoint.

## Add new endpoints guideline

### Per-endpoint checklist

1. Find the operation in `specs/bling-openapi-reference.json`.
2. Record `path`, HTTP method, `x-api-resource`, and `x-api-action`.
3. Record path params, query params, request schema, and response schema.
4. Add the resource to `RESOURCES` in `scripts/generate_openapi_contracts.py` if missing.
5. Add the action to `ACTION_TO_SDK_METHOD` in `scripts/generate_openapi_contracts.py` if missing.
6. Add each Bling parameter to `PARAMETER_TO_SDK_NAME` in `scripts/generate_openapi_contracts.py` if missing.
7. Run `uv run python scripts/generate_openapi_contracts.py`.
8. Check the generated contract in `src/bling_erp_api/contracts/generated/<resource>.py`.
9. Check the generated docs in `docs/resources/<resource>.md`.
10. Add or update `tests/unit/test_<resource>_contracts.py`.
11. In the contract test, compare generated operations with OpenAPI operations.
12. Regenerate models with `uv run python scripts/generate_models.py` when schemas or resource model exports need to change.
13. Check `src/bling_erp_api/models/generated/<resource>.py` and `src/bling_erp_api/models/generated/schemas/<schema_module>.py`.
14. Add request models for body schemas.
15. Add response models for important responses.
16. Keep public model fields in Python `snake_case`; Bling names must exist only as Pydantic validation/serialization aliases.
17. Use `validation_alias=AliasChoices("<snake_case>", "<BlingName>")` plus `serialization_alias="<BlingName>"` for generated fields whose Bling name is not already snake_case.
18. Keep `extra="allow"` through `BlingModel`; do not bypass its alias normalization or duplicate-alias conflict validation.
19. Export stable models from `src/bling_erp_api/models/aliases.py`.
20. Create or update `src/bling_erp_api/resources/<resource>.py`.
21. Add the canonical pt-BR method named from `x-api-action`.
22. Add explicit keyword params; never use `**filters`.
23. Convert SDK param names to Bling param names in a helper.
24. Use `compact_params()` for optional query params.
25. Use `to_json_object()` for request model payloads.
26. Add an English alias only when preserving compatibility.
27. Expose a new resource namespace in `src/bling_erp_api/client.py` if needed.
28. Add the resource class to `src/bling_erp_api/resources/__init__.py` if new.
29. Add mapping tests in `tests/unit/test_resources.py`.
30. Mapping tests must assert method, path, params, and body.
31. Add a fixture in `tests/fixtures/responses/` for important responses.
32. Add model tests in `tests/unit/test_<resource>_models.py`.
33. Add tests that verify model constructors/signatures expose snake_case, aliases parse Bling payloads, `to_json_object()` serializes Bling names, and conflicting snake_case/Bling keys are rejected.
34. Add docs example only in generated docs or `examples/` when commonly used; examples must instantiate models with snake_case fields and typed nested models.
35. Run `make check`.

### File map

1. OpenAPI source: `specs/bling-openapi-reference.json`.
2. Contract generator: `scripts/generate_openapi_contracts.py`.
3. Generated contracts: `src/bling_erp_api/contracts/generated/`.
4. Generated docs: `docs/resources/`.
5. Generated models: `src/bling_erp_api/models/generated/`.
6. Public model aliases: `src/bling_erp_api/models/aliases.py`.
7. Resource methods: `src/bling_erp_api/resources/`.
8. Resource exports: `src/bling_erp_api/resources/__init__.py`.
9. Client namespaces: `src/bling_erp_api/client.py`.
10. Mapping tests: `tests/unit/test_resources.py`.
11. Contract tests: `tests/unit/test_<resource>_contracts.py`.
12. Model tests: `tests/unit/test_<resource>_models.py`.
13. Response fixtures: `tests/fixtures/responses/`.
14. Examples: `examples/`.

### Naming rules

1. Use pt-BR as canonical public API.
2. Use snake_case for SDK params.
3. Keep exact Bling names only in payload aliases and query mapping.
4. Use `listar` for `ObterMultiplos`.
5. Use `obter` for `Obter`.
6. Use `criar` for `Criar`.
7. Use `alterar` for full `PUT` updates.
8. Use `alterar_parcialmente` for partial `PATCH` updates.
9. Use `remover` for `Remover`.
10. Use `remover_varios` for `RemoverMultiplos`.
11. Use `alterar_situacao` for `AlterarSituacao`. Nota: este método só deve ser usado quando o OpenAPI spec daquele recurso declarar a operação `AlterarSituacao` (recursos como `categorias_receitas_despesas` não possuem esta operação, por exemplo).
12. Keep English aliases thin and secondary.

### Model and payload naming rules

1. Public Python model fields and constructor kwargs must be snake_case, including nested request models and examples.
2. Bling field names such as `descricaoCurta`, `dataValidade`, and `idsProdutos` are wire-format names only.
3. Generated Pydantic models must accept Bling field names for parsing API responses and compatibility payloads, but they must not expose those names as the preferred constructor signature.
4. Generated fields with a non-snake-case Bling name must use `validation_alias=AliasChoices("<snake_case>", "<BlingName>")` and `serialization_alias="<BlingName>"`; do not use plain `alias="<BlingName>"`.
5. `BlingModel` owns alias normalization and duplicate-key protection. Do not bypass it with ad hoc dict munging in resources.
6. If a user payload provides both a Python field name and its Bling alias with different values, validation must fail instead of serializing both keys.
7. Resource write methods (`POST`, `PUT`, `PATCH`) should accept request models when an OpenAPI body schema exists, and must serialize them through `to_json_object()`.
8. Raw `JsonObject` bodies are acceptable only for endpoints not yet modeled or deliberately flexible payloads; when using raw dicts, the caller is responsible for Bling wire-format keys.
9. Examples should prefer normal model constructors over `model_construct()` so type checking and validation catch field-name drift.

### Docstring Guidelines

Every resource method MUST include a Google-style docstring with the following structure:

1. **First line**: Brief description in pt-BR for canonical methods. For EN aliases: ``Compatibility alias for ``metodo_pt()``.`` followed by a blank line and the description.
2. **Endpoint line**: ``Endpoint: GET|POST|PUT|PATCH|DELETE /path/{param}`` documenting the exact Bling API path.
3. **Description paragraph**: 1-2 sentences explaining what the method does.
4. **Args section**: One line per parameter with:
   - SDK parameter name (snake_case)
   - Description including the Bling parameter name in backticks (e.g., ``Bling: ``idProduto``, integer, obrigatório``)
   - For path params, mark as ``obrigatório``; for query params, ``opcional``
5. **Returns section**: ``Bling API response. Response schemas: <codes with DTO names>``
   - List each possible response code with the corresponding schema DTO name (e.g., ``200: ContatosDadosBaseDTO; 404: ErrorResponse``)
   - For 204 responses with no body, use ``204: NoContent``
6. **Class docstring**: Must be descriptive including:
   - What endpoints the class maps
   - Mention that canonical methods are in pt-BR and EN aliases available for compatibility

Reference ``ProductsResource`` in ``src/bling_erp_api/resources/products.py`` as the canonical example.

### Docstring example

```python
def obter(self, id_produto: int) -> JsonObject:
    """Obtém um produto.

    Endpoint: GET /produtos/{idProduto}

    Obtém um produto pelo ID.

    Args:
        id_produto: ID do produto (Bling: ``idProduto``, integer, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: ProdutosDadosBaseDTO; 404: ErrorResponse
    """
    return self._get(f"/produtos/{id_produto}")
```

English alias example:

```python
def get(self, product_id: int) -> JsonObject:
    """Compatibility alias for ``obter()``.

    Obtém um produto.

    Endpoint: GET /produtos/{idProduto}

    Obtém um produto pelo ID.

    Args:
        product_id: ID do produto (Bling: ``idProduto``, integer, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: ProdutosDadosBaseDTO; 404: ErrorResponse
    """
    return self.obter(id_produto=product_id)
```

### Runtime behavior

1. Keep the transport rate limiter enabled by default.
2. Default local limit is 3 requests per second.
3. Retry 429 responses through the transport.
4. Respect `Retry-After` when Bling returns it.
5. Keep integration tests gated behind explicit env vars.

### Implemented

1. `PedidosVenda`: resource methods, pt-BR canonical API, English aliases.
2. `PedidosVenda`: OpenAPI contracts and generated docs.
3. `PedidosVenda`: semi-generated models and fixtures.
4. `Produtos`: main `/produtos` resource methods.
5. `Produtos`: pt-BR canonical API and English aliases.
6. `Produtos`: explicit list filters from OpenAPI.
7. `Produtos`: semi-generated models and fixtures.
8. Product subgroups: contracts and docs generated.
9. `ProdutosEstruturas`: resource methods (`client.produtos_estruturas` / `client.product_structures`).
10. `ProdutosFornecedores`: resource methods (`client.produtos_fornecedores` / `client.product_suppliers`).
11. `ProdutosLojas`: resource methods (`client.produtos_lojas` / `client.product_stores`).
12. `Lotes`: resource methods (`client.lotes` / `client.product_batches`).
13. `LotesLancamentos`: resource methods (`client.lotes_lancamentos` / `client.product_batch_entries`).
14. `ProdutosVariacoes`: resource methods (`client.produtos_variacoes` / `client.product_variations`).
15. Transport accepts JSON arrays as request bodies where Bling expects them (`JsonPayload`).
16. Transport: local rate limiter and 429 retry.
17. Client namespaces: `client.pedidos_vendas`, `client.produtos`, `client.contatos`, product sub-resources e inglês onde há alias (`client.contacts`, etc.).
18. `Contatos`: resource methods (`client.contatos` / `client.contacts`), contratos OpenAPI, docs gerados e modelos semi-gerados.
19. `NotasFiscais` (NF-e): resource methods (`client.notas_fiscais` / `client.invoices`), 12 pt-BR canonical methods.
20. `NotasFiscais` (NFC-e): resource methods (`client.notas_fiscais_consumidor` / `client.consumer_invoices`), 10 pt-BR canonical methods.
21. `NFSe` (NFS-e): resource methods (`client.notas_servicos` / `client.service_invoices`), pt-BR canonical methods.
22. `NotasFiscais`: OpenAPI contracts and generated docs.
23. `NFSe`: OpenAPI contracts and generated docs.
24. `NotasFiscais`: semi-generated models and fixtures.
25. `NFSe`: semi-generated models and fixtures.
26. `Anuncios`: resource methods (`client.anuncios` / `client.ads`), 7 pt-BR canonical methods, OpenAPI contracts, generated docs, semi-generated models and fixtures.
27. `AnunciosCategorias`: resource methods (`client.anuncios_categorias` / `client.ad_categories`), 2 pt-BR canonical methods, OpenAPI contracts, generated docs, semi-generated models.
28. `Borderos`: resource methods (`client.borderos`), 2 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
29. `CaixasBancos`: resource methods (`client.caixas_bancos` / `client.cash_entries`), 5 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
30. `CategoriasLojas`: resource methods (`client.categorias_lojas` / `client.store_categories`), 5 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
31. `CategoriasProdutos`: resource methods (`client.categorias_produtos` / `client.product_categories`), 5 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
32. `CategoriasReceitasDespesas`: resource methods (`client.categorias_receitas_despesas` / `client.income_expense_categories`), 6 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
33. `ContasPagar`: resource methods (`client.contas_pagar` / `client.accounts_payable`), 6 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
34. `ContasReceber`: resource methods (`client.contas_receber` / `client.accounts_receivable`), 8 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
35. `ContasContabeis`: resource methods (`client.contas_contabeis` / `client.financial_accounts`), 2 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
36. `Depositos`: resource methods (`client.depositos` / `client.warehouses`), 4 pt-BR canonical methods. **Nota**: Não há método `remover` — a API do Bling não expõe um endpoint de exclusão para depósitos. OpenAPI contracts, generated docs, models and fixtures.
37. `Empresas`: resource methods (`client.empresas` / `client.companies`), 1 pt-BR canonical method, OpenAPI contracts, generated docs, models and fixtures.
38. `Estoques`: resource methods (`client.estoques` / `client.stock`), 3 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
39. `FormasPagamentos`: resource methods (`client.formas_pagamentos` / `client.payment_methods`), 7 pt-BR canonical methods, OpenAPI contracts, models and fixtures.
40. `GruposProdutos`: resource methods (`client.grupos_produtos` / `client.product_groups`), 6 pt-BR canonical methods, OpenAPI contracts, models and fixtures.
41. `Homologacao`: resource methods (`client.homologacao` / `client.homologation`), 5 pt-BR canonical methods, OpenAPI contracts, models and fixtures.
42. `Logisticas`: resource methods (`client.logisticas` / `client.logistics`), 5 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
43. `LogisticasServicos`: resource methods (`client.logisticas_servicos` / `client.logistics_services`), 5 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
44. `LogisticasObjetos`: resource methods (`client.logisticas_objetos` / `client.logistics_objects`), 4 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
45. `LogisticasEtiquetas`: resource methods (`client.logisticas_etiquetas` / `client.logistics_labels`), 1 pt-BR canonical method, OpenAPI contracts, generated docs, models and fixtures.
46. `LogisticasRemessas`: resource methods (`client.logisticas_remessas` / `client.logistics_shipments`), 5 pt-BR canonical methods, OpenAPI contracts, generated docs, models and fixtures.
47. `NaturezasOperacoes`: resource methods (`client.naturezas_operacoes` / `client.tax_natures`), 2 pt-BR canonical methods, OpenAPI contracts, generated docs, semi-generated models and fixtures.
48. `Notificacoes`: resource methods (`client.notificacoes` / `client.notifications`), 3 pt-BR canonical methods, OpenAPI contracts, generated docs, semi-generated models and fixtures.
49. `OrdensProducao`: resource methods (`client.ordens_producao` / `client.production_orders`), 7 pt-BR canonical methods, OpenAPI contracts, generated docs, semi-generated models and fixtures.
50. `PedidosCompras`: resource methods (`client.pedidos_compras` / `client.purchase_orders`), 11 pt-BR canonical methods.
51. `PedidosCompras`: OpenAPI contracts and generated docs.
52. `PedidosCompras`: semi-generated models and fixtures.
53. `PropostasComerciais`: resource methods (`client.propostas_comerciais` / `client.commercial_proposals`), 7 pt-BR canonical methods.
54. `PropostasComerciais`: OpenAPI contracts and generated docs.
55. `PropostasComerciais`: semi-generated models and fixtures.
56. `Situacoes`: resource methods (`client.situacoes` / `client.situations`), 4 pt-BR canonical methods.
57. `SituacoesModulos`: resource methods (`client.situacoes_modulos` / `client.situation_modules`), 4 pt-BR canonical methods.
58. `SituacoesTransicoes`: resource methods (`client.situacoes_transicoes` / `client.situation_transitions`), 4 pt-BR canonical methods.
59. `Situacoes`: OpenAPI contracts and generated docs.
60. `Situacoes`: semi-generated models and fixtures.
61. `Vendedores`: resource methods (`client.vendedores` / `client.sellers`), 2 pt-BR canonical methods.
62. `Vendedores`: OpenAPI contracts and generated docs.
63. `Vendedores`: semi-generated models and fixtures.
64. `Usuarios`: resource methods (`client.usuarios` / `client.users`), 3 pt-BR canonical methods.

### Pending

1. Expand model generation beyond semi-generated models.
2. Continue vertical slices for accounts, stocks, categories, logistics, and ads.
