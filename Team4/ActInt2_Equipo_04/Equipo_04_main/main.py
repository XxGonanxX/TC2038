import numpy as np
from scipy.spatial import distance
from scipy.optimize import linear_sum_assignment
from scipy.sparse import csr_matrix
import heapq

def read_input(filename):
    with open(filename, 'r') as file:
        N = int(file.readline())
        _ = file.readline() # Ignorar línea vacía
        distances = [list(map(int, file.readline().split())) for _ in range(N)]
        _ = file.readline() # Ignorar línea vacía
        capacities = [list(map(int, file.readline().split())) for _ in range(N)]
        _ = file.readline() # Ignorar línea vacía
        central_locations = [tuple(map(int, file.readline().strip('()\n').split(','))) for _ in range(N)]
        _ = file.readline() # Ignorar línea vacía
        new_central_location = tuple(map(int, file.readline().strip('()\n').split(',')))

    return N, distances, capacities, central_locations, new_central_location

def prim(matrix):
    start_vertex = 0
    visited = set([start_vertex])
    edges = [(cost, start_vertex, to) for to, cost in enumerate(matrix[start_vertex])]
    heapq.heapify(edges)
    MST = []

    while edges:
        _, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            MST.append((frm, to))
            for next_to, next_cost in enumerate(matrix[to]):
                if next_to not in visited and next_cost < float('inf'):
                    heapq.heappush(edges, (next_cost, to, next_to))

    return MST

# Enfoque de vecino mas cercano
def tsp(matrix):
    num_nodes = len(matrix)
    unvisited_nodes = set(range(num_nodes))
    current_node = 0  # Comenzamos desde el nodo 0
    path = []
    total_cost = 0

    while unvisited_nodes:
        nearest_neighbor = min(unvisited_nodes, key=lambda x: matrix[current_node][x])
        total_cost += matrix[current_node][nearest_neighbor]
        current_node = nearest_neighbor
        path.append(current_node)
        unvisited_nodes.remove(current_node)

    # Agregamos el retorno al nodo de inicio
    total_cost += matrix[current_node][path[0]]
    path.append(path[0])

    return path

def ford_fulkerson(graph, source, sink):
    residual_graph = np.array(graph)
    max_flow = 0

    while True:
        path = find_augmenting_path(residual_graph, source, sink)
        if not path:
            break

        min_capacity = min(residual_graph[u, v] for u, v in zip(path[:-1], path[1:]))
        max_flow += min_capacity

        for u, v in zip(path[:-1], path[1:]):
            residual_graph[u, v] -= min_capacity
            residual_graph[v, u] += min_capacity

    return max_flow


def find_augmenting_path(graph, source, sink):
    visited = set()
    stack = [(source, [source])]

    while stack:
        u, path = stack.pop()
        visited.add(u)

        for v, capacity in enumerate(graph[u]):
            if capacity > 0 and v not in visited:
                if v == sink:
                    return path + [v]
                stack.append((v, path + [v]))

    return None

def main(input_filename):
    N, distances, capacities, central_locations, new_central_location = read_input(input_filename)

    # 1. Forma de cablear las colonias con fibra
    prim_path = prim(distances)

    # 2. Ruta para repartir correspondencia
    tsp_path = tsp(distances)

    # 3. Flujo máximo de información
    max_flow_graph = ford_fulkerson(capacities, 0, N - 1)

    # 4. Distancia más corta entre la nueva central y la más cercana
    

    # Resultados
    print("Forma de cablear las colonias con fibra:\n")
    print(str(prim_path) + '\n\n')
    print("Ruta para repartir correspondencia:\n")
    print(str(tsp_path) + '\n\n')
    print("Flujo máximo de información:\n")
    print(str(max_flow_graph) + '\n\n')
    print("Distancia más corta entre la nueva central y la más cercana:\n")
    print("DISTANCIA")

main("Equipo_04_Entrada_1.txt")
