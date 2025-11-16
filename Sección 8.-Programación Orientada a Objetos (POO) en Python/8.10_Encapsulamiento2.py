# El encapsulamiento nos permite ocultar la información que almacena un objeto,
# Tambien conocido como el estado del objeto

# Para aplicar el concepto de encapsulamiento se deben aplicar dos caracteristicas:

# 1) Atributos protegidos o privados:
# self._nombre -> atributo protegido
# self.__apellido -> atributo privado

# 2) Crear los metodos conocidos como get (leer) y set (modificar)

# Definimos la clase

class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo publico
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo privado

    def conducir(self):
        print(f"""Conduciendo el coche:
              Marca: {self._marca}
              Modelo: {self._modelo}
              Color: {self._color}""")
        
    def get_marca(self): # Metodo para leer la marca
        return self._marca # Retornamos el valor de marca
    
    def set_marca(self, marca): # Metodo para modificar la marca
        self._marca = marca
    
    def get_modelo(self): # Metodo para leer el modelo
        return self._modelo # Retornamos el valor del modelo
    
    def set_modelo(self, modelo): # Metodo para modificar el modelo
        self._modelo = modelo

    def get_color(self): # Metodo para leer el color
        return self._color # Retornamos el valor de color
    
    def set_color(self, color): # Metodo para modificar el color
        self._color = color
        
# Programa Principal (Aqui es donde aplica el encapsulamiento)

if __name__ == "__main__":
    # Creación de un primer coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()

    # Utilizar el concepto de encapsulamiento (get/set)

    coche1.set_marca("Toyota 2") # Ahora de esta forma podemos modificar la marca de mi coche.
    coche1.set_modelo("Yaris 2") # Ahora de esta forma podemos modificar el modelo de mi vehiculo.
    coche1.set_color("Azul 2") # Ahora de esta forma podemos modificar el color de mi vehiculo.
    coche1.conducir()

    coche1.marca = "Toyota 3" # El atributo ya no se llama marca, se llama _marca, estamos tratando de utilizar
    # un metodo que ya no existe, se crea un nuevo atributo, pero solo de coche1. Esto es una mala practica.
    print(f"Atributo del coche1: {coche1.__dict__}") # __dict__ es un diccionario para ver todos nuestros atributos

    # Crea un segundo objeto

    coche2 = Coche("Chevrolet", "Trax", "Negro")
    print(f"Atributos coche2: {coche2.__dict__}")