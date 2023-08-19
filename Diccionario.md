## Introducción
A lo largo de este diccionario, se irán definiendo los 
conceptos o palabras necesarias para el curso.


## TUPLA
Sucesión finita de elementos donde el *orden si importa*. 
Se representan entre paréntesis y separados por comas. 
EJ:  
(a,b,c) != (b,c,a)

En caso de que la tupla tenga dos elementos, se le conoce 
como "Par", si son tres, es "Tercia". Si tiene más, siendo 
el número de elementos K, se nombra K-tupla.
EJ:  
(a,b,c,d) == 4-Tupla


## PRODUCTO CARTESIANO
Conjunto de todos los posibles pares ordenados, siendo A X 
B, se expresa como "A cruz B", la descripción es:  
A X B = {(x,y) x ∈A ∧y ∈B}
Esto se lee como:  
El producto A cruz B es el conjunto de parejas ordenadas 
(x,y) tal que x pertenece a A y y pertenece a B
EJ:
A = {1,2}
B = {a,b}

A X B = {(1,a),(1,b),(2,a),(2,b)}


##  RELACIÓN
Cualquier suconjunto de un producto cruz, es decir, 
conjunto donde sus elementos son tuplas.
EJ:  
R = A X B == R = {(a,b| a ∈ A, b ∈ B) 
(La relación de A CRUZ (O sea, producto cartesiano) B es 
igual a la relación de a y b donde a es formada por 
elementos de A y b está formada por elementos de B)

### Reflexividad
Una relación que para cada elemento a ∈ A existe un par ordenado (a,a) ∈ R.

### Simétrica
Una relación para cada elemento (a,b) ∈ R existe un par ordenado (b, a) ∈ R.

### Antisimétrica
Una relación para cada elemento (a,b) ∈ R, no existe (b,a) ∈ R. 

### Transitiva
Una relación para cada elemento (a,b) ∈ R y (b,c) ∈ R, y (a,c) ∈ R.


## GRAFO DIRIGIDO VS NO DIRIGIDO
El grafo dirgido es aquel en el que las aristas tienen un 
sentido definido, en el no definido, las aristas son 
simétricas y no apuntan a ningún sentido.

EJ:  

Dirigido = A --> B
No dirigido = A --- B

## Función
Una regla que asocia elementos de un conjunto A con elementos del conjunto B de modo que el elemento *del conjunto A se asocio con uno y sólo un elemento* del segundo conjunto.  


## Cotas

### Cota superior
Conocida como función ceil, redondea x hacia arriba, es decir, al número entero más cercano mayor o igual a x

### Cota inferior
Conocida como función floor, rendondea x hacia abajo, al número entero más cercano menor o igual a x.

## Truncar
Dar como resultado solo la parte entera de un resultado.

## Sucesiones
Tipo especial de función que tiene por dominio un conjunto de enteros consecutivos, los cuales indican las posiciones de los elementos dentro de la posicion por lo que se les conoce como índices.

### Progresión aritmética
Sucesión en forma a, a+d, a+2d, a+3d,..., a+nd.

### Progresión geométrica
Sucesión en forma a, ar, ar^2, ..., ar^n.

## Complejidad de algoritmos
La función complejidad f(n) donde n es el tamaño del problema. Busca dar una medida de la cantidad de recursos que un algoritmo necesitará al implementarse y ejecutarse en una computadora.

### Complejidad espacial
Se deben sumar todas las celdas de memoria que se utilizan, estáticas y dinámicas.

### Complejidad temporal
Generalmente más relevanet que la espacial. Refleja la cantidad de trabajo realizado al dar una medida de tiempo que requerirá ejecución de un algoritmo para resolver un problema.

### Clasificación de funciones
Se deben comparar las funciones para saber cual es mejor.

### Tasa de crecimiento
Estimación que nos indica la cantidad de recursos que requiere un algoritmo conforme crece el problema

## Análisis de complejidad

<img width="608" alt="Captura de pantalla 2023-08-18 a la(s) 6 21 41 p m" src="https://github.com/XxGonanxX/TC2038/assets/89163839/ac0800c3-7cce-4354-b9c3-215150abffaa">


