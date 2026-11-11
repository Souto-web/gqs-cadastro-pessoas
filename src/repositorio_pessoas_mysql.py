
"""Persistencia de pessoas utilizando MySQL."""

import os

import mysql.connector

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMySQL(RepositorioPessoas):
    """Implementa o armazenamento de pessoas no MySQL."""

    def __init__(self):
        self.config = {
            "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
            "port": int(os.getenv("MYSQL_PORT", "3307")),
            "user": os.getenv("MYSQL_USER", "root"),
            "password": os.environ["MYSQL_PASSWORD"],
            "database": os.getenv("MYSQL_DATABASE", "cadastro_pessoas"),
        }
        self.criar_tabela()

    def conectar(self):
        """Abre uma conexao com o banco."""
        return mysql.connector.connect(**self.config)

    def criar_tabela(self):
        """Cria a tabela caso ela nao exista."""
        conexao = self.conectar()
        try:
            cursor = conexao.cursor()
            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pessoas (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(150) NOT NULL,
                        idade INT NOT NULL,
                        email VARCHAR(255) NOT NULL
                    )
                """)
                conexao.commit()
            finally:
                cursor.close()
        finally:
            conexao.close()

    def cadastrar(self, pessoa):
        """Salva uma pessoa no banco."""
        conexao = self.conectar()
        try:
            cursor = conexao.cursor()
            try:
                cursor.execute(
                    "INSERT INTO pessoas (nome, idade, email) "
                    "VALUES (%s, %s, %s)",
                    (
                        pessoa.getNome(),
                        pessoa.getIdade(),
                        pessoa.getEmail(),
                    ),
                )
                conexao.commit()
            finally:
                cursor.close()
        finally:
            conexao.close()

    def buscar(self, nome):
        """Busca uma pessoa pelo nome."""
        conexao = self.conectar()
        try:
            cursor = conexao.cursor()
            try:
                cursor.execute(
                    "SELECT nome, idade, email FROM pessoas "
                    "WHERE nome = %s ORDER BY id LIMIT 1",
                    (nome,),
                )
                resultado = cursor.fetchone()
            finally:
                cursor.close()
        finally:
            conexao.close()

        if resultado:
            return Pessoa(*resultado)
        return None

    def listar(self):
        """Lista todas as pessoas cadastradas."""
        conexao = self.conectar()
        try:
            cursor = conexao.cursor()
            try:
                cursor.execute(
                    "SELECT nome, idade, email "
                    "FROM pessoas ORDER BY id"
                )
                resultados = cursor.fetchall()
            finally:
                cursor.close()
        finally:
            conexao.close()

        return [Pessoa(*dados) for dados in resultados]

    def alterar(self, nome, nova_pessoa):
        """Atualiza uma pessoa identificada pelo nome."""
        conexao = self.conectar()
        try:
            cursor = conexao.cursor()
            try:
                cursor.execute(
                    """
                    UPDATE pessoas
                    SET nome = %s, idade = %s, email = %s
                    WHERE nome = %s
                    ORDER BY id
                    LIMIT 1
                    """,
                    (
                        nova_pessoa.getNome(),
                        nova_pessoa.getIdade(),
                        nova_pessoa.getEmail(),
                        nome,
                    ),
                )
                alterado = cursor.rowcount > 0
                conexao.commit()
                return alterado
            finally:
                cursor.close()
        finally:
            conexao.close()
