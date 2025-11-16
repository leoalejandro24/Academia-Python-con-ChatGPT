class Persona:

    # Atributo de clase
    contador_personas = 0 

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del artibuto de clase
        Persona.contador_personas += 1 # Cuando creo un objeto mi contador se le suma 1
        self.id = Persona.contador_personas # Se le asigna el id, siempre sera uno nuevo, ya que va sumando 1
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f"Persona: {self.id}, {self.nombre}, {self.apellido}")

    @staticmethod # Metodo estatico y se asocia con la clase misma
    def get_contador_persona_estatico():
        print("Metodo estatico")
        return Persona.contador_personas # De manera formal asi accedemos a los atributos de clase.
    
    @classmethod
    def get_contador_persona_clase(cls): # cls = class
        print(f"Metodo de clase")
        return cls.contador_personas # cls es como escribir Persona (la clase)

    




# Código principal

if __name__ == "__main__":
    persona1 = Persona("Gerardo", "Perez")
    persona1.mostrar_persona()

    persona2 = Persona("Daniel", "Sanchez")
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de persona
    print(Persona.contador_personas)

    print(f"Imprimir contador Persona (static): {Persona.get_contador_persona_estatico()}")
    print(f"Imprimir contador Persona (clase): {Persona.get_contador_persona_clase()}")