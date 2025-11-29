def cargar_ranking(nombre: str) -> None:

    with open("ranking.csv", "a") as archivo:
        archivo.write(f"{nombre}, 1\n")


def leer_ranking() -> None:
    ranking = []
    with open("ranking.csv", "r") as archivo:
        ranking.append(archivo.readlines())

    lista = []
    for i in range(len(ranking)):
        for j in range(len(ranking[i])):
            lista.append(ranking[i][j].strip())


    print("Los 3 mejores jugadores")
    for i in range(3):
        print(lista[i], end="\n")