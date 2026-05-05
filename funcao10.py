def eh_par(numero):
    # O operador % retorna o resto da divisão. Se for 0, o número é par.
    if numero % 2 == 0:
        return True
    else:
        return False

# --- Programa Principal ---

# Pede um número ao usuário e converte para inteiro
num = int(input("Digite um número: "))

# Verifica o retorno da função e exibe a mensagem correspondente
if eh_par(num):
    print("Este número é par")
else:
    print("Este número é ímpar")
