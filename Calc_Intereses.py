def crea_tarjeta():
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

    cardData = {'nombre':cardName, 'tasa':cardInterest, 'deuda':cardDebt, 'pagos':cardPay, 'cargos':cardNewCharges}
    return cardData

def captura_nueva_deuda(cardData):
    interesMensual = cardData['tasa']/12
    cardData['deudaRecalc'] = (cardData['deuda']-cardData['pagos'])*(1+interesMensual)
    cardData['nuevaDeuda'] = cardData['deudaRecalc'] + cardData['cargos']
    return cardData

def generar_reporte(cardData):
    print("\n//////////////////////////////////////////////////////////////////////")
    print("¡Hola!\nEste es el estado de cuenta de la tarjeta {} del mes" .format(cardData['nombre']))
    print("//////////////////////////////////////////////////////////////////////\n")
    print("Deuda inicial ${} \t Interés anual {}% \t " .format(cardData['deuda'],cardData['tasa']*100))
    print("Pago realizado ${} \t Deuda recalculada ${}" .format(cardData['pagos'],cardData['deudaRecalc']))
    print("Nuevos cargos del mes ${}".format(cardData['cargos']))
    print("****** DEUDA ACTUAL ${} ******\n".format(cardData['nuevaDeuda']))

def varios_reportes(cards):
    
    for card in cards:
        generar_reporte(captura_nueva_deuda(card))

def pago_recurrente(cardData,amount):
    cardData['pagos']=amount
    cardData['cargos']=0
    contador = 0
    while cardData['deuda'] > 0:
        print("############ MES {} ############".format(contador+1))
        contador +=1
        if cardData['deuda'] < cardData['pagos']:
            cardData['pagos'] = cardData['deuda']
        
        generar_reporte(captura_nueva_deuda(cardData))
        cardData['deuda'] = cardData['nuevaDeuda']

print("******** Solo una tarjeta ********")
generar_reporte(captura_nueva_deuda(crea_tarjeta()))
print("******** Varios reportes ********")
card1=crea_tarjeta()
print("\n")
card2=crea_tarjeta()
print("\n")
card3=crea_tarjeta()
varios_reportes([card1,card2,card3])
print("******** Pago recurrente ********")
card=crea_tarjeta()
pago_recurrente(card,3200)
print("******** FIN ********\n")