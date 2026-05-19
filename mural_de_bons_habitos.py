def criar_mural():
    open('mural_habitos.txt', 'w').close
    print("\nMural de bons hábitos criados! ")

def adicionar_habito():
    habito = input("\nDigite um bom hábito para adicionar: ")
    with open('mural_habitos.txt', 'a') as mural:
        mural.write(habito + "\n")
        print("Hábito adicionado com sucesso!\n ")

def listagem():
    print("Hábitos adicionados: ")
    with open('mural_habitos.txt', 'r') as mural:
        habitos = mural.readlines()
        i = 0
        for habito in habitos:
            print(f"{i} - {habito.strip()}\n")
            i += 1

def substituir_habito():
    listagem()
    idx = int(input("Número do hábito a ser substituido: "))
    subs = input("Novo hábito: ")
    with open("mural_habitos.txt", 'r') as mural:
        linhas = mural.readlines()
    linhas[idx] = subs + '\n'
    with open("mural_habitos.txt",'w') as mural:
        mural.writelines(linhas)
    print("Hábito susbtituído! ")

def excluir_habito():
    listagem()
    idx = int(input("Número do hábito a ser excluido: "))
    with open("mural_habitos.txt", 'r') as mural:
        linhas = mural.readlines()
    del linhas[idx]
    with open("mural_habitos.txt", 'w') as mural:
        mural.writelines(linhas)
    print("Hábito excluido. ")

while True:
    print(" 1 - Adicionar Hábito\n 2 - Listar Hábitos\n 3 - Substituir Hábitos\n 4 - Excluir Hábito\n 5 - Finalizar programa\n 6 - Criar arquivo\n")
    opcao = int(input("Operação: "))

    if opcao == 1:
        adicionar_habito()
    elif opcao == 2:
        listagem()
    elif opcao == 3:
        substituir_habito()
    elif opcao == 4:
        excluir_habito()
    elif opcao == 5:
        break
    elif opcao == 6:
        criar_mural
print("Programa encerrado.")
        