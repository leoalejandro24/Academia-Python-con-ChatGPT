# Los constructores se refieren a metodos especiales dentro de una clase que se utilizan para inicializar
# objetos de esa clase.

class Persona: # Por buenas practicas la primer letra del nombre de la clase se deja en mayuscula

    # Constructor __init__
    def __init__(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
        

    # def inicializar_persona(self, nombre, apellido): # Función pero al estar dentro de una clase es un metodo.
    #     # Creación de atributos de la clase
    #     # self.nombre es el atributo, nombre es el parametro del metodo
    #     self.nombre = nombre # self puede tener cualquier nombre pero como recomendación utilizamos self
    #     self.apellido = apellido

    def mostrar_contacto(self): # Metodo
        print(f"""Persona:
              Nombre: {self.nombre} 
              Apellido: {self.apellido}""") # Accedemos al valor del atributo

# Creación de Objetos

if __name__ == "__main__":
    # Este objeto se crea en la memoria heap. Se guardan en memoria hexadecimal.
    # ejemplo: x333. El parametro de self busca la refrencia del objeto (x333).
    # La variable persona 1 almacena la posicion.
    persona1 = Persona("Leandro", "Salazar") # Se llama de manera automatica el constructor
    # persona1.inicializar_persona("Leandro", "Salazar") Ahora no necesitamos utilizar ocupar un metodo
    # para crear a la persona, podemos pasar los parametros en la llamada de Persona()
    persona1.mostrar_contacto() # Nos imprime los valores de nombre y apellido
    print(f"Dir. mem persona1: {id(persona1)}") # 1609039899216 <- Estos valores cambian
    print(f"Dir. mem hex persona1: {hex(id(persona1))}") # 0x176a2406a50 <- Estos valores cambian

    
    
