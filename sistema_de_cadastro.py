import sqlite3

conecao = sqlite3. connect('escola.db')
cursor = conecao.cursor()

cursor.execute('''
                CREAT TABLE IF NOT EXIST cadastro_alunos(
                id integrer primary key autoincrement
                nome text not null,
                telefone text,
                turma text,
                idade_aluno interger,
                cpf text unique not null 
                )''')
nome_aluno = input("digite o nome do aluno")
idade_aluno = int(input("digite o telefone do aluno: "))
turma_aluno = input("digite a turma: ")
telefone_aluno = input("digite o telefone do aluno")
cpf_aluno = input("digite o cpf do aluno ")

