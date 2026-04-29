def senha_valida(senha):
    return len(senha) >= 6

senha = ""
while not senha_valida(senha):
    senha = input("Digite uma senha (mínimo 6 caracteres): ")

print("Senha cadastrada com sucesso!")
