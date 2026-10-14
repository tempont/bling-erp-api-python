# Comece por aqui

## Instalação

Install with `pip`:

```bash
pip install bling-erp-api
```

Or with `uv`:

```bash
uv add bling-erp-api
```

## Criando um Client

Antes de criar um client, você precisa das credenciais OAuth2 da sua
aplicação no Bling ERP (ver [Autenticação](authentication.md)).

### Via variáveis de ambiente (recomendado)

Configure as seguintes variáveis de ambiente:

```bash
export BLING_CLIENT_ID="seu_client_id"
export BLING_CLIENT_SECRET="seu_client_secret"
export BLING_REFRESH_TOKEN="seu_refresh_token"
```

Depois crie um client com `from_env()`:

```python
from bling_erp_api import BlingClient

client = BlingClient.from_env()
```

### Com um token provider personalizado

```python
from bling_erp_api import BlingClient
from bling_jwt_auth import BlingAuth

auth = BlingAuth(
    client_id="seu_client_id",
    client_secret="seu_client_secret",
    refresh_token="seu_refresh_token",
)

client = BlingClient(auth=auth)
```

### Usando context manager

Sempre que possível, use o client como context manager para garantir que os
recursos HTTP sejam liberados corretamente:

```python
from bling_erp_api import BlingClient

with BlingClient.from_env() as client:
    # Faça suas chamadas aqui
    pass
```

## Primeira Chamada à API

### Listar produtos

```python
from bling_erp_api import BlingClient

with BlingClient.from_env() as client:
    # pt-BR canonical method
    response = client.produtos.listar(limit=5)

    for produto in response.get("data", []):
        print(f'{produto.get("id")}: {produto.get("nome")}')
```

Ou com o alias em inglês:

```python
with BlingClient.from_env() as client:
    response = client.products.list(limit=5)

    for product in response.get("data", []):
        print(f'{product.get("id")}: {product.get("nome")}')
```

### Obter um contato

```python
with BlingClient.from_env() as client:
    contato = client.contatos.obter(42)
    print(contato)
```

### Trabalhando com modelos tipados

Para endpoints que possuem modelos Pydantic, você recebe objetos tipados:

```python
from bling_erp_api import BlingClient
from bling_erp_api.models.generated.schemas.contatos import ContatoDTO

with BlingClient.from_env() as client:
    contato = client.contatos.obter(42)

    # O payload pode ser acessado com notação de dicionário ou atributos
    if isinstance(contato, dict):
        print(contato.get("data", {}).get("nome"))
```

### Paginação

Endpoints de listagem aceitam `page` e `limit`:

```python
with BlingClient.from_env() as client:
    # Página 2, 20 itens por página
    response = client.produtos.listar(page=2, limit=20)
```

Para autopaginação, veja [Paginação](pagination.md).

## Tratamento de Erros

Os erros da API são mapeados para exceções tipadas:

```python
from bling_erp_api import BlingClient
from bling_erp_api import (
    BlingAPIError,
    BlingAuthenticationError,
    BlingNotFoundError,
    BlingRateLimitError,
    BlingValidationError,
)

with BlingClient.from_env() as client:
    try:
        produtos = client.produtos.listar()
    except BlingAuthenticationError:
        print("Credenciais inválidas ou expiradas")
    except BlingNotFoundError as exc:
        print(f"Recurso não encontrado: {exc}")
    except BlingValidationError as exc:
        print(f"Erro de validação: {exc}")
    except BlingRateLimitError:
        print("Limite de taxa excedido")
    except BlingAPIError as exc:
        print(f"Erro na API: {exc.status_code} - {exc}")
```

Veja [Erros](errors.md) para a hierarquia completa de exceções.
