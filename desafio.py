saldo = 1000

print("1-deposito")
print("2-saque")
print("3-extrato")

operacao = int(input("qual operaçao voce irá realizar:"))

if operacao == "1":
    deposito = float(input("qual o valor que voce quer depositar: "))
    valorfinal = saldo + deposito

if operacao == "2":
    saque = float(input("qual o valor do saque?  R$:"))
    valorfinal = saldo - saque 

if operacao == "3":
    valorfinal = saldo
    print("seu saldo agora é R$:" , valorfinal)