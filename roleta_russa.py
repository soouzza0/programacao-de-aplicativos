senha_acesso = (input(" \n digite sua senha:"))
tentativas = int(input("digite o numero de tentativas:"))
token = input("possui token? (s/n):")

senha = "admin123"

if senha_acesso == senha and tentativas %3 == 0 or token == "s":
    print(f"tentativa nº {tentativas}: ACESSO CONCEDIDO.")

else:
    print(f"tentaviva nº {tentativas}: ACESSO BLOQUEADO POR PROTOCOLO.")
