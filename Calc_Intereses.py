cardName = input("¿Cuál es el nombre de la tarjeta? ")
cardInterest = float(input("¿Cuál es el porcentaje de interés en decimal? (0.xx)? "))
cardDebt = int(input("¿Cuál es la deuda? (Sólo números) "))

while True:
    cardPay = int(input("¿Cuál es el pago a realizar? "))
    if cardPay>cardDebt:
        print("ERROR. No se puede pagar más que la deuda actual. Inténtalo de nuevo")
    else:
        break
cardNewCharges = int(input("¿Cuáles son los nuevos cargos? "))

interesMensual = cardInterest/12
deudaRecalculada = (cardDebt-cardPay)*(1+interesMensual)
nuevaDeuda = deudaRecalculada + cardNewCharges

print("\n///////////////////////////////////////////////////")
print("¡Hola {}!\nEste es el estado de cuenta del mes" .format(cardName))
print("///////////////////////////////////////////////////\n")
print("Deuda inicial ${} \t Interés anual {}% \t " .format(cardDebt,cardInterest*100))
print("Nuevos cargos del mes ${}".format(cardNewCharges))
print("Pago realizado ${} \t Deuda actual ${}" .format(cardPay,nuevaDeuda))