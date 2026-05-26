# Notas Fiscais

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
notas = client.invoices.listar(pagina=1, limite=10)
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

- Bling: `POST /nfe/{idNotaFiscal}/lancar-estoque/{idDeposito}`
- Ação oficial: `LancarEstoqueDeposito`
- Resumo oficial: Lança o estoque de uma nota fiscal especificando o depósito

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal` | `idNotaFiscal` | `path` | sim |
| `id_deposito` | `idDeposito` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `remover_varios`

- Bling: `DELETE /nfe`
- Ação oficial: `RemoverMultiplos`
- Resumo oficial: Remove múltiplas notas fiscais

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_notas` | `idsNotas[]` | `query` | sim |

- Schemas de response: 200: NotasFiscaisExclusaoDTO, 400: ErrorResponse

### `listar_nfe`

- Bling: `GET /nfe`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém notas fiscais

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `numero_loja` | `numeroLoja` | `query` | não |
| `id_transportador` | `idTransportador` | `query` | não |
| `chave_acesso` | `chaveAcesso` | `query` | não |
| `numero` | `numero` | `query` | não |
| `serie` | `serie` | `query` | não |
| `situacao` | `situacao` | `query` | não |
| `tipo` | `tipo` | `query` | não |
| `data_emissao_inicial` | `dataEmissaoInicial` | `query` | não |
| `data_emissao_final` | `dataEmissaoFinal` | `query` | não |

- Schemas de response: 200: NotasFiscaisDadosBaseDTO

### `criar_nfe`

- Bling: `POST /nfe`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma nota fiscal

- Schemas de request: `NotasFiscaisDadosBaseDTO`, `NotasFiscaisDadosPostDTO`
- Schemas de response: 201: BasePostResponse/NotaFiscalResponse_POST, 400: ErrorResponse

### `obter_documento_nota_fiscal`

- Bling: `GET /nfe/documento/{chaveAcesso}`
- Ação oficial: `ObterDocumentoNotaFiscal`
- Resumo oficial: Obtém o documento de uma nota fiscal

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `chave_acesso` | `chaveAcesso` | `path` | sim |
| `formato` | `formato` | `query` | sim |

- Schemas de response: 200: NotasFiscaisDocumentoDTO, 400: ErrorResponse, 404: ErrorResponse

### `obter_id_nota_fiscal`

- Bling: `GET /nfe/{idNotaFiscal}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma nota fiscal

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal` | `idNotaFiscal` | `path` | sim |

- Schemas de response: 200: NotasFiscaisDadosBaseDTO/NotasFiscaisDadosGetDTO, 404: ErrorResponse

### `alterar_id_nota_fiscal`

- Bling: `PUT /nfe/{idNotaFiscal}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma nota fiscal

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal` | `idNotaFiscal` | `path` | sim |

- Schemas de request: `NotasFiscaisDadosBaseDTO`, `NotasFiscaisDadosPostDTO`
- Schemas de response: 200: BasePostResponse/ErrorField/NotaFiscalResponse_POST, 404: ErrorResponse, 400: ErrorResponse

### `autorizar_enviar`

- Bling: `POST /nfe/{idNotaFiscal}/enviar`
- Ação oficial: `Autorizar`
- Resumo oficial: Envia uma nota fiscal

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal` | `idNotaFiscal` | `path` | sim |
| `enviar_email` | `enviarEmail` | `query` | não |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `estornar_contas_estornar_contas`

- Bling: `POST /nfe/{idNotaFiscal}/estornar-contas`
- Ação oficial: `EstornarContas`
- Resumo oficial: Estorna as contas de uma nota fiscal

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal` | `idNotaFiscal` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `estornar_estoque_estornar_estoque`

- Bling: `POST /nfe/{idNotaFiscal}/estornar-estoque`
- Ação oficial: `EstornarEstoque`
- Resumo oficial: Estorna o estoque de uma nota fiscal

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal` | `idNotaFiscal` | `path` | sim |

- Schemas de response: 404: ErrorResponse

### `lancar_contas_lancar_contas`

- Bling: `POST /nfe/{idNotaFiscal}/lancar-contas`
- Ação oficial: `LancarContas`
- Resumo oficial: Lança as contas de uma nota fiscal

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal` | `idNotaFiscal` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `lancar_estoque_lancar_estoque`

- Bling: `POST /nfe/{idNotaFiscal}/lancar-estoque`
- Ação oficial: `LancarEstoque`
- Resumo oficial: Lança o estoque de uma nota fiscal no depósito padrão

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_fiscal` | `idNotaFiscal` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse
