import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    conexao.execute("PRAGMA foreign_keys = ON")
    
    try:
        cursor.execute ("INSERT INTO series (nome_serie, id_escola) VALUES (?,?)",
                        (nome_serie, id_escola))
    except sqlite3.integrityError:
        print("erro: escola inexistente!")
    finally:
        conexao.close()

# o aluno tenta cadastrar uma serie com id_escola = 999 (que não existe).
# o SQlite aceita o cadastro mesmo assim. o que está faltando ativar?
#R: a tabela precisa de uma chave estrangeira "foreign_keys"