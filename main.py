from tablero import imprimir_tablero, colocar_elementos_aleatorios
from movimientos import mover_manual_gato, mover_manual_raton
from minimaxRaton import mejor_jugada_raton
from minimaxGato import mejor_jugada_gato

if __name__ == "__main__":

    profundidad=10
    filas = int(input("Inserte la cantidad de filas que desea \n"))
    cols = int(input("Inserte la cantidad de columnas que desea \n"))
    
    # Se crea el tablero vacio
    tablero = [[" " for _ in range(cols)] for _ in range (filas)]

    # Simbolo del raton, del gato, del queso y del obstaculo
    simbolo_gato = "🐱" 
    simbolo_raton = "🐭" 
    simbolo_queso = "🧀"
    simbolo_obstaculo = "🪨"

    # Posiciones iniciales del raton y del gato
    pos_gato = (0,0)
    pos_raton = (filas-1,cols-1)

    fila_g, col_g = pos_gato
    fila_r, col_r = pos_raton

    tablero [fila_g][col_g] = simbolo_gato
    tablero [fila_r][col_r] = simbolo_raton

    # Definir la cantidad de quesos y columnas
    num_quesos = filas // 2
    num_obstaculos = (filas * cols * 25 + 99) // 100 #aprox el 25%

    # Colocar los quesos y los obstaculos de manera aleatoria
    pos_quesos = colocar_elementos_aleatorios(tablero, simbolo_queso, num_quesos)
    pos_obstaculos = colocar_elementos_aleatorios(tablero, simbolo_obstaculo, num_obstaculos)

    # Cantidad de quesos que quedan por comer
    quesos_restantes = set(pos_quesos)
    total_quesos = len(pos_quesos)

    print("Existen 30 turnos")
    print("Tablero inicial:")
    imprimir_tablero(tablero)

while True:    
    modo = input("Que desea ser? El Gato (G) o el Raton (R)? O escriba 'auto' si solo desea mirar esta batalla\n")
    if modo == "g" or modo =="r" or modo == "auto":
        break
    print("Eleccion invalida.")


for turno in range(1,31):

    old_gato = pos_gato
    old_raton = pos_raton

    # Calcular nueva posicion segun el juego
    if modo == "auto":
        pos_gato = mejor_jugada_gato(pos_gato, pos_raton, tablero, profundidad, quesos_restantes, total_quesos)
        pos_raton = mejor_jugada_raton(pos_gato, pos_raton, tablero, profundidad, quesos_restantes, total_quesos)
    elif modo == "g":
        pos_gato = mover_manual_gato(tablero, pos_gato)
        pos_raton = mejor_jugada_raton(pos_gato, pos_raton, tablero, profundidad, quesos_restantes, total_quesos)
    elif modo == "r":
        pos_raton = mover_manual_raton(tablero, pos_raton)
        pos_gato = mejor_jugada_gato(pos_gato, pos_raton, tablero, profundidad, quesos_restantes, total_quesos)

    # Si el raton llego a un queso, lo come
    if pos_raton in quesos_restantes:
        quesos_restantes.remove(pos_raton)
        print(f"🐭 ¡Queso comido! Quedan {len(quesos_restantes)}")

    # Limpieza del tablero
        # Limpiar todo
    for fila_actual in range(filas):
        for col_actual in range(cols):
            tablero[fila_actual][col_actual]= " "

        # Colocar obstaculos
    for (fila_obs, col_obs) in pos_obstaculos:
        tablero[fila_obs][col_obs] = simbolo_obstaculo

        # Colocar los quesos que quedan
    for (fila_queso, col_queso) in quesos_restantes:
        tablero[fila_queso][col_queso]= simbolo_queso

    
    tablero[pos_gato[0]][pos_gato[1]]=simbolo_gato
    tablero[pos_raton[0]][pos_raton[1]]=simbolo_raton

    # Comprobar condiciones de victoria
    if not quesos_restantes:
        print("🏆 ¡El ratón recogió todos los quesos! VICTORIA del ratón.")
        imprimir_tablero(tablero)
        break
            
    if pos_gato == pos_raton:
        print("FINAL!")
        tablero[old_gato[0]][old_gato[1]] = " "
        tablero[pos_gato[0]][pos_gato[1]] = simbolo_gato
        imprimir_tablero(tablero)
        print("🚨 El gato atrapó al ratón. FIN DEL JUEGO.")
        break
    
    print(f"Turno {turno}")
    imprimir_tablero(tablero)
    
else:
    print("🏁 El ratón logró escapar después de 30 turnos. VICTORIA del ratón.")
            
