# class Persona(object): Normalmente cuando creamos la primera clase esto es lo que hace
# Pero obviamos eso y las creamos como abajo
class Persona:
    def __init__(self, nombre, apellido): # Aqui hacemos una sobreescritura de la clase init de object
        self.nombre = nombre
        self.apellido = apellido

    # Sobreescribimos el metodo __str__

    def __str__(self):
        return f"Persona \nnombre = {self.nombre} \napellido = {self.apellido}\nDir. Mem. {super.__str__(self)}"
        # Al ingresar super, accedemos al metodo de la clase padre
    
# Codigo principal

persona1 = Persona("Ana", "Martinez")
print(persona1) # Al imprimir el objeto nos retorna el estado del objeto "__str__"
# El metodo print llama automaticamente al metodo __str__

# Veremos el comportamiento por default del metodo __str__
class Persona:
    def __init__(self, nombre, apellido): # Aqui hacemos una sobreescritura de la clase init de object
        self.nombre = nombre
        self.apellido = apellido

    # Sobreescribimos el metodo __str__

    # def __str__(self):
    #     return f"Persona \nnombre = {self.nombre} \napellido = {self.apellido}"
    
# Codigo principal

persona1 = Persona("Ana", "Martinez")
#print(persona1) # Al imprimir el objeto nos retorna el estado del objeto "__str__"
# El metodo print llama automaticamente al metodo __str__
print(persona1) # Retorna <__main__.Persona object at 0x0000018168516BA0>
# __main__ es el archivo que se esta ejecutando, desde la clase Persona, es un objeto ubicado en la memoria: 0x0000018168516BA0
