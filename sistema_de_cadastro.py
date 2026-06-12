import sqlite3

conecao = sqlite3. connect('escola.db')
cursor = conecao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS cadastro_alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                turma TEXT,
                idade_aluno INTEGER,
                cpf TEXT UNIQUE NOT NULL)''')
nome_aluno = input("digite o nome do aluno: ")
idade_aluno = int(input("digite a idade do aluno: "))
turma_aluno = input("digite a turma: ")
telefone_aluno = input("digite o telefone do aluno")
cpf_aluno = input("digite o cpf do aluno ")

comando_inserir = (f''' INSERT INTO alunos("nome,idade,turma,telefone,cpf")
                   VALUES('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}''')