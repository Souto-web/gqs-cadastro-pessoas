
"""Define o contrato para o armazenamento de pessoas."""

from abc import ABC, abstractmethod
from typing import List, Optional

from pessoa import Pessoa


class RepositorioPessoas(ABC):
    """Contrato abstrato para repositorios de pessoas."""

    @abstractmethod
    def cadastrar(self, pessoa: Pessoa) -> None:
        """Armazena uma pessoa."""

    @abstractmethod
    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Busca uma pessoa pelo nome."""

    @abstractmethod
    def listar(self) -> List[Pessoa]:
        """Retorna a lista de pessoas."""

    @abstractmethod
    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Altera uma pessoa identificada pelo nome."""
