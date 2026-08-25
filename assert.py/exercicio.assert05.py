def calcular_frete(valor_compra):
    if valor_compra >= 200:
        return 0
    elif valor_compra >= 100:
        return 10
    return 20

assert calcular_frete(74) == 20 
assert calcular_frete(100) == 10
assert calcular_frete(184) == 10
assert calcular_frete(200) == 0
assert calcular_frete(284) == 0

