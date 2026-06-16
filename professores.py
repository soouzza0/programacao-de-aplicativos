import sqlite3

conecao = sqlite3. connect('escola.db')
cursor = conecao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS professores(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                materia TEXT,
                idade_professor INTEGER,
                cpf TEXT UNIQUE NOT NULL,
                salario REAL NOT NULL,
                nome_da_escola TEXT,''')

nome_professor = input("digite o nome do professor: ")
idade_professor = int(input("digite a idade do professor: "))
materia = input("digite a materia: ")
telefone_professor = input("digite o telefone do professor: ")
cpf_professor = input("digite o cpf do professor: ")
salario_professor = float(input("digite o salario:"))
nome_da_escola = input("digite o nome da escola:")

comando_inserir = (f''' INSERT INTO alunos("nome,idade,materia,telefone,cpf,salario,")
                   VALUES('{nome_professor}', '{telefone_professor}', '{materia}', '{idade_professor}', '{cpf_professor}''')