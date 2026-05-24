# bling-erp-api

SDK Python **não oficial** em torno da [API do Bling](https://developer.bling.com.br/): wrapper tipado que resolve autenticação, paginação, helpers e toda a lógica necessária para operar a API do ERP com Python.

## Autenticação

- O projeto atual separa a lógica de autenticação da lógica de requisições HTTP, utilizando o pacote [Bling JWT Auth](https://pypi.org/project/bling-jwt-auth/) para autenticação.
