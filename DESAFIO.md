# Desafio Prático: API REST para Acesso a Dados de Saúde

Imagine que você teve acesso a um banco de dados de atendimentos de saúde exportado de um sistema de terceiros. Sua equipe de Ciência de Dados precisa acessar esses dados de forma sistematizada. Após uma reunião, decidiu-se que a melhor abordagem seria criar uma API REST para fornecer acesso aos dados.

Seu desafio é criar essa API REST usando Python e o framework Flask.

## Orientações

Aqui estão algumas orientações sobre como abordar o desafio:

1.  O banco de dados é representado pelo arquivo **`atendimentos.csv`**.
2.  A linguagem usada deve ser obrigatoriamente **Python**.
3.  O framework a ser utilizado deve ser o **Flask**.

## Requisitos

- O endpoint deve estar acessível na URL: `http://localhost:8001/api/v1/atendimentos`.
- Este endpoint deve ser capaz de receber filtros e retornar os resultados corretos para esses filtros. Os filtros necessários são:
  - `data_atendimento (str): Formato 'YYYY-mm-dd'`.
  - `condicao_saude (str): hipertensao|diabetes|ferida vascular|dengue|tuberculose`.
  - `unidade (str)`.
- Os filtros podem ser combinados entre si, permitindo uma maior flexibilidade de consultas. Por exemplo:
  - `http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01`.
  - `http://localhost:8001/api/v1/atendimentos?data_atendimento=2024-01-01&condicao_saude=hipertensao`.

## Considerações Finais

- Você tem liberdade para tratar os dados da forma que julgar necessária para produzir um resultado de qualidade.
- Defina a melhor arquitetura e organização de código que julgar necessária.
- Forneça instruções detalhadas sobre como executar seu código localmente. Códigos que não puderem ser executados serão desclassificados (o desejável seria usar docker-compose para provisionar o ambiente, mas não é obrigatório).
- Mostre o melhor do seu trabalho. Apesar de pequeno, este desafio é suficiente para avaliar sua organização de código, domínio da linguagem e do framework, capacidade de solução de problemas, conhecimento de arquitetura de software, boas práticas e documentação de código.
- A entrega deverá ser feita por meio de um link do seu repositório no github.

Boa sorte.

**May the force be with you.**
