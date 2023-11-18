# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sánchez - A01708668

# Escribe un programa en Python que resuelva el problema de la mochila (Knapsack problem).

# La entrada al programa es un número N que representa el número de elementos posibles disponibles,
# seguido de N enteros que representan el valor de cada uno de esos elementos,
# seguido de N enteros que representan los pesos asociados a cada elemento.
# por último, un entero W, que representa el peso máximo o capacidad de la mochila.
# La salida del programa debe ser la ganancia (o beneficio) óptimo.

# Además, se deberá mostrar la matriz generada a lo largo del proceso.


# Ejemplo de entrada:

# Número de elementos	3
# Beneficios	
# 1
# 2
# 3
# Pesos	
# 4
# 5
# 1
# Peso máximo de la mochila	4
# Ejemplo de salida:

# Beneficio óptimo	3
# Matriz generada:

# < mostrar matriz final >

# Ejemplo de entrada 2
# 2
# 5,2
# 1,6
# 5

#Ejemplo de entrada 3
# 4
# 1,2,5,6
# 2,3,4,5
# 8

#Ejemplo de entrada 4
# 5
# 1,2,3,4,5
# 2,3,4,5,6
# 8


def knapsack(N, beneficios, pesos, W):
    # Inicializar matriz
    matriz = [[0 for x in range(W + 1)] for x in range(N + 1)]
    # Recorrer elementos
    for i in range(N + 1):
        # Recorrer pesos
        for w in range(W + 1):
            # Si no hay elementos o no hay peso, se coloca 0
            if i == 0 or w == 0:
                matriz[i][w] = 0
            # Si el peso del elemento es menor o igual al peso actual, se calcula el máximo entre el beneficio anterior y el beneficio actual más el beneficio anterior del elemento anterior
            elif pesos[i - 1] <= w:
                matriz[i][w] = max(beneficios[i - 1] + matriz[i - 1][w - pesos[i - 1]], matriz[i - 1][w])
            # Si el peso del elemento es mayor al peso actual, se coloca el beneficio anterior
            else:
                matriz[i][w] = matriz[i - 1][w]
    # Se regresa el beneficio máximo
    return matriz[N][W]

# Necesito una función que me regrese la matriz generada
def matriz(N, beneficios, pesos, W):
    # Inicializar matriz
    matriz = [[0 for x in range(W + 1)] for x in range(N + 1)]
    # Recorrer elementos
    for i in range(N + 1):
        # Recorrer pesos
        for w in range(W + 1):
            # Si no hay elementos o no hay peso, se coloca 0
            if i == 0 or w == 0:
                matriz[i][w] = 0
            # Si el peso del elemento es menor o igual al peso actual, se calcula el máximo entre el beneficio anterior y el beneficio actual más el beneficio anterior del elemento anterior
            elif pesos[i - 1] <= w:
                matriz[i][w] = max(beneficios[i - 1] + matriz[i - 1][w - pesos[i - 1]], matriz[i - 1][w])
            # Si el peso del elemento es mayor al peso actual, se coloca el beneficio anterior
            else:
                matriz[i][w] = matriz[i - 1][w]
    # Se regresa la matriz
    return matriz
    

def main():
    # Ingresar número de elementos
    print("Por favor, ingrese el número de elementos:")
    N = int(input())
    # Ingresar beneficios
    print("Por favor, ingrese los beneficios separados por comas, sin los corchetes:")
    beneficios = [int(x) for x in input().split(',')]
    # Ingresar pesos
    print("Por favor, ingrese los pesos separados por comas, sin los corchetes:")
    pesos = [int(x) for x in input().split(',')]
    # Ingresar peso máximo
    print("Por favor, ingrese el peso máximo:")
    W = int(input())
    # Imprimir beneficio máximo
    print("El beneficio máximo es:")
    print(knapsack(N, beneficios, pesos, W))
    print("La matriz generada es:")
    print(matriz(N, beneficios, pesos, W))
    
main()