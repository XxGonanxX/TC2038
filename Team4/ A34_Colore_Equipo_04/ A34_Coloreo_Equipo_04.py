# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sáncez - A01708668

# La entrada al programa es un grafo no dirigido, en forma de matriz de adyacencias.

# Si no es posible asignar colores diferentes a cada nodo, se despliega el mensaje "No es posible asignar colores a los nodos".
# Si es posible asignar colores diferentes a nodos adyacentes, el output es una lista de colores asignados a cada nodo (lista mínima) .

# El input lo da el usuario, y el output es la lista de colores asignados a cada nodo.

# Ejemplo de entrada:

# Nodos: 5

# Matriz de adyacencias:

# 0 1 1 1 0
# 1 0 1 0 1
# 1 1 0 1 1
# 1 0 1 0 1
# 0 1 1 1 0

# Ejemplo de salida:

# Vértice 0: Color 1
# Vértice 1: Color 2
# Vértice 2: Color 3
# Vértice 3: Color 2
# Vértice 4: Color 1

# Caso 2

# Nodos: 5

# Matriz de adyacencias:

# 0 0 1 0 1
# 0 0 1 1 1
# 1 1 0 1 0
# 0 1 1 0 1
# 1 1 0 1 0

# Ejemplo de salida:

# Vértice 0 : Color 1
# Vértice 1 : Color 1
# Vértice 2 : Color 2
# Vértice 3 : Color 3
# Vértice 4 : Color 2

# Caso 3

# Nodos: 2

# Matriz de adyacencias:

# 0 1
# 1 0

# Ejemplo de salida:

# Vértice 0 : Color 1
# Vértice 1 : Color 2

# Caso 4

# Nodos: 3

# Matriz de adyacencias:

# 0 1 1
# 1 0 1
# 1 1 0

# Ejemplo de salida:

# Vértice 0 : Color 1
# Vértice 1 : Color 2
# Vértice 2 : Color 3



def main():
    # Se obtiene el número de nodos del grafo
    nodos = int(input("Nodos: "))
    # Se crea la matriz de adyacencias
    matriz = []
    # Se llena la matriz de adyacencias
    for i in range(nodos):
        matriz.append(list(map(int, input().split())))

    # Se crea la lista de colores
    colores = []
    # Se llena la lista de colores
    for i in range(nodos):
        colores.append(0)

    # Se llama a la función de coloreo
    coloreo(matriz, colores, nodos)
    
def coloreo(matriz, colores, nodos):
    # Se asigna el color 1 al primer nodo
    colores[0] = 1
    # Se llama a la función de coloreo recursivo
    if coloreoRecursivo(matriz, colores, 1, nodos) == False:
        # Si no es posible colorear, se despliega el mensaje
        print("No es posible asignar colores a los nodos")
        return False
    
    # Se despliega la lista de colores asignados a cada vértice
    for i in range(nodos):
        print("Vértice", i, ": Color", colores[i])
    
    return True

def coloreoRecursivo(matriz, colores, nodo, nodos):
    # Si se llega al último nodo, se regresa True
    if nodo == nodos:
        return True
    # Se recorren los colores
    for i in range(1, nodos+1):
        # Si es posible asignar el color al nodo
        if esColor(matriz, colores, nodo, i, nodos):
            # Se asigna el color al nodo
            colores[nodo] = i
            # Se llama a la función de coloreo recursivo
            if coloreoRecursivo(matriz, colores, nodo+1, nodos) == True:
                return True
            # Si no es posible asignar el color al nodo, se asigna el color 0
            colores[nodo] = 0

def esColor(matriz, colores, nodo, color, nodos):
    # Se recorren los nodos
    for i in range(nodos):
        # Si el nodo es adyacente y tiene el mismo color, se regresa False
        if matriz[nodo][i] == 1 and color == colores[i]:
            return False
    # Si no es adyacente o tiene diferente color, se regresa True
    return True

main()
