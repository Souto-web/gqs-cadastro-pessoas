
"""Implementa o repositório de pessoas em memória."""

from typing import List, Optional

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMemoria(RepositorioPessoas):
    """Armazena pessoas em uma lista na memória."""

    def __init__(self) -> None:
        self.__pessoas: List[Pessoa] = []

    def cadastrar(self, pessoa: Pessoa) -> None:
        """Adiciona uma pessoa ao repositório."""
        self.__pessoas.append(pessoa)

    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Busca uma pessoa pelo nome."""
        for pessoa in self.__pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def listar(self) -> List[Pessoa]:
        """Retorna uma cópia da lista de pessoas."""
        return list(self.__pessoas)

    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Substitui uma pessoa identificada pelo nome."""
        for indice, pessoa in enumerate(self.__pessoas):
            if pessoa.getNome() == nome:
                self.__pessoas[indice] = nova_pessoa
                return True
        return False
