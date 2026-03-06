print("")
print("---seguranca no chao da fabrica---")
print("")

curso = input("voce conclui o curso de segurança?  (s/n): ")

if curso =="s":
    instrutor = input("o instrutor esta presente na sala?  (s/n): ")

    print("")

    if instrutor == "s":
        print("acesso liberado: operção iniciada")

    else:
        print("aguarde o instrutor para ligar a maquina")

else:
    print("acesso negado: faça o treinamento primeiro")

print("")
print("-" *  35)