# Pedindo os dados
id_usuario = int(input("Digite o ID do usuário: "))
valor_compra = float(input("Digite o valor da compra: "))

# Verificando a regra
if id_usuario % 2 == 0 and valor_compra > 500:
    print(f"Parabéns, usuário {id_usuario}! Você ganhou um cupom para sua compra de R$ {valor_compra}.")
else:
    print(f"Obrigado pela compra, usuário {id_usuario}. Continue acompanhando nossas promoções!")
