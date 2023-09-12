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

# Función para validar si una casilla es válida
def es_valida(x, y, laberinto, solucion):
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 1 and solucion[x][y] == 0

# Backtracking: Resuelve el laberinto utilizando la técnica de "backtracking"
def backtracking_laberinto(m, n, laberinto):
    solucion = [[0] * n for _ in range(m)]
    
    def resolver(x, y):
        if x == m - 1 and y == n - 1:  # Llegamos a la salida
            solucion[x][y] = 1
            return True

        # Intentar moverse hacia abajo primero
        if es_valida(x + 1, y, laberinto, solucion):
            solucion[x][y] = 1
            if resolver(x + 1, y):
                return True
            solucion[x][y] = 0  # Retroceder si no se encontró una solución en esta dirección

        # Si no puede moverse hacia abajo, intentar hacia la derecha
        elif es_valida(x, y + 1, laberinto, solucion):
            solucion[x][y] = 1
            if resolver(x, y + 1):
                return True
            solucion[x][y] = 0  # Retroceder si no se encontró una solución en esta dirección

        # Si no puede moverse hacia la derecha, intentar hacia la izquierda
        elif es_valida(x, y - 1, laberinto, solucion):
            solucion[x][y] = 1
            if resolver(x, y - 1):
                return True
            solucion[x][y] = 0  # Retroceder si no se encontró una solución en esta dirección

        # Si no puede moverse hacia derecha ni hacia la izquierda, intentar hacia arriba
        elif es_valida(x - 1, y, laberinto, solucion):
            solucion[x][y] = 1
            if resolver(x - 1, y):
                return True
            solucion[x][y] = 0  # Retroceder si no se encontró una solución en esta dirección

        return False

    if not resolver(0, 0):
        print("No se encontró una solución utilizando Backtracking")
    else:
        print("Backtracking")
        for fila in solucion:
            print(" ".join(map(str, fila)))



# Ramificación y Poda: Resuelve el laberinto utilizando la técnica de "ramificación y poda"
def ramificacion_y_poda(m, n, laberinto):
    solucion = [[0] * n for _ in range(m)]
    
    def resolver(x, y):
        if x == m - 1 and y == n - 1:  # Llegamos a la salida
            solucion[x][y] = 1
            return True
        if es_valida(x, y, laberinto, solucion):
            solucion[x][y] = 1

            # Movimiento hacia abajo
            if resolver(x + 1, y):
                return True
            # Movimiento hacia la derecha
            if resolver(x, y + 1):
                return True

            # Si no se encontró una solución, marcamos esta casilla como no válida
            solucion[x][y] = 0
            return False

    if not resolver(0, 0):
        print("No se encontró una solución utilizando Ramificación y Poda")
    else:
        print("Ramificación y Poda")
        for fila in solucion:
            print(" ".join(map(str, fila)))

# Función principal
def main():
    try:
        M, N = map(int, input("Ingrese M y N separados por un espacio: ").split())
        if M <= 0 or N <= 0:
            raise ValueError("M y N deben ser enteros positivos")

        laberinto = []
        for i in range(M):
            fila = list(map(int, input().split()))
            if len(fila) != N or any(x not in (0, 1) for x in fila):
                raise ValueError("Los valores de la fila deben ser 0 o 1")
            laberinto.append(fila)

        backtracking_laberinto(M, N, laberinto)
        print()
        ramificacion_y_poda(M, N, laberinto)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
