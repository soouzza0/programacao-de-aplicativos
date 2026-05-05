def somar_carrinho(precos):
    # Calcula a soma total da lista de preços
    total = sum(precos)
    
    # Aplica desconto de 10% se o total for maior que R$ 500,00
    if total > 500:
        total = total * 0.90
        
    return total

# --- Programa Principal ---

# Definindo uma lista de compras (preços dos produtos)
minha_lista = [150.00, 200.00, 300.00, 50.00]

# Chamando a função e armazenando o resultado
valor_final = somar_carrinho(minha_lista)

# Exibindo o valor que o cliente deve pagar
print(f"O valor final a ser pago é: R$ {valor_final:.2f}")
