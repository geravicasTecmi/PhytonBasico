from credit.Tarjeta import captura_nueva_deuda, generar_reporte


def varios_reportes(cards):

    """ Función que genera múltiples reportes de 'n' tarjetas enviadas """

    for card in cards:
        generar_reporte(captura_nueva_deuda(card))