ID = int(input("qual o seu id? "))
temperatura = float(input("qual a temperatura ?"))
tempo_de_uso = float(input("qual o seu tempo de uso?" ))
if (ID % 3 == 0) and (temperatura >40 or tempo_de_uso >8):
    print(f"funcionario{ID} voce foi escalado para a manutencao preventiva hoje")
else:
    print(f"funcionario {ID} sua maquina opera dentro dos padroes normais")