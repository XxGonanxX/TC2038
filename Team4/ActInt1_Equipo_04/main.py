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


# primero, leeremos todos los archivos, primero los transmision y luego los mcode, cada uno en una lista separada

# leer archivos de transmision
transmission1 = []
transmission2 = []

with open("Team4/ActInt1_Equipo_04/transmission01.txt", "r") as file:
    for line in file:
        transmission1.append(line)
        
with open("Team4/ActInt1_Equipo_04/transmission02.txt", "r") as file:
    for line in file:
        transmission2.append(line)
        
# leer archivos de mcode
mcode1 = []
mcode2 = []
mcode3 = []

with open("Team4/ActInt1_Equipo_04/mcode01.txt", "r") as file:
    for line in file:
        mcode1.append(line)
        
with open("Team4/ActInt1_Equipo_04/mcode02.txt", "r") as file:
    for line in file:
        mcode2.append(line)
        
with open("Team4/ActInt1_Equipo_04/mcode03.txt", "r") as file:
    for line in file:
        mcode3.append(line)
        
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
        print(mcode_string)
        
    # ahora, vamos a buscar el mcode dentro del transmission
    if mcode_string in transmission_string:
        # Necesito saber la posicion en la que inicia el codigo
        start = transmission_string.find(mcode_string)
        # Necesito saber la posicion en la que termina el codigo
        end = start + len(mcode_string)
        # Necesito imprimir el resultado
        print("true", start, end)
        return True
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
        print("true", start, end)
        return True
    else:
        return False
    
# Ahora, vamos a entregarle a la funcion los archivos que queremos analizar
# print(contains_code(transmission1, mcode1))
# print(contains_code(transmission1, mcode2))
print(contains_code(transmission1, mcode3))
# print(contains_code(transmission2, mcode1))
# print(contains_code(transmission2, mcode2))
# print(contains_code(transmission2, mcode3))
