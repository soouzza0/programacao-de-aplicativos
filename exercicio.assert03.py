def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


assert calcular_desconto(100, 0) == 100
assert calcular_desconto(30,10) == 27
assert calcular_desconto(20,50) == 10
assert calcular_desconto(70,100) == 0
assert calcular_desconto(120.45,0) == 120.45