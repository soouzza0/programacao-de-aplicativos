import sqlite3

conecao = sqlite3. connect('escola.db')
cursor = conecao.cursor()

def cadastrar_aluno():
        
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS alunos(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    turma TEXT, 
                    idade_aluno INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    id_professor INTENGER,
                    FOREIGN KEY (id_professor)
                    REFERENCES professores(id))''')
    nome_aluno = input("digite o nome do aluno: ")
    idade_aluno = int(input("digite a idade do aluno: "))
    turma_aluno = input("digite a turma: ")
    telefone_aluno = input("digite o telefone do aluno")
    cpf_aluno = input("digite o cpf do aluno ")
    id_professor = int(input("digite o id do professor "))
    comando_inserir = (f''' INSERT INTO alunos(nome,idade_aluno,turma,telefone,cpf,id_professor)
                    VALUES('{nome_aluno}', '{idade_aluno}', '{turma_aluno}', '{telefone_aluno}', '{cpf_aluno}',{id_professor})''')

    cursor.execute(comando_inserir)
    conecao.commit()

def listar():

    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT* FROM alunos")
    todos_alunos = cursor.fetchall()

    if not todos_alunos:
        print("Nenhum aluno cadastrado")

        print("=== Lista de alunos ===")
    else:
        for aluno in todos_alunos: 
            print(f"ID: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Telefone: {aluno[2]}")
            print(f"Turma: {aluno[3]}")
            print(f"Idade: {aluno[4]}")
            print(f"CPF: {aluno[5]}")
            print(f"Professor: {aluno[6]}")
            print("-" * 30)

            conexao.close()

def buscar():
    id_aluno = int(input("Digite o id do aluno: "))
    cursor.execute(f"SELECT * FROM alunos WHERE ID = {id_aluno}")

    aluno = cursor.fetchone()
    if aluno:
        print("Aluno encontrado ")
        print(aluno)

    else:
        print("Aluno não encontrado")


def atualizar():
    id_aluno = int(input("Digite o id do aluno: "))
    novo_nome = input("Digite o novo nome: ")
    novo_telefone = input("Digite o novo telefone: ")
    nova_turma = input("Digite a nova turma: ")
    nova_idade = int(input("Digite a nova idade: "))
    novo_cpf = input("Digite o novo CPF: ")
    novo_professor = int(input("digite o id do novo professor: "))
    cursor.execute(f'''
                   UPDATE alunos
                    SET nome = '{novo_nome}', telefone = '{novo_telefone}',turma = '{nova_turma}', idade_aluno = {nova_idade}, cpf = '{novo_cpf}',id_professor = {novo_professor} WHERE id = {id_aluno}''')
    
    conecao.commit()

    print("Dados atualizados com sucesso! ")


def remover():
    id_aluno = int(input("Digite o ID do aluno que deseja remover: "))
    cursor.execute(
        "DELETE FROM alunos WHERE id = ?", (id_aluno,)
    )

    conecao.commit()
    if cursor.rowcount > 0 :
        print("Aluno removido com sucesso.")
    else:
        print("Nenhum aluno encontrado com esse ID. ")

opcao_while = 0
while True:
    print("1 - CADASTRAR ALUNO\n2 - LISTAR ALUNOS\n3 - BUSCAR ALUNO\n4 - ATUALIZAR DADOS\n5 - EXCLUIR CADASTRO\n6 - FECHAR PROGRAMA ")
    opcao_while = int(input("Qual ação deseja realizar: "))
    if opcao_while == 1:
        cadastrar_aluno()
    elif opcao_while == 2:
        listar()
    elif opcao_while == 3:
        buscar()
    elif opcao_while == 4:
        atualizar()
    elif opcao_while == 5:
        remover()
    elif opcao_while == 6:
        conecao.close()
        break