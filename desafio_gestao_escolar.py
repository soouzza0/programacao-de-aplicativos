import sqlite3

def conectar():
    banco = sqlite3.connect("gestao_escolar.db")
    banco.execute("PRAGMA foreign_keys = ON")
    return banco


def criar_tabelas():
    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT NOT NULL,
            id_escola INTEGER,
            FOREIGN KEY (id_escola) REFERENCES escolas(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            id_turma INTEGER,
            FOREIGN KEY (id_turma) REFERENCES turmas(id)
        )
    """)

    banco.commit()
    banco.close()

import sqlite3
from banco import conectar


def cadastrar():
    nome = input("Nome da escola: ")
    cidade = input("Cidade: ")

    try:
        assert nome != "", "O nome não pode ficar vazio!"
        assert cidade != "", "A cidade não pode ficar vazia!"

        banco = conectar()
        banco.execute(
            "INSERT INTO escolas (nome, cidade) VALUES (?, ?)",
            (nome, cidade)
        )
        banco.commit()
        banco.close()

        print("Escola cadastrada!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.Error:
        print("Erro no banco de dados!")


def listar():
    banco = conectar()
    escolas = banco.execute("SELECT * FROM escolas").fetchall()
    banco.close()

    print("\n--- ESCOLAS ---")

    for escola in escolas:
        print(escola)


def alterar():
    try:
        id = int(input("ID da escola: "))
        nome = input("Novo nome: ")
        cidade = input("Nova cidade: ")

        assert nome != "", "O nome não pode ficar vazio!"
        assert cidade != "", "A cidade não pode ficar vazia!"

        banco = conectar()
        banco.execute(
            "UPDATE escolas SET nome = ?, cidade = ? WHERE id = ?",
            (nome, cidade, id)
        )
        banco.commit()
        banco.close()

        print("Escola alterada!")

    except ValueError:
        print("Digite um ID válido!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.Error:
        print("Erro no banco de dados!")


def excluir():
    try:
        id = int(input("ID da escola: "))

        banco = conectar()
        banco.execute("DELETE FROM escolas WHERE id = ?", (id,))
        banco.commit()
        banco.close()

        print("Escola excluída!")

    except ValueError:
        print("Digite um ID válido!")

    except sqlite3.IntegrityError:
        print("Não é possível excluir. Existem turmas nessa escola!")

    except sqlite3.Error:
        print("Erro no banco de dados!")


import sqlite3
from banco import conectar


def cadastrar():
    nome = input("Nome da turma: ")

    try:
        id_escola = int(input("ID da escola: "))

        assert nome != "", "O nome da turma não pode ficar vazio!"
        assert id_escola > 0, "O ID deve ser maior que zero!"

        banco = conectar()
        banco.execute(
            "INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)",
            (nome, id_escola)
        )
        banco.commit()
        banco.close()

        print("Turma cadastrada!")

    except ValueError:
        print("Digite um ID válido!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.IntegrityError:
        print("Essa escola não existe!")

    except sqlite3.Error:
        print("Erro no banco de dados!")


def listar():
    banco = conectar()
    turmas = banco.execute("SELECT * FROM turmas").fetchall()
    banco.close()

    print("\n--- TURMAS ---")

    for turma in turmas:
        print(turma)


def alterar():
    try:
        id = int(input("ID da turma: "))
        nome = input("Novo nome: ")
        id_escola = int(input("ID da escola: "))

        assert nome != "", "O nome não pode ficar vazio!"
        assert id_escola > 0, "O ID deve ser maior que zero!"

        banco = conectar()
        banco.execute(
            """
            UPDATE turmas
            SET nome_turma = ?, id_escola = ?
            WHERE id = ?
            """,
            (nome, id_escola, id)
        )
        banco.commit()
        banco.close()

        print("Turma alterada!")

    except ValueError:
        print("Digite números válidos!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.IntegrityError:
        print("Essa escola não existe!")

    except sqlite3.Error:
        print("Erro no banco de dados!")


def excluir():
    try:
        id = int(input("ID da turma: "))

        banco = conectar()
        banco.execute("DELETE FROM turmas WHERE id = ?", (id,))
        banco.commit()
        banco.close()

        print("Turma excluída!")

    except ValueError:
        print("Digite um ID válido!")

    except sqlite3.IntegrityError:
        print("Não é possível excluir. Existem alunos nessa turma!")

    except sqlite3.Error:
        print("Erro no banco de dados!")



import sqlite3
from banco import conectar


def cadastrar():
    nome = input("Nome da turma: ")

    try:
        id_escola = int(input("ID da escola: "))

        assert nome != "", "O nome da turma não pode ficar vazio!"
        assert id_escola > 0, "O ID deve ser maior que zero!"

        banco = conectar()
        banco.execute(
            "INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)",
            (nome, id_escola)
        )
        banco.commit()
        banco.close()

        print("Turma cadastrada!")

    except ValueError:
        print("Digite um ID válido!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.IntegrityError:
        print("Essa escola não existe!")

    except sqlite3.Error:
        print("Erro no banco de dados!")


def listar():
    banco = conectar()
    turmas = banco.execute("SELECT * FROM turmas").fetchall()
    banco.close()

    print("\n--- TURMAS ---")

    for turma in turmas:
        print(turma)

def alterar():
    try:
        id = int(input("ID da turma: "))
        nome = input("Novo nome: ")
        id_escola = int(input("ID da escola: "))

        assert nome != "", "O nome não pode ficar vazio!"
        assert id_escola > 0, "O ID deve ser maior que zero!"

        banco = conectar()
        banco.execute(
            """
            UPDATE turmas
            SET nome_turma = ?, id_escola = ?
            WHERE id = ?
            """,
            (nome, id_escola, id)
        )
        banco.commit()
        banco.close()

        print("Turma alterada!")

    except ValueError:
        print("Digite números válidos!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.IntegrityError:
        print("Essa escola não existe!")

    except sqlite3.Error:
        print("Erro no banco de dados!")


def excluir():
    try:
        id = int(input("ID da turma: "))

        banco = conectar()
        banco.execute("DELETE FROM turmas WHERE id = ?", (id,))
        banco.commit()
        banco.close()

        print("Turma excluída!")

    except ValueError:
        print("Digite um ID válido!")

    except sqlite3.IntegrityError:
        print("Não é possível excluir. Existem alunos nessa turma!")

    except sqlite3.Error:
        print("Erro no banco de dados!")


import sqlite3
from banco import conectar


def cadastrar():
    nome = input("Nome do aluno: ")

    try:
        idade = int(input("Idade: "))
        id_turma = int(input("ID da turma: "))

        assert nome != "", "O nome não pode ficar vazio!"
        assert idade >= 3, "A idade deve ser maior ou igual a 3!"

        banco = conectar()
        banco.execute(
            """
            INSERT INTO alunos (nome, idade, id_turma)
            VALUES (?, ?, ?)
            """,
            (nome, idade, id_turma)
        )
        banco.commit()
        banco.close()

        print("Aluno cadastrado!")

    except ValueError:
        print("Digite números válidos!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.IntegrityError:
        print("Essa turma não existe!")

    except sqlite3.Error:
        print("Erro no banco de dados!")


def listar():
    banco = conectar()
    alunos = banco.execute("SELECT * FROM alunos").fetchall()
    banco.close()

    print("\n--- ALUNOS ---")

    for aluno in alunos:
        print(aluno)


def alterar():
    try:
        id = int(input("ID do aluno: "))
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        id_turma = int(input("ID da turma: "))

        assert nome != "", "O nome não pode ficar vazio!"
        assert idade >= 3, "A idade deve ser maior ou igual a 3!"

        banco = conectar()
        banco.execute(
            """
            UPDATE alunos
            SET nome = ?, idade = ?, id_turma = ?
            WHERE id = ?
            """,
            (nome, idade, id_turma, id)
        )
        banco.commit()
        banco.close()

        print("Aluno alterado!")

    except ValueError:
        print("Digite números válidos!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.IntegrityError:
        print("Essa turma não existe!")

    except sqlite3.Error:
        print("Erro no banco de dados!")


def excluir():
    try:
        id = int(input("ID do aluno: "))

        banco = conectar()
        banco.execute("DELETE FROM alunos WHERE id = ?", (id,))
        banco.commit()
        banco.close()

        print("Aluno excluído!")

    except ValueError:
        print("Digite um ID válido!")

    except sqlite3.Error:
        print("Erro no banco de dados!")

import banco
import escola
import turma
import aluno


banco.criar_tabelas()


def Menu():

    while True:

        print("\n===== GESTÃO ESCOLAR =====")
        print("1 - Cadastrar escola")
        print("2 - Listar escolas")
        print("3 - Alterar escola")
        print("4 - Excluir escola")

        print("5 - Cadastrar turma")
        print("6 - Listar turmas")
        print("7 - Alterar turma")
        print("8 - Excluir turma")

        print("9 - Cadastrar aluno")
        print("10 - Listar alunos")
        print("11 - Alterar aluno")
        print("12 - Excluir aluno")

        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            escola.cadastrar()

        elif opcao == "2":
            escola.listar()

        elif opcao == "3":
            escola.alterar()

        elif opcao == "4":
            escola.excluir()

        elif opcao == "5":
            turma.cadastrar()

        elif opcao == "6":
            turma.listar()

        elif opcao == "7":
            turma.alterar()

        elif opcao == "8":
            turma.excluir()

        elif opcao == "9":
            aluno.cadastrar()

        elif opcao == "10":
            aluno.listar()

        elif opcao == "11":
            aluno.alterar()

        elif opcao == "12":
            aluno.excluir()

        elif opcao == "0":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")


Menu()
