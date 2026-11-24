"""Testes das operações de cadastro."""
from cadastro import CadastroPessoas

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
    """Encontra uma pessoa já cadastrada."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")

    encontrada = cadastro.buscarPorNome("Ana")

    assert encontrada is not None
    assert encontrada.getNome() == "Ana"
    assert encontrada.getIdade() == 20
    assert encontrada.getEmail() == "ana@example.com"


def test_alterar_pessoa():
    """Verifica a atualizacao dos dados de uma pessoa."""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ana", 20, "ana@example.com")

    alterada = cadastro.alterar("Ana", "Maria", 25, "maria@example.com")

    assert alterada is not None
    assert alterada.getNome() == "Maria"
    assert alterada.getIdade() == 25
    assert alterada.getEmail() == "maria@example.com"
    assert cadastro.buscarPorNome("Ana") is None
    assert cadastro.buscarPorNome("Maria") is alterada
    assert len(cadastro.listar()) == 1


def test_alterar_pessoa_inexistente():
    """Verifica o retorno ao alterar uma pessoa inexistente."""
    cadastro = CadastroPessoas()

    resultado = cadastro.alterar("Ana", "Maria", 25, "maria@example.com")

    assert resultado is None
    assert len(cadastro.listar()) == 0
