from clase_monitor import Monitor
from clase_raton import Raton
from clase_teclado import Teclado



class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, raton, teclado):
        Computadora.contador_computadora += 1
        self.id = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.raton = raton
        self.teclado = teclado

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}\nMonitor: {self.monitor}\nRaton: {self.raton}\nTeclado: {self.teclado}"

if __name__ == "__main__":
    teclado1 = Teclado("HP", "USB")
    raton1 = Raton("HP", "USB")
    monitor1 = Monitor("HP", 27)
    computadora1 = Computadora("HP", monitor1, raton1, teclado1)
    print(computadora1)

    # Al llamar las otras clases se les imprime el metodo str de las demas clases.
    # en las variables, teclado1, raton1, monitor1.