import sqlite3

conecao = sqlite3. connect('escola.db')
cursor = conecao.cursor()

def cadastrar_professor():
    cursor.execute('''  
                    CREATE TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    materia TEXT,
                    idade_professor INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    salario REAL NOT NULL,
                    nome_da_escola TEXT,
                    endereco TEXT,
                    cidade TEXT,
                    estado TEXT
                    )
                    ''')


    nome_professor = input("digite o nome do professor: ")
    idade_professor = int(input("digite a idade do professor: "))
    materia = input("digite a materia: ")
    telefone_professor = input("digite o telefone do professor: ")
    cpf_professor = input("digite o cpf do professor: ")
    salario_professor = float(input("digite o salario:"))
    nome_da_escola = input("digite o nome da escola:")
    endereco = input("digite o seu endereco ")
    cidade = input("digite a sua cidade")
    estado = input("digite o seu estado")
    comando_inserir = (f''' INSERT INTO professores(nome,telefone,materia,idade_professor,cpf,salario,nome_da_escola,endereco,cidade,estado)                    
                       VALUES('{nome_professor}', '{telefone_professor}', '{materia}', {idade_professor}, '{cpf_professor}', {salario_professor}, '{nome_da_escola}', '{endereco}', '{cidade}', '{estado}')''')

    cursor.execute(comando_inserir)
    conecao.commit()



def listar():

    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT* FROM professores")
    todos_professores = cursor.fetchall()

    if not todos_professores:
        print("Nenhum professor cadastrado")

        print("=== Lista de Professores ===")
    else:
        for professores in todos_professores: 
            print(f"ID: {professores[0]}")
            print(f"Nome: {professores[1]}")
            print(f"Telefone: {professores[2]}")
            print(f"Materia: {professores[3]}")
            print(f"Idade: {professores[4]}")
            print(f"CPF: {professores[5]}")
            print(f"Salario: {professores[6]}")
            print(f"Escola: {professores[7]}")
            print(f"endereço: {professores[8]}")
            print(f"cidade: {professores[9]}")
            print(f"estado: {professores[10]}")
            print("-" * 30)

            conexao.close()


def atualizar_dados():
    id_professor = int(input("Digite o ID do professor: "))
    novo_nome_professor = input("Digite o novo nome d professor: ")
    novo_telefone_professor = input("Digite o novo telefone do professor: ")
    nova_materia = input("Digite a nova materia do professor: ")
    nova_idade_professor = int(input("Digite a nova idade: "))
    novo_cpf_professor = input("Digite o novo CPF: ")
    novo_salario = input("Digite o novo salário: ")
    nova_escola = input("Digite a nova escola: ")
    novo_endereco = input("digite seu novo endereco")
    nova_cidade = input("digite sua nova cidade")
    novo_estado = input("digite seu novo estado")
    comando_inserir = f'''
                    UPDATE professores
                    SET nome = '{novo_nome_professor}', telefone = '{novo_telefone_professor}', materia = '{nova_materia}',
                    idade_professor = '{nova_idade_professor}', cpf = '{novo_cpf_professor}', salario = '{novo_salario}', nome_da_escola = '{nova_escola}'
                    WHERE id = {id_professor}, endereco = '{novo_endereco}', cidade = '{nova_cidade}', 'estado = {novo_estado}', '''
    
    cursor.execute(comando_inserir)
    conecao.commit()
    print("Dados atualizados com sucesso! ")

        

def excluir_professores():

    listar()
    id_professor =int(input("digite seu id"))
    
    cursor.execute(f'''DELETE FROM professores WHERE id = {id_professor}''')
    conecao.commit()


def menu():
    opcao = 0
    while opcao != 5:
        print("\n")
        print("-------------------MENU-------------------")
        print("1- CADASTRAR PROFESSOR\n2-LISTAR PROFESSORES\n3-ATUALIZAR DADOS\n4-EXCLUIR PROFESSOR\n5-ENCERRAR PROGRAMA")
        opcao = int(input("Digite a ação a ser realizada: "))
        if opcao == 1:
            cadastrar_professor()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar_dados()
        elif opcao == 4:
            excluir_professores()
        elif opcao == 5:
            print("PROGRAMA ENCERRADO")
            break


menu()