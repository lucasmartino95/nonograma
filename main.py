from paquete.dibujos import *
from paquete.logica import *

jugando = True

while jugando:

    print("[1] Jugar")
    print("[2] Ver ranking")
    print("[3] Salir")

    opcion = int(input("Elige una opción: "))

    match opcion:
        case 1:
            juego_activo = True
            nombre_jugador = input("Ingresa tu nombre: ")
            while juego_activo:
                mostrar_dibujo(dibujo_jugador)
                mostrar_pistas_por_fila()
                mostrar_pistas_por_columna()
                fila = int(input("Ingresa una fila: "))
                columna = int(input("Ingresa una columna: "))
                valor_ingresado = comprobar(dibujo, fila, columna)
                if valor_ingresado:
                    dibujo_jugador[fila][columna] = 1
                else:
                    #restar_vida()
                    pass
        case 2:
            pass
        case 3:
            pass
