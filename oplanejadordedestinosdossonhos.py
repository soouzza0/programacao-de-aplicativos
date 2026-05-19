def criar_arquivo():
    open('viagens.txt', 'w').close()
    print("Arquivo Recriado! ")
def adicionar():
    lugar = input("Digite um lugar dos seus sonhos: ")
    with open('viagens.txt', 'a') as viagens:
        viagens.write(lugar + '\n')
        print("Destino adicionado! ")

def verificar():
    with open('viagens.txt', 'r') as viagens:
        lugares = viagens.readlines()
        i = 0
        for lugar in lugares:
            print(f"\n{i} - {lugar.strip()}")
            i += 1

def atualizar():
    verificar()
    idx = int(input("Digite o ID do lugar que você deseja alterar: "))
    novo_lugar = input("Digite o novo lugar: ")
    with open('viagens.txt', 'r') as viagens:
        linhas = viagens.readlines()
    linhas[idx] = novo_lugar + '\n'
    with open('viagens.txt', 'w') as viagens:
        viagens.writelines(linhas)
    print("Aluno atualizado! ")

def deletar():
    verificar()
    idx = int(input("Digite o ID do lugar que você deseja deletar: "))

    with open('viagens.txt', 'r') as viagens:
        linhas = viagens.readlines()
    
    del linhas[idx]

    with open('viagens.txt', 'w') as viagens:
        viagens.writelines(linhas)
    print("Aluno removido ")
opcao = 0
while opcao != "5":
    print("\n1-adicionar, \n2-verificar, \n3-editar, \n4-excluir, \n5-sair, \n6-Recriar arquivo.")
    opcao = input("Defina a ação: ")

    if opcao == "1": 
        adicionar()
    elif opcao == "2":
        verificar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        deletar()
    elif opcao == "6":
        criar_arquivo()
print("Fim da operação! ")