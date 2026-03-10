# Programa para controle da esteira de garrafas

garrafas = int(input("Digite o número total de garrafas que já passaram pela esteira hoje: "))

# Verifica limpeza (múltiplos de 500)
if garrafas % 500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!")

# Verifica controle de qualidade (múltiplos de 100)
if garrafas % 100 == 0:
    print("CONTROLE DE QUALIDADE: Verificar garrafa.")

# Caso não seja nenhum dos dois
if garrafas % 500 != 0 and garrafas % 100 != 0:
    print(f"Produção em dia. Garrafa número {garrafas} processada.")