

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de llamar la función de saludar")
        resultado = funcion(*args, **kwargs) # Llamamos a nuestra función
        print("Despues de llamar la función saludar")
        return resultado
    return wrapper

@decorador 
def saludar(nombre):
    print(f"Hola {nombre}") 

saludar("Carlos") # Resultado: Hola Carlos


