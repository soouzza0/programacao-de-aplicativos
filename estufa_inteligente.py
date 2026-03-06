print("")
print("---estufa inteligente---")
print("")

temperatura = float(input("qual a temperatura atual?"))

if temperatura <= 30:
    print("clima estável")

elif temperatura > 30:
    print("alerta de calor!")

    print("")

    unidade = float(input("qual a unidade atual: "))
    
    if umidade < 40:
        print("açao: ligar apenas ventiladores")

    else:
        print("açao ligar irrigaçao!")

print("")
print("-" * 26)