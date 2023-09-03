# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sánchez - A01708668

# Utilizando las técnicas de programación de "programación dinámica", 
# y la de "algoritmos avaros", escribe en Python un programa que resuelva 
# el problema del cambio de monedas.

# El programa recibe un numero entero N, seguido de N valores enteros 
# (uno en cada línea, no necesariamente están ordenados) que representan 
# las diferentes denominaciones disponibles de las monedas.
# 
# Seguido de esto, el programa recibe dos números enteros: P y Q, (uno 
# en cada línea) por la entrada estándar, que representan P: el precio de 
# un producto dado y Q: es el billete o moneda con el que se paga dicho 
# producto.

# La salida del programa es una lista de N valores correspondientes al 
# número de monedas de cada denominación, de mayor a menor, una en cada 
# línea, que se tienen que dar para dar el cambio por el producto pagado, 
# primero utilizando programación dinámica, y luego utilizando un 
# algoritmo avaro.

def cambio_avaros(denominaciones, monto):
    n = len(denominaciones)
    monedas = [0] * n

    for i in range(n):
        while monto >= denominaciones[i]:
            monedas[i] += 1
            monto -= denominaciones[i]

    return monedas


def cambio_dinamico(denominaciones, monto):
    n = len(denominaciones)
    dp = [0] * (monto + 1)

    for i in range(1, monto + 1):
        dp[i] = float('inf')
        for j in range(n):
            if denominaciones[j] <= i:
                subproblema = dp[i - denominaciones[j]]
                if subproblema != float('inf') and subproblema + 1 < dp[i]:
                    dp[i] = subproblema + 1

    monedas = [0] * n
    i = n - 1
    while monto > 0 and i >= 0:
        if monto >= denominaciones[i] and dp[monto] == dp[monto - denominaciones[i]] + 1:
            monedas[i] += 1
            monto -= denominaciones[i]
        else:
            i -= 1

    return monedas
        

def main():
    # Se inicializa la lista de monedas
    lista_monedas = []
    print("Bienvenido al algoritmo de cambios de monedas, por favor, ingrese la cantidad de monedas disponibles:")
    lista_len = int(input())
    len = 0
    print("Ingrese las denominaciones de las monedas disponibles:")
    while len < lista_len:
        # Se añade la denominación
        lista_monedas.append(int(input()))
        len += 1
    print("Ingrese el precio del producto:")
    precio = int(input())
    print("Ingrese el billete o moneda con el que se paga el producto:")
    billete = int(input())
    # Se calcula el cambio
    cambio = billete - precio
    # Se calcula el cambio con programación dinámica
    cambio_dinamica = cambio_dinamico(lista_monedas, cambio)
    # Se calcula el cambio con algoritmos avaros
    cambio_avaro = cambio_avaros(lista_monedas, cambio)
    print("El cambio con programación dinámica es:")
    print(cambio_dinamica)
    print("El cambio con algoritmos avaros es:")
    print(cambio_avaro)

main()