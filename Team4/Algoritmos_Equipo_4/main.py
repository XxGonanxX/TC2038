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

class Camisas:
    def __init__(self, camisas, dias):
        
        self.camisas = camisas
        self.dias = dias


# Resulta que ha llegado una nueva máquina embotelladora de refrescos, 
# el contenedor principal de la máquina tiene forma cilíndrica. Se sabe 
# que cada envase de refresco debe contener M mililitros. Se desea saber 
# cuántos refrescos puede llenar la máquina de una sola vez, sin recargar
# el contenedor. Solo se tienen los datos del radio de la base y la 
# altura medidos en metros.

class Embotelladora:
    def __init__(self, radio, altura):
        
        self.radio = radio
        self.altura = altura
        
        
# Se crea el main para llamar funciones
def main():
    print("Se imprimen los datos")
    
# Se llama main
main()