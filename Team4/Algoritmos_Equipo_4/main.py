# Alan Patricio González Bernal - A01067546
# Alan Rodrigo Castillo Sánchez - A01708668

# En una maquila, un supervisor de producción registra la cantidad de 
# producto terminado (camisas) que cada línea de producción genera 
# durante un día completo de trabajo. Se tienen 2 líneas de producción 
# que, por diversas razones, no necesariamente producen la misma 
# cantidad diaria del producto.

# Se desea tener un programa que permita saber en cuantos días es 
# posible surtir un pedido de N camisas. Con la intención de mejorar 
# la planeación de los tiempos de entrega y de los insumos necesarios 
# para producirlas ya que últimamente se han registrado retrasos en los 
# tiempos de entrega.

# El punto es usar cotas superiores e inferiores, así que trata de 
# seguir con eso. La cota superior es cualquier número superior
# al conjunto, la cota inferior es el que es inferior al conjunto


def ProduccionLineas(x, y, N):
    # X es el valor de playeras que produce la primera línea
    # Y es el valor de playeras que produce la segunda línea
        
    Pedido = N

    # Este cálculo lo que hace es dividir el pedido entre la producción
    # de cada línea, para saber cuántos días se tarda en producir el pedido
    # en el peor de los casos, siendo este la cota inferior
    
    Cota_superior = max(Pedido // x, Pedido // y)

    Cota_inferior = (Pedido // (x + y))   
    
    ProduccionDiaria = (x + y)
    
    ListaBin = [Cota_inferior]
    
    num = Cota_inferior
    
    while num < Cota_superior:
        num += 1
        ListaBin.append(num)
    
    dias = 0
    
    # Se hace una búsqueda binaria para encontrar el número de días
    while len(ListaBin) > 1:
        mitad = len(ListaBin) // 2
        if ListaBin[mitad] > Pedido // ProduccionDiaria:
            ListaBin = ListaBin[:mitad]
            dias += 1
        else:
            ListaBin = ListaBin[mitad:]
            dias += 1
            
    print("El pedido estará listo en ",dias," días")
    
# Resulta que ha llegado una nueva máquina embotelladora de refrescos, 
# el contenedor principal de la máquina tiene forma cilíndrica. Se sabe 
# que cada envase de refresco debe contener M mililitros. Se desea saber 
# cuántos refrescos puede llenar la máquina de una sola vez, sin recargar
# el contenedor. Solo se tienen los datos del radio de la base y la 
# altura medidos en metros.

def ProduccionEmbotelladora(radio, altura, M):
    # Radio es el radio del cilindro
    # Altura es la altura del cilindro
    # M es la cantidad de mililitros que debe contener cada envase
    
    # Se calcula el volumen del cilindro
    Volumen = 3.1416 * (radio ** 2) * altura
    
    # Se calcula cuántos mililitros se pueden almacenar en el cilindro
    Mililitros = Volumen * 1000
    
    # Se calcula cuántos envases se pueden llenar con la cantidad de 
    # mililitros que se pueden almacenar en el cilindro
    Envases = Mililitros // M
    
    print("La máquina puede llenar ",Envases," envases de refresco")
        
        
# Se crea el main para llamar funciones
def main():
    print("Bienvenido a los sitemas de producción, el primero es el de playeras")
    print("Ingrese la producción de la primera línea")
    x = int(input())
    print("Ingrese la producción de la segunda línea")
    y = int(input())
    print("Ingrese el número de playeras que se desean producir")
    N = int(input())
    ProduccionLineas(x, y, N)
    print("")
    
    print("Bienvenido al sistema de embotelladora")
    print("Ingrese el radio del cilindro")
    radio = int(input())
    print("Ingrese la altura del cilindro")
    altura = int(input())
    print("Ingrese la cantidad de mililitros que debe contener cada envase")
    M = int(input())
    ProduccionEmbotelladora(radio, altura, M)
    print("")
    
    print("Gracias por usar nuestros sistemas de producción, este sistema \n fue desarrollado por Alan Patricio González Bernal y Alan Rodrigo Castillo Sánchez")
    
# Se llama main
main()
