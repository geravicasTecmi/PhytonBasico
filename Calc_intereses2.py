from credit.Tarjeta import captura_nueva_deuda, crea_tarjeta, generar_reporte, pago_recurrente, pagos_distintos
from credit.User import varios_reportes


print("Selecciona una opción:")
print("1. Generar sólo una tarjeta.")
print("2. Generar varios reportes.")
print("3. Corrida de pagos fijos.")
print("4. Corrida de pagos variados.")
eleccion = int(input())

if eleccion == 1:
    generar_reporte(captura_nueva_deuda(crea_tarjeta()))

elif eleccion == 2:
    repetir = int(input("¿Cuántas tarjetas deseas ingresar? "))
    cardo = list()
    for cant in range(repetir):
        cardo.append(crea_tarjeta())
        print("\n")
    varios_reportes(cardo)

elif eleccion == 3:
    card = crea_tarjeta()
    amount = int(input("¿Cuál será el pago fijo que realizarás? "))
    pago_recurrente(card, amount)

elif eleccion == 4:
    card = crea_tarjeta()
    repetir = int(input("¿Cuántos pagos variados realizarás? "))
    payments = list()
    count = 0
    for cant in range(repetir):
        payments.append(input("Ingresa el pago {} " .format(count+1)))
        count +=1
    pagos_distintos(card,payments)

else:
    print("Opción seleccionada no válida. Fin del programa.")