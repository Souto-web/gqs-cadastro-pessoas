"""Contrato para repositorios de pessoas."""

from abc import ABC, abstractmethod


class RepositorioPessoas(ABC):
    """Define as operacoes do repositorio."""

    @abstractmethod
    def adicionar(self, pessoa):
        """Adiciona uma pessoa."""

    @abstractmethod
    def buscarPorNome(self, nome):
        """Busca uma pessoa pelo nome."""

    @abstractmethod
    def listar(self):
        """Retorna as pessoas cadastradas."""
