# Social Network API

Este é um projeto de API para uma rede social, construído com FastAPI e Tortoise ORM. A API permite o registro e login de usuários, além de outras funcionalidades que podem ser implementadas.

## Tecnologias Utilizadas

- **FastAPI**: Um framework moderno e rápido para construir APIs com Python 3.6+ baseado em tipos de dados.
- **Tortoise ORM**: Um ORM assíncrono para Python, projetado para ser fácil de usar e com suporte a relações.
- **Poetry**: Uma ferramenta de gerenciamento de dependências e empacotamento para projetos Python.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/social-network.git
   cd social-network
   ```

2. Instale as dependências usando o Poetry:
   ```bash
   poetry install
   ```

3. Ative o ambiente virtual:
   ```bash
   poetry shell
   ```

## Configuração do Banco de Dados

Certifique-se de que o banco de dados está configurado corretamente no seu arquivo de configuração. O Tortoise ORM suporta vários bancos de dados, como SQLite, PostgreSQL, etc.

## Executando a Aplicação

Para executar a aplicação, utilize o seguinte comando:
    ```bash
   poetry run uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload
   ```

A aplicação estará disponível em `http://localhost:8000`.

## Endpoints

### Registro de Usuário

- **POST** `/users/register`
  - **Body**: 
    ```json
    {
      "name": "Nome do Usuário",
      "email": "email@exemplo.com",
      "password": "senha"
    }
    ```

### Login de Usuário

- **POST** `/users/login`
  - **Body**: 
    ```json
    {
      "email": "email@exemplo.com",
      "password": "senha"
    }
    ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.