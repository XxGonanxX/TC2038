def build_suffix_array(text):
    # Crea una lista de sufijos y les asigna índices iniciales.
    suffixes = [(text[i:], i) for i in range(len(text))]
    
    # Ordena los sufijos lexicográficamente.
    suffixes.sort(key=lambda x: x[0])
    
    # Extrae los índices ordenados de los sufijos.
    suffix_array = [suffix[1] for suffix in suffixes]
    
    return suffix_array

# Función para imprimir el "suffix array" ordenado alfabéticamente.
def print_sorted_suffix_array(text):
    suffix_array = build_suffix_array(text)
    for index in suffix_array:
        print(text[index:])

# Ejemplo de uso
def main():
    input_string = "banana"
    print("Sufijos ordenados alfabéticamente:")
    print_sorted_suffix_array(input_string)
    
main()