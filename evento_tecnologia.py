idade = int(input("digite sua idade"))
saldo = float(input("digite seu saldo"))

if idade >= 18 and saldo >= 50.00:
    print("acesso autorizado! bem-vindo")
elif idade <18 and saldo < 50.00:
    print("infelizmente voce nao cumpre os requisitos de entrada")
elif idade < 18 and saldo >= 50.00:
    print("acesso negado!")
elif idade >= 18 and saldo < 50.00:
    print("acesso negado!")