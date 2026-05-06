def analisar_vendas(nome, lista_vendas, meta_mensal):
   
    total = 0
    for venda in lista_vendas:
        total = total + venda
    
    media = total / len(lista_vendas)
    

    if media >= meta_mensal:
        status = "bateu"
    else:
        status = "não bateu"
    

    return f"O vendedor {nome} teve média de {media} e {status} a meta"

vendedor = "Carlos"
vendas = [1200, 1500, 1100, 1900]
meta = 1400

resultado = analisar_vendas(vendedor, vendas, meta)
print(resultado)
