# Contatos

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
contatos = client.contatos.listar(pesquisa="Ana", limite=10)
contato = client.contatos.obter(123456)
```

## Operações

### `remover_varios`

- Bling: `DELETE /contatos`
- Ação oficial: `RemoverMultiplos`
- Resumo oficial: Remove múltiplos contatos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_contatos` | `idsContatos[]` | `query` | sim |

- Schemas de response: 200: ContatosAlertasResponse, 400: ErrorResponse

### `listar`

- Bling: `GET /contatos`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém contatos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `pesquisa` | `pesquisa` | `query` | não |
| `criterio` | `criterio` | `query` | não |
| `data_inclusao_inicial` | `dataInclusaoInicial` | `query` | não |
| `data_inclusao_final` | `dataInclusaoFinal` | `query` | não |
| `data_alteracao_inicial` | `dataAlteracaoInicial` | `query` | não |
| `data_alteracao_final` | `dataAlteracaoFinal` | `query` | não |
| `id_tipo_contato` | `idTipoContato` | `query` | não |
| `id_vendedor` | `idVendedor` | `query` | não |
| `uf` | `uf` | `query` | não |
| `telefone` | `telefone` | `query` | não |
| `ids_contatos` | `idsContatos[]` | `query` | não |
| `numero_documento` | `numeroDocumento` | `query` | não |
| `tipo_pessoa` | `tipoPessoa` | `query` | não |

- Schemas de response: 200: ContatosDadosBaseDTO

### `criar`

- Bling: `POST /contatos`
- Ação oficial: `Criar`
- Resumo oficial: Cria um contato

- Schemas de request: `ContatosDadosBaseDTO`, `ContatosDadosDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `obter_consumidor_final`

- Bling: `GET /contatos/consumidor-final`
- Ação oficial: `Obter`
- Resumo oficial: Obtém os dados do contato Consumidor Final

- Schemas de response: 200: ContatosDadosBaseDTO/ContatosDadosDTO

### `alterar_situacao_varios`

- Bling: `POST /contatos/situacoes`
- Ação oficial: `AlterarSituacaoMultiplos`
- Resumo oficial: Altera a situação de múltiplos contatos

- Schemas de response: 200: ContatosAlertasResponse, 400: ErrorResponse

### `listar_tipos`

- Bling: `GET /contatos/tipos`
- Ação oficial: `ObterTipoContatoMultiplos`
- Resumo oficial: Obtém tipos de contato

- Schemas de response: 200: ContatosTipoContatoDTO

### `remover`

- Bling: `DELETE /contatos/{idContato}`
- Ação oficial: `Remover`
- Resumo oficial: Remove um contato

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_contato` | `idContato` | `path` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `obter`

- Bling: `GET /contatos/{idContato}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um contato

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_contato` | `idContato` | `path` | sim |

- Schemas de response: 200: ContatosDadosBaseDTO/ContatosDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /contatos/{idContato}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera um contato

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_contato` | `idContato` | `path` | sim |

- Schemas de request: `ContatosDadosBaseDTO`, `ContatosDadosDTO`
- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `alterar_situacao`

- Bling: `PATCH /contatos/{idContato}/situacoes`
- Ação oficial: `AlterarSituacao`
- Resumo oficial: Altera a situação de um contato

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_contato` | `idContato` | `path` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `obter_tipo_contato`

- Bling: `GET /contatos/{idContato}/tipos`
- Ação oficial: `ObterTipoContato`
- Resumo oficial: Obtém os tipos de contato de um contato

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_contato` | `idContato` | `path` | sim |

- Schemas de response: 200: ContatosTipoContatoDTO, 404: ErrorResponse
