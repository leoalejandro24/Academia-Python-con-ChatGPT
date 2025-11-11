# Crear un diccionario de persona con llave y valor

persona = {"nombre": "Sergio",
           "edad": 30,
           "ciudad": "Mexico"}

print(f"Diccionario de persona: {persona}")

# Acceder a los elementos del diccionario

print(f"Nombre: {persona["nombre"]}") # Accedemos al diccionario, llave nombre
print(f"Edad: {persona["edad"]}") # Accedemos al diccionario, llave edad
print(f"Ciudad: {persona["ciudad"]}") # Accedemos al diccionario, llave ciudad

# Modificar un valor del diccionario

persona["edad"] = 35 # Cambiamos el valor de 30 a 35
print(f"Diccionario de persona: {persona}")

# Agregar un nuevo elemento al diccionario

persona["profesion"] = "Ingeniero"
print(f"Diccionario de persona: {persona}")

# Eliminar un elemento del diccionario

del persona["ciudad"]
print(f"Diccionario de persona: {persona}")

# Iterar los elementos de un diccionario (llave, valor) (key, value)

for clave, valor in persona.items(): # Nos devuelve llave y valor, y lo que hacemos es desempaquetar los valores, al igual que una tupla
    print(f"Clave: {clave}, Valor: {valor}")


