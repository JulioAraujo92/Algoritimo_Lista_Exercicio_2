peso = float(input("\nDigite peso: "))
altura = float(input("\nDigite altura: "))
imc = peso / altura**2

if imc < 20:
    print(f"\nAbaixo do peso")
elif imc <= 25:
    print(f"\nPeso normal")
elif imc <= 30:
    print(f"\nExcesso de peso")
elif imc <= 35:
    print(f"\nObesidade")
else:
    print(f"\nObesidade mórbida")
