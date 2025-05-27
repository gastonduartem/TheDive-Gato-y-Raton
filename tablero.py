<<<<<<< HEAD
import random

=======
>>>>>>> origin/main
def imprimir_tablero(tablero):
    for fila in tablero:
        print("+--------" * len(fila) + "+")
        for celda in fila:
            print(f"|  {celda:^5} ", end="")
        print("|")
<<<<<<< HEAD
    print("+--------" * len(tablero[0]) + "+")

def colocar_elementos_aleatorios(tablero, simbolo, cantidad):
    # Se lee la cantidad de filas y columnas
    filas_totales, columnas_totales = len(tablero), len(tablero[0])

    # Se almacena las posiciones ya ocupadas para evitar duplicados con la funcion set
    posiciones_usadas = set()

    while len(posiciones_usadas) < cantidad:
        columnas = random.randrange(filas_totales)
        filas = random.randrange(columnas_totales)

        if tablero[columnas][filas] == " ":
            tablero[columnas][filas] = simbolo
            posiciones_usadas.add((columnas, filas))
    
    return posiciones_usadas
=======
    print("+--------" * len(tablero[0]) + "+")
>>>>>>> origin/main
