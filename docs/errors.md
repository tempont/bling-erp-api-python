# Erros

## Hierarquia de Exceções

Todas as exceções do SDK herdam de `BlingAPIError`:

```
BlingAPIError                      # Base class para todos os erros do SDK
├── BlingTransportError            # Erro de transporte HTTP (conexão, timeout)
├── BlingAuthenticationError       # Erro de autenticação (401, 403)
├── BlingValidationError           # Erro de validação da requisição (400, 422)
├── BlingNotFoundError             # Recurso não encontrado (404)
├── BlingRateLimitError            # Limite de taxa excedido (429)
└── BlingServerError               # Erro interno do servidor (500+)
```

### BlingAPIError

Classe base para todos os erros. Expõe os seguintes atributos:

| Atributo | Tipo | Descrição |
|---|---|---|
| `status_code` | `int \| None` | Código HTTP da resposta |
| `payload` | `JsonValue \| None` | Payload JSON da resposta (se houver) |
| `response` | `httpx.Response \| None` | Objeto `Response` completo do httpx |

### BlingTransportError

Erro de transporte — quando a requisição HTTP não pode ser completada
por problemas de conexão, timeout, DNS, etc.
Também é disparado para código HTTP 408 (Request Timeout).

```python
from bling_erp_api import BlingTransportError
```

### BlingAuthenticationError

Erro de autenticação ou autorização. Disparado para códigos HTTP 401
(Unauthorized) e 403 (Forbidden).

```python
from bling_erp_api import BlingAuthenticationError
```

### BlingValidationError

Erro de validação da requisição. Disparado para códigos de 400 a 499
(exceto 401, 403, 404, 408 e 429).

```python
from bling_erp_api import BlingValidationError
```

### BlingNotFoundError

Recurso não encontrado. Disparado para código HTTP 404.

```python
from bling_erp_api import BlingNotFoundError
```

### BlingRateLimitError

Limite de taxa excedido. Disparado para código HTTP 429.

O SDK já faz retry automático com backoff respeitando o header
`Retry-After`, mas você pode capturar esta exceção se quiser
personalizar o tratamento:

```python
from bling_erp_api import BlingRateLimitError
```

### BlingServerError

Erro interno do servidor Bling. Disparado para códigos HTTP 500+.

```python
from bling_erp_api import BlingServerError
```

## Tratamento de Erros

### Try/except básico

```python
from bling_erp_api import BlingClient, BlingAPIError

with BlingClient.from_env() as client:
    try:
        produtos = client.produtos.listar()
    except BlingAPIError as exc:
        print(f"Erro: {exc}")
        print(f"Status code: {exc.status_code}")
        if exc.payload:
            print(f"Payload: {exc.payload}")
```

### Com exceções específicas

```python
from bling_erp_api import (
    BlingAPIError,
    BlingAuthenticationError,
    BlingNotFoundError,
    BlingRateLimitError,
    BlingServerError,
    BlingTransportError,
    BlingValidationError,
)

with BlingClient.from_env() as client:
    try:
        response = client.contatos.obter(99999)
    except BlingAuthenticationError:
        print("Suas credenciais expiraram ou são inválidas")
    except BlingNotFoundError as exc:
        print(f"Contato não encontrado (HTTP {exc.status_code})")
    except BlingValidationError as exc:
        print(f"Dados inválidos: {exc}")
        if exc.payload and isinstance(exc.payload, dict):
            print(f"Detalhes: {exc.payload.get('error', {})}")
    except BlingRateLimitError:
        print("Muitas requisições — aguarde antes de tentar novamente")
    except BlingTransportError:
        print("Erro de conexão — verifique sua rede")
    except BlingServerError:
        print("Erro interno do Bling — tente novamente mais tarde")
    except BlingAPIError as exc:
        print(f"Erro não categorizado: {exc.status_code} - {exc}")
```

## Informações da Resposta

Toda exceção carrega o máximo de informação possível para debug:

```python
except BlingAPIError as exc:
    # Mensagem formatada (método + path + status + mensagem)
    print(str(exc))

    # Código HTTP
    print(exc.status_code)

    # Payload JSON da resposta (dict com "error" geralmente)
    print(exc.payload)

    # Objeto Response completo do httpx
    if exc.response:
        print(exc.response.headers)
        print(exc.response.request.method, exc.response.request.url)
```

## Erros Comuns

| Cenário | Exceção | Causa |
|---|---|---|
| Credenciais inválidas | `BlingAuthenticationError` | Client ID/secret ou refresh token incorretos |
| Token expirado | `BlingAuthenticationError` | Refresh token precisa ser renovado |
| Recurso não existe | `BlingNotFoundError` | ID inválido ou recurso removido |
| Dados obrigatórios faltando | `BlingValidationError` | Campo obrigatório não enviado |
| Formato inválido | `BlingValidationError` | CPF/CNPJ, email ou formato de data incorreto |
| Muitas requisições | `BlingRateLimitError` | Reduza a taxa (o SDK faz retry automático) |
| Timeout de rede | `BlingTransportError` | Conexão lenta ou Bling indisponível |
| Erro interno 500 | `BlingServerError` | Problema temporário no servidor do Bling |
