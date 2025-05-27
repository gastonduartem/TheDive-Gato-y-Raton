# Gato y Ratón: Juego por turnos con Minimax y Obstáculos

## Descripción

Juego de tablero por turnos en Python donde un gato (🐱) persigue a un ratón (🐭) que debe recoger todos los quesos (🧀) antes de ser atrapado. El tablero incluye obstáculos (🪨) que impiden el paso de ambos.

**Qué funcionó:**

* Implementación básica del tablero y movimientos.
* Minimax para ambos jugadores.
* Colocación aleatoria de quesos y obstáculos.

**Qué fue un desastre:**

* Inicialmente el Minimax no consideraba los quesos; complicó agregar la lógica de “priorizar quesos”.
* Manejo de estados con parámetros adicionales (quesos_restantes) generó muchos errores de firma de funciones.

**Mejor “¡ajá!”:**
Fue cuando funcionó el minimax del gato. El minimax del ratón lo logré de manera realtivamente rápida, pero el minimax del ratón si costó más. Tambien tuve problemas con mi github, que EDu y Ceci me ayudaron y se pudo solucionar, pero aprender a usar github bien es algo pendiente para el siguiente challenge.

## Estructura del Proyecto

```
Dive-Challenge-Gato-Raton/
├── main.py               # Lógica principal y flujo de juego
├── tablero.py            # Funciones de impresión y colocación aleatoria
├── movimientos.py        # Movimientos válidos y funciones de desplazamiento
├── minimaxRaton.py       # Implementación de Minimax para el ratón
└── minimaxGato.py        # Implementación de Minimax para el gato
```

## Requisitos

* Python 3.7+

## Módulos y Funciones Principales

### `main.py`

* **Flujo principal**:

  * Solicita tamaño del tablero.
  * Inicializa posiciones del gato y el ratón.
  * Coloca quesos y obstáculos.
  * Bucle de turnos (hasta 30): mueve personajes (manual o Minimax), actualiza estado y comprueba victoria.

### `tablero.py`

* `imprimir_tablero(tablero)`:
  Dibuja el tablero por consola con bordes ASCII.
* `colocar_elementos_aleatorios(tablero, simbolo, cantidad)`:
  Inserta símbolos (queso u obstáculo) en celdas vacías evitando duplicados.

### `movimientos.py`

* `movimientos_validos_raton(pos, tablero)` / `movimientos_validos_gato(pos, tablero)`:
  Devuelven lista de celdas accesibles (no fuera de rango ni sobre obstáculo).
* `mover_manual_raton(...)`, `mover_manual_gato(...)`:
  Desplazan por WASD, validan entradas.
* `mover_raton_inteligente(...)`, `mover_gato_inteligente(...)`:
  Mueven en la casilla que maximiza/minimiza la distancia (heurística simple).

### `minimaxRaton.py` y `minimaxGato.py`

* `minimax_raton(...)`, `minimax_gato(...)`:
  Algoritmo Minimax para priorizar captura de quesos y persecución.
* `mejor_jugada_raton(...)`, `mejor_jugada_gato(...)`:
  Invocan Minimax y devuelven el siguiente movimiento óptimo.

## Ejemplos de Uso

```bash
$ python3 main.py
Inserte la cantidad de filas que desea
5
Inserte la cantidad de columnas que desea
5
Existen 30 turnos
Tablero inicial:
+---+---+---+---+---+
|🐱 |   |🪨 |🧀 |   |
... (resto del tablero)

¿Qué desea ser? El Gato (G) o el Ratón (R)? o 'auto'
auto
Turno 1
... (movimientos automáticos)
```

---

*Documento generado para el proyecto Dive Challenge: El Laberinto del Gato y el Ratón: Un Duelo de Inteligencias en Python. Hecho por Gastón Duarte*
