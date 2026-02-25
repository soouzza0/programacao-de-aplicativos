nome = input("digite seu nome")

ataque = int(input("digite seu ataque"))
defesa = int(input("digite sua defesa"))


dano = ataque - defesa

if dano <= 0:
    print(" o vilao bloqueou o ataque")
elif dano >= 0:
    print(" ataque critico! voce causou dano ao vilao:" , dano)