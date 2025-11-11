# Función que acepta argumentos variables de tipo llave valor

def imprimir_info(**kwargs):
    print("Valores recibidos: ")
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")

# Llamamos a la función
imprimir_info(nombre = "Karla", edad = 30, ciudad = "Mexico")