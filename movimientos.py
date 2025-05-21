import random

# Indicamos como puede moverse
deltas_raton = [(-1,0),(1,0),(0,-1),(0,1)]
deltas_gato = [(-1,0),(1,0),(0,-1),(0,1)]
# ,(-1,-1),(-1,1),(1,-1),(1,1)

deltas_manual = {
    "w" : (-1,0),
    "s" : (1,0),
    "a" : (0,-1),
    "d" : (0,1)
}

# Definimos los movimientos validos del raton
def movimientos_validos_raton(pos, tablero):
    filas = len(tablero)
    cols = len(tablero[0])
    fila, col   = pos
    validos_raton= []
    for dx, dy in deltas_raton:
        nueva = (fila + dx, col + dy)
        # Definimos que se quede dentro del tablero cuando se le 'suma' o 'resta' la delta a la posicion actual dependiendo de donde quiera moverse
        if dentro_del_tablero(nueva, tablero):
            validos_raton.append(nueva)
    return validos_raton

# Definimos los movimientos validos del gato
def movimientos_validos_gato(pos, tablero):
    filas = len(tablero)
    cols = len(tablero[0])
    fila, col   = pos
    validos_gato = []
    for dx, dy in deltas_gato:
        nueva = (fila + dx, col + dy)
        # Definimos que se quede dentro del tablero cuando se le 'suma' o 'resta' la delta a la posicion actual dependiendo de donde quiera moverse
        if dentro_del_tablero(nueva, tablero):
            validos_gato.append(nueva)
    return validos_gato

# Definimos los movimientos validos manuales
def movimientos_validos_manuales(pos, tablero):
    filas = len(tablero)
    cols = len(tablero[0])
    fila, col = pos
    validos_manual = []
    for dx, dy in deltas_manual:
        nueva = (fila + dx, col + dy)
        if dentro_del_tablero(nueva, tablero):
            validos_manual.append(nueva)
    return validos_manual

# Definimos que no salga del tablero
def dentro_del_tablero(pos, tablero):
    filas = len(tablero)
    cols = len(tablero[0])
    fila, col = pos
    return 0 <= fila < filas and 0 <= col < cols

# Mueve al ratón a una de esas posiciones al azar
def mover_raton_aleatorio(tablero, pos_raton):

    opciones = movimientos_validos_raton(pos_raton, tablero)

    # Se 'rompe' la fila y columnas en dos variables
    fila_act_raton, col_act_raton = pos_raton
    
    # Se selecciona una nueva opcion de la lista de opciones validas
    nueva_pos = random.choice(opciones)
    nueva_fila, nueva_col = nueva_pos
    
    # Limpia la celda vieja
    tablero[fila_act_raton][col_act_raton] = " "
    
    # Coloca la "R" en la nueva posición
    tablero[nueva_fila][nueva_col] = "🐭" 
    
    return nueva_pos

# Se calcula la distancia de Manhattan

def distancia_manhattan(p1, p2):
    return abs(p1[0]- p2[0]) + abs(p1[1] - p2[1])

# El raton se moviliza al casilla mas lejano para maximizar su distancia con el gato
def mover_raton_inteligente(tablero, pos_raton, pos_gato):
    
    # Se lee las posiciones del raton
    fila_act_raton, col_act_raton = pos_raton

    # Opciones validas de movimiento
    opciones = movimientos_validos_raton(pos_raton, tablero)

    # Se declara la variable 'mejor', que dp contendra la casilla con mayor distancia
    mejor = None

    # Arranca con un valor -1, pero dp se sobrescirbe por la mayor distancia que haya
    max_dist=-1

    # Opt va recorriendo cada posicion posible y se calcula la distancia con 'd', luego se verifica que sea la distancia mas larga de entre las opciones
    for opt_raton in opciones:
        d = distancia_manhattan(opt_raton, pos_gato)
        if d > max_dist:
            max_dist, mejor = d, opt_raton

    tablero[fila_act_raton][col_act_raton]= " "
    tablero[mejor[0]][mejor[1]] = "🐭" 

    return mejor

# El gato se moviliza a la casilla mas cercana para minimizar la distancia con el raton
def mover_gato_inteligente(tablero, pos_gato, pos_raton):
    
    # Se lee las posiciones del gato
    fila_act_gato, col_act_gato = pos_gato

    #Opciones validas de movimiento
    opciones=movimientos_validos_gato(pos_gato, tablero)

     # Se declara la variable 'mejor', que dp contendra la casilla con menor distancia
    mejor = None

    # Arranca con un valor -1, pero dp se sobrescirbe por la mayor distancia que haya
    min_dist = 1000000

      # Opt va recorriendo cada posicion posible y se calcula la distancia con 'd', luego se verifica que sea la distancia mas larga de entre las opciones
    for opt_gato in opciones:
        d = distancia_manhattan(opt_gato, pos_raton)
        if d < min_dist:
            min_dist, mejor = d, opt_gato

    tablero[fila_act_gato][col_act_gato]= " "
    tablero[mejor[0]][mejor[1]] = "🐱"

    return mejor

def mover_manual_gato(tablero, pos_gato):

    # Se descompone las posiciones actuales del gato
    fila_act_gato, col_act_gato = pos_gato

    # Se inicia el nucle
    while True:
        tecla = input("Utilice W/A/S/D para perseguir al raton \n")

        tecla = tecla.lower().strip()

        # Se verifica que la tecla presionada este dentro de las opciones
        if tecla not in deltas_manual:
            print("Tecla invalida, utilice solo teclas W/A/S/D para moverse \n")
            continue

        # Se descompone la tecla presionadas en filas y columnas 
        dx, dy = deltas_manual[tecla]

        # Se le 'suma'o 'resta' las posiciones de la tecla presionada a la posicio actual y se le asigna a una nueva variable
        nueva = (fila_act_gato + dx, col_act_gato + dy)

        # Se verifica este dentro del tablero
        if not dentro_del_tablero(nueva,tablero):
            print("Te saliste del tablero, proba moverte en otra direciion!! \n")
            continue

        #Se limpia la posicion anterior
        tablero[fila_act_gato][col_act_gato]=" "
        
        # Se descompone la nueva posicion en fila y columna
        fila_act_gato, col_act_gato = nueva

        # Se 'imprime' la nueva posicion del gato
        tablero[fila_act_gato][col_act_gato]= "🐱"

        break
    
    # Se devuelve la posicion actual del gato
    return (fila_act_gato, col_act_gato)

def mover_manual_raton(tablero, pos_raton):

    # Se descompone las posiciones actuales del gato
    fila_act_raton, col_act_raton = pos_raton

    # Se inicia el nucle
    while True:
        tecla = input("Utilice W/A/S/D para perseguir al raton")

        tecla = tecla.lower().strip()

        # Se verifica que la tecla presionada este dentro de las opciones
        if tecla not in deltas_manual:
            print("Tecla invalida, utilice solo teclas W/A/S/D para moverse")
            continue

        # Se descompone la tecla presionadas en filas y columnas 
        dx, dy = deltas_manual[tecla]

        # Se le 'suma'o 'resta' las posiciones de la tecla presionada a la posicio actual y se le asigna a una nueva variable
        nueva = (fila_act_raton + dx, col_act_raton + dy)

        # Se verifica este dentro del tablero
        if not dentro_del_tablero(nueva,tablero):
            print("Te saliste del tablero, proba moverte en otra direciion!!")
            continue

        #Se limpia la posicion anterior
        tablero[fila_act_raton][col_act_raton]=" "
        
        # Se descompone la nueva posicion en fila y columna
        fila_act_raton, col_act_raton = nueva

        # Se 'imprime' la nueva posicion del gato
        tablero[fila_act_raton][col_act_raton]= "🐭" 

        break
    
    # Se devuelve la posicion actual del gato
    return (fila_act_raton, col_act_raton)
