from movimientos import movimientos_validos_gato, movimientos_validos_raton, deltas_gato, deltas_raton, deltas_manual

# Se calcula la distancia de Manhattan
def distancia_manhattan(p1, p2):
    return abs(p1[0]- p2[0]) + abs(p1[1] - p2[1])

# Se evaluan los estados de acuerdo a la distancia de manhattan para el gato y el raton
def evaluar_estado_raton(pos_gato, pos_raton):
    return distancia_manhattan(pos_gato, pos_raton)

def minimax_raton (pos_gato, pos_raton, tablero, profundidad, es_turno_raton):

    # El gato atrapo al raton -> peor caso para el raton
    if pos_gato == pos_raton:
        return -float("inf")
    
    # La profundidad va a 0 -> se vuelve a evaluar el estado
    if profundidad == 0:
        return evaluar_estado_raton(pos_gato, pos_raton)
    
    if es_turno_raton:

        # El raton elije la distancia que maximiza la distancia con el gato
        mejor = -float("inf")

        for mov_r in movimientos_validos_raton(pos_raton, tablero):
            valor = minimax_raton(pos_gato, mov_r, tablero, profundidad-1, False)

            if valor > mejor:
                mejor = valor
        
        return mejor
    
    else:

        # El gato elije la distancia que minimiza la distancia con el raton
        peor = float("inf")

        for mov_g in movimientos_validos_gato(pos_gato, tablero):
            valor = minimax_raton(mov_g, pos_raton, tablero, profundidad-1, True)

            if valor < peor:
                peor = valor

        return peor
    
def mejor_jugada_raton (pos_gato, pos_raton, tablero, profundidad):
    
    mejor_valor = -float("inf")
    
    # Por si no haya ninguna jugada mejor
    mejor_mov = pos_raton 

    for mov in movimientos_validos_raton(pos_raton, tablero):

        valor = minimax_raton(pos_gato, mov, tablero, profundidad-1, False)

        # Para que guarde el movimiento que mas distancia le da
        if valor > mejor_valor:
            
            mejor_valor = valor
            mejor_mov = mov 

    return mejor_mov