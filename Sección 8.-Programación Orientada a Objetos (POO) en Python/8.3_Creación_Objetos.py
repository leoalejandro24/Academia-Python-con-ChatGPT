class Persona: # Por buenas practicas la primer letra del nombre de la clase se deja en mayuscula
    def inicializar_persona(self, nombre, apellido): # Función pero al estar dentro de una clase es un metodo.
        # Creación de atributos de la clase
        # self.nombre es el atributo, nombre es el parametro del metodo
        self.nombre = nombre # self puede tener cualquier nombre pero como recomendación utilizamos self
        self.apellido = apellido

    def mostrar_contacto(self): # Metodo
        print(f"""Persona:
              Nombre: {self.nombre} 
              Apellido: {self.apellido}""") # Accedemos al valor del atributo

# Creación de Objetos

if __name__ == "__main__":
    persona1 = Persona() # Crea un objeto vacio en memoria
    persona1.inicializar_persona("Leandro", "Salazar")
    persona1.mostrar_contacto() # Nos imprime los valores de nombre y apellido