# Notas Fiscais de Serviço

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
notas = client.nfse.listar(pagina=1, limite=10)
```

## Operações

### `listar`

- Bling: `GET /nfse`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém notas de serviços

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `situacao` | `situacao` | `query` | não |
| `data_emissao_inicial` | `dataEmissaoInicial` | `query` | não |
| `data_emissao_final` | `dataEmissaoFinal` | `query` | não |

- Schemas de response: 200: NotasServicosDadosBaseDTO, 400: ErrorResponse

### `criar`

- Bling: `POST /nfse`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma nota de serviço

- Schemas de request: `NotasServicosDadosBaseDTO_POST`, `NotasServicosDadosDTO_POST`
- Schemas de response: 201: BasePostResponse/NotasServicosResponse_POST_PUT, 400: ErrorResponse

### `obter_configuracoes`

- Bling: `GET /nfse/configuracoes`
- Ação oficial: `ObterConfiguracoes`
- Resumo oficial: Configurações de nota de serviço

- Schemas de response: 200: ConfiguracaoNotaServicoDadosBaseDTO

### `alterar_configuracoes`

- Bling: `PUT /nfse/configuracoes`
- Ação oficial: `AlterarConfiguracoes`
- Resumo oficial: Configurações de nota de serviço

- Schemas de request: `ConfiguracaoNotaServicoDadosBaseDTO`
- Schemas de response: 400: ErrorResponse

### `remover`

- Bling: `DELETE /nfse/{idNotaServico}`
- Ação oficial: `Remover`
- Resumo oficial: Exclui uma nota de serviço

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_servico` | `idNotaServico` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter`

- Bling: `GET /nfse/{idNotaServico}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma nota de serviço

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_servico` | `idNotaServico` | `path` | sim |

- Schemas de response: 200: NotasServicosDadosBaseDTO/NotasServicosDadosDTO, 404: ErrorResponse

### `cancelar`

- Bling: `POST /nfse/{idNotaServico}/cancelar`
- Ação oficial: `Cancelar`
- Resumo oficial: Cancela uma nota de serviço

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_servico` | `idNotaServico` | `path` | sim |

- Schemas de request: `NotasServicosCancelamentoDTO`
- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `autorizar`

- Bling: `POST /nfse/{idNotaServico}/enviar`
- Ação oficial: `Autorizar`
- Resumo oficial: Envia uma nota de serviço

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_nota_servico` | `idNotaServico` | `path` | sim |

- Schemas de response: 200: NotasServicosDadosBaseDTO/NotasServicosDadosDTO, 404: ErrorResponse, 400: ErrorResponse
