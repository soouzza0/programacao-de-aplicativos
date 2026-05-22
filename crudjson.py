import json #serve para o codigo nao dar erro, e tambem serve para  codigo ser lido e escrevido 
import os #ele permite que navegue pelas pastas e arquivos 

BANCO_DADOS = 'alunos.json' # cria uma variavel e armazena nela o nome de um arquivo 

def cadastrar(): #criar uma funçao
    print("\n--- Novo Cadastro ---") #mostrar a mensagem exibida dentro do print
    

    if os.path.exists(BANCO_DADOS): #whith open serve para abrir o arquivo
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # serve para ler os dados 
            alunos = json.load(f) #aqui ele ta lendo dados do arquivo 
    else: #serve para executar um bloco de codigo alternativo quando a condiçao do comando for falsa
        alunos = [] #serve como banco de dados dos alunos cadastrados 

    novo_aluno = { #guardar dados ou descrever carcteristicas de um unico objeto ou pessoa 
        "nome": input("Nome: "), #exibe o texto na tela de espera 
        "telefone": input("Telefone: "), #salva o texto digitado é guardado na chave 
        "turma": input("Turma: "), #salva o numero digitado como texto na chave 
        "idade": int(input("Idade: ")), #transforma o numero digitado em um numero inteiro 
        "cpf": input("CPF: ") #exibe o texto digitado na chave 
    }
    
    

    alunos.append(novo_aluno) # salva o aluno no banco de dados 

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: #  2. Adiciona à lista da memória e abre o arquivo no modo 'w' para salvar
        json.dump(alunos, f, indent=4, ensure_ascii=False) #salva a lista "" representada pela variavel F, permite salvar acentos e caracteres especiais 
        
    print("Aluno cadastrado com sucesso!") #exibe uma mensagem na tela informando que o cadrasto foi concluido 

def listar(): # cria uma funçao chama listar responsavel por exiber os alunos salvos 
    print("\n--- Lista de Alunos ---") #emprime um cabeçalho no console 


    if os.path.exists(BANCO_DADOS): #verifica se o arquivo difinido na variavel realmente existe 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo do banco de dados em modo leitura, e fecha o arquivo automaticamente quando termina 
            alunos = json.load(f) # le o arquivo json eo transforma de volta em uma lista 
    else:
        alunos = [] #cria uma lista vazia para evitar erros nas proximas linhas 

    if not alunos: #verifica se a lista esta vazia 
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos: #cria um laço que passa aluno por aluno da lista 
        print(f"ID: {aluno['id']} | Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") #exibe na tela os dados informados de cada aluno do laço 

def atualizar():
    print("\n--- Atualizar Aluno ---") #imprime o cabeçalho da funcionalidade de alteraçoes de dados 
    if not os.path.exists(BANCO_DADOS): # verifica se o arquivo do banco de dados existe 
        print("Nenhum aluno cadastrado no sistema.") #avisa que nao tem nenhum aluno cadastrado no sistema 
        return #intenrompe ou encerra a funçao 
    
  

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #Abre o arquivo do banco de dados em modo de leitura ('r') com suporte a acentos (utf-8). O with garante que o arquivo seja fechado sozinho depois.
        alunos = json.load(f)
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) 
    
    for aluno in alunos:
        if aluno['cpf'] == cpf_busca:
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']

           

            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("Dados atualizados com sucesso!")
            return
            
    print("Aluno não encontrado.")

def excluir():
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))


    nova_lista = [a for a in alunos if a['id'] != id_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

        # --- MENU PRINCIPAL ---

def menu():
    # Cria o arquivo com uma lista vazia se ele não existir ao iniciar o programa
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu() #chamando a funçao do def