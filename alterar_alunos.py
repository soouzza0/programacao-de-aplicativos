import sqlite3
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

cursor.execute (''' DROP TABLE alunos ''')