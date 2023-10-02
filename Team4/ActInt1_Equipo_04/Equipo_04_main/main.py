# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sánchez - A01708668

import glob

# primero, leeremos todos los archivos, primero los transmision y luego los mcode, cada uno en una lista separada

print()
print("Bienvenido al algoritmo de Naive de detección de código malicioso, desarrollado por Alan Patricio González Bernal y Alan Rodrigo Castillo Sánchez")
print("leyendo archivos...")
print()

# leer archivos de transmision
transmission1 = []
transmission2 = []


# Directorio donde se encuentran los archivos
directoriotrans =''

# Patrón para buscar archivos que comiencen con "transmission"
patrontrans = f'transmission*'

# Obtener una lista de archivos que coinciden con el patrón
archivostrans = glob.glob(patrontrans)


    # Procesa cada archivo según tus necesidades
print(f"Leyendo archivo: {archivostrans[0]}")
with open(archivostrans[0], 'r') as f:
    contenido = f.read()
    for line in contenido:
        transmission1.append(line)
    print("Lectura exitosa")
    
print(f"Leyendo archivo: {archivostrans[1]}")
with open(archivostrans[1], 'r') as f:
    contenido = f.read()
    for line in contenido:
        transmission2.append(line)
    print("Lectura exitosa")
            
# leer archivos de mcode
mcode1 = []
mcode2 = []
mcode3 = []

# Directorio donde se encuentran los archivos
directoriomcode = ''

# Patrón para buscar archivos que comiencen con "transmission"
patronmcode = f'mcode*'

# Obtener una lista de archivos que coinciden con el patrón
archivosmcode = glob.glob(patronmcode)


    # Procesa cada archivo según tus necesidades
print(f"Leyendo archivo: {archivosmcode[0]}")
with open(archivosmcode[0], 'r') as f:
    contenido = f.read()
    for line in contenido:
        mcode1.append(line)
    print("Lectura exitosa")
    
print(f"Leyendo archivo: {archivosmcode[1]}")
with open(archivosmcode[1], 'r') as f:
    contenido = f.read()
    for line in contenido:
        mcode2.append(line)
    print("Lectura exitosa")
    
print(f"Leyendo archivo: {archivosmcode[2]}")
with open(archivosmcode[2], 'r') as f:
    contenido = f.read()
    for line in contenido:
        mcode3.append(line)
    print("Lectura exitosa")
    
print()
        
# ahora, vamos a crear una funcion que nos permita saber si un archivo contiene el codigo de otro archivo
# esto lo haremos con el metodo de fuerza bruta, visto como Naive

def contains_code(transmission, mcode):
    
    # primero, vamos a convertir el archivo de transmision en un string
    transmission_string = ""
    for line in transmission:
        transmission_string += line
        
    # ahora, vamos a convertir el archivo de mcode en un string
    mcode_string = ""
    for line in mcode:
        mcode_string += line


    # ahora, vamos a buscar el mcode dentro del transmission
    if mcode_string in transmission_string:
        # Necesito saber la posicion en la que inicia el codigo
        start = transmission_string.find(mcode_string)
        # Necesito saber la posicion en la que termina el codigo
        end = start + len(mcode_string)
        # Necesito imprimir el resultado
        return True, start
    else:
        return False
    
def contains_code2(transmission, mcode):
    
    # primero, vamos a convertir el archivo de transmision en un string
    transmission_string = ""
    for line in transmission:
        transmission_string += line
        
    # ahora, vamos a convertir el archivo de mcode en un string
    mcode_string = ""
    for line in mcode:
        mcode_string += line


    # ahora, vamos a buscar el mcode dentro del transmission
    if mcode_string in transmission_string:
        # Necesito saber la posicion en la que inicia el codigo
        start = transmission_string.find(mcode_string)
        # Necesito saber la posicion en la que termina el codigo
        end = start + len(mcode_string)
        # Necesito imprimir el resultado
        return True, start, end
    else:
        return False
    
# ahora, vamos a crear una funcion que nos permita saber si un archivo contiene el codigo de otro archivo, pero al reves

    

def longestSubstring(str1,str2):
    # Necesito saber la longitud de cada string
    m = len(str1)
    n = len(str2)

    # Necesito crear una matriz para almacenar los resultados de los subproblemas
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

    # Necesito almacenar la longitud del substring más largo
    result = 0

    # Necesito almacenar el índice de la última fila
    end = 0

    # Necesito crear dos bucles anidados, uno para cada string
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (str1[i-1] == str2[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                if (result < LCSuff[i][j]):
                    result = LCSuff[i][j]
                    end = i
            else:
                LCSuff[i][j] = 0

    # Necesito crear un string para almacenar el substring más largo
    res = ""

    # Necesito crear un bucle para agregar los caracteres del substring más largo al string
    while (result > 0):
        res = str1[end - 1] + res
        end = end - 1
        result = result - 1

    # Necesito imprimir el substring más largo
    return res



def encontrar_substring_comun(transmission1, transmission2):
    longitud_max_substring = 0
    substring_comun = ""
    posiciones_comunes_t1 = []
    posiciones_comunes_t2 = []

    for i in range(len(transmission1)):
        for j in range(len(transmission2)):
            m, n = i, j
            longitud_substring = 0
            while m < len(transmission1) and n < len(transmission2) and transmission1[m] == transmission2[n]:
                longitud_substring += 1
                m += 1
                n += 1

            if longitud_substring > longitud_max_substring:
                longitud_max_substring = longitud_substring
                substring_comun = transmission1[i:i + longitud_max_substring]
                posiciones_comunes_t1 = [(i, i + longitud_max_substring - 1)]
                posiciones_comunes_t2 = [(j, j + longitud_max_substring - 1)]
            elif longitud_substring == longitud_max_substring:
                posiciones_comunes_t1.append((i, i + longitud_substring - 1))
                posiciones_comunes_t2.append((j, j + longitud_substring - 1))

    return substring_comun, posiciones_comunes_t1, posiciones_comunes_t2

substring_comun, posiciones_comunes_t1, posiciones_comunes_t2 = encontrar_substring_comun(transmission1, transmission2)

#Busco el palindromo, solo debo regresar las posiciones iniciales y finales
def ispalindrome(transmission):

    max_length = 1
    startAt = 0
    for i in range(len(transmission)):
        for j in range(i, len(transmission)):
            flag = 1
            for k in range(0, ((j - i) // 2) + 1):
                if (transmission[i + k] != transmission[j - k]):
                    flag = 0
            if (flag != 0 and (j - i + 1) > max_length):
                startAt = i
                max_length = j - i + 1
            
    return startAt, startAt + max_length - 1

print("PARTE 1:")
print()
print(f"En el archivo de {archivostrans[0]} se encuentra el código {archivosmcode[0]}?", (contains_code(transmission1, mcode1)))
print(f"En el archivo de {archivostrans[0]} se encuentra el código {archivosmcode[1]}?", (contains_code(transmission1, mcode2)))
print(f"En el archivo de {archivostrans[0]} se encuentra el código {archivosmcode[2]}?", (contains_code(transmission1, mcode3)))
print(f"En el archivo de {archivostrans[1]} se encuentra el código {archivosmcode[0]}?", (contains_code(transmission2, mcode1)))
print(f"En el archivo de {archivostrans[1]} se encuentra el código {archivosmcode[1]}?", (contains_code(transmission2, mcode2)))
print(f"En el archivo de {archivostrans[1]} se encuentra el código {archivosmcode[2]}?", (contains_code(transmission2, mcode3)))
print()
print("PARTE 2:")
print()
print(ispalindrome(transmission1))
print(ispalindrome(transmission2))
print()
print("PARTE 3:")
print("El substring más largo común entre los archivos de transmisión es:", longestSubstring(transmission1, transmission2))
print(f"Posiciones en la {archivostrans[0]}:")
for inicio, fin in posiciones_comunes_t1:
    print(f"Posición inicial: {inicio + 1}, Posición final: {fin + 1}")
    break
print()
print(f"Posiciones en la {archivostrans[1]}:")
for inicio, fin in posiciones_comunes_t2:
    print(f"Posición inicial: {inicio + 1}, Posición final: {fin + 1}")

    
