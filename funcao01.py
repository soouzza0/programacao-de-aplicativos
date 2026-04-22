def avaliar_desempenho(nota):
    if nota >= 9:
        return "excelente"
    elif nota >= 7:
        return "bom"
    elif nota > 5:
        return "regular"
    else: return "insuficiente"

nota_usuario = int(input("digite a sua nota: "))
mensagem = avaliar_desempenho(nota_usuario)

print(mensagem)