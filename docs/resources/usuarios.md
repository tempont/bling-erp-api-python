# Usuários

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
client.usuarios.recuperar_senha('user@example.com')
```

## Operações

### `recuperar_senha`

- Bling: `POST /usuarios/recuperar-senha`
- Ação oficial: `post`
- Resumo oficial: Envia solicitação de recuperação de senha

- Schemas de response: 400: ErrorResponse

### `redefinir_senha`

- Bling: `PATCH /usuarios/redefinir-senha`
- Ação oficial: `patch`
- Resumo oficial: Redefine senha do usuário

- Schemas de response: 400: ErrorResponse

### `verificar_hash`

- Bling: `GET /usuarios/verificar-hash`
- Ação oficial: `get`
- Resumo oficial: Valida o hash recebido

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `hash` | `hash` | `query` | sim |

- Schemas de response: 400: ErrorResponse
