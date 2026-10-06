# Notas Fiscais (NF-e)

Nas respostas de leitura, `contato.tipo_pessoa` e `contato.contribuinte` podem
estar ausentes. O OpenAPI do Bling marca `tipoPessoa` e `contribuinte` como
`writeOnly`: sua obrigatoriedade aplica-se à requisição, conforme a
[especificação OpenAPI 3.0](https://swagger.io/specification/v3/#schema-object).
O SDK usa `NotasFiscaisContatoResponseDTO` nessas respostas, preserva os valores
quando presentes e representa a ausência como `None`. `to_json_object()` omite
esses campos ausentes; não preenche valores fiscais por conta própria.

Essa distinção também vale para a listagem, a paginação e as leituras de NFC-e
que reutilizam o mesmo schema. `NotasFiscaisContatoDTO` e os modelos de criação e
alteração continuam exigindo ambos os campos. Os métodos públicos e seus aliases
mantêm as assinaturas; o tipo do contato retornado passa a ser a variante de
resposta. `nome` e `numero_documento` continuam obrigatórios, e os aliases e a
rejeição de chaves conflitantes permanecem ativos.

A geração faz essa projeção numa cópia temporária do OpenAPI, sem alterar
`specs/bling-openapi-reference.json`. A revisão de campos `writeOnly` obrigatórios
do schema versionado identificou somente esses dois campos; os demais campos
`writeOnly` já eram opcionais nas respostas. Contratos de outros recursos e
todos os request bodies são preservados por testes de regressão.

::: bling_erp_api.resources.nfe.NfeResource
    options:
      members:
        - listar
        - iterar
        - obter
        - criar
        - alterar
        - remover_varios
        - autorizar
        - lancar_contas
        - estornar_contas
        - lancar_estoque
        - estornar_estoque
        - obter_documento_nota_fiscal
