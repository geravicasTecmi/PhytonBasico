cardName = input("¿Cuál es el nombre de la tarjeta? ")
cardInterest = input("¿Cuál es el porcentaje de interés en decimal? (0.xx)? ")
cardDebt = input("¿Cuál es la deuda? (Sólo números) ")
cardPay = input("¿Cuál es el pago a realizar? ")
cardNewCharges = input("¿Cuáles son los nuevos cargos? ")

cardInterest = float(cardInterest)
cardDebt = int(cardDebt)
cardPay = int(cardPay)
cardNewCharges = int(cardNewCharges)

interesMensual = cardInterest/12
deudaRecalculada = (cardDebt-cardPay)*(1+interesMensual)
nuevaDeuda = deudaRecalculada + cardNewCharges

print("\n///////////////////////////////////////////////////")
print("¡Hola {}!\nEste es el estado de cuenta del mes" .format(cardName))
print("///////////////////////////////////////////////////\n")
print("Deuda inicial ${} \t Interés anual {}% \t " .format(cardDebt,cardInterest*100))
print("Nuevos cargos del mes ${}".format(cardNewCharges))
print("Pago realizado ${} \t Deuda actual ${}" .format(cardPay,nuevaDeuda))