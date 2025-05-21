def imprimir_tablero(tablero):
    for fila in tablero:
        print("+--------" * len(fila) + "+")
        for celda in fila:
            print(f"|  {celda:^5} ", end="")
        print("|")
    print("+--------" * len(tablero[0]) + "+")