# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sánchez - A01708668

def MergeSort(lista):
    # Si la lista tiene más de un elemento, se divide en dos
    if len(lista) > 1:
        mitad = len(lista)//2
        # Se crea una lista de la mitad izquierda y otra de la derecha
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        # Se ordena cada mitad
        MergeSort(izquierda)
        MergeSort(derecha)
        # Se crea un índice para cada mitad
        i = 0
        j = 0
        k = 0
        # Se ordenan los elementos de la lista
        while i < len(izquierda) and j < len(derecha):
            # Si el elemento de la mitad izquierda es menor que el de la derecha se coloca en la lista original
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            # Si el elemento de la mitad derecha es menor que el de la izquierda se coloca en la lista original
            else:
                lista[k] = derecha[j]
                j += 1
            # Se aumenta el índice de la lista original
            k += 1
        # Se colocan los elementos restantes de la mitad izquierda y derecha en la lista original
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        # Se colocan los elementos restantes de la mitad derecha en la lista original
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

def main():
    # ingresa numero de elementos separados por comas

    print("Por favor, ingrese la lista de números separados por comas, sin los corchetes:")
    lista = [int(x) for x in input().split(',')]
    print("La lista ingresada es:")
    print(lista)
    MergeSort(lista)
    print("Después de ejecutar MergeSort, la lista es:")
    print(lista)
    
main()

    # Datos de entrada:
    # 38, 27, 43, 3, 9, 82, 10
    # 100, 400, 125, 10, 0, 20, 642, 13, 63, 35, 25, 85, 7, 2, 6
    #
    # Salida:
    # [3, 9, 10, 27, 38, 43, 82]
    # [0, 2, 6, 7, 10, 13, 20, 25, 35, 63, 85, 100, 125, 400, 642]