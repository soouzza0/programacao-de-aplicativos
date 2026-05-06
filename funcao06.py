def converter_km_para_ms(kmh):
    return kmh / 3.6

try:
    v = float(input("Velocidade atual (km/h): "))

    if v > 80:
        
        print(f"Alerta: {v} km/h equivale a {converter_km_para_ms(v):.1f} m/s.")
        print("Reduza a velocidade!")
    else:
        print("Velocidade segura.")
except ValueError:
    print("Por favor, digite apenas números.")
