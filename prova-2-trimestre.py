import sqlite3


def criar_banco():
    try:
        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sistemas_biblioteca (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_orgao TEXT,
                municipio TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS unidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_predio TEXT,
                id_sistema INTEGER,
                FOREIGN KEY (id_sistema) REFERENCES sistemas_biblioteca(id)
            )
        ''')

        banco.commit()
        banco.close()

    except Exception as erro:
        print("Erro:", erro)



def cadastrar_sistema():
    try:
        nome = input("Nome do orgao: ")
        municipio = input("Municipio: ")

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


def listar_sistemas():
    try:
        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM sistemas_biblioteca")
        dados = cursor.fetchall()

        banco.close()

        if not dados:
            print("Nenhum sistema cadastrado.")
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



def cadastrar_unidade():
    try:
        nome_predio = input("Nome do prédio: ")
        id_sistema = int(input("Digite o ID do sistema: "))

        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        
        cursor.execute(
            "SELECT * FROM sistemas_biblioteca WHERE id = ?",
            (id_sistema,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            print("ID do sistema não encontrado.")
        else:
            cursor.execute(
                "INSERT INTO unidades (nome_predio, id_sistema) VALUES (?, ?)",
                (nome_predio, id_sistema)
            )

            banco.commit()
            print("Unidade cadastrada!")

        banco.close()

    except Exception as erro:
        print("Erro:", erro)


def listar_unidades():
    try:
        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM unidades")
        dados = cursor.fetchall()

        banco.close()

        if not dados:
            print("Nenhuma unidade cadastrada.")
        else:
            for unidade in dados:
                print(unidade)

    except Exception as erro:
        print("Erro:", erro)


def atualizar_unidade():
    try:
        id_unidade = int(input("Digite o ID da unidade: "))
        nome_predio = input("Novo nome do prédio: ")
        id_sistema = int(input("Digite o novo ID do sistema: "))

        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        
        cursor.execute(
            "SELECT * FROM unidades WHERE id = ?",
            (id_unidade,)
        )

        unidade = cursor.fetchone()

        if unidade is None:
            print("ID da unidade não encontrado.")
        else:

            
            cursor.execute(
                "SELECT * FROM sistemas_biblioteca WHERE id = ?",
                (id_sistema,)
            )

            sistema = cursor.fetchone()

            if sistema is None:
                print("ID do sistema não encontrado.")
            else:
                cursor.execute("""
                    UPDATE unidades
                    SET nome_predio = ?, id_sistema = ?
                    WHERE id = ?
                """, (nome_predio, id_sistema, id_unidade))

                banco.commit()
                print("Unidade atualizada!")

        banco.close()

    except Exception as erro:
        print("Erro:", erro)


def excluir_unidade():
    try:
        id_unidade = int(input("Digite o ID da unidade: "))

        banco = sqlite3.connect("biblioteca.db")
        cursor = banco.cursor()

        cursor.execute(
            "SELECT * FROM unidades WHERE id = ?",
            (id_unidade,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            print("ID da unidade não encontrado.")
        else:
            cursor.execute(
                "DELETE FROM unidades WHERE id = ?",
                (id_unidade,)
            )

            banco.commit()
            print("Unidade excluída!")

        banco.close()

    except Exception as erro:
        print("Erro:", erro)


def menu():
    try:
        while True:
            print("\n1 - Cadastrar sistema")
            print("2 - Listar sistemas")
            print("3 - Atualizar sistema")
            print("4 - Excluir sistema")
            print("5 - Cadastrar unidade")
            print("6 - Listar unidades")
            print("7 - Atualizar unidade")
            print("8 - Excluir unidade")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cadastrar_sistema()

            elif opcao == "2":
                listar_sistemas()

            elif opcao == "3":
                atualizar_sistema()

            elif opcao == "4":
                excluir_sistema()

            elif opcao == "5":
                cadastrar_unidade()

            elif opcao == "6":
                listar_unidades()

            elif opcao == "7":
                atualizar_unidade()

            elif opcao == "8":
                excluir_unidade()

            elif opcao == "0":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")

    except Exception as erro:
        print("Erro no menu:", erro)

criar_banco()
menu()