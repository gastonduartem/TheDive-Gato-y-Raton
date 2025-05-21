from tablero import imprimir_tablero
from movimientos import mover_raton_inteligente, mover_gato_inteligente, mover_manual_gato, mover_manual_raton
from minimaxRaton import mejor_jugada_raton
from minimaxGato import mejor_jugada_gato

if __name__ == "__main__":

    profundidad=10
    filas = 9
    cols = 9
    
    # Se crea el tablero vacio
    tablero = [[" " for _ in range(filas)] for _ in range (cols)]

    # Simbolo del raton y del gato
    simbolo_gato = "🐱" 
    simbolo_raton = "🐭" 

    # Posiciones iniciales del raton y del gato
    pos_gato = (0,0)
    pos_raton = (8,8)

    fila_g, col_g = pos_gato
    fila_r, col_r = pos_raton

    tablero [fila_g][col_g] = simbolo_gato
    tablero [fila_r][col_r] = simbolo_raton

    print("Existen 30 turnos")
    print("Tablero inicial:")
    imprimir_tablero(tablero)

  #  for turno in range(1,21):
  #      pos_raton = mover_raton_inteligente(tablero,pos_raton, pos_gato)
  #      pos_gato = mover_gato_inteligente(tablero, pos_gato, pos_raton)
  #      if pos_raton == pos_gato:
  #          print("Final")
  #          imprimir_tablero(tablero)
  #          print("Termino el juego")
  #          break
  #      print(f"Turno {turno}:")
  #      imprimir_tablero(tablero)

  #  else:    
  #      print("🏁 El ratón logró escapar después de 20 turnos. VICTORIA del ratón.")

while True:    
    modo = input("Que desea ser? El Gato (G) o el Raton (R)? O escriba 'auto' si solo desea mirar esta batalla\n")
    if modo == "g" or modo =="r" or modo == "auto":
        break
    print("Eleccion invalida.")


for turno in range(1,31):

    old_gato = pos_gato
    old_raton = pos_raton

    if modo == "auto":
        pos_gato = mejor_jugada_gato(pos_gato, pos_raton, tablero, profundidad)
        pos_raton = mejor_jugada_raton(pos_gato, pos_raton, tablero, profundidad)
    elif modo == "g":
        pos_gato = mover_manual_gato(tablero, pos_gato)
        pos_raton = mejor_jugada_raton(pos_gato, pos_raton, tablero, profundidad)
    elif modo == "r":
        pos_raton = mover_manual_raton(tablero, pos_raton)
        pos_gato = mejor_jugada_gato(pos_gato, pos_raton, tablero, profundidad)
        
    if pos_gato == pos_raton:
        imprimir_tablero(tablero)
        print("🚨 El gato atrapó al ratón. FIN DEL JUEGO.")
        break
    print(f"Turno {turno}")

    tablero[old_gato[0]][old_gato[1]]=" "
    tablero[old_raton[0]][old_raton[1]]=" "
    tablero[pos_gato[0]][pos_gato[1]]=simbolo_gato
    tablero[pos_raton[0]][pos_raton[1]]=simbolo_raton
    imprimir_tablero(tablero)
    
else:
    print("🏁 El ratón logró escapar después de 30 turnos. VICTORIA del ratón.")
            
