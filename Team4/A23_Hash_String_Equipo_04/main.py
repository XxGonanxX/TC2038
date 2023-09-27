# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sánchez - A01708668

# Escribe un programa en python que reciba el nombre de un archivo de texto (datos.txt), seguido de un entero n, donde n es un entero múltiplo de 4 y (16 <= n <=64).

# La salida es una cadena de longitud n/4 que es una representación hexadecimal que corresponde al hasheo del archivo de texto de entrada de acuerdo con las siguientes reglas:

# El entero n determina el número de columnas que contendrá una tabla donde se irán acomodando los caracteres del archivo de texto (incluyendo saltos de líneas) en los renglones que sean necesarios.
# Si el número de caracteres en el archivo de entrada no es múltiplo de n, el último renglón se "rellena" con el valor de n.
# En un arreglo a de longitud n se calcula a[i] = (la suma de los ASCII de cada char en la columna) % 256.
# La salida se genera concatenando la representación hexadecimal (mayúsculas) a dos dígitos de cada posición en el arreglo.
# La longitud de la cadena de salida será de n/4.
# Muestra la tabla generada, el arreglo a, y la cadena de salida.

# Abre el archivo en modo lectura
with open('Team4/A23_Hash_String_Equipo_04/datos.txt', 'r') as archivo:

    contenido = archivo.read()
    
# Pide el valor de n
n = int(input("Ingrese el valor de n (múltiplo de 4 y 16 <= n <= 64): "))
# Si n no es múltiplo de 4 o no está entre 16 y 64, imprime un mensaje de error
if n % 4 != 0 or n < 16 or n > 64:
    print("Valor inválido")
    
# Calcula los espacios faltantes para que la longitud del contenido sea múltiplo de n
espacios_faltantes = n - (len(contenido) % n)

# Reemplaza los saltos de línea por espacios
contenido = contenido.replace("\n", " ")
# Agrega espacios faltantes al final del contenido
contenido += "[" * espacios_faltantes

# Crea una matriz vacía
matriz = []
# Crea un arreglo de longitud n
a = [0] * n

# Recorre el contenido de n en n
for i in range(0, len(contenido), n):
    # Crea una fila con el contenido de n en n
    fila = contenido[i : i + n]
    # Agrega la fila a la matriz
    matriz.append(fila)
    # Recorre la fila
    for j in range(n):
        # Calcula el valor de a[j]
        a[j] = (a[j] + ord(fila[j])) % 256
        
# Crea una cadena con la representación hexadecimal de cada valor de a

salida = "".join([format(valor, "02X") for valor in a])

# Imprime la matriz

print("Matriz:")
for fila in matriz:
    print(fila)
# Imprime el arreglo a
print(
    "\nSuma de columnas mod 256:\n",
    *a
)

# Imprime la representación hexadecimal

print("\nAhora en hexadecimal:\n", salida)

# Imprime o realiza operaciones con el contenido del archivo

