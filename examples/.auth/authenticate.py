"""Exemplo de código para autenticação com o Bling de forma interativa.

Usa o pacote bling_jwt_auth.

Documentação: https://github.com/tempont/bling-jwt-auth-python
Variáveis:
    - BLING_CLIENT_ID
    - BLING_CLIENT_SECRET
    - BLING_REDIRECT_URI
"""  # noqa

import os

from bling_jwt_auth import BlingAuthSettings, OAuthClient, TokenManager, create_token_store

# 1. Carrega os settings de variáveis de ambiente.
settings = BlingAuthSettings.load()

# 2. Cria o armazenamento de tokens. (default: SQLite)
store = create_token_store(settings)

# 3. Cria o cliente Oauth e o TokenManager e inicia a autenticação via CLI/Browser.
with OAuthClient(settings) as oauth:
    manager = TokenManager(oauth, store, settings)

    # 4. Build authorization URL for the browser
    auth_url = oauth.build_authorization_url(state=os.urandom(16).hex())
    print(f"Open in browser: {auth_url}")
    # User opens URL, approves access, Bling redirects to BLING_REDIRECT_URI?code=...

    # 5. Exchange the callback code for tokens (saves to store automatically)
    code = input("Paste authorization code: ").strip()
    manager.save_from_code(code)

    # 6. Now ready — every subsequent call auto-refreshes
    token = manager.get_access_token()
    print(f"Access token acquired: {token[:24]}...")
