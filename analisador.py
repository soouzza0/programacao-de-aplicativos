def contar_caracteres(texto):
    return len(texto)

# Programa principal
usuario = input("Digite o nome de usuário: ")

if contar_caracteres(usuario) < 5:
    print("Nome de usuário muito curto")
else:
    print("Nome aceito")
