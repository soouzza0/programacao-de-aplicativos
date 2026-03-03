idade = int(input("qual a sua idade:"))
ingresso = input("possui o ingresso ? (sim/nao): ")
convite = input("é convidado ? (sim/nao): ")
if (idade >= 18 and ingresso == "sim") or convite == "sim":
    print("entrada permitida, bem vindo! ")
else:
    print("entrada negada.")