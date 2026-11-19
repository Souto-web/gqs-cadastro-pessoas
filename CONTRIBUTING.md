# Contribuindo com o projeto

Este projeto é desenvolvido na disciplina de **Gestão da Qualidade de Software**, da UTFPR.

As contribuições devem ser realizadas de forma incremental, com testes, análise de qualidade e registro das alterações no GitHub.

## 1. Preparação do ambiente

Clone o repositório:

```powershell
git clone https://github.com/joenckk/gqs-cadastro-pessoas.git
cd gqs-cadastro-pessoas
```

Crie e ative o ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Configure os hooks automáticos:

```powershell
pre-commit install
```

## 2. Atualização do repositório

Antes de começar uma alteração, atualize a branch utilizada na atividade GCS-01:

```powershell
git switch base-gcs-01
git pull origin base-gcs-01
git status
```

Verifique se existem alterações locais antes de iniciar o trabalho.

## 3. Criação de branches

Cada alteração deve ser desenvolvida em uma branch própria.

Exemplo:

```powershell
git switch -c feature/minha-alteracao
```

Para mudanças de documentação:

```powershell
git switch -c docs/minha-documentacao
```

Evite desenvolver diretamente na branch `base-gcs-01`.

## 4. Execução da aplicação

A aplicação utiliza MySQL com Docker Compose.

Inicie os serviços:

```powershell
docker compose -f infra/compose.yaml up -d
```

Confira se os contêineres estão saudáveis:

```powershell
docker compose -f infra/compose.yaml ps
```

Configure a senha do MySQL na sessão atual do PowerShell:

```powershell
$env:MYSQL_PASSWORD = Read-Host "Digite a senha do MySQL"
```

Execute o programa:

```powershell
python src/main.py
```

Não inclua senhas em arquivos versionados, commits ou Pull Requests.

## 5. Testes automatizados

Antes de registrar uma alteração, execute:

```powershell
python -m pytest -v
```

Os testes verificam as operações de cadastro, busca e persistência da alteração.

Caso algum teste falhe, investigue e corrija o problema antes de solicitar o merge.

## 6. Qualidade do código

Execute a análise estática:

```powershell
pylint src tests
```

Também é possível executar os hooks manualmente:

```powershell
pre-commit run --all-files
```

Os hooks configurados são executados automaticamente durante os commits.

## 7. Commits

Confira as modificações:

```powershell
git status
git diff
git diff --check
```

Adicione somente os arquivos relacionados à alteração:

```powershell
git add caminho/do/arquivo
```

Crie um commit com uma mensagem objetiva:

```powershell
git commit -m "docs: atualiza documentacao do projeto"
```

Exemplos de prefixos:

- `feat:` — nova funcionalidade.
- `fix:` — correção.
- `test:` — testes.
- `refactor:` — reorganização de código.
- `docs:` — documentação.

Não utilize `git add .` sem conferir os arquivos, para evitar incluir arquivos temporários ou dados sensíveis.

## 8. Pull Requests e revisão

Depois de criar o commit, envie sua branch:

```powershell
git push -u origin nome-da-branch
```

No GitHub, abra um Pull Request para a branch `base-gcs-01` deste repositório.

Na descrição do Pull Request, informe:

- O objetivo da alteração.
- Os arquivos ou funcionalidades modificados.
- Os testes realizados.
- Os resultados do Pytest e do Pylint.

Confira os arquivos alterados e possíveis conflitos antes de realizar o merge.

Em contribuições entre estudantes, o autor e o revisor devem estar identificados no histórico do GitHub.

## 9. Arquivos que não devem ser enviados

Não adicione ao Git:

- Senhas e arquivos com credenciais.
- Ambientes virtuais, como `.venv/`.
- Arquivos temporários e cópias de segurança.
- Diretórios `__pycache__/`.
- Arquivos `.pyc`.

Consulte o `.gitignore` e confira o resultado de `git status` antes de cada commit.

## 10. Histórico e evidências

Para consultar os commits:

```powershell
git log --oneline
```

Para consultar um commit específico:

```powershell
git show HASH_DO_COMMIT
```

Os Pull Requests, os commits e os resultados das verificações podem ser utilizados como evidências no diário técnico da atividade.

## Autoria

**Isabella Vieira Joenck**

Gestão da Qualidade de Software — UTFPR

Repositório: https://github.com/joenckk/gqs-cadastro-pessoas
