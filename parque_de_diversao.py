nome = input("digite seu nome")

altura = float(input("digite sua altura:"))

if altura <1.50:
    print("desculpe, voce nao tem altura minima" , nome)
elif altura >= 1.50:
    print("aceso liberado ! divirta-se", nome)