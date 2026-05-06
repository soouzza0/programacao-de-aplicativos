def gerar_relatorio_saude(nome, peso, altura, idade):
    
    imc = peso / (altura * altura)
    
  
    if imc < 18.5:
        categoria = "Baixo peso"
    elif imc <= 24.9:
        categoria = "Normal"
    elif imc <= 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    

    return f"Olá {nome}, você tem {idade} anos. Seu IMC é {imc:.2f} e sua categoria é: {categoria}."


nome_usuario = input("Digite o nome: ")
peso_usuario = float(input("Digite o peso (kg): "))
altura_usuario = float(input("Digite a altura (ex: 1.75): "))
idade_usuario = int(input("Digite a idade: "))

relatorio = gerar_relatorio_saude(nome_usuario, peso_usuario, altura_usuario, idade_usuario)
print(relatorio)
