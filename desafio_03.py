codigo = int(input("digite o codigo do drone: "))
autorizacao = input("o drone possui autorizacao da torre? (s/n)")

if codigo == 999 or autorizacao == "s":
    bateria = int(input("qual o nivel da bateria?: (0 a 100): "))
    clima = input("como esta o clima? (ensolarado/chuvoso): ")
    vento = int(input("qual a velocidade do vento? (km/h): "))

#regra 01
    if bateria < 10:
        print("")
        print("pouso autorizado imediatamente por seguranca!")

#regra 02
    elif bateria >= 10 and (clima == "ensolarado" and vento < 30) or (clima == "chuvoso" and vento < 10):
        print("POUSO AUTORIZADO: iniciando descida.")

    else:
        print("POUSO NEGADO: condições meteorologicas perigosas. aguardando em órbita.")


else:
    print("ERRO 01: drone nao identificado. retornando á base.")