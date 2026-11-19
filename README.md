# Cadastro de Pessoas — GQS

Projeto desenvolvido na disciplina de **Gestão da Qualidade de Software**, utilizando Python, MySQL, Docker e GitHub.

O sistema permite cadastrar, consultar, alterar, listar e analisar os dados de pessoas. Os registros são armazenados em um banco de dados MySQL.

## Tecnologias utilizadas

- Python
- MySQL 8.4
- Docker Compose
- Pytest
- Pylint
- Pre-commit
- Git e GitHub

## Estrutura do projeto

- `src/` — código-fonte da aplicação.
- `src/main.py` — menu principal.
- `src/cadastro.py` — regras de gerenciamento do cadastro.
- `src/repositorio_pessoas_memoria.py` — armazenamento em memória.
- `src/repositorio_pessoas_mysql.py` — persistência no MySQL.
- `infra/compose.yaml` — configuração do MySQL principal e da réplica.
- `tests/` — testes automatizados.
- `requirements.txt` — dependências do Python.
- `CONTRIBUTING.md` — orientações para contribuição.

## Preparação do ambiente

Clone o repositório:

```powershell
git clone https://github.com/joenckk/gqs-cadastro-pessoas.git
cd gqs-cadastro-pessoas
```

Crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente no Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a execução do script, libere-a somente para a sessão atual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

## Banco de dados MySQL

O projeto utiliza dois serviços no Docker Compose:

- **Principal:** porta `3307`.
- **Réplica:** porta `3308`.

É necessário ter o Docker Desktop instalado e em execução.

Para iniciar os serviços:

```powershell
docker compose -f infra/compose.yaml up -d
```

Para verificar o estado dos contêineres:

```powershell
docker compose -f infra/compose.yaml ps
```

Aguarde até os serviços aparecerem como `healthy`.

O banco utilizado pela aplicação é `cadastro_pessoas`, com a tabela `pessoas`.

## Configuração da conexão

Antes de executar a aplicação, configure a variável de ambiente `MYSQL_PASSWORD` com a senha do MySQL definida no seu ambiente.

No PowerShell:

```powershell
$env:MYSQL_PASSWORD = Read-Host "Digite a senha do MySQL"
```

Por segurança, **não coloque senhas diretamente no código, no README ou em commits**.

A aplicação utiliza, por padrão:

- Host: `127.0.0.1`
- Porta: `3307`
- Usuário: `root`
- Banco: `cadastro_pessoas`

Essas configurações podem ser ajustadas pelas variáveis de ambiente `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER` e `MYSQL_DATABASE`.

## Execução do programa

Com o ambiente virtual ativado, o Docker funcionando e a variável `MYSQL_PASSWORD` configurada, execute:

```powershell
python src/main.py
```

O menu permite:

1. Cadastrar pessoa.
2. Consultar pessoa.
3. Alterar pessoa.
4. Listar pessoas.
5. Avaliar cadastro.
6. Sair.

## Testes automatizados

Execute os testes com:

```powershell
python -m pytest -v
```

Os testes verificam cadastro, busca e persistência da alteração em dois tipos de repositório.

## Qualidade do código

Execute o Pylint:

```powershell
pylint src tests
```

Para instalar os hooks locais do projeto:

```powershell
pre-commit install
```

Os hooks configurados verificam o código antes dos commits.

## Colaboração e versionamento

O desenvolvimento utiliza branches, commits e Pull Requests no GitHub.

A branch `base-gcs-01` reúne as alterações da atividade GCS-01.

As orientações para contribuir estão disponíveis em `CONTRIBUTING.md`.

## Autoria

**Isabella Vieira Joenck**
Gestão da Qualidade de Software — UTFPR

Repositório: https://github.com/joenckk/gqs-cadastro-pessoas
