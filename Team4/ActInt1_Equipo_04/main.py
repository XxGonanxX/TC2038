# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sánchez - A01708668

# escribe un programa en Python que lea 5 archivos de texto (de nombre fijo, no se piden al usuario) que 
# contienen exclusivamente caracteres del 0 al 9, caracteres entre A y F y saltos de línea.

# Los archivos de transmisión contienen caracteres de texto que representan el envío de datos de un
# dispositivo a otro.	     

# transmission1.txt
# transmission2.txt

# Los archivos mcodex.txt representan código malicioso que se puede encontrar dentro de una transmisión.

# mcode1.txt
# mcode2.txt
# mcode3.txt

# El programa debe analizar si el contenido de los archivos mcode1.txt, mcode2.txt y mcode3.txt están 
# contenidos en los archivos transmission1.txt y transmission2.txt y desplegar un true o false si es que
# las secuencias de chars están contenidas o no. En caso de ser true, muestra true, seguido de exactamente
# un espacio, seguido de la posición en el archivo de transmissiónX.txt donde inicia el código de mcodeY.txt

# Suponiendo que el código malicioso tiene siempre código "espejeado" (palíndromos de chars), sería buena 
# idea buscar este tipo de código en una transmisión. El programa después debe buscar si hay código 
# "espejeado" dentro de los archivos de transmisión. (palíndromo a nivel chars, no meterse a nivel bits). 
# El programa muestra en una sola línea dos enteros separados por un espacio correspondientes a la posición 
# (iniciando en 1) en donde inicia y termina el código "espejeado" más largo (palíndromo) para cada archivo de 
# transmisión. Puede asumirse que siempre se encontrará este tipo de código.

# Finalmente el programa analiza que tan similares son los archivos de transmisión, y debe mostrar la posición 
# inicial y la posición final (iniciando en 1) del primer archivo en donde se encuentra el substring más largo 
# común entre ambos archivos de transmisión.

# input
#      nada, solamente deben existir los 5 archivos en la misma ruta donde se ejecuta el programa    

# output
#   parte 1
#      (true | false) si es que el archivo transmission1.txt contiene el código (secuencia de chars) contenido en el archivo mcode1.txt    
#      (true | false) si es que el archivo transmission1.txt contiene el código (secuencia de chars) contenido en el archivo mcode2.txt
#      (true | false) si es que el archivo transmission1.txtcontiene el código (secuencia de chars) contenido en el archivo mcode3.txt
#      (true | false) si es que el archivo transmission2.txt contiene el código (secuencia de chars) contenido en el archivo mcode1.txt
#      (true | false) si es que el archivo transmission2.txtcontiene el código (secuencia de chars) contenido en el archivo mcode2.txt
#      (true | false) si es que el archivo transmission2.txt contiene el código (secuencia de chars) contenido en el archivo mcode3.txt

# Para cada caso true, muestra true, seguido de exactamente un espacio, seguido de la posición en el archivo de 
# transmissiónX.txt donde inicia el código de mcodeY.txt 

#   parte2
#      posiciónInicial posiciónFinal (para archivo de transmisión1)
#      posiciónInicial posiciónFinal (para archivo de transmisión2)
#   parte3
#       posiciónInicial posiciónFinal (de substring común más largo entre archivos de transmisión)

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
directoriotrans = 'Team4/ActInt1_Equipo_04'

# Patrón para buscar archivos que comiencen con "transmission"
patrontrans = f'{directoriotrans}/transmission*'

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
directoriomcode = 'Team4/ActInt1_Equipo_04'

# Patrón para buscar archivos que comiencen con "transmission"
patronmcode = f'{directoriomcode}/mcode*'

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

def contains_code_reversed(transmission, mcode):
    # primero, vamos a convertir el archivo de transmision en un string
    transmission_string = ""
    for line in transmission:
        transmission_string += line
        
    # ahora, vamos a convertir el archivo de mcode en un string
    mcode_string = ""
    for line in mcode:
        mcode_string += line
        
    # ahora, vamos a buscar el mcode dentro del transmission
    if mcode_string[::-1] in transmission_string:
        # Necesito saber la posicion en la que inicia el codigo
        start = transmission_string.find(mcode_string[::-1])
        # Necesito saber la posicion en la que termina el codigo
        end = start + len(mcode_string)
        # Necesito imprimir el resultado
        start, end
        return True, start
    else:
        return False
    
def contains_code_reversed2(transmission, mcode):
    # primero, vamos a convertir el archivo de transmision en un string
    transmission_string = ""
    for line in transmission:
        transmission_string += line
        
    # ahora, vamos a convertir el archivo de mcode en un string
    mcode_string = ""
    for line in mcode:
        mcode_string += line
        
    # ahora, vamos a buscar el mcode dentro del transmission
    if mcode_string[::-1] in transmission_string:
        # Necesito saber la posicion en la que inicia el codigo
        start = transmission_string.find(mcode_string[::-1])
        # Necesito saber la posicion en la que termina el codigo
        end = start + len(mcode_string)
        # Necesito imprimir el resultado
        start, end
        return True, start, end
    else:
        return False
    
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

# Ahora, vamos a entregarle a la funcion los archivos que queremos analizar

print("PARTE 1:")
print()
print(f"En el archivo de {archivostrans[0]} se encuentra el código {archivosmcode[0]}?", (contains_code(transmission1, mcode1)))
print(f"En el archivo de {archivostrans[0]} se encuentra el código {archivosmcode[1]}?", (contains_code(transmission1, mcode2)))
print(f"En el archivo de {archivostrans[0]} se encuentra el código {archivosmcode[2]}?", (contains_code(transmission1, mcode3)))
print(f"En el archivo de {archivostrans[1]} se encuentra el código {archivosmcode[0]}?", (contains_code(transmission2, mcode1)))
print(f"En el archivo de {archivostrans[1]} se encuentra el código {archivosmcode[1]}?", (contains_code(transmission2, mcode2)))
print(f"En el archivo de {archivostrans[1]} se encuentra el código {archivosmcode[2]}?", (contains_code(transmission2, mcode3)))
print()
print(f"El archivo de {archivostrans[0]} contiene el codigo de {archivosmcode[0]} en reversa?", (contains_code_reversed(transmission1, mcode1)))
print(f"El archivo de {archivostrans[0]} contiene el codigo de {archivosmcode[1]} en reversa?", (contains_code_reversed(transmission1, mcode2)))
print(f"El archivo de {archivostrans[0]} contiene el codigo de {archivosmcode[2]} en reversa?", (contains_code_reversed(transmission1, mcode3)))
print(f"El archivo de {archivostrans[1]} contiene el codigo de {archivosmcode[0]} en reversa?", (contains_code_reversed(transmission2, mcode1)))
print(f"El archivo de {archivostrans[1]} contiene el codigo de {archivosmcode[1]} en reversa?", (contains_code_reversed(transmission2, mcode2)))
print(f"El archivo de {archivostrans[1]} contiene el codigo de {archivosmcode[2]} en reversa?", (contains_code_reversed(transmission2, mcode3)))
print()
print("PARTE 2:")
print()
print(f"En el archivo de {archivostrans[0]} se encuentra el código {archivosmcode[0]}?", (contains_code2(transmission1, mcode1)))
print(f"En el archivo de {archivostrans[0]} se encuentra el código {archivosmcode[1]}?", (contains_code2(transmission1, mcode2)))
print(f"En el archivo de {archivostrans[0]} se encuentra el código {archivosmcode[2]}?", (contains_code2(transmission1, mcode3)))
print(f"En el archivo de {archivostrans[1]} se encuentra el código {archivosmcode[0]}?", (contains_code2(transmission2, mcode1)))
print(f"En el archivo de {archivostrans[1]} se encuentra el código {archivosmcode[1]}?", (contains_code2(transmission2, mcode2)))
print(f"En el archivo de {archivostrans[1]} se encuentra el código {archivosmcode[2]}?", (contains_code2(transmission2, mcode3)))
print()
print(f"El archivo de {archivostrans[0]} contiene el codigo de {archivosmcode[0]} en reversa?", (contains_code_reversed2(transmission1, mcode1)))
print(f"El archivo de {archivostrans[0]} contiene el codigo de {archivosmcode[1]} en reversa?", (contains_code_reversed2(transmission1, mcode2)))
print(f"El archivo de {archivostrans[0]} contiene el codigo de {archivosmcode[2]} en reversa?", (contains_code_reversed2(transmission1, mcode3)))
print(f"El archivo de {archivostrans[1]} contiene el codigo de {archivosmcode[0]} en reversa?", (contains_code_reversed2(transmission2, mcode1)))
print(f"El archivo de {archivostrans[1]} contiene el codigo de {archivosmcode[1]} en reversa?", (contains_code_reversed2(transmission2, mcode2)))
print(f"El archivo de {archivostrans[1]} contiene el codigo de {archivosmcode[2]} en reversa?", (contains_code_reversed2(transmission2, mcode3)))
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

    
    
    

        
    
