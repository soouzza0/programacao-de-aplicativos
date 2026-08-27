def calcular_desconto(preco, percentual):
 	return preco - percentual

 # Escreva seus testes aqui.

assert calcular_desconto(100,10) == 90
assert calcular_desconto(200,20) == 180
