def calcular_area(largura, comprimento):
    return largura * comprimento

contador = 1
while contador <= 3:
    print(f"\n--- Terreno {contador} ---")
    l = float(input("Largura (m): "))
    c = float(input("Comprimento (m): "))
    
    area = calcular_area(l, c)
    print(f"A área deste terreno é: {area:.2f} m²")
    
    contador += 1
