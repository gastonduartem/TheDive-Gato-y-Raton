from movimientos import movimientos_validos_gato, movimientos_validos_raton, deltas_gato, deltas_raton, deltas_manual
<from mofrom movimientos import movimientos_validos_gato, movimientos_validos_raton, deltas_gato, deltas_raton, deltas_manual
from minimaxRaton import evaluar_estado_raton
from minimaxRaton import evaluar_estado_raton
<<<<<<< HEAD
from minimaxRaton import evaluar_estado_raton
=======
>>>>>>> origin/main<<<<< Hfrom movimientos import movimientos_validos_gato, movimientos_validos_raton, deltas_gato, deltas_raton, deltas_manual
<<<<<<< Hfrom movimientos import movimientos_validos_gato, movimientos_validos_raton, deltas_gato, deltas_raton, deltas_manual
<<<<<<< HEAD
from minimaxRaton import evaluar_estado_raton
=======
>>>>>>> origin/mainEAD
from minimaxRaton import evaluar_estado_raton
=======
>>>>>>> origin/mainEAD
from minimaxRaton import evaluar_estado_rafrom movimientos import movimientos_validos_gato, movimientos_validos_raton, deltas_gato, deltas_raton, deltas_manual
<<<<<<< HEAD
from minimaxRaton import evalufrom movimientos import movimientos_validos_gato, movimientos_validos_raton, deltas_gato, deltas_raton, deltas_manual
<<<<<<< HEAD
from minimaxRaton import evaluar_estado_raton
=======
>>>>>>> origin/mainar_estado_raton
=======
>>>>>>> origin/mainton
=======
>>>>>>> origin/main

# Se calcula la distancia de Manhattan
def distancia_manhattan(p1, p2):
    return abs(p1[0]- p2[0]) + abs(p1[1] - p2[1])

# Se evaluan los estados de acuerdo a la distancia de manhattan para el gato y el raton
def evaluar_estado_gato(pos_gato, pos_raton):
    return -distancia_manhattan(pos_gato, pos_raton)

<<<<<<< HEAD
def minimax_gato(pos_gato, pos_raton, tablero, profundidad, es_turno_gato, quesos_restantes, total_quesos):
=======
def minimax_gato(pos_gato, pos_raton, tablero, profundidad, es_turno_gato):
>>>>>>> origin/main

    # Si el gato atrapa al raton -> victoria del gato
    if pos_gato == pos_raton:
        return float("inf")
    
     # La profundidad va a 0 -> se vuelve a evaluar el estado
    if profundidad == 0:
        return evaluar_estado_gato(pos_gato, pos_raton)
    
    if es_turno_gato:
        
        # Turno del gato, quiere maximizar la distancia (acercarse)
        mejor = -float("inf")

<<<<<<< HEAD
        for mov_g in movimientos_validos_gato(pos_gato, tablero, ):

            valor = minimax_gato(mov_g, pos_raton, tablero, profundidad-1, False, quesos_restantes, total_quesos)
=======
        for mov_g in movimientos_validos_gato(pos_gato, tablero):

            valor = minimax_gato(mov_g, pos_raton, tablero, profundidad-1, False)
>>>>>>> origin/main

            if valor > mejor:
                mejor = valor

        return mejor
    
    else:

        #Turno del raton, intenta minimizar la distancia (alejarse)
        peor = float("inf")

        for mov_r in movimientos_validos_raton(pos_raton, tablero):
            
<<<<<<< HEAD
            valor = minimax_gato(pos_gato, mov_r, tablero, profundidad-1, True, quesos_restantes, total_quesos)
=======
            valor = minimax_gato(pos_gato, mov_r, tablero, profundidad-1, True)
>>>>>>> origin/main

            if valor < peor:
                peor = valor

        return peor

<<<<<<< HEAD
def mejor_jugada_gato (pos_gato, pos_raton, tablero, profundidad, quesos_restantes, total_quesos):
=======
def mejor_jugada_gato (pos_gato, pos_raton, tablero, profundidad):
>>>>>>> origin/main

    mejor_valor = -float("inf")

    # Por si no haya un mejor movimiento
    mejor_mov = pos_gato 

    for mov in movimientos_validos_gato(pos_gato, tablero):

        # Simula mover al gato y luego es el turno del raton
<<<<<<< HEAD
        valor = minimax_gato(mov, pos_raton, tablero, profundidad-1, False, quesos_restantes, total_quesos)
=======
        valor = minimax_gato(mov, pos_raton, tablero, profundidad-1, False)
>>>>>>> origin/main

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov

    return mejor_mov