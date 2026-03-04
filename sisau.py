usuario = input("usuario:") 
senha = int(input("senha:"))
if usuario == ("admin" or "root") and senha == 12345:
    print("acesso liberado")
else:
    print("acesso negado")