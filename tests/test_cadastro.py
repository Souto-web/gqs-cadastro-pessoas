"""Testes das operacoes de cadastro."""
import os
import uuid
import pytest

from cadastro import CadastroPessoas
from repositorio_pessoas_mysql import RepositorioPessoasMySQL


def test_cadastrar_pessoa():
    """Confere armazenamento e quantidade."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")

    pessoas = cadastro.listar()
    assert len(pessoas) == 1
    assert pessoas[0].getNome() == "Ana"
    assert pessoas[0].getIdade() == 20
    assert pessoas[0].getEmail() == "ana@example.com"


def test_buscar_por_nome():
    """Encontra uma pessoa ja cadastrada."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")

    encontrada = cadastro.buscarPorNome("Ana")

    assert encontrada is not None
    assert encontrada.getNome() == "Ana"
    assert encontrada.getIdade() == 20
    assert encontrada.getEmail() == "ana@example.com"


def test_alterar_pessoa():
    """Altera os dados de uma pessoa cadastrada."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")

    alterada = cadastro.alterar("Ana", "Ana Silva", 21, "ana.silva@example.com")

    assert alterada is not None
    assert alterada.getNome() == "Ana Silva"
    assert alterada.getIdade() == 21
    assert cadastro.buscarPorNome("Ana Silva") is not None


@pytest.mark.skipif(not os.getenv("DB_PASSWORD"), reason="DB_PASSWORD nao definida")
def test_persistencia_mysql():
    """Valida cadastro, busca, listagem e alteracao no MySQL."""
    repo = RepositorioPessoasMySQL()
    cadastro = CadastroPessoas(repo)
    sufixo = uuid.uuid4().hex[:6]
    nome_inicial = f"Gabriel Teste {sufixo}"
    nome_final = f"Gabriel Alterado {sufixo}"

    cadastro.cadastrar(nome_inicial, 22, "gabriel@utfpr.edu.br")
    buscada = cadastro.buscarPorNome(nome_inicial)
    assert buscada is not None
    assert buscada.getEmail() == "gabriel@utfpr.edu.br"

    alterada = cadastro.alterar(
        nome_inicial, nome_final, 23, "gabriel.novo@utfpr.edu.br"
    )
    assert alterada is not None
    assert any(p.getNome() == nome_final for p in cadastro.listar())
