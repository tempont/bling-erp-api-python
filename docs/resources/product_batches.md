# Produtos - Lotes

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
lotes = client.lotes.listar(ids_produtos=[123456789], limite=10)
lote = client.lotes.obter(123456789)
controle = client.lotes.listar_produtos_controlam_lote(ids_produtos=[123456789])
```

## Operações

### `remover_varios`

- Bling: `DELETE /produtos/lotes`
- Ação oficial: `RemoverMultiplos`
- Resumo oficial: Remove lotes de produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_lotes` | `idsLotes[]` | `query` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `listar`

- Bling: `GET /produtos/lotes`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém lotes de produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `ids_produtos` | `idsProdutos[]` | `query` | sim |
| `ids_lotes` | `idsLotes[]` | `query` | não |
| `ids_depositos` | `idsDepositos[]` | `query` | não |
| `codigos_lotes` | `codigosLotes[]` | `query` | não |
| `status` | `status` | `query` | não |
| `data_validade_inicial` | `dataValidadeInicial` | `query` | não |
| `data_validade_final` | `dataValidadeFinal` | `query` | não |
| `data_fabricacao_inicial` | `dataFabricacaoInicial` | `query` | não |
| `data_fabricacao_final` | `dataFabricacaoFinal` | `query` | não |
| `data_criacao_inicial` | `dataCriacaoInicial` | `query` | não |
| `data_criacao_final` | `dataCriacaoFinal` | `query` | não |

- Schemas de response: 200: LotesDTO, 400: ErrorResponse

### `criar_varios`

- Bling: `PUT /produtos/lotes`
- Ação oficial: `CriarMultiplos`
- Resumo oficial: Salva lotes de produtos

- Schemas de request: `LotesDTO`
- Schemas de response: 200: SaveResponseLotsDTO, 400: ErrorResponse

### `listar_produtos_controlam_lote`

- Bling: `GET /produtos/lotes/controla-lote`
- Ação oficial: `ObterMultiplosProdutoControlaLote`
- Resumo oficial: Obtém a informação se determinados produtos possuem controle de lote

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_produtos` | `idsProdutos[]` | `query` | sim |

- Schemas de response: 200: ProdutoControlaLotesDTO, 400: ErrorResponse

### `obter`

- Bling: `GET /produtos/lotes/{idLote}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um lote de um produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_lote` | `idLote` | `path` | sim |

- Schemas de response: 200: LotesDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /produtos/lotes/{idLote}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera um lote de um produto

- Schemas de request: `LotePutRequestDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `alterar_situacao`

- Bling: `PATCH /produtos/lotes/{idLote}/status`
- Ação oficial: `AlterarSituacao`
- Resumo oficial: Altera o status de um lote do produto

- Schemas de request: `LoteStatusDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `alterar_situacao_desativar`

- Bling: `POST /produtos/{idProduto}/lotes/controla-lote/desativar`
- Ação oficial: `AlterarSituacao`
- Resumo oficial: Desativa controle de lotes para o produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto` | `idProduto` | `path` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse
