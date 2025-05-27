from movimientos import movimientos_validos_gato, movimientos_validos_raton, deltas_gato, deltas_raton, deltas_manual

<<<<<<< HEAD
# Queso premio

=======
>>>>>>> origin/main
# Se calcula la distancia de Manhattan
def distancia_manhattan(p1, p2):
    return abs(p1[0]- p2[0]) + abs(p1[1] - p2[1])

# Se evaluan los estados de acuerdo a la distancia de manhattan para el gato y el raton
<<<<<<< HEAD
def evaluar_estado_raton(pos_gato, pos_raton, quesos_restantes, total_quesos):

      # El gato atrapo al raton -> peor caso para el raton
    if pos_gato == pos_raton:
        return -float("inf")

    dist_gato = distancia_manhattan(pos_gato, pos_raton)
    if dist_gato <= 2:
        return dist_gato * 10000
    
    # Calculo de cuantos quesos ya comio
    quesos_comidos = total_quesos - len(quesos_restantes)

    if quesos_restantes:
        dist_queso = min(
            distancia_manhattan(pos_raton, queso)
            for queso in quesos_restantes
        )
    else:
        dist_queso = 0
    
    return quesos_comidos * 5000 - dist_queso

def minimax_raton (pos_gato, pos_raton, tablero, profundidad, es_turno_raton, quesos_restantes, total_quesos):

  
    # La profundidad va a 0 -> se vuelve a evaluar el estado
    if profundidad == 0:
        return evaluar_estado_raton(pos_gato, pos_raton, quesos_restantes, total_quesos)
    
    if not quesos_restantes:
        return float("inf")
    
=======
def evaluar_estado_raton(pos_gato, pos_raton):
    return distancia_manhattan(pos_gato, pos_raton)

def minimax_raton (pos_gato, pos_raton, tablero, profundidad, es_turno_raton):

    # El gato atrapo al raton -> peor caso para el raton
    if pos_gato == pos_raton:
        return -float("inf")
    
    # La profundidad va a 0 -> se vuelve a evaluar el estado
    if profundidad == 0:
        return evaluar_estado_raton(pos_gato, pos_raton)
>>>>>>> origin/main
    
    if es_turno_raton:

        # El raton elije la distancia que maximiza la distancia con el gato
        mejor = -float("inf")

        for mov_r in movimientos_validos_raton(pos_raton, tablero):
<<<<<<< HEAD

            nuevos_quesos = quesos_restantes.copy()

            if mov_r in nuevos_quesos:
                nuevos_quesos.remove(mov_r)

            valor = minimax_raton(pos_gato, mov_r, tablero, profundidad-1, False, nuevos_quesos, total_quesos)
=======
            valor = minimax_raton(pos_gato, mov_r, tablero, profundidad-1, False)
>>>>>>> origin/main

            if valor > mejor:
                mejor = valor
        
        return mejor
    
    else:

        # El gato elije la distancia que minimiza la distancia con el raton
        peor = float("inf")

        for mov_g in movimientos_validos_gato(pos_gato, tablero):
<<<<<<< HEAD
            valor = minimax_raton(mov_g, pos_raton, tablero, profundidad-1, True, quesos_restantes, total_quesos)
=======
            valor = minimax_raton(mov_g, pos_raton, tablero, profundidad-1, True)
>>>>>>> origin/main

            if valor < peor:
                peor = valor

        return peor
    
<<<<<<< HEAD
def mejor_jugada_raton (pos_gato, pos_raton, tablero, profundidad, quesos_restantes, total_quesos):
=======
def mejor_jugada_raton (pos_gato, pos_raton, tablero, profundidad):
>>>>>>> origin/main
    
    mejor_valor = -float("inf")
    
    # Por si no haya ninguna jugada mejor
    mejor_mov = pos_raton 

    for mov in movimientos_validos_raton(pos_raton, tablero):

<<<<<<< HEAD
        valor = minimax_raton(pos_gato, mov, tablero, profundidad-1, False, quesos_restantes, total_quesos)
=======
        valor = minimax_raton(pos_gato, mov, tablero, profundidad-1, False)
>>>>>>> origin/main

        # Para que guarde el movimiento que mas distancia le da
        if valor > mejor_valor:
            
            mejor_valor = valor
            mejor_mov = mov 

    return mejor_mov