# Logísticas - Serviços

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
servicos = client.logisticas_servicos.listar()
servico = client.logisticas_servicos.obter(123456)
```

## Operações

### `listar_servicos`

- Bling: `GET /logisticas/servicos`
- Ação oficial: `ObterServicoLogisticoMultiplos`
- Resumo oficial: Obtém serviços de logísticas

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `tipo_integracao` | `tipoIntegracao` | `query` | não |

- Schemas de response: 200: LogisticasServicosDadosDTO, 400: ErrorResponse

### `criar_servico`

- Bling: `POST /logisticas/servicos`
- Ação oficial: `CriarLogisticaServico`
- Resumo oficial: Cria um serviço de logística

- Schemas de request: `LogisticasServicosDadosCreateRequestDTO`
- Schemas de response: 201: LogisticasServicosDadosSaveDTO, 400: ErrorResponse

### `obter_servico`

- Bling: `GET /logisticas/servicos/{idLogisticaServico}`
- Ação oficial: `ObterServicoLogistico`
- Resumo oficial: Obtém um servico de logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica_servico` | `idLogisticaServico` | `path` | sim |

- Schemas de response: 200: LogisticasServicosDadosDTO, 404: ErrorResponse

### `alterar_servico`

- Bling: `PUT /logisticas/servicos/{idLogisticaServico}`
- Ação oficial: `AlterarLogisticaServico`
- Resumo oficial: Altera um serviço de logística pelo ID

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica_servico` | `idLogisticaServico` | `path` | sim |

- Schemas de request: `LogisticasServicosDadosSaveRequestDTO`
- Schemas de response: 200: LogisticasServicosDadosSaveDTO, 400: ErrorResponse, 404: ErrorResponse

### `alterar_situacao_servico`

- Bling: `PATCH /logisticas/{idLogisticaServico}/situacoes`
- Ação oficial: `AlterarSituacaoLogisticaServico`
- Resumo oficial: Desativa ou ativa um serviço de uma logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica_servico` | `idLogisticaServico` | `path` | sim |

- Schemas de request: `LogisticasServicosDadosSituationDTO`
- Schemas de response: 404: ErrorResponse, 400: ErrorResponse
