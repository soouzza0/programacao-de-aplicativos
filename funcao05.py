vida = 100

def sofrer_dano(valor_dano):
    global vida
    vida = vida - valor_dano
    return vida

# Programa principal
while vida > 0:
    print(f"Vida atual: {vida}")
    dano = int(input("Quanto de dano o monstro causou? "))
    sofrer_dano(dano)

print("Game Over")
