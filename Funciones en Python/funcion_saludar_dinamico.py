# Sintaxis de las funciones

# def nombre_de_la_funcion(argumento1, argumento2, etc..): Usamos la palabra reservada def a continuación seguimos con el nombre de la función y los argumentos de entrada

# 1.- Definir una funcion llamada saludar

def saludar(mensaje): # mensaje es un parametro
    print(f"Mensaje recibido: {mensaje}")
    return "Termino ok la ejecución de la función saludar"

# 2.- Llamamos a la funcion (ya tiene que estar definida)

argumento = "Hola desde la función saludar"
valor_devuelto = saludar(argumento)
print(f"Valor devuelto de la función; {valor_devuelto}")


