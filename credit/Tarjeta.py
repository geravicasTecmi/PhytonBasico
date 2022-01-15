""" Módulo para realizar cálulos de tarjetas """

from ast import arg

def crea_tarjeta():

    """ Función que solicita los datos de la tarjeta y los guarda en un diccionario. """

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

    """ 
    Función que realiza los cálculos de la deuda del diccionario de la tarjet que se ingresa. 
    """

    interesMensual = cardData['tasa']/12
    cardData['deudaRecalc'] = (cardData['deuda']-cardData['pagos'])*(1+interesMensual)
    cardData['nuevaDeuda'] = cardData['deudaRecalc'] + cardData['cargos']
    return cardData

def generar_reporte(cardData):
    
    """ Función que genera un reporte del diccionario de la tarjeta """

    print("\n//////////////////////////////////////////////////////////////////////")
    print("¡Hola!\nEste es el estado de cuenta de la tarjeta {} del mes" .format(cardData['nombre']))
    print("//////////////////////////////////////////////////////////////////////\n")
    print("Deuda inicial ${} \t Interés anual {}% \t " .format(cardData['deuda'],cardData['tasa']*100))
    print("Pago realizado ${} \t Deuda recalculada ${}" .format(cardData['pagos'],cardData['deudaRecalc']))
    print("Nuevos cargos del mes ${}".format(cardData['cargos']))
    print("****** DEUDA ACTUAL ${} ******\n".format(cardData['nuevaDeuda']))

def pago_recurrente(cardData, amount):

    """
    Función que realiza la corrida de un pago recurrente hasta que la deuda se liquide.
    Requiere de ingresar una tarjeta en diccionario y una cantidad fija de pagos.
    No admite nuevos cargos cada mes.
    """

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

def pagos_distintos (cardData, list):

    """
    Función que realiza la corrida de 'n' cantidad de meses dependiendo de la cantidad de pagos que ingrese.
    Requiere de ingresar una tarjeta en diccionario y 'n' cantidades de pagos distintos.
    No admite nuevos cargos cada mes.
    """

    cardData['cargos']=0
    for arg in list:
        cardData['pagos']= int(arg)
        if cardData['deuda'] < cardData['pagos']:
            cardData['pagos'] = cardData['deuda']
        
        generar_reporte(captura_nueva_deuda(cardData))
        cardData['deuda'] = cardData['nuevaDeuda']