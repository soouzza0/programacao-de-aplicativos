def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    
    if (nota_teste > 80 and anos_xp > 2) or possui_certificacao == True:
        return True
    else:
        return False


nota = float(input("Digite a nota do teste (0-100): "))
xp = int(input("Digite os anos de experiência: "))
certificacao_input = input("Possui certificação? (sim/nao): ").lower()


tem_certificacao = certificacao_input == "sim"


if verificar_aprovacao(nota, xp, tem_certificacao):
    print("Resultado: Contratar")
else:
    print("Resultado: Descartar")
