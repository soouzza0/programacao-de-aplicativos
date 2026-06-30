import sqlite3

def vincular_aluno_turma():
    nome = input("nome do aluno:")
    # se o usuario digitar "turma B" em vez do número do ID, o sistema quebra.
    # o try/except abaixo falhou em capturar esse erro. qual o problema?
    try:
        id_turma = int(input("digite o ID numerico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO alunos (nome_turma) VALUES (?,?)",
              (nome, id_turma)
              )
        
        conexao.commit()
        conexao.close()

    except ValueError:

        print("Erro: o ID da turma deve ser um número inteiro.")

    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")



#R: se o usuario digitar "turma B" vai dar erro por "id_turma" ser int
#R: O try/except falhou porque o erro não é sqlite3.Error