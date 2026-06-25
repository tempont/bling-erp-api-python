# Notas Fiscais do Consumidor (NFC-e)

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
notas = client.notas_fiscais_consumidor.listar(pagina=1, limite=10)
nota = client.notas_fiscais_consumidor.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /nfce`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém notas fiscais de consumidor

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `id_transportador` | `idTransportador` | `query` | não |
| `chave_acesso` | `chaveAcesso` | `query` | não |
| `numero` | `numero` | `query` | não |
| `serie` | `serie` | `query` | não |
| `situacao` | `situacao` | `query` | não |
| `data_emissao_inicial` | `dataEmissaoInicial` | `query` | não |
| `data_emissao_final` | `dataEmissaoFinal` | `query` | não |

- Schemas de response: 200: NotasFiscaisDadosBaseDTO, 404: ErrorResponse

### `criar`

- Bling: `POST /nfce`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma nota fiscal de consumidor

- Schemas de request: `NotasFiscaisDadosBaseDTO`, `NotasFiscaisDadosPostDTO`
- Schemas de response: 201: BasePostResponse/NotaFiscalResponse_POST, 400: ErrorResponse

### `obter`

- Bling: `GET /nfce/{idNotaFiscalConsumidor}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma nota fiscal de consumidor

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal_consumidor` | `idNotaFiscalConsumidor` | `path` | sim |

- Schemas de response: 200: NotasFiscaisDadosBaseDTO/NotasFiscaisDadosGetDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /nfce/{idNotaFiscalConsumidor}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma nota fiscal de consumidor

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal_consumidor` | `idNotaFiscalConsumidor` | `path` | sim |

- Schemas de request: `NotasFiscaisDadosBaseDTO`, `NotasFiscaisDadosPostDTO`
- Schemas de response: 200: BasePostResponse/NotaFiscalResponse_POST, 404: ErrorResponse, 400: ErrorResponse

### `autorizar`

- Bling: `POST /nfce/{idNotaFiscalConsumidor}/enviar`
- Ação oficial: `Autorizar`
- Resumo oficial: Envia uma nota de consumidor

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal_consumidor` | `idNotaFiscalConsumidor` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `estornar_contas`

- Bling: `POST /nfce/{idNotaFiscalConsumidor}/estornar-contas`
- Ação oficial: `EstornarContas`
- Resumo oficial: Estorna as contas de uma nota fiscal

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal_consumidor` | `idNotaFiscalConsumidor` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `estornar_estoque`

- Bling: `POST /nfce/{idNotaFiscalConsumidor}/estornar-estoque`
- Ação oficial: `EstornarEstoque`
- Resumo oficial: Estorna o estoque de uma nota fiscal

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal_consumidor` | `idNotaFiscalConsumidor` | `path` | sim |

- Schemas de response: 404: ErrorResponse

### `lancar_contas`

- Bling: `POST /nfce/{idNotaFiscalConsumidor}/lancar-contas`
- Ação oficial: `LancarContas`
- Resumo oficial: Lança as contas de uma nota fiscal

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal_consumidor` | `idNotaFiscalConsumidor` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `lancar_estoque`

- Bling: `POST /nfce/{idNotaFiscalConsumidor}/lancar-estoque`
- Ação oficial: `LancarEstoque`
- Resumo oficial: Lança o estoque de uma nota fiscal no depósito padrão

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal_consumidor` | `idNotaFiscalConsumidor` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `lancar_estoque_id_deposito`

- Bling: `POST /nfce/{idNotaFiscalConsumidor}/lancar-estoque/{idDeposito}`
- Ação oficial: `LancarEstoqueDeposito`
- Resumo oficial: Lança o estoque de uma nota fiscal especificando o depósito

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal_consumidor` | `idNotaFiscalConsumidor` | `path` | sim |
| `id_deposito` | `idDeposito` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse
