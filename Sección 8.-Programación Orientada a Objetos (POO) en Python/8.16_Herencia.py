class Animal: # Clase padre, contiene metodos generales.

    def comer(self):
        print("Como muchas veces al día")

    def dormir(self):
        print("Duermo muchas horas")

class Perro(Animal): #Creamos una clase hija la cual hereda los metodos, entreparentesis asignamos la clase padre

    def hacer_sonido(self):
        print("Puedo ladrar")

# Programa principal

print("*** Ejemplo de Herencia en Python ***")
print("Clase padre, soy un Animal")

animal1 = Animal()

animal1.comer()
animal1.dormir()

print("\n Clase hija, soy un Perro")

perro1 = Perro()

perro1.comer() # Puedo heredar el metodo de la clase Padre
perro1.dormir() # Puedo heredar el metodo de la clase Padre
perro1.hacer_sonido() # Ademas el metodo de la clase misma.
    