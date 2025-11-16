class Persona:

    atributo_clase = 0 # Es un atributo de clase, el cual afectara a todas las clases Persona

    def __init__(self, atributo_instancia): # Atributo de instancia, los cuales se aplican de forma individual.
        self.atributo_instancia = atributo_instancia

# Programa principal

if __name__ == "__main__":
    print(f"Atributo de clase {Persona.atributo_clase}") # Para acceder al atributo de clase, debemos hacer un
    # llamado a la clase y el atributo.

    # Modificamos el atributo de clase 
    Persona.atributo_clase = 10
    print(f"Atributo de clase {Persona.atributo_clase}")

    # Creamos un objeto
    persona1 = Persona(15)
    # persona1.atributo_clase Podemos acceder al atributo de clase desde un objeto pero lo mejor es acceder desde
    # la misma clase
    print(f"Atributo de clase desde persona1: {persona1.atributo_clase}") # Este se comparte con todos los objetos
    print(f"Atributo de instancia desde persona1: {persona1.atributo_instancia}") # Valor personal

    print()
    persona2 = Persona(30)
    # persona1.atributo_clase Podemos acceder al atributo de clase desde un objeto pero lo mejor es acceder desde
    # la misma clase
    print(f"Atributo de clase desde persona1: {persona2.atributo_clase}") # Este se comparte con todos los objetos
    print(f"Atributo de instancia desde persona1: {persona2.atributo_instancia}") # Valor personal

    



    