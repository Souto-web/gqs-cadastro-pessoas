# Contribuindo com o projeto

Este projeto é utilizado na disciplina de Gestão da Qualidade de Software.

As alterações devem ser realizadas de forma incremental e verificável, preservando o funcionamento do sistema durante sua evolução.

## Preparação do ambiente

Após clonar o repositório:

```bash
git clone https://github.com/julianolamb/gqs-cadastro-pessoas.git
cd gqs-cadastro-pessoas
```

Instale as ferramentas utilizadas no projeto:

```bash
pip install pylint radon pre-commit
```

Ative o hook do pre-commit:

```bash
pre-commit install
```

O comando `pre-commit install` deve ser executado em cada novo clone do repositório, pois o hook é instalado localmente no diretório `.git`.

O arquivo `.pre-commit-config.yaml` faz parte do projeto e é versionado pelo Git. Portanto, ele é obtido normalmente ao realizar o clone.

## Antes de iniciar uma alteração

Atualize a branch principal:

```bash
git switch main
git pull
```

Verifique o estado do repositório:

```bash
git status
```

A árvore de trabalho deve estar limpa antes de iniciar uma nova alteração.

## Trabalhando com branches

Alterações relevantes devem ser realizadas em uma branch própria.

Exemplo:

```bash
git switch -c refactor/orientacao-objetos
```

A branch permite desenvolver e verificar uma alteração sem modificar diretamente a versão estável disponível em `main`.

## Durante o desenvolvimento

Faça alterações pequenas e relacionadas a um único objetivo.

Após cada etapa:

1. execute o programa;
2. verifique se o comportamento esperado foi preservado;
3. confira os arquivos modificados;
4. registre a alteração em um commit.

Para executar o programa:

```bash
python src/main.py
```

Para verificar as alterações:

```bash
git status
git diff
```

## Análise estática

O projeto utiliza Pylint para análise estática.

A análise pode ser executada manualmente com:

```bash
pylint src
```

O projeto também utiliza `pre-commit`. O hook configurado é executado automaticamente durante a realização dos commits.

Se a verificação falhar, o commit não será realizado. Os problemas apontados devem ser analisados e corrigidos antes de uma nova tentativa.

Também é possível executar manualmente todos os hooks configurados:

```bash
pre-commit run --all-files
```

## Métricas

A complexidade ciclomática pode ser analisada com Radon:

```bash
radon cc src -s
```

Os resultados devem ser interpretados considerando a responsabilidade e o contexto de cada função ou método.

## Commits

Antes de realizar um commit, verifique as alterações:

```bash
git status
git diff
```

Adicione somente os arquivos relacionados à alteração:

```bash
git add <arquivos>
```

Os commits devem representar alterações pequenas e verificáveis, com mensagens que indiquem claramente o objetivo da mudança.

Exemplos:

```text
refactor: reorganiza estrutura do projeto
refactor: cria classe Pessoa
refactor: encapsula operacoes em CadastroPessoas
refactor: separa interface da aplicacao
docs: atualiza orientacoes de contribuicao
style: corrige apontamentos do pylint
```

Depois do commit, o histórico pode ser consultado com:

```bash
git log --oneline
```

Para inspecionar as alterações registradas em um commit específico:

```bash
git show <hash>
```

## Arquivos que não devem ser versionados

Arquivos temporários ou gerados automaticamente pelas ferramentas não devem ser adicionados ao repositório.

O arquivo `.gitignore` define arquivos e diretórios que devem ser ignorados pelo Git.

Exemplos:

```text
__pycache__/
*.pyc
```

## Antes de integrar uma alteração

Antes de realizar o merge, execute o programa e as verificações previstas:

```bash
python src/main.py
pylint src
radon cc src -s
git status
```

Confirme que:

- o comportamento esperado foi preservado;
- não existem problemas de análise estática que precisem ser corrigidos;
- as métricas foram verificadas quando pertinentes;
- não existem alterações pendentes no repositório.

Somente depois dessas verificações a alteração deve ser integrada à branch principal.
## Testes Automatizados e Pull Request

Execute a suíte de testes automatizados com PyTest antes de abrir um Pull Request:

```bash
python -m pytest -v
```

Publique sua branch dedicada no GitHub e abra um Pull Request apontando para `main`:

```bash
git push -u origin <nome-da-branch>
```

A contribuição será revisada (`Files changed`) e integrada  à `main` após aprovação nos testes e nO Pylint.
