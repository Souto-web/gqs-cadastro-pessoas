# Cadastro de Pessoas

Sistema evolutivo de cadastro de pessoas em Python, desenvolvido na disciplina **Gestão da Qualidade de Software (GQS)**, aplicando separação de responsabilidades, gerência de configuração e persistência em MySQL.

## Objetivo e Organização dos Arquivos

- `src/pessoa.py`: Entidade de domínio `Pessoa`.
- `src/cadastro.py`: Regras de negócio do cadastro (`CadastroPessoas`).
- `src/repositorio_pessoas.py`: Interface abstrata (`RepositorioPessoas`) que define o contrato de persistência.
- `src/repositorio_pessoas_memoria.py`: Implementação do repositório em memória.
- `src/repositorio_pessoas_mysql.py`: Implementação do repositório com persistência em MySQL.
- `src/main.py`: Ponto de entrada e menu interativo da aplicação.
- `infra/compose.yaml`: Configuração dos contêineres Docker para MySQL (`principal` e `replica`).
- `tests/test_cadastro.py`: Testes automatizados com PyTest.

## Requisitos e Ambiente Python

1. Crie e ative o ambiente virtual (`.venv`):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Instale as dependências do projeto:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Docker, Contêineres e Replicação

A infraestrutura do banco de dados executa dois serviços MySQL em contêineres:
- `principal`: acessível localmente na porta `3307` (mapeada para `3306` no contêiner).
- `replica`: acessível localmente na porta `3308` (mapeada para `3306` no contêiner).

Para iniciar os serviços na pasta `infra/`:
```bash
cd infra
docker compose up -d
```
Para configurar o vínculo inicial de replicação GTID entre `principal` e `replica` e verificar ambos os servidores, siga os procedimentos da Aula 11.

## Tabela `pessoa` e Variáveis de Ambiente

A persistência utiliza o banco `cadastro` e a tabela `pessoa`. Defina as variáveis de ambiente na sessão atual (sem versionar senhas nem arquivos `.env`):
```bash
export DB_HOST="localhost"
export DB_PORT="3307"
export DB_USER="root"
defina DD%�ASSWORD
export DB_NAME="cadastro"
```

## Executar e Escolher a Persistência

Na raiz do projeto, com a `.venv` ativa, execute:
```bash
python src/main.py
```
Para alternar entre armazenamento em MySQL e em memória, ajuste a constante `USAR_MYSQLp (`True` ou `False`) em `src/main.py`.
