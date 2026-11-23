"""Repositorio de pessoas com persistencia em MySQL."""
import os
from typing import List, Optional

import mysql.connector

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMySQL(RepositorioPessoas):
    """Implementacao do repositorio de pessoas utilizando MySQL."""

    def __init__(self) -> None:
        self.__config = {
            "host": os.getenv("DB_HOST", "localhost"),
            "port": int(os.getenv("DB_PORT", "3307")),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD", ""),
            "database": os.getenv("DB_NAME", "cadastro"),
        }
        self.__garantir_tabela()

    def __conectar(self):
        return mysql.connector.connect(**self.__config)

    def __garantir_tabela(self) -> None:
        query = (
            "CREATE TABLE IF NOT EXISTS pessoa ("
            "id INT AUTO_INCREMENT PRIMARY KEY, "
            "nome VARCHAR(120) NOT NULL UNIQUE, "
            "idade INT NOT NULL, "
            "email VARCHAR(120) NOT NULL)"
        )
        with self.__conectar() as con:
            with con.cursor() as cursor:
                cursor.execute(query)
            con.commit()

    def cadastrar(self, pessoa: Pessoa) -> None:
        query = "INSERT INTO pessoa (nome, idade, email) VALUES (%s, %s, %s)"
        dados = (pessoa.getNome(), pessoa.getIdade(), pessoa.getEmail())
        with self.__conectar() as con:
            with con.cursor() as cursor:
                cursor.execute(query, dados)
            con.commit()

    def buscar(self, nome: str) -> Optional[Pessoa]:
        query = "SELECT nome, idade, email FROM pessoa WHERE nome = %s"
        with self.__conectar() as con:
            with con.cursor() as cursor:
                cursor.execute(query, (nome,))
                linha = cursor.fetchone()
        if linha is None:
            return None
        return Pessoa(linha[0], linha[1], linha[2])

    def listar(self) -> List[Pessoa]:
        query = "SELECT nome, idade, email FROM pessoa ORDER BY id"
        with self.__conectar() as con:
            with con.cursor() as cursor:
                cursor.execute(query)
                linhas = cursor.fetchall()
        return [Pessoa(linha[0], linha[1], linha[2]) for linha in linhas]

    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        query = (
            "UPDATE pessoa SET nome = %s, idade = %s, email = %s "
            "WHERE nome = %s"
        )
        dados = (
            nova_pessoa.getNome(),
            nova_pessoa.getIdade(),
            nova_pessoa.getEmail(),
            nome,
        )
        with self.__conectar() as con:
            with con.cursor() as cursor:
                cursor.execute(query, dados)
                alteradas = cursor.rowcount
            con.commit()
        return alteradas > 0
