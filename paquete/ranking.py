def cargar_ranking(nombre: str) -> None:

    with open("ranking.csv", "a") as archivo:
        archivo.write(f"{nombre}, 1\n")
