# Definición de la función

def persona_mayusculas(nombre, apellido, edad):
    print(f"Esta función regresa varios valores (tupla)")
    return nombre.upper(), apellido.upper(), edad # Debido a que los valores estan separado por comas, Python los convierte en tuplas.


# Programa principal

nombre, apellido, edad = persona_mayusculas("Sandra", "Jimenez", 42) # Concepto de unpacking
print(f"Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}")