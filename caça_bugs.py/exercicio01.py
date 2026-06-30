import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXIST escolas (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    nome TEXT NOT NULL
    )
    ''')

    # o banco nao está salvando as alteraçoes. por que ? 
    # R: nao foi criado um banco de dados, e faltou o "conexao.commit()"" para salvar as alteraçoes.

    conexao.close()
    conexao.commit()

