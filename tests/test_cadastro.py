"""Testes das operacoes de cadastro."""

import copy

import pytest

from cadastro import CadastroPessoas
from pessoa import Pessoa
from repositorio_pessoas_memoria import RepositorioPessoasMemoria


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


class RepositorioDeCopias(RepositorioPessoasMemoria):
    """Devolve copias, simulando objetos reconstruidos."""

    def buscar(self, nome):
        """Retorna uma copia da pessoa encontrada."""
        pessoa = super().buscar(nome)

        if pessoa is None:
            return None

        return copy.copy(pessoa)


@pytest.mark.parametrize(
    "fabrica",
    [RepositorioPessoasMemoria, RepositorioDeCopias]
)
def test_alterar_persiste(fabrica):
    """Verifica se a alteracao fica salva no repositorio."""
    repositorio = fabrica()
    repositorio.cadastrar(
        Pessoa("Ana Souza", 30, "ana@example.com")
    )

    cadastro = CadastroPessoas(repositorio)
    cadastro.alterar(
        "Ana Souza",
        "Ana Souza",
        31,
        "ana.s@example.com"
    )

    pessoa = repositorio.buscar("Ana Souza")

    assert pessoa is not None
    assert pessoa.getIdade() == 31
    assert pessoa.getEmail() == "ana.s@example.com"
