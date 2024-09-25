# Rural Producer API

Esta é uma API desenvolvida para gerenciar informações sobre produtores e suas fazendas, projetada com foco em boas práticas de desenvolvimento utilizando SOLID, KISS, Clean Code e Layered Architecture.


## Como Executar a Aplicação

### Localmente

Para executar a aplicação localmente, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd nome-do-repositorio

2. Se estiver em ambiente linux pode criar sua env utilizando:
   ```bash
   make create-env

3. instale as libs utiliando
    ```bash
    make install

4. Faça o migrate utilizando
    ```bash
    make migrate

5. para executar local
    ```bash
    make run


### Localmente
A aplicação dispẽs de um swagger no cmainho **localhost/swagger** ou **localhost/redoc**

### Teste
Foram desenvolvidos alguns teste para garantir as regras de negócios dos model, para executa-los

    pytest

### pre-commit
Na aplicação foi adicionado um pre-commit para validar o codigo antes do commit você pode executa-lo antes de commitar ou executando:

    pre-commit
