# Logísticas

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
logisticas = client.logisticas.listar()
servicos = client.logisticas_servicos.listar()
```

## Operações

### `listar`

- Bling: `GET /logisticas`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém logísticas

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `tipo_integracao` | `tipoIntegracao` | `query` | não |
| `tipos_integracoes` | `tiposIntegracoes[]` | `query` | não |
| `situacao` | `situacao` | `query` | não |
| `logisticas_reversas` | `logisticasReversas` | `query` | não |

- Schemas de response: 200: LogisticasDadosBaseDTO, 404: ErrorResponse

### `criar`

- Bling: `POST /logisticas`
- Ação oficial: `Criar`
- Resumo oficial: Cria logística

- Schemas de request: `LogisticasDadosPostDTO`
- Schemas de response: 201: LogisticasLogisticaDTO, 400: ErrorResponse

### `obter_etiquetas`

- Bling: `GET /logisticas/etiquetas`
- Ação oficial: `ObterEtiquetaMultiplos`
- Resumo oficial: Obtém etiquetas das vendas

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `formato` | `formato` | `query` | sim |
| `ids_vendas` | `idsVendas[]` | `query` | sim |

- Schemas de response: 200: LogisticasEtiquetasDadosResponseDTO, 400: ErrorResponse, 404: ErrorResponse

### `criar_objeto`

- Bling: `POST /logisticas/objetos`
- Ação oficial: `CriarLogisticaObjeto`
- Resumo oficial: Cria um objeto de logística

- Schemas de request: `LogisticasObjetosDadosCreateRequestDTO`
- Schemas de response: 201: LogisticasObjetosObjetoDTO, 400: ErrorResponse

### `remover_objeto`

- Bling: `DELETE /logisticas/objetos/{idObjeto}`
- Ação oficial: `RemoverObjetoLogistico`
- Resumo oficial: Remove um objeto de logística personalizada

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_objeto` | `idObjeto` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter_objeto`

- Bling: `GET /logisticas/objetos/{idObjeto}`
- Ação oficial: `ObterObjetoLogistico`
- Resumo oficial: Obtém um objeto de logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_objeto` | `idObjeto` | `path` | sim |

- Schemas de response: 200: LogisticasObjetosDadosDTO, 404: ErrorResponse

### `alterar_objeto`

- Bling: `PUT /logisticas/objetos/{idObjeto}`
- Ação oficial: `AlterarLogisticaObjeto`
- Resumo oficial: Altera um objeto de logística pelo ID

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_objeto` | `idObjeto` | `path` | sim |

- Schemas de request: `LogisticasObjetosUpdateRequestDTO`
- Schemas de response: 200: LogisticasObjetosObjetoDTO, 400: ErrorResponse, 404: ErrorResponse

### `criar_remessa`

- Bling: `POST /logisticas/remessas`
- Ação oficial: `CriarRemessa`
- Resumo oficial: Cria uma remessa de postagem de uma logística

- Schemas de request: `LogisticasRemessasDadosPostDTO`
- Schemas de response: 201: LogisticasRemessaRemessaDTO, 400: ErrorResponse

### `remover_remessa`

- Bling: `DELETE /logisticas/remessas/{idRemessa}`
- Ação oficial: `RemoverRemessa`
- Resumo oficial: Remove uma remessa de postagem

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_remessa` | `idRemessa` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter_remessa`

- Bling: `GET /logisticas/remessas/{idRemessa}`
- Ação oficial: `ObterRemessa`
- Resumo oficial: Obtém uma remessa de postagem

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_remessa` | `idRemessa` | `path` | sim |

- Schemas de response: 200: LogisticasRemessasDadosBaseDTO, 404: ErrorResponse

### `alterar_remessa`

- Bling: `PUT /logisticas/remessas/{idRemessa}`
- Ação oficial: `AlterarRemessa`
- Resumo oficial: Altera uma remessa de postagem

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_remessa` | `idRemessa` | `path` | sim |

- Schemas de request: `LogisticasRemessasDadosBaseDTOCommon`
- Schemas de response: 200: LogisticasRemessaRemessaDTO, 400: ErrorResponse, 404: ErrorResponse

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

### `remover`

- Bling: `DELETE /logisticas/{idLogistica}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica` | `idLogistica` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter`

- Bling: `GET /logisticas/{idLogistica}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica` | `idLogistica` | `path` | sim |
| `listar_servicos_inativos` | `listarServicosInativos` | `query` | não |

- Schemas de response: 200: LogisticasDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /logisticas/{idLogistica}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica` | `idLogistica` | `path` | sim |

- Schemas de request: `LogisticasDadosPutDTO`
- Schemas de response: 400: ErrorResponse

### `listar_remessas_por_logistica`

- Bling: `GET /logisticas/{idLogistica}/remessas`
- Ação oficial: `ObterLogisticaRemessaMultiplos`
- Resumo oficial: Obtém as remessas de postagem de uma logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica` | `idLogistica` | `path` | sim |

- Schemas de response: 200: LogisticasRemessasDadosDTO, 404: ErrorResponse, 400: ErrorResponse
