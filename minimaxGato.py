from movimientos import movimientos_validos_gato, movimientos_validos_raton, deltas_gato, deltas_raton, deltas_manual

# Se calcula la distancia de Manhattan
def distancia_manhattan(p1, p2):
    return abs(p1[0]- p2[0]) + abs(p1[1] - p2[1])

# Se evaluan los estados de acuerdo a la distancia de manhattan para el gato y el raton
def evaluar_estado_gato(pos_gato, pos_raton):
    return -distancia_manhattan(pos_gato, pos_raton)

def minimax_gato(pos_gato, pos_raton, tablero, profundidad, es_turno_gato, quesos_restantes, total_quesos):

    # Si el gato atrapa al raton -> victoria del gato
    if pos_gato == pos_raton:
        return float("inf")
    
     # La profundidad va a 0 -> se vuelve a evaluar el estado
    if profundidad == 0:
        return evaluar_estado_gato(pos_gato, pos_raton)
    
    if es_turno_gato:
        
        # Turno del gato, quiere maximizar la distancia (acercarse)
        mejor = -float("inf")

        for mov_g in movimientos_validos_gato(pos_gato, tablero):

            valor = minimax_gato(mov_g, pos_raton, tablero, profundidad-1, False, quesos_restantes, total_quesos)

            if valor > mejor:
                mejor = valor

        return mejor
    
    else:

        #Turno del raton, intenta minimizar la distancia (alejarse)
        peor = float("inf")

        for mov_r in movimientos_validos_raton(pos_raton, tablero):
            
            valor = minimax_gato(pos_gato, mov_r, tablero, profundidad-1, True, quesos_restantes, total_quesos)

            if valor < peor:
                peor = valor

        return peor

def mejor_jugada_gato (pos_gato, pos_raton, tablero, profundidad, quesos_restantes, total_quesos):

    mejor_valor = -float("inf")

    # Por si no haya un mejor movimiento
    mejor_mov = pos_gato 

    for mov in movimientos_validos_gato(pos_gato, tablero):

        # Simula mover al gato y luego es el turno del raton
        valor = minimax_gato(mov, pos_raton, tablero, profundidad-1, False, quesos_restantes, total_quesos)

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov

    return mejor_mov