"""Gerenciamento do cadastro de pessoas."""

from pessoa import Pessoa
from repositorio_pessoas_memoria import RepositorioPessoasMemoria


class CadastroPessoas:
    """Gerencia o cadastro usando um repositorio."""

    def __init__(self, repositorio=None):
        if repositorio is None:
            repositorio = RepositorioPessoasMemoria()
        self.__repositorio = repositorio

    def cadastrar(self, nome, idade, email):
        pessoa = Pessoa(nome, idade, email)
        self.__repositorio.adicionar(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        return self.__repositorio.buscarPorNome(nome)

    def listar(self):
        return self.__repositorio.listar()

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        pessoa = self.buscarPorNome(nome)

        if pessoa is None:
            return None

        pessoa.setNome(novo_nome)
        pessoa.setIdade(nova_idade)
        pessoa.setEmail(novo_email)

        return pessoa
