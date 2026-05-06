def esta_na_lista(lista, busca):
    for item in lista:
        if item == busca:
            return "Encontrado!"
    return "Não disponível"


ferramentas = ["Martelo", "Chave de fenda", "Alicate", "Serrote"]

resultado = esta_na_lista(ferramentas, "Alicate")
print(resultado)
