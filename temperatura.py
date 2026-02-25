temperatura =float(input("digite a temperatura atual"))

if temperatura >= 80:
    print("PERIGO! desligando servidor por superaquecimento.")
elif temperatura >= 50:
    print("alerta ventoinhas ligadas no maximo!")
elif temperatura < 50:
    print("temperatura estavel, sistema operando normalmente.")
