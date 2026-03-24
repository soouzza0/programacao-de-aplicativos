vagas = ["livre", "ocupado", "livre" "ocupado"]
escolha = int(input("digite um numero de 0 a 3: "))
if escolha % 2 == 0 and vagas [escolha] == "livre":
    print(f"vaga {escolha} autorizada para estacionar." ) 

else:
    print (f"{escolha} indisponivel ou fora das regras.")
    