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
        self.marca = marca # Atributo publico
        self._modelo = modelo # Atributo protegido
        self.__color = color # Atributo privado

    def conducir(self):
        print(f"""Conduciendo el coche:
              Marca: {self.marca}
              Modelo: {self._modelo}
              Color: {self.__color}""")
        
# Programa Principal (Aqui es donde aplica el encapsulamiento)

if __name__ == "__main__":
    # Creación de un primer coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()

    # En este momento no deberias acceder directamente a los atributos protegidos o privados.
    coche1.marca = "Toyota 2" # Este seria al unico atributo que podriamos acceder ya que es publico.
    coche1._modelo = "Yaris 2" # No es buena practica. No es buena practica.
    coche1.__color = "Azul 2" # Python ignora la modificación en un atributo privado.
    coche1._Coche__color = "Azul 3" # De esta forma podemos cambiar el atributo pero es mala practica.
    coche1.conducir()