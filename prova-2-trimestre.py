import sqlite3
def criar_banco():
    try:
        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sistemas_biblioteca (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_orgao TEXT,
                municipio TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_predio TEXT,
                id_sistema INTEGER,
                FOREIGN KEY (id_sistema) REFERENCES sistemas_biblioteca(id)
            )
        """)

        banco.commit()
        banco.close()

    except Exception as erro:
        print("Erro:", erro)

def cadastrar_sistema():
    try:
        nome = input("nome do orgao: ")
        municipio = input("municipio: ")

        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        cursor.execute(
            "INSERT INTO sistemas_biblioteca (nome_orgao, municipio) VALUES (?, ?)",
            (nome, municipio)
        )

        banco.commit()
        banco.close()

        print("Sistema cadastrado!")

    except Exception as erro:
        print("Erro:", erro)

def listas_sistemas():
    try:
        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM sistemas_biblioteca")
        dados = cursor.fetchall()

        banco.close()

        if not dados:
            print("nenhum sistema cadastrado.")
        else:
            for sistema in dados:
                print(sistema)

    except Exception as erro:
        print("Erro:", erro)

def atualizar_sistema():
    try:
        id_sistema = int(input("Digite o ID do sistema: "))
        nome = input("Novo nome do órgão: ")
        municipio = input("Novo município: ")

        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        cursor.execute(
            "SELECT * FROM sistemas_biblioteca WHERE id = ?",
            (id_sistema,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            print("ID não encontrado.")
        else:
            cursor.execute("""
                UPDATE sistemas_biblioteca
                SET nome_orgao = ?, municipio = ?
                WHERE id = ?
            """, (nome, municipio, id_sistema))

            banco.commit()
            print("Sistema atualizado!")

        banco.close()

    except Exception as erro:
        print("Erro:", erro)

def excluir_sistema():
    try:
        id_sistema = int(input("Digite o ID do sistema: "))

        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        cursor.execute(
            "SELECT * FROM sistemas_biblioteca WHERE id = ?",
            (id_sistema,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            print("ID não encontrado.")
        else:
            cursor.execute(
                "DELETE FROM sistemas_biblioteca WHERE id = ?",
                (id_sistema,)
            )

            banco.commit()
            print("Sistema excluído!")

        banco.close()

    except Exception as erro:
        print("Erro:", erro)
   

   