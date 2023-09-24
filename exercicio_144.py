saldomedio = float(input("\nDigite saldo médio: "))
credito = 0

if saldomedio < 501:
    credito = 0
elif saldomedio < 1001:
    credito = saldomedio * 0.30
elif saldomedio < 3001:
    credito = saldomedio * 0.40
elif saldomedio < 3001:
    credito = saldomedio * 0.4
else:
    credito = saldomedio * 0.5

if credito == 0:
    print(f"\nComo seu sando era de: {saldomedio} você não terá nenhum crédito\n")
else:
    print(f"\nComo seu sando era de: {saldomedio} seu crédito será de {credito}\n")