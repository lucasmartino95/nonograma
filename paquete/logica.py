total_vidas = 3

def comprobar(dibujo: list,
              fila: int,
              columna: int) -> bool:

    if dibujo[fila][columna] == 1:
        return True
    else:
        return False
    

def restar_vida(total_vidas: int) -> None:

    total_vidas -= 1

    return total_vidas


# Agregar parámetro "mensaje"
def gano(dibujo: list,
         dibujo_jugador: list) -> bool:
    
    contador = 0
    contador_jugador = 0
    

    # Modularizar los búcles for, creando una función
    # que recorra una matriz
    for i in range(len(dibujo)):
        for j in range(len(dibujo[i])):
            if dibujo[i][j] == 1:
                contador += 1


    for i in range(len(dibujo_jugador)):
        for j in range(len(dibujo_jugador[i])):
            if dibujo_jugador[i][j] == 1:
                contador_jugador += 1
                
    if contador == contador_jugador:
        return True
    else:
        return False


def limpiar_dibujo(dibujo_jugador: list) -> None:

    for i in range(len(dibujo_jugador)):
        for j in range(len(dibujo_jugador[i])):
            dibujo_jugador[i][j] = 0