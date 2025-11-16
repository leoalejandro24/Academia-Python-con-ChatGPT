# La sobreescritura nos permite modificar el metodo del padre desde el hijo.

class Animal: # Clase padre, contiene metodos generales.

    def comer(self):
        print("Como muchas veces al día")

    def dormir(self):
        print("Duermo muchas horas")

class Perro(Animal): #Creamos una clase hija la cual hereda los metodos, entreparentesis asignamos la clase padre

    def hacer_sonido(self):
        print("Puedo ladrar")

    def dormir(self): # Nos aseguramos de llamar al mismo metodo que la clase padre
        print("Duermo 15 horas al día")

# Programa principal

print("*** Ejemplo de Herencia en Python ***")
print("Clase padre, soy un Animal")

animal1 = Animal()

animal1.comer()
animal1.dormir()

print("\nClase hija, soy un Perro")

perro1 = Perro()

perro1.comer() # Puedo heredar el metodo de la clase Padre
perro1.dormir() # Aqui se llama al metodo sobreescrito en la clase hija.
perro1.hacer_sonido() # Ademas el metodo de la clase misma.
    