def somar_carrinho(precos):
    
    total = sum(precos)
    
    if total > 500:
        
        total = total * 0.90
        
    return total


minha_lista = [150.00, 200.00, 300.00, 50.00]

valor_final = somar_carrinho(minha_lista)

print(f"O valor final a ser pago é: R$ {valor_final:.2f}")
