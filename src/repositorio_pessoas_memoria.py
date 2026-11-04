"""Repositorio de pessoas armazenadas em memoria."""

from repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMemoria(RepositorioPessoas):
    """Armazena pessoas em uma lista."""

    def __init__(self):
        self.__pessoas = []

    def adicionar(self, pessoa):
        self.__pessoas.append(pessoa)

    def buscarPorNome(self, nome):
        for pessoa in self.__pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def listar(self):
        return self.__pessoas
