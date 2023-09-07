# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sánchez - A01708668


# Investiga sobre el uso de backtracking y poda para aplicaciones de laberintos.

# Utilizando la técnica de programación de "backtracking" y la de "ramificación 
# y poda", escribe en C++ un programa que resuelva un laberinto.

# El programa recibe dos números enteros M y N, seguido de M líneas de N valores 
# booleanos(0|1) separados por un espacio, por la entrada estándar que representan 
# el laberinto. Un 1 representa una casilla en la que es posible moverse, un 0 es 
# una casilla por la que NO se puede pasar. 

# El origen o casilla de inicio es siempre la casilla (0,0) y la salida o meta 
# es siempre la casilla (M-1, N-1).

# La salida del programa es una matriz de valores booleanos (0|1) que representan 
# el camino para salir del laberinto. Mostrar la solución utilizando la técnica de 
# backtracking, o utilizando la técnica de ramificación y poda. Especifica cuál de 
# las dos estás utilizando.

# Muestra en pantalla el laberinto inicial y después las soluciones encontradas.

# Ejemplo de entrada:
# 4
# 4
# 1 0 0 0
# 1 1 0 1
# 0 1 0 0
# 1 1 1 1


# Ejemplo de salida:

# Backtracking
# 1 0 0 0
# 1 1 0 0
# 0 1 0 0
# 0 1 1 1

# Ramificación y poda
# 1 0 0 0
# 1 1 0 0
# 0 1 0 0
# 0 1 1 1

# Algunos ejemplos y consideraciones:

# En los ejemplos: señalar error en caso de que se ingresen datos diferentes a 
# los enteros positivos M y N, y a los valores booleanos, según corresponda.
# Indica en los comentarios, el criterio de avance, ejemplo: hacia el frente y 
# hacia abajo, etc. 
