# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sánchez - A01708668

# Escribe un programa en Python que implemente los algoritmos de Dijkstra y Floyd para encontrar la distancia más corta entre parejas de nodos en un grafo dirigido. 

# El programa debe leer un número n seguido de n x n valores enteros no negativos que representan una matriz de adyacencias de un grafo dirigido.

# El primer número representa el número de nodos, los siguientes valores en la matriz, el valor en la posición i,j representan el peso del arco del nodo i al nodo j. Si no hay un arco entre el nodo i y el nodo j, el valor en la matriz debe ser -1.
# La salida del programa es, primero con el algoritmo de Dijkstra la distancia del nodo i al nodo j para todos los nodos, y luego, la matriz resultado del algoritmo de Floyd

# Datos muestra:

# 4
# 0 2 -1 3
# -1 0 1 5
# 2 3 0 -1
# 3 -1 4 0

# 3
# -1 3 1
# 2 -1 4
# 1 5 -1

# 4
# 0 2 6 -1
# 0 0 3 -1
# 1 -1 0 1
# 1 1 1 0

# 5
# 0 1 2 3 -1
# 5 2 5 -1 3
# 1 6 7 -1 3
# 7 3 1 6 -1
# -1 5 2 6 3




# Dijkstra
def dijkstra(graph, source):
    # Inicializar variables
    distance = {}
    visited = {}
    path = {}
    for node in graph:
        distance[node] = float('inf')
        visited[node] = False
        path[node] = []
    distance[source] = 0
    # Recorrer nodos
    for _ in range(len(graph)):
        # Encontrar nodo con distancia mínima
        min_dist = float('inf')
        min_node = None
        for node in graph:
            if not visited[node] and distance[node] < min_dist:
                min_dist = distance[node]
                min_node = node
        # Actualizar distancias
        for neighbor in graph[min_node]:
            if not visited[neighbor]:
                new_dist = distance[min_node] + graph[min_node][neighbor]
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    path[neighbor] = path[min_node] + [min_node]
        visited[min_node] = True
    # Regresar distancias
    return distance, path

def floyd(graph, source):
    # Inicializar variables
    distance = {}
    path = {}
    for node in graph:
        distance[node] = {}
        path[node] = {}
        for neighbor in graph:
            distance[node][neighbor] = float('inf')
            path[node][neighbor] = []
        distance[node][node] = 0
        path[node][node] = [node]
        for neighbor in graph[node]:
            distance[node][neighbor] = graph[node][neighbor]
            path[node][neighbor] = [node]
    # Recorrer nodos
    for k in graph:
        for i in graph:
            for j in graph:
                new_dist = distance[i][k] + distance[k][j]
                if new_dist < distance[i][j]:
                    distance[i][j] = new_dist
                    path[i][j] = path[i][k] + path[k][j]
    # Regresar distancias
    return distance, path


def main():
    print("Bienvenido al algoritmo Dijkstra y Floyd, por favor, ingresa el tamaño del grafo y sus valores:")
    # Leer grafo
    graph = {}
    n = int(input())
    for i in range(n):
        graph[i+1] = {}
        line = input().split()
        for j in range(n):
            if line[j] != '-1':
                graph[i+1][j+1] = int(line[j])
    # Dijkstra
    print('\nDijkstra:')
    for i in range(n):
        for j in range(n):
            if i != j:
                distance, path = dijkstra(graph, i+1)
                print('node', i+1, 'to node', j+1, ': ', distance[j+1])
    # Floyd
    print('\nFloyd:')
    distance, path = floyd(graph, 1)
    for i in range(n):
        for j in range(n):
            print(distance[i+1][j+1], end=' ')
        print()
        
        
main()