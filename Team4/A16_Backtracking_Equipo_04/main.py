# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sánchez - A01708668


# Investiga sobre el uso de backtracking y poda para aplicaciones de laberintos.

# Utilizando la técnica de programación de "backtracking" y la de "ramificación 
# y poda", escribe en Python un programa que resuelva un laberinto.

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
# M:4 N:4
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

import numpy as np

# Función para verificar si una casilla es válida para moverse
def is_valid(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

# Función para resolver el laberinto mediante Backtracking
def solve_backtracking(maze, x, y, solution):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        solution[x][y] = 1
        return True
    if is_valid(maze, x, y):
        solution[x][y] = 1
        # Intentar mover hacia la derecha (DFS)
        if solve_backtracking(maze, x, y + 1, solution):
            return True
        # Intentar mover hacia abajo (DFS)
        if solve_backtracking(maze, x + 1, y, solution):
            return True
        solution[x][y] = 0
        return False

# Función para verificar si es prometedor explorar desde una casilla
def is_promising(maze, x, y, solution):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1 and solution[x][y] == 0

# Función para resolver el laberinto mediante Branch and Bound
def solve_branch_and_bound(maze, x, y, solution):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        solution[x][y] = 1
        return True
    if is_promising(maze, x, y, solution):
        solution[x][y] = 1
        if solve_branch_and_bound(maze, x + 1, y, solution) or solve_branch_and_bound(maze, x, y + 1, solution):
            return True
        solution[x][y] = 0
        return False

# Función principal para resolver el laberinto
def solve_maze(maze):
    M, N = len(maze), len(maze[0])

    # Verificar si el laberinto es válido
    for row in maze:
        if len(row) != N or any(val not in [0, 1] for val in row):
            print("Error: El laberinto no es válido.")
            return

    # Inicializar matrices de solución
    solution_backtracking = np.zeros((M, N), dtype=int)
    solution_branch_and_bound = np.zeros((M, N), dtype=int)

    # Resolver mediante Backtracking
    print("\nBacktracking")
    if solve_backtracking(maze, 0, 0, solution_backtracking):
        for row in solution_backtracking:
            print(" ".join(map(str, row)))
    else:
        print("No se encontró solución para el laberinto.")

    # Resolver mediante Branch and Bound
    print("\nRamificación y Poda")
    if solve_branch_and_bound(maze, 0, 0, solution_branch_and_bound):
        for row in solution_branch_and_bound:
            print(" ".join(map(str, row)))
    else:
        print("No se encontró solución para el laberinto.")

if __name__ == "__main__":
    try:
        M, N = map(int, input("Ingrese M y N separados por espacio: ").split())
        maze = []
        print("Ingrese el laberinto:")
        for _ in range(M):
            row = list(map(int, input().split()))
            maze.append(row)
        
        solve_maze(maze)
    except ValueError:
        print("Error: Ingrese valores enteros para M y N.")
