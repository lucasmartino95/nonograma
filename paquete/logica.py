def comprobar(dibujo: list,
              fila: int,
              columna: int) -> bool:

    if dibujo[fila][columna] == 1:
        return True
    else:
        return False
